## -*- coding: utf-8 -*-
import logging
from loader import bot;
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton;
from loader import dp;
from aiogram.dispatcher.filters import Text
from aiogram import types;
from aiogram.types import ReplyKeyboardRemove;
from db import mycursor, mydb;
import requests;
TOKEN = "5533174693:AAEoKmwRzH9-tLsDVxpvZ5xaZDjaIzfvN_w";

#* SQL requests
SQL_REQUESTS = {
    "SELECT_ALL": "SELECT * FROM patient",
    "SELECT_ID_AND_CHAT_ID": "SELECT ID, CHAT_ID FROM patient",
    "SELECT_CHAT_ID": "SELECT CHAT_ID FROM patient",
    "INSERT_ALL": "INSERT INTO patient (CHAT_ID, GROUP_REC, PUSH_NOTIFICATIONS) VALUES (%s,%s,%s)"
}


#* Клавиатура
push_notifications_boolean_answer_yes_btn = KeyboardButton('Да');
push_notifications_boolean_answer_no_btn = KeyboardButton('Нет');
push_notifications_boolean_answer_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True);
push_notifications_boolean_answer_kb.row(
    push_notifications_boolean_answer_yes_btn,
    push_notifications_boolean_answer_no_btn
);

dominance_in_the_diet_question_first_btn = KeyboardButton('Преобладают углеводы');
dominance_in_the_diet_question_second_btn = KeyboardButton('Преобладают жиры');
dominance_in_the_diet_answer_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True);
dominance_in_the_diet_answer_kb.add(dominance_in_the_diet_question_first_btn).add(dominance_in_the_diet_question_second_btn);

consent_to_the_processing_of_personal_data_answer_yes_btn = KeyboardButton('Да, согласен');
consent_to_the_processing_of_personal_data_answer_no_btn = KeyboardButton('Нет, не согласен');
consent_to_the_processing_of_personal_data_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True);
consent_to_the_processing_of_personal_data_kb.row(
    consent_to_the_processing_of_personal_data_answer_yes_btn,
    consent_to_the_processing_of_personal_data_answer_no_btn
);

unsubscibe_notific_yes_sure_btn = KeyboardButton('Да, уверен');
unsubscibe_notific_no_sure_btn = KeyboardButton('Отмена');
unsubscibe_notific_sure_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True);
unsubscibe_notific_sure_kb.add(unsubscibe_notific_yes_sure_btn).add(unsubscibe_notific_no_sure_btn);

#* Проверяет есть ли телеграмм айди в базе данных (input int, return boolean)
def checkUniqueTelegramId(id):
    mycursor.execute(SQL_REQUESTS["SELECT_CHAT_ID"]);
    ids = mycursor.fetchall();
    for i in range(len(ids)):
        ids[i] = ids[i][0];
    if id in ids: return True;
    else: return False;
#* Получает айди в базе данных (input int, return int)
def getPrimaryKey(id):
    mycursor.execute(SQL_REQUESTS["SELECT_ID_AND_CHAT_ID"]);
    ids = mycursor.fetchall();
    for i in range(len(ids)):
        if ids[i][1] == id:
            return ids[i][0];


#* Обработка команды подписки на уведомления
@dp.message_handler(Text(equals='Подписаться на уведомления'))
async def process_start_command(msg: types.Message):
    logging.info(f"notifications_subscribe: user = {msg.from_user.id}");
    data = {
        "chat_id": msg.from_user.id,
        "photo": "https://sun9-east.userapi.com/sun9-57/s/v1/ig2/rA95IZAE9jQ5HxZHUHZIEMD99Sj57_N-uFvy31K0uDOuhRpLVaOT_92-J8sQMbhQ55OHS71FJ8nMaYBNytSy68h7.jpg?size=1280x1280&quality=96&type=album",
        "caption": "📢Здравствуйте, не желаете ли подписаться на уведомления?",
        "reply_markup": push_notifications_boolean_answer_kb
    }
    await bot.send_photo(data["chat_id"], data["photo"], data["caption"], reply_markup=push_notifications_boolean_answer_kb);
    # await msg.answer('📢Здравствуйте, не желаете ли подписаться на уведомления?', reply_markup=push_notifications_boolean_answer_kb);

@dp.message_handler(Text(equals='Отписаться от уведомлений'))
async def unsubcribe_notifications_command(msg: types.Message):
    logging.info(f"notifications_unsubscribe: user = {msg.from_user.id}");
    await msg.answer('Вы уверены, что хотите отписаться от уведомлений?', reply_markup=unsubscibe_notific_sure_kb);

@dp.message_handler(Text(equals='Нет'))
async def no_func(msg: types.Message):
    await msg.answer('Хорошо, вы в любой другой момент можете подписаться на уведомления', reply_markup=ReplyKeyboardRemove());
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True);
    kb.add(KeyboardButton('Вернуться в меню'))
    await msg.answer('Вернуться в главное меню?', reply_markup=kb);

@dp.message_handler(Text(equals='Да'))
async def yes_func(msg: types.Message):
    await msg.answer('🍽Что преобладает в Вашем рационе?\n🍫Углеводы (белый хлеб, сахар, сладкие газированные напитки, молочный шоколад, мучное)\n🍖Жиры (жареное, соления, сдобное тесто, крепкие мясные и рыбные бульоны, копчености, колбасы)', reply_markup=dominance_in_the_diet_answer_kb);

@dp.message_handler(Text(equals='Преобладают углеводы'))
async def group_one_func(msg: types.Message):
    logging.info(f"notifications_group: user = {msg.from_user.id}, answer = {msg.text}");
    global group_rec;
    group_rec = 1;
    await msg.answer('Вы согласны на обработку персональных данных?', reply_markup=consent_to_the_processing_of_personal_data_kb);

