# -*- coding: utf-8 -*-
import logging;
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from loader import dp
from openpyxl import load_workbook
from aiogram.dispatcher.filters import Text
from aiogram import types
# * Открытие файла excel для чтения
read = load_workbook("Produkty.xlsx", data_only=True)
read_sheet = read.active

from db import mycursor, mydb, SQL_REQUESTS;

product_classification = [
    "Молоко и молочные продукты",
    "Яйцепродукты",
    "Мясо и мясные продукты",
    "Рыба. Нерыбные объекты промысла и продукты из них",
    "Жировые продукты (жирностью более 50%)",
    "Зерно и продукты его переработки",
    "Бобовые, орехи",
    "Овощи, грибы и продукты их переработки",
    "Фрукты, ягоды и продукты их переработки",
    "Кондитерские изделия",
    "Напитки",
    "Вспомогательные пищевые продукты и улучшители вкуса"
]

def product_classification_menu0(exceptions):
    product_arr = []
    product = read_sheet["A4:A150"];
    for i in range(len(product)): product_arr.append(product[i][0].value.strip());
    if exceptions == '':
        kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True);
        kb.add(KeyboardButton('Вернуться к выбору классификации'));
        for i in range(len(product_arr)): btn = KeyboardButton(product_arr[i]); kb.add(btn);
        return kb;
    else:
        exc = exceptions.split(',');
        if exc[-1] == '': exc.pop(-1);
        for i in range(len(exc)):
            if exc[i] in product_arr: product_arr.remove(exc[i].strip());
        kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        kb.add(KeyboardButton('Вернуться к выбору классификации'))
        for i in range(len(product_arr)): btn = KeyboardButton(product_arr[i]); kb.add(btn);
        return kb;

def product_classification_menu1(exceptions):
    product_arr = []
    product = read_sheet["A152:A164"];
    for i in range(len(product)): product_arr.append(product[i][0].value.strip());
    if exceptions == '':
        kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True);
        kb.add(KeyboardButton('Вернуться к выбору классификации'));
        for i in range(len(product_arr)): btn = KeyboardButton(product_arr[i]); kb.add(btn);
        return kb;
    else:
        exc = exceptions.split(',');
        if exc[-1] == '': exc.pop(-1);
        for i in range(len(exc)):
            if exc[i] in product_arr: product_arr.remove(exc[i].strip());
        kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        kb.add(KeyboardButton('Вернуться к выбору классификации'))
        for i in range(len(product_arr)): btn = KeyboardButton(product_arr[i]); kb.add(btn);
        return kb;

def product_classification_menu2(exceptions):
    product_arr = []
    product = read_sheet["A166:A348"];
    for i in range(len(product)): product_arr.append(product[i][0].value.strip());
    if exceptions == '':
        kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True);
        kb.add(KeyboardButton('Вернуться к выбору классификации'));
        for i in range(len(product_arr)): btn = KeyboardButton(product_arr[i]); kb.add(btn);
        return kb;
    else:
        exc = exceptions.split(',');
        if exc[-1] == '': exc.pop(-1);
        for i in range(len(exc)):
            if exc[i] in product_arr: product_arr.remove(exc[i].strip());
        kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        kb.add(KeyboardButton('Вернуться к выбору классификации'))
        for i in range(len(product_arr)): btn = KeyboardButton(product_arr[i]); kb.add(btn);
        return kb;

def product_classification_menu3(exceptions):
    product_arr = []
    product = read_sheet["A350:A500"];
    for i in range(len(product)): product_arr.append(product[i][0].value.strip());
    if exceptions == '':
        kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True);
        kb.add(KeyboardButton('Вернуться к выбору классификации'));
        for i in range(len(product_arr)): btn = KeyboardButton(product_arr[i]); kb.add(btn);
        return kb;
    else:
        exc = exceptions.split(',');
        if exc[-1] == '': exc.pop(-1);
        for i in range(len(exc)):
            if exc[i] in product_arr: product_arr.remove(exc[i].strip());
        kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        kb.add(KeyboardButton('Вернуться к выбору классификации'))
        for i in range(len(product_arr)): btn = KeyboardButton(product_arr[i]); kb.add(btn);
        return kb;

