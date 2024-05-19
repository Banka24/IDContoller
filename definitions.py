def input_data(): 
    print("Вы должны ввести фамилию и имя")
    first_name, second_name = input("Введите имя: "), input("Введите фамилию: ")
    for char in first_name.lower():
        if char not in "абвгдеёжзийклмнопрстуфхцчшщъыьэюя": 
            first_name = ''
    for char in second_name.lower():
        if char not in "абвгдеёжзийклмнопрстуфхцчшщъыьэюя": 
            second_name = ''
    birthdate = input("Введите дату рождения (ГГГГ-ММ-ДД): ")     
    return first_name, second_name, birthdate
