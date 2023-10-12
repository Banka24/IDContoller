from connect import connection
from definitions import CheckName
from add_delete import add_users, delete_users
from check_update import check_users, update_users

SystemOn = True

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
            add_users()

        case 2:
            check_users()    
                        
        case 3:
           delete_users()

        case 4:
            update_users()      
            
        case 5:
            connection.close()                       
            SystemOn = False     