def product_classification_menu4(exceptions):
    product_arr = []
    product = read_sheet["A502:A539"];
    for i in range(len(product)): product_arr.append(product[i][0].value.strip());
    if exceptions == '':
        kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True);
        kb.add(KeyboardButton('Вернуться к выбору классификации'));
        for i in range(len(product_arr)): btn = KeyboardButton(product_arr[i]); kb.add(btn);
        return kb;
    else:
        exc = exceptions.split(',');
        if exc[-1] == '': exc.pop(-1);
        for i in range(len(exc)):
            if exc[i] in product_arr: product_arr.remove(exc[i].strip());
        kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        kb.add(KeyboardButton('Вернуться к выбору классификации'))
        for i in range(len(product_arr)): btn = KeyboardButton(product_arr[i]); kb.add(btn);
        return kb;

def product_classification_menu5(exceptions):
    product_arr = []
    product = read_sheet["A541:A655"];
    for i in range(len(product)): product_arr.append(product[i][0].value.strip());
    if exceptions == '':
        kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True);
        kb.add(KeyboardButton('Вернуться к выбору классификации'));
        for i in range(len(product_arr)): btn = KeyboardButton(product_arr[i]); kb.add(btn);
        return kb;
    else:
        exc = exceptions.split(',');
        if exc[-1] == '': exc.pop(-1);
        for i in range(len(exc)):
            if exc[i] in product_arr: product_arr.remove(exc[i].strip());
        kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        kb.add(KeyboardButton('Вернуться к выбору классификации'))
        for i in range(len(product_arr)): btn = KeyboardButton(product_arr[i]); kb.add(btn);
        return kb;

def product_classification_menu6(exceptions):
    product_arr = []
    product = read_sheet["A657:A684"];
    for i in range(len(product)): product_arr.append(product[i][0].value.strip());
    if exceptions == '':
        kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True);
        kb.add(KeyboardButton('Вернуться к выбору классификации'));
        for i in range(len(product_arr)): btn = KeyboardButton(product_arr[i]); kb.add(btn);
        return kb;
    else:
        exc = exceptions.split(',');
        if exc[-1] == '': exc.pop(-1);
        for i in range(len(exc)):
            if exc[i] in product_arr: product_arr.remove(exc[i].strip());
        kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        kb.add(KeyboardButton('Вернуться к выбору классификации'))
        for i in range(len(product_arr)): btn = KeyboardButton(product_arr[i]); kb.add(btn);
        return kb;

def product_classification_menu7(exceptions):
    product_arr = []
    product = read_sheet["A686:A842"];
    for i in range(len(product)): product_arr.append(product[i][0].value.strip());
    if exceptions == '':
        kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True);
        kb.add(KeyboardButton('Вернуться к выбору классификации'));
        for i in range(len(product_arr)): btn = KeyboardButton(product_arr[i]); kb.add(btn);
        return kb;
    else:
        exc = exceptions.split(',');
        if exc[-1] == '': exc.pop(-1);
        for i in range(len(exc)):
            if exc[i] in product_arr: product_arr.remove(exc[i].strip());
        kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        kb.add(KeyboardButton('Вернуться к выбору классификации'))
        for i in range(len(product_arr)): btn = KeyboardButton(product_arr[i]); kb.add(btn);
        return kb;

def product_classification_menu8(exceptions):
    product_arr = []
    product = read_sheet["A844:A917"];
    for i in range(len(product)): product_arr.append(product[i][0].value.strip());
    if exceptions == '':
        kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True);
        kb.add(KeyboardButton('Вернуться к выбору классификации'));
        for i in range(len(product_arr)): btn = KeyboardButton(product_arr[i]); kb.add(btn);
        return kb;
    else:
        exc = exceptions.split(',');
        if exc[-1] == '': exc.pop(-1);
        for i in range(len(exc)):
            if exc[i] in product_arr: product_arr.remove(exc[i].strip());
        kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        kb.add(KeyboardButton('Вернуться к выбору классификации'))
        for i in range(len(product_arr)): btn = KeyboardButton(product_arr[i]); kb.add(btn);
        return kb;

