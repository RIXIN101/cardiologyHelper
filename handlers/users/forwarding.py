## -*- coding: utf-8 -*-
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton;
import gspread
from loader import dp;
import logging;
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types;
from loader import bot;

#* Google Sheet
gc = gspread.service_account(filename='credentials.json')
gsheet = gc.open_by_key("1HAwz_xpkr2PckconEV2AZq_5ZMzrmqlI0HCVn0S0rBg")
wsheet = gsheet.worksheet("Лист1")

#* Переадрессация на врача
def cols(): return len(wsheet.col_values(1));
class Form(StatesGroup):
    name = State();
    phone = State();
    question = State();

@dp.message_handler(Text(equals='Задать вопрос врачу'))
async def cmd_start(msg: types.Message):
    logging.info(f'forwarding_start: user = {msg.from_user.id}');
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True);
    kb.add('Да, подтверждаю');
    kb.add('Нет, отказываюсь')
    await msg.answer('Задавая вопрос врачу, вы подтверждаете согласие на обработку персональных данных?', reply_markup=kb)

@dp.message_handler(Text(equals='Да, подтверждаю'))
async def yes_sure(msg: types.Message):
    logging.info(f'forwarding_personal_data: user = {msg.from_user.id}, answer = {msg.text}');
    await Form.name.set();
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True);
    kb.add(KeyboardButton("Отменить обращение к врачу"));
    data = {
        "chat_id": msg.from_user.id,
        "photo": "https://sun9-east.userapi.com/sun9-18/s/v1/ig2/CM92nke8WF3VOY89wXwKZI36Kyh0lEqjsPt2AvVcwI7RD7kkSVpu5OF2j77wyfpEXykimUK7Qv8iXRHIBGZVON7u.jpg?size=1280x1280&quality=96&type=album",
        "caption": "👩‍⚕👨‍⚕Вы хотите обратиться к врачу за помощью, напишите как я могу к вам обращаться?",
        "reply_markup": kb
    }
    await bot.send_photo(data["chat_id"], data["photo"], data["caption"], reply_markup=kb);
    # await msg.answer("👩‍⚕👨‍⚕Вы хотите обратиться к врачу за помощью, напишите как я могу к вам обращаться?", reply_markup=kb);

@dp.message_handler(Text(equals='Отменить обращение к врачу', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None: return;
    logging.info(f'forwarding_cancellation: user = {message.from_user.id}, answer = {message.text}');
    await state.finish()
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True);
    kb.add(KeyboardButton("Вернуться в меню"));
    await message.answer('Переадрессация на врача отменена', reply_markup=kb)

@dp.message_handler(state=Form.name)
async def process_name(message: types.Message, state: FSMContext):
    logging.info(f'forwarding_name: user = {message.from_user.id}, answer = {message.text}');
    async with state.proxy() as data: data['name'] = message.text;
    await Form.next()
    await message.answer("📞Продиктуйте ваш номер телефона для того, чтобы связаться с вами:")

@dp.message_handler(state=Form.phone)
async def process_phone(message: types.Message, state: FSMContext):
    logging.info(f'forwarding_phone: user = {message.from_user.id}, answer = {message.text}');
    await Form.next();
    await state.update_data(phone=message.text);
    await message.answer("❓Напишите интересующий вас вопрос:")

@dp.message_handler(state=Form.question)
async def process_gender(message: types.Message, state: FSMContext):
    logging.info(f'forwarding_question: user = {message.from_user.id}, answer = {message.text}');
    async with state.proxy() as data: data['question'] = message.text
    patient_data = [data["name"],data["phone"],data["question"]];
    wsheet.insert_row(patient_data, cols()+1);
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True);
    kb.add(KeyboardButton("Вернуться в меню"));
    await message.answer('❤️Ваш вопрос успешно отправлен, в скором времени с вами свяжуться.', reply_markup=kb);
    await state.finish();

@dp.message_handler(Text(equals='Нет, отказываюсь'))
async def no_not_sure(msg: types.Message):
    logging.info(f'forwarding_personal_data: user = {msg.from_user.id}, answer = {msg.text}');
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True);
    kb.add('Вернуться в меню');
    await msg.answer('Вы можете в любой другой момент задать вопрос врачу!', reply_markup=kb);