@dp.message_handler(Text(equals='Преобладают жиры'))
async def second_group_func(msg: types.Message):
    logging.info(f"notifications_group: user = {msg.from_user.id}, answer = {msg.text}");
    global group_rec;
    group_rec = 2;
    await msg.answer('Вы согласны на обработку персональных данных?', reply_markup=consent_to_the_processing_of_personal_data_kb);

@dp.message_handler(Text(equals='Да, согласен'))
async def yes_sure_func(msg: types.Message):
    logging.info(f"notifications_subscribe_start: user = {msg.from_user.id}");
    id = msg["from"]["id"];
    if not(checkUniqueTelegramId(id)):
        logging.info(f"notifications_ended: user = {msg.from_user.id}");
        val = (id, group_rec, 1);
        mycursor.execute(SQL_REQUESTS["INSERT_ALL"], val);
        mydb.commit();
        await msg.answer('⚡️Вы подписаны на уведомления.', reply_markup=ReplyKeyboardRemove());
        kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True);
        kb.add(KeyboardButton('Вернуться в меню'))
        await msg.answer('Вернуться в главное меню?', reply_markup=kb);
    else:
        logging.info(f"notifications_ended: user = {msg.from_user.id}");
        mycursor.execute("SELECT ID, CHAT_ID, GROUP_REC, PUSH_NOTIFICATIONS FROM patient");
        ids = mycursor.fetchall();
        if checkUniqueTelegramId(id) and ids[getPrimaryKey(id)-1][3] == 1 and ids[getPrimaryKey(id)-1][2] == group_rec:
            logging.info(f"notifications_ended: user = {msg.from_user.id}");
            text = '⚡️Вы уже подписаны на уведомления.';
            await msg.answer(text, reply_markup=ReplyKeyboardRemove());
            kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True);
            kb.add(KeyboardButton('Вернуться в меню'))
            await msg.answer('Вернуться в главное меню?', reply_markup=kb);
        elif checkUniqueTelegramId(id) and ids[getPrimaryKey(id)-1][3] == 1 and ids[getPrimaryKey(id)-1][2] != group_rec:
            logging.info(f"notifications_ended: user = {msg.from_user.id}");
            sql_update = "UPDATE patient SET GROUP_REC = %s WHERE ID = %s";
            val = (group_rec, getPrimaryKey(id));
            mycursor.execute(sql_update, val);
            mydb.commit();
            text = '⚡️Вы поменяли свой выбор по поводу диеты. Произведена повторная запись на уведомления по вашему выбору.'
            await msg.answer(text, reply_markup=ReplyKeyboardRemove());
            kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True);
            kb.add(KeyboardButton('Вернуться в меню'))
            await msg.answer('Вернуться в главное меню?', reply_markup=kb);
        elif checkUniqueTelegramId(id) and ids[getPrimaryKey(id)-1][3] == 0 and ids[getPrimaryKey(id)-1][2] == group_rec:
            logging.info(f"notifications_ended: user = {msg.from_user.id}");
            sql = "UPDATE patient SET PUSH_NOTIFICATIONS = %s WHERE ID = %s";
            val = (1, getPrimaryKey(id));
            mycursor.execute(sql, val);
            mydb.commit();
            text = '⚡️Вы обратно подписались на уведомления не изменив группу.'
            await msg.answer(text, reply_markup=ReplyKeyboardRemove());
            kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True);
            kb.add(KeyboardButton('Вернуться в меню'))
            await msg.answer('Вернуться в главное меню?', reply_markup=kb);
        elif checkUniqueTelegramId(id) and ids[getPrimaryKey(id)-1][3] == 0 and ids[getPrimaryKey(id)-1][2] != group_rec:
            logging.info(f"notifications_ended: user = {msg.from_user.id}");
            sql = "UPDATE patient SET PUSH_NOTIFICATIONS = %s, GROUP_REC = %s WHERE ID = %s";
            val = (1, group_rec, getPrimaryKey(id));
            mycursor.execute(sql, val);
            mydb.commit();
            text = '⚡️Вы обратно подписались на уведомления изменив свою группу.'
            await msg.answer(text, reply_markup=ReplyKeyboardRemove());
            kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True);
            kb.add(KeyboardButton('Вернуться в меню'))
            await msg.answer('Вернуться в главное меню?', reply_markup=kb);

@dp.message_handler(Text(equals='Нет, не согласен'))
async def not_sure_func(msg: types.Message):
    await msg.answer('Хорошо, вы в любой другой момент можете подписаться на уведомления', reply_markup=ReplyKeyboardRemove());
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True);
    kb.add(KeyboardButton('Вернуться в меню'))
    await msg.answer('Вернуться в главное меню?', reply_markup=kb);

@dp.message_handler(Text(equals='Да, уверен'))
async def not_sure_func(msg: types.Message):
    id = msg["from"]["id"];
    sql_update = "UPDATE patient SET PUSH_NOTIFICATIONS = %s WHERE ID = %s";
    val = (0, getPrimaryKey(id));
    mycursor.execute(sql_update, val);
    mydb.commit();
    text = 'Вы успешно отписались от уведомлений';
    await msg.answer(text, reply_markup=ReplyKeyboardRemove());
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True);
    kb.add(KeyboardButton('Вернуться в меню'))
    await msg.answer('Вернуться в главное меню?', reply_markup=kb);

@dp.message_handler(Text(equals='Отмена'))
async def not_sure_func(msg: types.Message):
    await msg.answer('Вы сможете в любой другой момент отписаться от уведомлений.', reply_markup=ReplyKeyboardRemove());
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True);
    kb.add(KeyboardButton('Вернуться в меню'))
    await msg.answer('Вернуться в главное меню?', reply_markup=kb);