def product_classification_menu9(exceptions):
    product_arr = []
    product = read_sheet["A919:A996"];
    for i in range(len(product)): product_arr.append(product[i][0].value.strip());
    if exceptions == '':
        kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True);
        kb.add(KeyboardButton('Вернуться к выбору классификации'));
        for i in range(len(product_arr)): btn = KeyboardButton(product_arr[i]); kb.add(btn);
        return kb;
    else:
        exc = exceptions.split(',');
        if exc[-1] == '': exc.pop(-1);
        for i in range(len(exc)):
            if exc[i] in product_arr: product_arr.remove(exc[i].strip());
        kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        kb.add(KeyboardButton('Вернуться к выбору классификации'))
        for i in range(len(product_arr)): btn = KeyboardButton(product_arr[i]); kb.add(btn);
        return kb;

def product_classification_menu10(exceptions):
    product_arr = []
    product = read_sheet["A998:A1069"];
    for i in range(len(product)): product_arr.append(product[i][0].value.strip());
    if exceptions == '':
        kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True);
        kb.add(KeyboardButton('Вернуться к выбору классификации'));
        for i in range(len(product_arr)): btn = KeyboardButton(product_arr[i]); kb.add(btn);
        return kb;
    else:
        exc = exceptions.split(',');
        if exc[-1] == '': exc.pop(-1);
        for i in range(len(exc)):
            if exc[i] in product_arr: product_arr.remove(exc[i].strip());
        kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        kb.add(KeyboardButton('Вернуться к выбору классификации'))
        for i in range(len(product_arr)): btn = KeyboardButton(product_arr[i]); kb.add(btn);
        return kb;

def product_classification_menu11(exceptions):
    product_arr = []
    product = read_sheet["A1071:A1091"];
    for i in range(len(product)): product_arr.append(product[i][0].value.strip());
    if exceptions == '':
        kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True);
        kb.add(KeyboardButton('Вернуться к выбору классификации'));
        for i in range(len(product_arr)): btn = KeyboardButton(product_arr[i]); kb.add(btn);
        return kb;
    else:
        exc = exceptions.split(',');
        if exc[-1] == '': exc.pop(-1);
        for i in range(len(exc)):
            if exc[i] in product_arr: product_arr.remove(exc[i].strip());
        kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        kb.add(KeyboardButton('Вернуться к выбору классификации'))
        for i in range(len(product_arr)): btn = KeyboardButton(product_arr[i]); kb.add(btn);
        return kb;

def createClassificationMenu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    kb.add('Отмена ввода дневника')
    for i in range(len(product_classification)):
        btn = KeyboardButton(product_classification[i])
        kb.add(btn)
    return kb

def createProductArr():
    product_arr = []
    product = read_sheet["A3:A1091"]
    for i in range(len(product)):
        product_arr.append(product[i][0].value.strip())
    for i in range(len(product_classification)):
        product_arr.remove(product_classification[i])
    return product_arr

def getUserFinded(id):
    mycursor.execute('select tg_id from diet_diary')
    result = mycursor.fetchall()
    arr = []
    for i in range(len(result)):
        arr.append(result[i][0])
    if id in arr: return True
    else: return False

@dp.message_handler(Text(equals=product_classification[0]))
async def product_classification0(msg: types.Message):
    text = msg["text"];
    id = msg["from"]["id"]
    if getUserFinded(msg["from"]["id"]):
        mycursor.execute(SQL_REQUESTS['SWITCH_OFF_SAFE_UPDATES']);
        mycursor.execute(SQL_REQUESTS["UPDATE_MENU_CLASSIFICATION"], (text, id));
        mydb.commit();

        mycursor.execute(f'select exceptions from diet_diary where tg_id={id}');
        rel = mycursor.fetchone()[0];
        if rel != '': await msg.answer('Выберите продукт:', reply_markup=product_classification_menu0(rel))
        else: await msg.answer('Выберите продукт:', reply_markup=product_classification_menu0(''))
    else:
        mycursor.execute(SQL_REQUESTS['INSERT'], (id, '', '', text, 0, ''));
        mydb.commit();
        mycursor.execute(f'select exceptions from diet_diary where tg_id={id}');
        rel = mycursor.fetchone()[0];
        if rel != '': await msg.answer('Выберите продукт:', reply_markup=product_classification_menu0(rel))
        else: await msg.answer('Выберите продукт:', reply_markup=product_classification_menu0(''))

