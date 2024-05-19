from config import host, user, password, db_name
import pymysql

host = host
user = user
password = password
db_name = db_name

try:
    connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    print("Подключение успешно...") 
    cursor = connection.cursor()
    table_name = "users"
    cursor.execute(f"SHOW TABLES LIKE '{table_name}'")
    result = cursor.fetchone()
    if result is None:
        create_table = "CREATE TABLE `users`(id int AUTO_INCREMENT, secondname varchar(32), firstname varchar(32), birthdate DATE, PRIMARY KEY (id))"
        cursor.execute(create_table)        

except Exception as ex:
    print("Connection refused...")
    print(ex) 