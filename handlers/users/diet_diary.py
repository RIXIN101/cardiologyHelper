## -*- coding: utf-8 -*-
import logging;
import requests;
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, ParseMode;
from loader import dp;
from openpyxl import load_workbook;
from aiogram.dispatcher.filters import Text
from aiogram import types;
from db import mycursor, mydb, SQL_REQUESTS;
#* Открытие файла excel для чтения
read = load_workbook("Produkty.xlsx", data_only=True);
read_sheet = read.active;
TOKEN = "5533174693:AAEoKmwRzH9-tLsDVxpvZ5xaZDjaIzfvN_w";

RECOMENDATIONS_TEXT = {
    "MORE_CARBONYHYDRATES": " 🍰🍬При избытке углеводов необходимо избегать чрезмерного потребления простых углеводов:❗️сахар,белый хлеб, вареный картофель, свекла, белый рис, кукурузные хлопья, манная каша, пшено, лапша из мягких сортов пшеницы, сдобная выпечка, молочный шоколад, джем, бананы, дыня❗️\n ❤️🍫 Для тех, кому сложно отказаться от сладкого альтернативой могут стать: мед, виноград, финики, курага, изюм без косточек, чернослив, арбуз 🍇🍉",

    "LESS_CARBONYHYDRATES": " 📉При дефиците углеводов в рационе следует употреблять больше пищи, содержащей сложные углеводы \n🥖🍝цельнозерновой хлеб и хлебцы, макароны из твердых сортов пшеницы, овсяную крупу, коричневый рис, гречневую крупу, чечевицу, фасоль, бобы, нут, редьку, морковь, шпинат, салат, капусту, петрушку, укроп, яблоки, абрикосы, горький шоколад🥬🥕\n ❗️Кроме того, дефицит углеводов можно восполнять и простыми углеводами (белый рис, кукурузные хлопья, картофель, манная каша, пшено, лапша из мягких сортов пшеницы, сдобная выпечка, молочный шоколад, мед, арбуз, ананас) 🥔🍫🍉\n ❗️🤓 При этом основная доля углеводов должна приходиться на сложные углеводы и только 5-10 % - на простые углеводы (сахара).",

    "MORE_PROTEINS": " 🥵💪🏻 При избытке белка в рационе следует ограничить ❌ потребление продуктов, богатых белками животного 🐮 и растительного 🌱 происхождения. \n 📍К первым относится: икра, рыба, мясо, птица, сыр и яйца 🥩🥚\n 📍Растительными белками богаты: фасоль, нут, грецкий орех, гречиха, пшеница, капуста белокочанная, тофу 🌰🫘",
    "LESS_PROTEINS": "😮‍💨💪🏻При недостатке белка в рационе следует употреблять больше пищи, в которой содержится необходимое количество животного белка 🐮🥩\n 📍В рацион включаются такие продукты, как: икра, рыба, мясо, птица, сыр и яйца.\n 📍Кроме того, включаются продукты, богатые растительными белками 🌱, это: фасоль, нут, грецкий орех, гречиха, пшеница, капуста белокочанная, тофу 🌰\n ❗️🤓 При этом одна половина суточной нормы должна быть растительного происхождения🌱, а вторая – животного🐮",

    "MORE_FATS": " 🆘🍕При избытке жиров в рационе следует уменьшить ❌ употребление насыщенных жиров, которые присутствуют в сливочном масле, мясе, сале, кокосовом и пальмовом маслах 🍖🧈\n ❗️❤️ Предпочтение отдать потреблению жиров, которые присутствуют в подсолнечном, кукурузном, хлопковом, соевом, льняном и рапсовом маслах 🌽жирных сортах рыбы и рыбьем жире 🐟 так же в оливковом и арахисовом маслах, авокадо, маслинах и мясе птицы 🥑\n ❗️Для снижения количества жиров в рационе необходимо перестать жарить пищу на масле 🥵 а использовать для этого сковороду с антипригарным покрытием 🤓\n ❗️В один или два приема пищи есть нежирный белок, например, нежирную рыбу, куриное филе, нежирный творог 🐟\n ❗️Снимать кожу с птицы и срезать видимый жир с мяса до приготовления 🔪 \n ❗️отказаться от фастфуда, колбас и полуфабрикатов ❌🍔🍟",

    "LESS_FATS": "📉При дефиците жиров в рационе необходимо потреблять продукты, богатые в первую очередь полиненасыщенными жирами 🧬 которые содержатся в: подсолнечном, кукурузном, хлопковом, соевом, льняном и рапсовом маслах; жирных сортах рыб и рыбьем жире 🐠🌽\n ❗️Кроме того, мононенасыщенные жиры содержатся в оливковом и арахисовом маслах, авокадо, маслинах и мясе птицы.🥑\n ❗️В последнюю очередь нужно отдавать предпочтение насыщенным жирам ☹️, которые присутствуют в сливочном масле, мясе, сале, кокосовом и пальмовом маслах 🧈🍖\n ☺️ Благоприятным считается соотношение 70% растительных жиров 🌱 к 30% животных жиров в рационе 🐮",

    "LESS_DIETARY_FIBER": "☹️🥕🍎 При дефиците пищевых волокон следует увеличить 📈 потребление неусвояемых углеводов, которыми богаты: 🥖хлеб грубого помола, недробленые крупы, отруби, свежие овощи, фрукты и ягоды, фасоль, горох, орехи и сухофрукты 🍅🥕🥦🍒",

}


