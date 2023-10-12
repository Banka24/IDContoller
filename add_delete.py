from definitions import input_data
from connect import connection


def add_users():
    first_name, second_name, birthdate = input_data()    
    if first_name != '' and second_name != '' and birthdate != '0000-00-00':
        try:
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO `users` (firstname, secondname, birthdate) VALUES (%s, %s, %s)", (first_name, second_name, birthdate))
                connection.commit()
            print(f"Пользователь {second_name} {first_name} был зарегестрирован.")
        except Exception:
            print("Произошла ошибка...")                    
    else:
        print("Некорректные данные.")

def delete_users():
    first_name, second_name, birthdate = input_data()    
    with connection.cursor() as cursor: 
        cursor.execute("DELETE FROM `users` WHERE firstname = %s AND secondname = %s AND birthdate = %s", (first_name, second_name, birthdate))
    commit = input("Вы уверены? да/нет: ")
    if commit == 'да':                                
        connection.commit() 
        print("Пользователь удалён успешно!")