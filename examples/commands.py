from djitellopy import Tello # импорт класса управления одним дроном

from time import sleep # импорт сна из стандартной библиотеки времени

drone = Tello() # дрон по адресу 192.168.10.1

# контекстным методом открываем файл commands.txt, указав кодировку
with open('commands.txt', encoding='utf-8-sig') as file:

    text = file.read() # сохраняем все содержимое файла в переменную

    text = text.split('\n') # разбиваем текст на массив строк по символу переноса

    drone.connect() # подключение к дрону

    for command in text: # для каждой строки в полученном массиве

        command = command.strip() # удаляем пробелы слева и справа

        if command[:5] == 'sleep': # если команда начинается со слова sleep

            sleep(int(command[6:])) # спать указанное число секунд

        elif command not in ('', '\n'): # иначе, если строка не пустая

            drone.send_command_with_return(command) # отправляем команду дрону со стандартной задержкой