product_classification = [
    "Молоко и молочные продукты",
    "Яйцепродукты",
    "Мясо и мясные продукты ",
    "Рыба. Нерыбные объекты промысла и продукты из них",
    "Жировые продукты (жирностью более 50%)",
    "Зерно и продукты его переработки",
    "Бобовые, орехи",
    "Овощи, грибы и продукты их переработки",
    "Фрукты, ягоды и продукты их переработки",
    "Кондитерские изделия",
    "Напитки",
    "Вспомогательные пищевые продукты и улучшители вкуса"
];

def createClassificationMenu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True);
    kb.add('Отмена ввода дневника')
    for i in range(len(product_classification)): btn = KeyboardButton(product_classification[i]); kb.add(btn);
    return kb;

def createProductArr():
    product_arr = [];
    product = read_sheet["A3:A1091"];
    for i in range(len(product)):
        product_arr.append(product[i][0].value);
    for i in range(len(product_classification)):
        product_arr.remove(product_classification[i]);
    return product_arr;

amount_product = read_sheet["A3:A1091"]
amount_arr = []
for i in range(len(amount_product)):
    a = amount_product[i][0].value.strip()
    for j in range(1, 11):
        amount_arr.append(f'{j}, {a}')

@dp.message_handler(Text(equals='Рассчитать дневник питания'))
async def test(msg: types.Message):
    logging.info(f'diet_diary_start: user = {msg.from_user.id}');
    await msg.answer('Выберите классификацию продукта:', reply_markup=createClassificationMenu());

@dp.message_handler(Text(equals='Отмена ввода дневника'))
async def cancellation(msg: types.Message):
    id = msg["from"]["id"];
    logging.info(f'diet_diary_cancellation: user = {msg.from_user.id}');
    await msg.answer('Отмена ввода дневника питания...', reply_markup=ReplyKeyboardRemove());
    mycursor.execute(f'delete from diet_diary where tg_id = {id}');
    mydb.commit();
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True);
    kb.add(KeyboardButton('Вернуться в меню'))
    await msg.answer('Вернуться в главное меню?', reply_markup=kb);

@dp.message_handler(Text(equals='Вернуться к выбору классификации'))
async def return_to_choice_product(msg: types.Message):
    await msg.answer('Возврат к выбору классификации продукта:', reply_markup=createClassificationMenu());

