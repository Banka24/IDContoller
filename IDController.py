import pymysql

SystemOn = True
host = "localhost"
user = "root"
password = "root"
db_name = "idcontroller"

# def CheckNumber():
#     number = int(input("Введите число: "))
#     if isinstance(number, int):
#         return number
#     else:
#         print("Введите число!")

def CheckName():
    name = input("Введите имя/фамилию: ")
    for char in name:
        if char not in "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя": 
            name = ''     
    return name 

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
        create_table = "CREATE TABLE `users`(id int AUTO_INCREMENT, firstname varchar(32), secondname varchar(32), PRIMARY KEY (id))"
        cursor.execute(create_table)        

except Exception as ex:
    print("Connection refused...")
    print(ex)  
        
while SystemOn: 

    print("IDControl v0.2", "Вы можете: 1)внести человека в БД, 2)проверить его наличие в БД, 3)удалить его из БД.","Если вы хотите выйти введите любую другую цифру.", sep='\n')

    try:
        operator = int(input("Введите номер операции: "))
    except ValueError:
        print("Введите число!")     

    match operator:

        case 1:
            print("Вы должны ввести имя и фамилию")            
            first_name = CheckName() 
            second_name = CheckName()    
            if first_name != '' and second_name != '':
                try:
                    with connection.cursor() as cursor:
                        cursor.execute("INSERT INTO `users`(firstname, secondname) VALUES (%s, %s)", (first_name, second_name))
                        connection.commit()
                    print(f"Пользователь {second_name} {first_name} был зарегестрирован.")
                except Exception as ex:
                    print("Произошла ошибка...")                    
            else:
                print("Некорректно введены имя или фамилия.")

        case 2:    
            first_name = CheckName()       
            second_name = CheckName()         
            try:
                with connection.cursor() as cursor:                    
                    cursor.execute("SELECT firstname, secondname FROM `users` WHERE firstname = %s AND secondname = %s", (first_name, second_name))
                    result = cursor.fetchone()
                    if result is not None:
                        print(f"Пользователь {result['firstname']}, {result['secondname']} найден в БД.")
                    else:
                        print("Такого имени нет в БД!")                                      
            except Exception as ex:
                print("Произошла ошибка...")       
                        
        case 3:
            first_name = CheckName()        
            second_name = CheckName()
            cursor.execute("DELETE FROM `users` WHERE firstname = %s AND secondname = %s", (first_name, second_name))                
            connection.commit() 
            print("Пользователь удалён успешно!")        
            
        case _:
            connection.close()                       
            SystemOn = False        
