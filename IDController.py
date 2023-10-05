import pymysql

SystemOn = True
host = "localhost"
user = "root"
password = "root"
db_name = "idcontroller"

def CheckSecondName():
    name = input("Введите фамилию: ")
    for char in name:
        if char not in "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя": 
            name = ''     
    return name 

def CheckFirstName():
    name = input("Введите имя: ")
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
        create_table = "CREATE TABLE `users`(id int AUTO_INCREMENT, secondname varchar(32), firstname varchar(32), birthdate DATE, PRIMARY KEY (id))"
        cursor.execute(create_table)        

except Exception as ex:
    print("Connection refused...")
    print(ex)  
        
while SystemOn: 

    print("IDControl v0.3", "Вы можете: 1)внести человека в БД, 2)проверить его наличие в БД, 3)удалить его из БД.","5) Выход из программы.", sep='\n')

    valid_input = False
while not valid_input:
    try:
        operator = int(input("Введите номер операции: "))
        valid_input = True
    except ValueError:
        print("Введите число!")            

    match operator:

        case 1:
            print("Вы должны ввести фамилию и имя")            
            first_name = CheckFirstName() 
            second_name = CheckSecondName()
            birthdate = input("Введите дату рождения (ГГГГ-ММ-ДД): ")    
            if first_name != '' and second_name != '' and birthdate != '0000-00-00':
                try:
                    with connection.cursor() as cursor:
                        cursor.execute("INSERT INTO `users` (firstname, secondname, birthdate) VALUES (%s, %s, %s)", (first_name, second_name, birthdate))
                        connection.commit()
                    print(f"Пользователь {second_name} {first_name} был зарегестрирован.")
                except Exception as ex:
                    print("Произошла ошибка...")                    
            else:
                print("Некорректные данные.")

        case 2:    
            first_name = CheckFirstName()       
            second_name = CheckSecondName()         
            try:
                with connection.cursor() as cursor:                    
                    cursor.execute("SELECT id, firstname, secondname, birthdate FROM `users` WHERE firstname = %s AND secondname = %s", (first_name, second_name))
                    result = cursor.fetchone()
                    if result is not None:
                        print(f"{result['id']} |{result['secondname']} | {result['firstname']}| {result['birthdate']}")
                    else:
                        print("Такого имени нет в БД!")                                      
            except Exception as ex:
                print("Произошла ошибка...")       
                        
        case 3:
            first_name = CheckFirstName()        
            second_name = CheckSecondName()
            birthdate = input("Введите дату рождения (ГГГГ-ММ-ДД): ")
            with connection.cursor() as cursor: 
                cursor.execute("DELETE FROM `users` WHERE firstname = %s AND secondname = %s AND birthdate = %s", (first_name, second_name, birthdate))
            commit = input("Вы уверены? y/n: ")
            if commit == 'y':                                
                connection.commit() 
                print("Пользователь удалён успешно!")        
            
        case 5:
            connection.close()                       
            SystemOn = False  
   
