from functional import *
import os


def mainMenu(fileContent, pos):                                   # Функция главного меню
    tempList = list()

    getQuit = False  # флаг для выхода из меню
    while getQuit != True:
        os.system('CLS')
        print('* * * * * * * * * * * * Список абонентов * * * * * * * * * * * ')
        printAb(fileContent)

        print('* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * ')
        print()
        print('Введите цифру пункта меню и нажмите Enter. ')
        print('1. Поиск абонента c возможностью изменения записи абонента')
        print('2. Поиск абонента c возможностью удаления записи абонента')
        print('3. Отображение списока абонентов')
        print('4. Добавление нового абонента')
        print('5. Сохранить изменения')
        print('Q/q - Выйти из программы')
        choice = input('Ваш выбор: ')
        choice = choice.lower()
        if choice == 'Q' or choice == 'q' or choice == 'й' or choice == 'Й':
            getQuit = True
            saveFile(fileContent, 'phoneBook.txt')
            print()
            print('До встречи!')
            print()
        if choice == '1':
            fileContent = findAbofCng(fileContent)

        if choice == '2':
            fileContent = findAbofDlt(fileContent)

        if choice == '3':
            printAb(readFile('phoneBook.txt'))

        if choice == '4':
            fileContent = addAb(readFile('phoneBook.txt'))

        if choice == '5':
            saveFile(fileContent, 'phoneBook.txt')

    return fileContent
