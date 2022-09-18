import logging
from loader import bot, storage;
from random import randint;
import schedule;
from threading import Thread;
import requests;
from time import sleep;
from db import mycursor;
TOKEN = '5533174693:AAEoKmwRzH9-tLsDVxpvZ5xaZDjaIzfvN_w';
#* SQL requests
SQL_REQUESTS = {
    "SELECT_ALL": "SELECT * FROM patient",
    "SELECT_ID_AND_CHAT_ID": "SELECT ID, CHAT_ID FROM patient",
    "SELECT_CHAT_ID": "SELECT CHAT_ID FROM patient",
    "INSERT_ALL": "INSERT INTO patient (CHAT_ID, GROUP_REC, PUSH_NOTIFICATIONS) VALUES (%s,%s,%s)"
}

evening1 = 'https://sun9-west.userapi.com/sun9-15/s/v1/ig2/8BDWYNHl5o-rZKTg0Vr-nMXZhHsZz1OeVhrnCqIiN8QePTitUYg9aQS1LM66iKenRUWqeISoTJZhp5r-qGqj3mds.jpg?size=2160x2160&quality=96&type=album';
evening2 = 'https://sun9-north.userapi.com/sun9-88/s/v1/ig2/sqPBjOy0Hyev5TX44nJlN-XjyBjZrDwZnK-sLYrYSuPJiackbzOvVWem7BUy9edLYFD-y8GHQUBpm5O-CWBv1wHo.jpg?size=2160x2160&quality=96&type=album';
evening3 = 'https://sun3.userapi.com/sun3-11/s/v1/ig2/ne0OA3Q_tn8cjEot6A1j5ZAShgWveI0uACjv61C26ZZFyVi1_viW6u1IVCmrqcPO9b8r22_Xz9CSNmEunOte5Ran.jpg?size=2160x2160&quality=96&type=album';
evening4 = 'https://sun9-west.userapi.com/sun9-50/s/v1/ig2/fWj5cI-pOSCqyzDpwfXHP9XNXTZtmyB98iHOKNZ5Y-3WHcu4JDFOmAH3lhyr6dNFNt7R_T_Ibn9g_gaszmI_090I.jpg?size=2160x2160&quality=96&type=album';
evening6 = 'https://sun9-north.userapi.com/sun9-84/s/v1/ig2/sovFUws9QRUavbNhS3643vtsxfmcx6pzcalTYc47BY-fYPFWC0YBGMahpsz5D0Sv5fECheJpZgtheN7fx5-XMuFG.jpg?size=2160x2160&quality=96&type=album';
evening7 = 'https://sun3.userapi.com/sun3-8/s/v1/ig2/r7x9jTGBR5zoqvK9MFA7WnJM5Mj-bJWn01sVwRdrPiVwSRUlGDGhpL5qZtLghhVIgJc6JFPa1q5hOuTkEDlEQV1H.jpg?size=2160x2160&quality=96&type=album';