@dp.message_handler(Text(equals=product_classification[1]))
async def product_classification1(msg: types.Message):
    text = msg["text"];
    id = msg["from"]["id"]
    if getUserFinded(msg["from"]["id"]):
        mycursor.execute(SQL_REQUESTS['SWITCH_OFF_SAFE_UPDATES']);
        mycursor.execute(SQL_REQUESTS["UPDATE_MENU_CLASSIFICATION"], (text, id));
        mydb.commit();
        mycursor.execute(f'select exceptions from diet_diary where tg_id={id}');
        rel = mycursor.fetchone()[0];
        if rel != '': await msg.answer('Выберите продукт:', reply_markup=product_classification_menu1(rel))
        else: await msg.answer('Выберите продукт:', reply_markup=product_classification_menu1(''))
    else:
        mycursor.execute(SQL_REQUESTS['INSERT'], (id, '', '', text, 0, ''));
        mydb.commit();
        mycursor.execute(f'select exceptions from diet_diary where tg_id={id}');
        rel = mycursor.fetchone()[0];
        if rel != '': await msg.answer('Выберите продукт:', reply_markup=product_classification_menu1(rel))
        else: await msg.answer('Выберите продукт:', reply_markup=product_classification_menu1(''))

@dp.message_handler(Text(equals=product_classification[2]))
async def product_classification2(msg: types.Message):
    text = msg["text"];
    id = msg["from"]["id"]
    if getUserFinded(msg["from"]["id"]):
        mycursor.execute(SQL_REQUESTS['SWITCH_OFF_SAFE_UPDATES']);
        mycursor.execute(SQL_REQUESTS["UPDATE_MENU_CLASSIFICATION"], (text, id));
        mydb.commit();
        mycursor.execute(f'select exceptions from diet_diary where tg_id={id}');
        rel = mycursor.fetchone()[0];
        if rel != '': await msg.answer('Выберите продукт:', reply_markup=product_classification_menu2(rel))
        else: await msg.answer('Выберите продукт:', reply_markup=product_classification_menu2(''))
    else:
        mycursor.execute(SQL_REQUESTS['INSERT'], (id, '', '', text, 0, ''));
        mydb.commit();
        mycursor.execute(f'select exceptions from diet_diary where tg_id={id}');
        rel = mycursor.fetchone()[0];
        if rel != '': await msg.answer('Выберите продукт:', reply_markup=product_classification_menu2(rel))
        else: await msg.answer('Выберите продукт:', reply_markup=product_classification_menu2(''))

@dp.message_handler(Text(equals=product_classification[3]))
async def product_classification3(msg: types.Message):
    text = msg["text"];
    id = msg["from"]["id"]
    if getUserFinded(msg["from"]["id"]):
        mycursor.execute(SQL_REQUESTS['SWITCH_OFF_SAFE_UPDATES']);
        mycursor.execute(SQL_REQUESTS["UPDATE_MENU_CLASSIFICATION"], (text, id));
        mydb.commit();
        mycursor.execute(f'select exceptions from diet_diary where tg_id={id}');
        rel = mycursor.fetchone()[0];
        if rel != '': await msg.answer('Выберите продукт:', reply_markup=product_classification_menu3(rel))
        else: await msg.answer('Выберите продукт:', reply_markup=product_classification_menu3(''))
    else:
        mycursor.execute(SQL_REQUESTS['INSERT'], (id, '', '', text, 0, ''));
        mydb.commit();
        mycursor.execute(f'select exceptions from diet_diary where tg_id={id}');
        rel = mycursor.fetchone()[0];
        if rel != '': await msg.answer('Выберите продукт:', reply_markup=product_classification_menu3(rel))
        else: await msg.answer('Выберите продукт:', reply_markup=product_classification_menu3(''))

