from functional import *
from menu import *
import os

os.system('CLS')  # очистка консоли
currPose = 0

fileContent = readFile('phoneBook.txt')  # чтение файла-хранилища в память
mainMenu(fileContent, currPose)