morning1 = 'https://sun9-west.userapi.com/sun9-68/s/v1/ig2/jQFpKEiQRORO_FSmMjHJwAm8sDo7GYuNhAvRXKh1RKu1Cq71wGy5XABwfH8PSC8DQc2SfVAGP45einZ6JUL-iCeH.jpg?size=2160x2160&quality=96&type=album';
morning2 = 'https://sun9-west.userapi.com/sun9-45/s/v1/ig2/YvQkHQal7Y4UkMrDZc6FeHYuFY04oLOvm5ZuDPh8qdE8BpQqNn_tnDXPnU5jf4__mEtrFWY2zW5Yap6YPCaj7zHt.jpg?size=2160x2160&quality=96&type=album';
morning3 = 'https://sun9-west.userapi.com/sun9-15/s/v1/ig2/QmSsIBysFxKd1iQ37ayUsB8bxYJAVCk-FfYlkraT8Wa4qV4A-NM2h9vv4lVgHyfHSwtGnAnRmer9uwq1Z4xmQRW1.jpg?size=2160x2160&quality=96&type=album'
morning4 = 'https://sun9-east.userapi.com/sun9-24/s/v1/ig2/8Z36B3ZtG4YbayAXy-Ur0PcpBlYZ1I-ye-io356XmxjLMjTmtBxVkLiKE9b2vk2YwA693RK79BfiGjlA03rSuqm5.jpg?size=2160x2160&quality=96&type=album'
morning5 = 'https://sun9-east.userapi.com/sun9-36/s/v1/ig2/qj6_dC90eGoSzEb4OPpEq50kU_eEPOhtLwYpTFK8RfjrEgVzvBPAbt_FzS-0ytt4_rEsIZ8H5SZvB4zh8zYYmvKC.jpg?size=2160x2160&quality=96&type=album'
morning6 = 'https://sun9-north.userapi.com/sun9-88/s/v1/ig2/gw4IulXWhSp43XBuafDb67aiRCtW3jG2yy1OZ5CcOHz0PM5sLdpgQJ2-pfnHHjR6LRK8yA-sV95Ncglm_gDZhDjR.jpg?size=2219x2160&quality=96&type=album'
morning7 = 'https://sun3.userapi.com/sun3-12/s/v1/ig2/mOGimbl-ryZPqcFTMwCY9mhEvLgCjc6WkKM1D3zxqpd7Ycw0u70UdOFp_g1RIDxFAMux6P2VKMKtDNW_9DzPQShx.jpg?size=2160x2160&quality=96&type=album'
PHOTOS_URLS_MORNING = [morning1, morning2, morning3, morning4, morning5, morning7]
PHOTOS_URLS_EVENING = [evening1, evening2, evening3, evening4, evening6, evening7]
#* Рекомендации на утро для пользователя с определенной группой (input int, return str)
def group_recomendations_morning(group):
    if group == 1:
        return PHOTOS_URLS_MORNING[randint(0, 6)];
    elif group == 2:
        return PHOTOS_URLS_MORNING[randint(0, 6)];
#* Рекомендации на вечер для пользователя с определенной группой (input int, return str)
def group_recomendations_evening(group):
    if group == 1:
        return PHOTOS_URLS_EVENING[randint(0, 5)];
    elif group == 2:
        return PHOTOS_URLS_EVENING[randint(0, 5)];
#* Отправляет сообщение определнной рекомендации из функций выше (input [int, str], return [Object|str])
def send_message(id, photo):
    data = {
        "chat_id": id,
        "photo": photo
    };
    body = requests.post(f'https://api.telegram.org/bot{TOKEN}/sendPhoto', data).json();
    if body["ok"]: return body;
    else: print(f'{body["error_code"]} {body["description"]}');
#* Отправка уведомлений всем пользователям утром
def push_notification_morning():
    mycursor.execute(SQL_REQUESTS["SELECT_ALL"]);
    ids = mycursor.fetchall();
    for i in range(len(ids)):
        tg_id = ids[i][1];
        group_rec = ids[i][2];
        push_notific = ids[i][3];
        if push_notific == 1:
            send_message(tg_id, group_recomendations_morning(group_rec));
#* Отправка уведомлений всем пользователям вечером
def push_notification_evening():
    mycursor.execute(SQL_REQUESTS["SELECT_ALL"]);
    ids = mycursor.fetchall();
    for i in range(len(ids)):
        tg_id = ids[i][1];
        group_rec = ids[i][2];
        push_notific = ids[i][3];
        if push_notific == 1:
            send_message(tg_id, group_recomendations_evening(group_rec));
#* Чекер времени для тредов
def schedule_checker():
    while True:
        schedule.run_pending();
        sleep(60);

async def on_shutdown(dp):
    await bot.close()
    await storage.close()


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp
    schedule.every().day.at('22:00').do(push_notification_morning);
    schedule.every().day.at('22:01').do(push_notification_evening);
    Thread(target=schedule_checker).start();
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, on_shutdown=on_shutdown)