@dp.message_handler(Text(equals=product_classification[4]))
async def product_classification4(msg: types.Message):
    text = msg["text"];
    id = msg["from"]["id"]
    if getUserFinded(msg["from"]["id"]):
        mycursor.execute(SQL_REQUESTS['SWITCH_OFF_SAFE_UPDATES']);
        mycursor.execute(SQL_REQUESTS["UPDATE_MENU_CLASSIFICATION"], (text, id));
        mydb.commit();
        mycursor.execute(f'select exceptions from diet_diary where tg_id={id}');
        rel = mycursor.fetchone()[0];
        if rel != '': await msg.answer('Выберите продукт:', reply_markup=product_classification_menu4(rel))
        else: await msg.answer('Выберите продукт:', reply_markup=product_classification_menu4(''))
    else:
        mycursor.execute(SQL_REQUESTS['INSERT'], (id, '', '', text, 0, ''));
        mydb.commit();
        mycursor.execute(f'select exceptions from diet_diary where tg_id={id}');
        rel = mycursor.fetchone()[0];
        if rel != '': await msg.answer('Выберите продукт:', reply_markup=product_classification_menu4(rel))
        else: await msg.answer('Выберите продукт:', reply_markup=product_classification_menu4(''))

@dp.message_handler(Text(equals=product_classification[5]))
async def product_classification5(msg: types.Message):
    text = msg["text"];
    id = msg["from"]["id"]
    if getUserFinded(msg["from"]["id"]):
        mycursor.execute(SQL_REQUESTS['SWITCH_OFF_SAFE_UPDATES']);
        mycursor.execute(SQL_REQUESTS["UPDATE_MENU_CLASSIFICATION"], (text, id));
        mydb.commit();
        mycursor.execute(f'select exceptions from diet_diary where tg_id={id}');
        rel = mycursor.fetchone()[0];
        if rel != '': await msg.answer('Выберите продукт:', reply_markup=product_classification_menu5(rel))
        else: await msg.answer('Выберите продукт:', reply_markup=product_classification_menu5(''))
    else:
        mycursor.execute(SQL_REQUESTS['INSERT'], (id, '', '', text, 0, ''));
        mydb.commit();
        mycursor.execute(f'select exceptions from diet_diary where tg_id={id}');
        rel = mycursor.fetchone()[0];
        if rel != '': await msg.answer('Выберите продукт:', reply_markup=product_classification_menu5(rel))
        else: await msg.answer('Выберите продукт:', reply_markup=product_classification_menu5(''))

@dp.message_handler(Text(equals=product_classification[6]))
async def product_classification6(msg: types.Message):
    text = msg["text"];
    id = msg["from"]["id"]
    if getUserFinded(msg["from"]["id"]):
        mycursor.execute(SQL_REQUESTS['SWITCH_OFF_SAFE_UPDATES']);
        mycursor.execute(SQL_REQUESTS["UPDATE_MENU_CLASSIFICATION"], (text, id));
        mydb.commit();
        mycursor.execute(f'select exceptions from diet_diary where tg_id={id}');
        rel = mycursor.fetchone()[0];
        if rel != '': await msg.answer('Выберите продукт:', reply_markup=product_classification_menu6(rel))
        else: await msg.answer('Выберите продукт:', reply_markup=product_classification_menu6(''))
    else:
        mycursor.execute(SQL_REQUESTS['INSERT'], (id, '', '', text, 0, ''));
        mydb.commit();
        mycursor.execute(f'select exceptions from diet_diary where tg_id={id}');
        rel = mycursor.fetchone()[0];
        if rel != '': await msg.answer('Выберите продукт:', reply_markup=product_classification_menu6(rel))
        else: await msg.answer('Выберите продукт:', reply_markup=product_classification_menu6(''))

