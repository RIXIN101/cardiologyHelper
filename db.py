import mysql.connector;
#* Создание коннектора к базе данных
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "A6KWL1Y9f7cM",
    database = "cardiodbnewversion"
);
mycursor = mydb.cursor();

SQL_REQUESTS = {
    "SWITCH_OFF_SAFE_UPDATES": "SET SQL_SAFE_UPDATES=0",
    "INSERT": "INSERT INTO diet_diary (tg_id, products, amount, menu_classification, counter, exceptions) VALUES (%s,%s,%s,%s,%s,%s)",
    "UPDATE_MENU_CLASSIFICATION": "UPDATE diet_diary SET menu_classification = %s WHERE tg_id = %s",
    "UPDATE_OTHER": "UPDATE diet_diary SET amount = %s, products = %s, exceptions = %s, counter = %s WHERE tg_id = %s",
    "SELECT_ALL": "SELECT * FROM patient",
    "SELECT_ID_AND_CHAT_ID": "SELECT ID, CHAT_ID FROM patient",
    "SELECT_CHAT_ID": "SELECT CHAT_ID FROM patient",
    "INSERT_ALL": "INSERT INTO patient (CHAT_ID, GROUP_REC, PUSH_NOTIFICATIONS) VALUES (%s,%s,%s)"
}