def getAllFromDietDiary(id):
    mycursor.execute(f'select * from diet_diary where tg_id = {id}');
    rel = mycursor.fetchall()[0];
    products = rel[1].split(',');
    if products[-1] == '': products.pop(-1);
    amount = rel[2].split(',');
    if amount[-1] == '': amount.pop(-1);
    string = ''
    for i in range(len(products)):
        string += f'   {amount[i]} порции/й {products[i]}\n';
    text = 'Вот что вы ввели в дневник питания:\n'+string+"\nХотите ещё добавить продукт или расчитать Ваш дневник питания?"
    return text;

@dp.message_handler(Text(equals=amount_arr))
async def product_handler(msg: types.Message):
    id = msg["from"]["id"];
    text = msg["text"].split(',')
    am = text[0]; text.remove(am);
    name = ''.join(text).strip();
    mycursor.execute(f'select products from diet_diary where tg_id = {id}'); products = mycursor.fetchone()[0];
    mycursor.execute(f'select amount from diet_diary where tg_id = {id}'); amount = mycursor.fetchone()[0];
    mycursor.execute(f'select exceptions from diet_diary where tg_id = {id}'); cur_exceptions = mycursor.fetchone()[0];
    mycursor.execute(f'select counter from diet_diary where tg_id = {id}'); counter = mycursor.fetchone()[0];
    mycursor.execute(SQL_REQUESTS["SWITCH_OFF_SAFE_UPDATES"]);
    mycursor.execute(SQL_REQUESTS["UPDATE_OTHER"], ( amount+am+',' , products+name+',' ,cur_exceptions+name+',' ,counter+1 , msg["from"]["id"]));
    mydb.commit();

    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True);
    kb.add(KeyboardButton('Добавить продукт'));
    kb.add(KeyboardButton('Рассчитать дневник'));

    await msg.answer(getAllFromDietDiary(id), reply_markup=kb)

@dp.message_handler(Text(equals='Добавить продукт'))
async def plus_one(msg: types.Message):
    logging.info(f'diet_diary_add: user = {msg.from_user.id}');
    id = msg["from"]["id"];
    mycursor.execute(f'select counter from diet_diary where tg_id = {id}'); counter = mycursor.fetchone()[0];
    if counter >= 10:
        kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True);
        kb.add(KeyboardButton('Рассчитать дневник'));
        await msg.answer(f'Вы не можете добавить больше 10 продуктов.\n{getAllFromDietDiary(id)}', reply_markup=kb);
    else: await msg.answer('Добавление продукта:', reply_markup=createClassificationMenu());

def createSheetArr():
    product_arr = [];
    product = read_sheet["A3:A1091"];
    for i in range(len(product)):
        product_arr.append(product[i][0].value.strip());
    return product_arr;

def getInfoFromProducts(names, id):
    products_and_classification_arr = createSheetArr();
    names_arr = names.split(',');
    if names_arr[-1] == '': names_arr.pop(-1);
    arr = [];
    mycursor.execute(f'select amount from diet_diary where tg_id={id}');
    amount = mycursor.fetchone()[0].split(',');
    if amount[-1] == '': amount.pop(-1);
    for i in range(len(names_arr)):
        product_index = products_and_classification_arr.index(names_arr[i])+3;
        middle_weight = read_sheet[f'B{product_index}'].value;
        calories = read_sheet[f'C{product_index}'].value;
        carbohydrates = read_sheet[f'D{product_index}'].value;
        proteins = read_sheet[f'E{product_index}'].value;
        fats = read_sheet[f'F{product_index}'].value;
        dietary_fiber = read_sheet[f'G{product_index}'].value;
        arr.append((int(amount[i]), middle_weight, calories, carbohydrates, proteins, fats, dietary_fiber));
    return arr;

def send_message_for_recomendations(text, id):
    data = {
        "chat_id": id,
        "text": text
    };
    body = requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage', data).json();
    return body;