@dp.message_handler(Text(equals=product_classification[7]))
async def product_classification7(msg: types.Message):
    text = msg["text"];
    id = msg["from"]["id"]
    if getUserFinded(msg["from"]["id"]):
        mycursor.execute(SQL_REQUESTS['SWITCH_OFF_SAFE_UPDATES']);
        mycursor.execute(SQL_REQUESTS["UPDATE_MENU_CLASSIFICATION"], (text, id));
        mydb.commit();
        mycursor.execute(f'select exceptions from diet_diary where tg_id={id}');
        rel = mycursor.fetchone()[0];
        if rel != '': await msg.answer('Выберите продукт:', reply_markup=product_classification_menu7(rel))
        else: await msg.answer('Выберите продукт:', reply_markup=product_classification_menu7(''))
    else:
        mycursor.execute(SQL_REQUESTS['INSERT'], (id, '', '', text, 0, ''));
        mydb.commit();
        mycursor.execute(f'select exceptions from diet_diary where tg_id={id}');
        rel = mycursor.fetchone()[0];
        if rel != '': await msg.answer('Выберите продукт:', reply_markup=product_classification_menu7(rel))
        else: await msg.answer('Выберите продукт:', reply_markup=product_classification_menu7(''))

@dp.message_handler(Text(equals=product_classification[8]))
async def product_classification8(msg: types.Message):
    text = msg["text"];
    id = msg["from"]["id"]
    if getUserFinded(msg["from"]["id"]):
        mycursor.execute(SQL_REQUESTS['SWITCH_OFF_SAFE_UPDATES']);
        mycursor.execute(SQL_REQUESTS["UPDATE_MENU_CLASSIFICATION"], (text, id));
        mydb.commit();
        mycursor.execute(f'select exceptions from diet_diary where tg_id={id}');
        rel = mycursor.fetchone()[0];
        if rel != '': await msg.answer('Выберите продукт:', reply_markup=product_classification_menu8(rel))
        else: await msg.answer('Выберите продукт:', reply_markup=product_classification_menu8(''))
    else:
        mycursor.execute(SQL_REQUESTS['INSERT'], (id, '', '', text, 0, ''));
        mydb.commit();
        mycursor.execute(f'select exceptions from diet_diary where tg_id={id}');
        rel = mycursor.fetchone()[0];
        if rel != '': await msg.answer('Выберите продукт:', reply_markup=product_classification_menu8(rel))
        else: await msg.answer('Выберите продукт:', reply_markup=product_classification_menu8(''))

@dp.message_handler(Text(equals=product_classification[9]))
async def product_classification9(msg: types.Message):
    text = msg["text"];
    id = msg["from"]["id"]
    if getUserFinded(msg["from"]["id"]):
        mycursor.execute(SQL_REQUESTS['SWITCH_OFF_SAFE_UPDATES']);
        mycursor.execute(SQL_REQUESTS["UPDATE_MENU_CLASSIFICATION"], (text, id));
        mydb.commit();
        mycursor.execute(f'select exceptions from diet_diary where tg_id={id}');
        rel = mycursor.fetchone()[0];
        if rel != '': await msg.answer('Выберите продукт:', reply_markup=product_classification_menu9(rel))
        else: await msg.answer('Выберите продукт:', reply_markup=product_classification_menu9(''))
    else:
        mycursor.execute(SQL_REQUESTS['INSERT'], (id, '', '', text, 0, ''));
        mydb.commit();
        mycursor.execute(f'select exceptions from diet_diary where tg_id={id}');
        rel = mycursor.fetchone()[0];
        if rel != '': await msg.answer('Выберите продукт:', reply_markup=product_classification_menu9(rel))
        else: await msg.answer('Выберите продукт:', reply_markup=product_classification_menu9(''))

