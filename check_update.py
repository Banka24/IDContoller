from definitions import input_data
from connect import connection

def check_users():
    first_name, second_name = input_data()    
    try:
        with connection.cursor() as cursor:                    
            cursor.execute("SELECT id, firstname, secondname, birthdate FROM `users` WHERE firstname = %s AND secondname = %s", (first_name, second_name))
            results = cursor.fetchall()
            if results:
                for result in results:
                    print(f"| {result['id']} | {result['secondname']} | {result['firstname']} | {result['birthdate']} |")
            else:
                print("Такого имени нет в БД!")                                      
    except Exception:
        print("Произошла ошибка...") 

def update_users():
    pass  