def getRecomendations(carbohydrates, proteins, fats, dietary_fiber):
    text = {
        "carbo": "",
        "prote": "",
        "fats": "",
        "diet_fib": ""
    };

    if carbohydrates > 200: text["carbo"] = RECOMENDATIONS_TEXT["MORE_CARBONYHYDRATES"];
    elif carbohydrates < 200: text["carbo"] = RECOMENDATIONS_TEXT["LESS_CARBONYHYDRATES"];

    if proteins > 50: text["prote"] = RECOMENDATIONS_TEXT["MORE_PROTEINS"];
    elif proteins < 50: text["prote"] = RECOMENDATIONS_TEXT["LESS_PROTEINS"];

    if fats > 50: text["fats"] = RECOMENDATIONS_TEXT["MORE_FATS"];
    elif fats < 50: text["fats"] = RECOMENDATIONS_TEXT["LESS_FATS"];

    if dietary_fiber < 30: text["diet_fib"] = RECOMENDATIONS_TEXT["LESS_DIETARY_FIBER"];

    return text;

def dietDiaryCalculation(info):
    diet = {
        "calories": 0,
        "carbohydrates": 0,
        "proteins": 0,
        "fats": 0,
        "dietary_fiber": 0,
        "weight": 0
    }
    #* количество порций* вес порции * значение / 100
    for i in range(len(info)):
        diet['calories'] += (info[i][0] * info[i][1] * info[i][2]) // 100;
        diet['carbohydrates'] += (info[i][0] * info[i][1] * info[i][3]) // 100;
        diet['proteins'] += (info[i][0] * info[i][1] * info[i][4]) // 100;
        diet['fats'] += (info[i][0] * info[i][1] * info[i][5]) // 100;
        diet['dietary_fiber'] += (info[i][0] * info[i][1] * info[i][6]) // 100;
        diet['weight'] += info[i][0] * info[i][1]
    return diet;

@dp.message_handler(Text(equals='Рассчитать дневник'))
async def diet_diary_handler(msg: types.Message):
    logging.info(f'diet_diary_ended: user = {msg.from_user.id}');
    id = msg["from"]["id"];
    mycursor.execute(f'select * from diet_diary where tg_id = {id}');
    result = mycursor.fetchone();
    info = getInfoFromProducts(result[1], id);
    diet = dietDiaryCalculation(info);
    calculated_diet_diary = f"⚠️Все данные усреднены. Калькулятор не является достоверным источником точных цифр и носит рекомендательный характер по питанию. Точную информацию и рекомендации даст лечащий врач!\n\nРасчет дневника питания:\n     Ккал: {round(diet['calories'], 2)}\n     Углеводы: {round(diet['carbohydrates'], 2)}\n     Белки: {round(diet['proteins'], 2)}\n     Жиры: {round(diet['fats'], 2)}\n     Пищевые волокна: {round(diet['dietary_fiber'], 2)}";
    additional_recommendations = getRecomendations(diet['carbohydrates'], diet['proteins'], diet['fats'], diet['dietary_fiber']);
    await msg.answer(calculated_diet_diary, reply_markup=ReplyKeyboardRemove());
    await msg.answer(additional_recommendations["carbo"], reply_markup=ReplyKeyboardRemove());
    await msg.answer(additional_recommendations["prote"], reply_markup=ReplyKeyboardRemove());
    await msg.answer(additional_recommendations["fats"], reply_markup=ReplyKeyboardRemove());
    if additional_recommendations["diet_fib"] != '':
        await msg.answer(additional_recommendations["diet_fib"], reply_markup=ReplyKeyboardRemove());

    mycursor.execute(f'delete from diet_diary where tg_id = {id}');
    mydb.commit();
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True);
    kb.add(KeyboardButton("Вернуться в меню"))
    await msg.answer("Вернуться в меню?", reply_markup=kb);