@dp.message_handler(Text(equals=product_classification[10]))
async def product_classification10(msg: types.Message):
    text = msg["text"];
    id = msg["from"]["id"]
    if getUserFinded(msg["from"]["id"]):
        mycursor.execute(SQL_REQUESTS['SWITCH_OFF_SAFE_UPDATES']);
        mycursor.execute(SQL_REQUESTS["UPDATE_MENU_CLASSIFICATION"], (text, id));
        mydb.commit();
        mycursor.execute(f'select exceptions from diet_diary where tg_id={id}');
        rel = mycursor.fetchone()[0];
        if rel != '': await msg.answer('Выберите продукт:', reply_markup=product_classification_menu10(rel))
        else: await msg.answer('Выберите продукт:', reply_markup=product_classification_menu10(''))
    else:
        mycursor.execute(SQL_REQUESTS['INSERT'], (id, '', '', text, 0, ''));
        mydb.commit();
        mycursor.execute(f'select exceptions from diet_diary where tg_id={id}');
        rel = mycursor.fetchone()[0];
        if rel != '': await msg.answer('Выберите продукт:', reply_markup=product_classification_menu10(rel))
        else: await msg.answer('Выберите продукт:', reply_markup=product_classification_menu10(''))

@dp.message_handler(Text(equals=product_classification[11]))
async def product_classification11(msg: types.Message):
    text = msg["text"];
    id = msg["from"]["id"]
    if getUserFinded(msg["from"]["id"]):
        mycursor.execute(SQL_REQUESTS['SWITCH_OFF_SAFE_UPDATES']);
        mycursor.execute(SQL_REQUESTS["UPDATE_MENU_CLASSIFICATION"], (text, id));
        mydb.commit();
        mycursor.execute(f'select exceptions from diet_diary where tg_id={id}');
        rel = mycursor.fetchone()[0];
        if rel != '': await msg.answer('Выберите продукт:', reply_markup=product_classification_menu11(rel))
        else: await msg.answer('Выберите продукт:', reply_markup=product_classification_menu11(''))
    else:
        mycursor.execute(SQL_REQUESTS['INSERT'], (id, '', '', text, 0, ''));
        mydb.commit();
        mycursor.execute(f'select exceptions from diet_diary where tg_id={id}');
        rel = mycursor.fetchone()[0];
        if rel != '': await msg.answer('Выберите продукт:', reply_markup=product_classification_menu11(rel))
        else: await msg.answer('Выберите продукт:', reply_markup=product_classification_menu11(''))

@dp.message_handler(Text(equals=createProductArr()))
async def product_amount(msg: types.Message):
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    kb.add('Вернуться к выбору продукта');
    for i in range(1, 11): btn = KeyboardButton(f'{i}, {msg["text"]}'); kb.add(btn);
    await msg.answer('Выберите количество употребляемого продукта:', reply_markup=kb)

def class_choice(classific, exceptions):
    if classific == product_classification[0]: return product_classification_menu0(exceptions)
    if classific == product_classification[1]: return product_classification_menu1(exceptions)
    if classific == product_classification[2]: return product_classification_menu2(exceptions)
    if classific == product_classification[3]: return product_classification_menu3(exceptions)
    if classific == product_classification[4]: return product_classification_menu4(exceptions)
    if classific == product_classification[5]: return product_classification_menu5(exceptions)
    if classific == product_classification[6]: return product_classification_menu6(exceptions)
    if classific == product_classification[7]: return product_classification_menu7(exceptions)
    if classific == product_classification[8]: return product_classification_menu8(exceptions)
    if classific == product_classification[9]: return product_classification_menu9(exceptions)
    if classific == product_classification[10]: return product_classification_menu10(exceptions)
    if classific == product_classification[11]: return product_classification_menu11(exceptions)

@dp.message_handler(Text(equals='Вернуться к выбору продукта'))
async def return_to_choice_product(msg: types.Message):
    id = msg["from"]["id"];
    mycursor.execute(f'SELECT menu_classification from diet_diary WHERE tg_id={id}');
    rel = mycursor.fetchone()[0];
    mycursor.execute(f'SELECT exceptions from diet_diary WHERE tg_id={id}');
    exc = mycursor.fetchone()[0];
    await msg.answer('Возврат к выбору продукта:', reply_markup=class_choice(rel, exc));


