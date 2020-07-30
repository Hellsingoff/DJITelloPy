# DJITelloPy
DJITelloPy - библиотека для Python 3.5 и выше, реализующая все команды, доступные в официальном [Tello SDK](https://dl-cdn.ryzerobotics.com/downloads/tello/20180910/Tello%20SDK%20Documentation%20EN_1.3.pdf) и [Tello EDU SDK](https://dl-cdn.ryzerobotics.com/downloads/Tello/Tello%20SDK%202.0%20User%20Guide.pdf). Некоторые функции становятся более понятными после изучения инструкции по [Mission Pad](https://dl-cdn.ryzerobotics.com/downloads/Tello/Tello%20Mission%20Pad%20User%20Guide.pdf).

Установка через pip
```
pip3 install https://github.com/Hellsingoff/DJITelloPy/archive/master.zip
```
## Использование

### Управление одним дроном

**Tello** - класс, реализующий управление одним дроном.

По умолчанию инициализация не трует аргументов, при этом IP дрона используется стандартный - 192.168.10.1, как при подключении к дрону по Wi-Fi. 

Если дрон подключен к локальной сети - при инициализации класса нужно как аргумент указать строку, содержащую IP дрона.
```python
from djitellopy import Tello # импорт класса управления одним дроном

drone1 = Tello() # дрон по адресу 192.168.10.1

drone2 = Tello('192.168.1.220') # дрон по адресу 192.168.1.220
```

### Методы, применимые к объекту класса Tello
____
#### connect()
Вход в режим управления командами.
```python
from djitellopy import Tello # импорт класса управления одним дроном

drone = Tello() # дрон по адресу 192.168.10.1

drone.connect() # подключение

drone.end() # удаляет drone
```
____
#### connect_to_wifi(ssid, password)
Подключение дрона к существующей локальной сети по Wi-Fi.

Команда поддерживается только Tello EDU.

Первый аргумент - имя сети (строка), второй аргумент - её пароль (строка).

После выполнения команды дрон перезагрузится и подключится к указанной сети.

Дрон запоминает настройку и всегда будет подключаться к этой сети. Для сброса настроек Wi-Fi надо включить дрон и пять секунд держать кнопку питания (до перезагрузки).
```python
from djitellopy import Tello # импорт класса управления одним дроном

drone = Tello() # дрон по адресу 192.168.10.1, мы подключились к создаваемой дроном точке доступа.

drone.connect() # подключение к дрону

drone.connect_to_wifi('example', 'pass') # дрон перезагрузится и подключится к точке example с паролем pass
```
____
#### curve_xyz_speed(x1, y1, z1, x2, y2, z2, speed)
Полёт по дуге (части окружности).

Летит в относительные координаты x2 y2 z2 через x1 y1 z1 со скоростью speed сантиметров в секунду.

Обе координаты указываются в сантиметрах относительно текущего положения, то есть дрон считается точкой начала координатных осей (0 0 0).

Движение по оси X - вперед. По оси Y - влево. По оси Z - вверх.

Координаты x2 y2 z2, x1 y1 z1 и текущее расположение дрона (координаты 0 0 0) должны находиться на окружности радиусом 0.5-10 метров.

Если такую окружность найти не удалось или её радиус не входит в допустимые значения - дрон отправит сообщение об ошибке и сядет.
| Аргумент | Данные | Допустимые значения |
|:----------:|:------------------:|:--------:|
| x1 | int (сантиметры) | -500 - 500 |
| y1 | int (сантиметры) | -500 - 500 |
| z1 | int (сантиметры) | -500 - 500 |
| x2 | int (сантиметры) | -500 - 500 |
| y2 | int (сантиметры) | -500 - 500 |
| z2 | int (сантиметры) | -500 - 500 |
| speed | int (сантиметры в секунду) | 10 - 60 |
```python
from djitellopy import Tello # импорт класса управления одним дроном

drone = Tello() # дрон по адресу 192.168.10.1

drone.connect() # подключение

drone.takeoff() # взлёт

drone.curve_xyz_speed(100, 100, 0, 200, 0, 0, 60) # полёт по полуокружности

drone.land() # приземление

drone.end() # удаляет drone
```
Визуализация примера выше:
![curve_flight](/images/curve.png)
____
#### curve_xyz_speed_mid(x1, y1, z1, x2, y2, z2, speed, mid)
Полёт по дуге (части окружности) относительно Mission pad (коврика).

Команда поддерживается только в Tello EDU.

Необходимо чтобы был активен поиск Mission Pad с помощью [enable_mission_pads()](https://github.com/Hellsingoff/DJITelloPy#enable_mission_pads), а так же чтобы Mission Pad находился в области видимости камеры дрона. (TODO ссылка на область камеры)

Если обнаруживает коврик mid, летит в относительные координаты x2 y2 z2 через x1 y1 z1 со скоростью speed сантиметров в секунду, иначе - выводит ошибку и приземляется.

Обе координаты указываются в сантиметрах относительно положения Mission Pad, то есть Mission Pad считается точкой начала координатных осей (0 0 0). (TODO check)

Движение по оси X - вперед (куда указывает ракета). По оси Y - влево относительно ракеты. По оси Z - вверх от Mission Pad.

Координаты x2 y2 z2, x1 y1 z1 и Mission Pad (координаты 0 0 0) должны находиться на окружности радиусом 0.5-10 метров.

Если такую окружность найти не удалось или её радиус не входит в допустимые значения - дрон отправит сообщение об ошибке и сядет.
| Аргумент | Данные | Допустимые значения |
|:----------:|:------------------:|:--------:|
| x1 | int (сантиметры) | -500 - 500 |
| y1 | int (сантиметры) | -500 - 500 |
| z1 | int (сантиметры) | -500 - 500 |
| x2 | int (сантиметры) | -500 - 500 |
| y2 | int (сантиметры) | -500 - 500 |
| z2 | int (сантиметры) | -500 - 500 |
| speed | int (сантиметры в секунду) | 10 - 60 |
| mid | int (Mission Pad ID) | 1 - 8 |
```python
from djitellopy import Tello # импорт класса управления одним дроном

drone = Tello() # дрон по адресу 192.168.10.1

drone.connect() # подключение

drone.takeoff() # взлёт

drone.curve_xyz_speed_mid(100, 100, 0, 200, 0, 0, 60, 1) # полёт по полуокружности, если найден MP1

drone.land() # приземление

drone.end() # удаляет drone
```
Визуализация примера выше:
![curve_flight](/images/curve.png)
____
#### disable_mission_pads()
Отключает определение Mission Pad.

Команда поддерживается только в Tello EDU.
```python
from djitellopy import Tello # импорт класса управления одним дроном

drone = Tello() # дрон по адресу 192.168.10.1

drone.connect() # подключение

drone.enable_mission_pads() # включаем функцию определения MP

drone.disable_mission_pads() # отключаем функцию определения MP

drone.end() # удаляет drone
```
____
#### emergency()
Экстренная остановка моторов.

Использовать осторожно, во время полёта это неизбежно приведет к падению дрона.

TODO Имеется баг - дрон не даёт никакого ответа на команду, а библиотека ждёт ответ.
```python
from djitellopy import Tello # импорт класса управления одним дроном

drone = Tello() # дрон по адресу 192.168.10.1

drone.connect() # подключение

drone.takeoff() # взлёт

drone.emergency() # экстренная остановка моторов

drone.end() # удаляет drone
```
____
#### enable_mission_pads()
Активация поиска Mission Pad.

Команда поддерживается только в Tello EDU.
```python
from djitellopy import Tello # импорт класса управления одним дроном

drone = Tello() # дрон по адресу 192.168.10.1

drone.connect() # подключение

drone.enable_mission_pads() # включаем функцию определения MP

drone.disable_mission_pads() # отключаем функцию определения MP

drone.end() # удаляет drone
```
____
#### end()
Завершение работы с дроном, удаляет объект дрона из памяти.
```python
from djitellopy import Tello # импорт класса управления одним дроном

drone = Tello() # дрон по адресу 192.168.10.1

drone.connect() # подключение

drone.takeoff() # взлёт

drone.land() # приземление

drone.end() # удаляет drone
```
____
#### flip(direction)
Сделать кувырок.

Кувырки могут не работать при заряде аккумулятора ниже 50%.

Требуется аргумент - направление кувырка (строка).
| Аргумент | Действие |
|:--------:|:------------------:|
| 'f' | Кувырок вперед |
| 'b' | Кувырок назад |
| 'l' | Кувырок влево |
| 'r' | Кувырок вправо |
```python
from djitellopy import Tello # импорт класса управления одним дроном

drone = Tello() # дрон по адресу 192.168.10.1

drone.connect() # подключение

drone.takeoff() # взлёт

drone.flip('l') # кувырок влево

drone.flip('r') # кувырок вправо

drone.flip('f') # кувырок вперед

drone.flip('b') # кувырок назад

drone.land() # приземление

drone.end() # удаляет drone
```
____
#### flip_back()
Кувырок назад.
```python
from djitellopy import Tello # импорт класса управления одним дроном

drone = Tello() # дрон по адресу 192.168.10.1

drone.connect() # подключение

drone.takeoff() # взлёт

drone.flip_back() # кувырок назад

drone.land() # приземление

drone.end() # удаляет drone
```
____
#### flip_forward()
Кувырок вперед.
```python
from djitellopy import Tello # импорт класса управления одним дроном

drone = Tello() # дрон по адресу 192.168.10.1

drone.connect() # подключение

drone.takeoff() # взлёт

drone.flip_forward() # кувырок вперед

drone.land() # приземление

drone.end() # удаляет drone
```
____
#### flip_left()
Кувырок влево.
```python
from djitellopy import Tello # импорт класса управления одним дроном

drone = Tello() # дрон по адресу 192.168.10.1

drone.connect() # подключение

drone.takeoff() # взлёт

drone.flip_left() # кувырок влево

drone.land() # приземление

drone.end() # удаляет drone
```
____
#### flip_right()
Кувырок вправо.
```python
from djitellopy import Tello # импорт класса управления одним дроном

drone = Tello() # дрон по адресу 192.168.10.1

drone.connect() # подключение

drone.takeoff() # взлёт

drone.flip_right() # кувырок вправо

drone.land() # приземление

drone.end() # удаляет drone
```
____
#### get_acceleration_x()
Запросить информацию об ускорении по оси X.

Возвращает float.
```python
from djitellopy import Tello # импорт класса управления одним дроном

drone = Tello() # дрон по адресу 192.168.10.1

drone.connect() # подключение

drone.takeoff() # взлёт

print(drone.get_acceleration_x()) # выводит значение ускорения по X

drone.land() # приземление

drone.end() # удаляет drone
```
____
#### get_acceleration_y()

Запросить информацию об ускорении по оси Y.

Возвращает float.
```python
from djitellopy import Tello # импорт класса управления одним дроном

drone = Tello() # дрон по адресу 192.168.10.1

drone.connect() # подключение

drone.takeoff() # взлёт

print(drone.get_acceleration_y()) # выводит значение ускорения по Y

drone.land() # приземление

drone.end() # удаляет drone
```
____
#### get_acceleration_z()
Запросить информацию об ускорении по оси Z.

Возвращает float.
```python
from djitellopy import Tello # импорт класса управления одним дроном

drone = Tello() # дрон по адресу 192.168.10.1

drone.connect() # подключение

drone.takeoff() # взлёт

print(drone.get_acceleration_z()) # выводит значение ускорения по Z

drone.land() # приземление

drone.end() # удаляет drone
```
____
#### get_barometer()
Запросить у дрона показания встроенного барометра. (TODO единицы измерения)

Возвращает int.
```python
from djitellopy import Tello # импорт класса управления одним дроном

drone = Tello() # дрон по адресу 192.168.10.1

drone.connect() # подключение

print(drone.get_barometer()) # выводит показания барометра

drone.end() # удаляет drone
```
____
#### get_battery()
Запросить уровень заряда аккумулятора.

Возвращает целое число процентов (0 - 100).
```python
from djitellopy import Tello # импорт класса управления одним дроном

drone = Tello() # дрон по адресу 192.168.10.1

drone.connect() # подключение

print(drone.get_battery()) # выводит уровень заряда аккумулятора

drone.end() # удаляет drone
```
____
#### get_current_state()
Запросить все показатели дрона.

Возвращает словарь:
| Ключ | Тип данных | Значение |
|:----:|:----------:|:--------:|
| pitch | int (градусы) | Наклон по X |
| roll | int (градусы) | Наклон по Y |
| yaw | int (градусы) | Поворот по Z |
| vgx | int (см/с) | Скорость по X |
| vgy | int (см/с) | Скорость по Y |
| vgz | int (см/с) | Скорость по Z |
| templ | int (°C) | Самая низкая температура с момента включения дрона |
| temph | int (°C) | Самая высокая температура с момента включения дрона |
| tof | int (сантиметры) | Показатель датчика расстояния до препятствия снизу |
| h | int (сантиметры) | Высота относительно координатной оси |
| bat | int (проценты) | Уровень заряда аккумулятора |
| baro | int (TODO) | Показания барометра |
| time | int (секунды) | Время полёта с последнего взлёта |
| agx | float (TODO) | Ускорение по X |
| agy | float (TODO) | Ускорение по Y |
| agz | float (TOFO) | Ускорение по Z |
| mid | int (номер) | ID найденного Mission Pad |
| x | int (сантиметры) | Расстояние до найденного Mission Pad по оси X относительно дрона. Поддерживается только в Tello EDU. |
| y | int (сантиметры) | Расстояние до найденного Mission Pad по оси Y относительно дрона. Поддерживается только в Tello EDU. |
| z | int (сантиметры) | Расстояние до найденного Mission Pad по оси Z относительно дрона. Поддерживается только в Tello EDU. |
| mpry | str (особый формат) | Углы между Mission Pad и дроном в формате 'x,y,z'. Поддерживается только в Tello EDU. |
```python
from djitellopy import Tello # импорт класса управления одним дроном

drone = Tello() # дрон по адресу 192.168.10.1

drone.connect() # подключение

print(drone.get_current_state()) # выводит весь словарь в "сыром" виде

# выводит весь словарь построчно:
state = drone.get_current_state()
for key in state:
    print(f'{key}: {state[key]}')

# вывод значения поля 'mpry'
print(drone.get_current_state()['mpry'])

drone.end() # удаляет drone
```
____
#### get_distance_tof()
Запросить у дрона расстояние до препятствия снизу.

Возвращает int.
```python
from djitellopy import Tello # импорт класса управления одним дроном

drone = Tello() # дрон по адресу 192.168.10.1

drone.connect() # подключение

print(drone.get_distance_tof()) # выводит расстояние до препятствия снизу

drone.end() # удаляет drone
```
____
#### get_flight_time()
Запросить у дрона время полёта в секундах с момента последнего взлёта.

Возвращает int.
```python
from djitellopy import Tello # импорт класса управления одним дроном

drone = Tello() # дрон по адресу 192.168.10.1

drone.connect() # подключение

print(drone.get_flight_time()) # выводит время полета

drone.end() # удаляет drone
```
____
#### get_frame_read()
Получить объект BackgroundFrameRead для подключения к камере дрона. (TODO check on WiFi)

Предварительно необходимо включить стрим камеры командой streamon() (TODO)

Позволяет получить в дальнейшем изображение с камеры.

Возвращает BackgroundFrameRead.
```python
import cv2 # импорт библиотеки компьютерного зрения для работы с камерой

from djitellopy import Tello # импорт класса управления одним дроном

drone = Tello() # дрон по адресу 192.168.10.1

drone.connect() # подключение

drone.streamon() # активация стрима камеры

drone_camera = drone.get_frame_read() # получаем объект доступа к камере

cv2.imwrite("picture.png", drone_camera.frame) # получить изображение с камеры и сохранить в файл picture.png

drone.end() # удаляет drone
```
____
#### get_height()
Запросить высоту дрона относительно оси координат в сантиметрах.

Возвращает int.
```python
from djitellopy import Tello # импорт класса управления одним дроном

drone = Tello() # дрон по адресу 192.168.10.1

drone.connect() # подключение

print(drone.get_height()) # выводит высоту дрона

drone.end() # удаляет drone
```
____
#### get_highest_temperature()
Запросить наивысшую, с момента включения, температуру дрона в °C.

Возвращает int.
```python
from djitellopy import Tello # импорт класса управления одним дроном

drone = Tello() # дрон по адресу 192.168.10.1

drone.connect() # подключение

print(drone.get_highest_temperature()) # выводит наивысшую температуру дрона

drone.end() # удаляет drone
```
____
#### get_lowest_temperature()
Запросить наименьшую, с момента включения, температуру дрона в °C.

Возвращает int.
```python
from djitellopy import Tello # импорт класса управления одним дроном

drone = Tello() # дрон по адресу 192.168.10.1

drone.connect() # подключение

print(drone.get_lowest_temperature()) # выводит наименьшую температуру дрона

drone.end() # удаляет drone
```
____
#### get_mission_pad_distance_x()
Запросить дистанцию по оси X до Mission Pad в сантиметрах.

Команда поддерживается только в Tello EDU.

Необходимо чтобы был активен поиск Mission Pad с помощью [enable_mission_pads()](https://github.com/Hellsingoff/DJITelloPy#enable_mission_pads), а так же чтобы какой-либо Mission Pad находился в области видимости камеры дрона. (TODO ссылка на область камеры)

Возвращает int.
```python
from djitellopy import Tello # импорт класса управления одним дроном

drone = Tello() # дрон по адресу 192.168.10.1

drone.connect() # подключение

print(drone.get_mission_pad_distance_x()) # выводит расстояние до MP по оси X

drone.end() # удаляет drone
```
____
#### get_mission_pad_distance_y()
Запросить дистанцию по оси Y до Mission Pad в сантиметрах.

Команда поддерживается только в Tello EDU.

Необходимо чтобы был активен поиск Mission Pad с помощью [enable_mission_pads()](https://github.com/Hellsingoff/DJITelloPy#enable_mission_pads), а так же чтобы какой-либо Mission Pad находился в области видимости камеры дрона. (TODO ссылка на область камеры)

Возвращает int.
```python
from djitellopy import Tello # импорт класса управления одним дроном

drone = Tello() # дрон по адресу 192.168.10.1

drone.connect() # подключение

print(drone.get_mission_pad_distance_y()) # выводит расстояние до MP по оси Y

drone.end() # удаляет drone
```
____
#### get_mission_pad_distance_z()
Запросить дистанцию по оси Z до Mission Pad в сантиметрах.

Команда поддерживается только в Tello EDU.

Необходимо чтобы был активен поиск Mission Pad с помощью [enable_mission_pads()](https://github.com/Hellsingoff/DJITelloPy#enable_mission_pads), а так же чтобы какой-либо Mission Pad находился в области видимости камеры дрона. (TODO ссылка на область камеры)

Возвращает int.
```python
from djitellopy import Tello # импорт класса управления одним дроном

drone = Tello() # дрон по адресу 192.168.10.1

drone.connect() # подключение

print(drone.get_mission_pad_distance_z()) # выводит расстояние до MP по оси Z

drone.end() # удаляет drone
```
____
#### get_mission_pad_id()
Запросить ID определенного камерой дрона Mission Pad.

Команда поддерживается только в Tello EDU.

Необходимо чтобы был активен поиск Mission Pad с помощью [enable_mission_pads()](https://github.com/Hellsingoff/DJITelloPy#enable_mission_pads), а так же чтобы какой-либо Mission Pad находился в области видимости камеры дрона. (TODO ссылка на область камеры)

Возвращает int.

Если Mission Pad не обнаружен - возвращает -1.
```python
from djitellopy import Tello # импорт класса управления одним дроном

drone = Tello() # дрон по адресу 192.168.10.1

drone.connect() # подключение

print(drone.get_mission_pad_id()) # выводит Mission Pad ID

drone.end() # удаляет drone
```
____
#### get_pitch()
Запросить наклон дрона по оси X в градусах.

Возвращает int.
```python
from djitellopy import Tello # импорт класса управления одним дроном

drone = Tello() # дрон по адресу 192.168.10.1

drone.connect() # подключение

print(drone.get_pitch()) # выводит угол

drone.end() # удаляет drone
```
____
#### get_roll()
Запросить наклон дрона по оси Y в градусах.

Возвращает int.
```python
from djitellopy import Tello # импорт класса управления одним дроном

drone = Tello() # дрон по адресу 192.168.10.1

drone.connect() # подключение

print(drone.get_roll()) # выводит угол

drone.end() # удаляет drone
```
____
#### get_speed_x()
Запросить текущую скорость по оси X в сантиметрах в секунду.

Возвращает int.
```python
from djitellopy import Tello # импорт класса управления одним дроном

drone = Tello() # дрон по адресу 192.168.10.1

drone.connect() # подключение

print(drone.get_speed_x()) # выводит скорость по оси X

drone.end() # удаляет drone
```
____
#### get_speed_y()
Запросить текущую скорость по оси Y в сантиметрах в секунду.

Возвращает int.
```python
from djitellopy import Tello # импорт класса управления одним дроном

drone = Tello() # дрон по адресу 192.168.10.1

drone.connect() # подключение

print(drone.get_speed_y()) # выводит скорость по оси Y

drone.end() # удаляет drone
```
____
#### get_speed_z()
Запросить текущую скорость по оси Z в сантиметрах в секунду.

Возвращает int.
```python
from djitellopy import Tello # импорт класса управления одним дроном

drone = Tello() # дрон по адресу 192.168.10.1

drone.connect() # подключение

print(drone.get_speed_z()) # выводит скорость по оси Z

drone.end() # удаляет drone
```
____
#### get_state_field(key)
Запросить у дрона значение определенного поля.

Аргумент - имя поля (строка).
| Ключ | Тип данных | Значение |
|:----:|:----------:|:--------:|
| pitch | int (градусы) | Наклон по X |
| roll | int (градусы) | Наклон по Y |
| yaw | int (градусы) | Поворот по Z |
| vgx | int (см/с) | Скорость по X |
| vgy | int (см/с) | Скорость по Y |
| vgz | int (см/с) | Скорость по Z |
| templ | int (°C) | Самая низкая температура с момента включения дрона |
| temph | int (°C) | Самая высокая температура с момента включения дрона |
| tof | int (сантиметры) | Показатель датчика расстояния до препятствия снизу |
| h | int (сантиметры) | Высота относительно координатной оси |
| bat | int (проценты) | Уровень заряда аккумулятора |
| baro | int (TODO) | Показания барометра |
| time | int (секунды) | Время полёта с последнего взлёта |
| agx | float (TODO) | Ускорение по X |
| agy | float (TODO) | Ускорение по Y |
| agz | float (TOFO) | Ускорение по Z |
| mid | int (номер) | ID найденного Mission Pad |
| x | int (сантиметры) | Расстояние до найденного Mission Pad по оси X относительно дрона. Поддерживается только в Tello EDU. |
| y | int (сантиметры) | Расстояние до найденного Mission Pad по оси Y относительно дрона. Поддерживается только в Tello EDU. |
| z | int (сантиметры) | Расстояние до найденного Mission Pad по оси Z относительно дрона. Поддерживается только в Tello EDU. |
| mpry | str (особый формат) | Углы между Mission Pad и дроном в формате 'x,y,z'. Поддерживается только в Tello EDU. |
```python
from djitellopy import Tello # импорт класса управления одним дроном

drone = Tello() # дрон по адресу 192.168.10.1

drone.connect() # подключение

print(drone.get_state_field('mpry')) # выводит значение поля 'mpry'

drone.end() # удаляет drone
```
____
#### get_temperature()
Запросить у дрона среднюю температуру (не текущую) в °C.

Фактически является средним между минимальным и максимальным значением.

Возвращает float.
```python
from djitellopy import Tello # импорт класса управления одним дроном

drone = Tello() # дрон по адресу 192.168.10.1

drone.connect() # подключение

print(drone.get_temperature()) # выводит среднюю температуру

drone.end() # удаляет drone
```
____
#### get_udp_video_address()
Запросить у дрона UDP адрес видео.

Внутренний метод библиотеки. Скорее всего, он Вам не нужен.

Возвращает str.
____
#### get_video_capture()
Запросить у дрона объект VideoCapture.

Ещё один внутренний библиотеки. Скорее всего он Вам не нужен.

Возвращает VideoCapture.
____
#### get_yaw()
Запросить угол поворота дрона относительно оси Z в градусах.

Возвращает int.
```python
from djitellopy import Tello # импорт класса управления одним дроном

drone = Tello() # дрон по адресу 192.168.10.1

drone.connect() # подключение

print(drone.get_yaw()) # выводит угол

drone.end() # удаляет drone
```
____
#### go_xyz_speed(x, y, z, speed)
Полёт в координаты x y z со скоростью speed сантиметров в секунду. (TODO check speed)

За начало осей координат (0 0 0) берется текущее местоположение дрона. (TODO check z)

Хотя бы одна из координат x y z должна быть не менее 20, попытка лететь на меньшую дистанцию вызовет ошибку.

Допустимые значения аргументов:
| Аргумент | Данные | Допустимые значения |
|:----------:|:------------------:|:--------:|
| x | int (сантиметры) | -500 - 500 |
| y | int (сантиметры) | -500 - 500 |
| z | int (сантиметры) | -500 - 500 |
| speed | int (сантиметры в секунду) | 10 - 100 |
```python
from djitellopy import Tello # импорт класса управления одним дроном

drone = Tello() # дрон по адресу 192.168.10.1

drone.connect() # подключение

drone.takeoff() # взлёт

drone.go_xyz_speed(100, 0, 0, 100) # полёт на метр вперед со скоростью 100 см/с

drone.land() # приземление

drone.end() # удаляет drone
```
____
#### go_xyz_speed_mid(x, y, z, speed, mid)
Полёт в координаты x y z относительно Mission Pad mid со скоростью speed сантиметров в секунду. (TODO check speed)

Команда поддерживается только в Tello EDU.

За начало осей координат (0 0 0) берется Mission Pad.

Если Mission Pad с ID mid не обнаружен - выводит ошибку и приземляется.

Необходимо чтобы был активен поиск Mission Pad с помощью [enable_mission_pads()](https://github.com/Hellsingoff/DJITelloPy#enable_mission_pads), а так же чтобы Mission Pad находился в области видимости камеры дрона. (TODO ссылка на область камеры)

Хотя бы одна из координат x y z должна быть не менее 20, попытка лететь на меньшую дистанцию вызовет ошибку.

Допустимые значения аргументов:
| Аргумент | Данные | Допустимые значения |
|:----------:|:------------------:|:--------:|
| x | int (сантиметры) | -500 - 500 |
| y | int (сантиметры) | -500 - 500 |
| z | int (сантиметры) | -500 - 500 |
| speed | int (сантиметры в секунду) | 10 - 100 |
| mid | int (Mission Pad ID) | 1 - 8 |
```python
from djitellopy import Tello # импорт класса управления одним дроном

drone = Tello() # дрон по адресу 192.168.10.1

drone.connect() # подключение

drone.takeoff() # взлёт

drone.go_xyz_speed(100, 0, 0, 100, 1) # полёт на метр вперед относительно MP1 со скоростью 100 см/с

drone.land() # приземление

drone.end() # удаляет drone
```
____
#### go_xyz_speed_yaw_mid(x, y, z, speed, yaw, mid1, mid2)
Полёт в координаты x y z относительно Mission Pad mid1 со скоростью speed сантиметров в секунду. В точке x y z производится поиск Mission Pad mid2 и дрон поворачивается на угол yaw относительно направления mid2. (TODO check speed)

Команда поддерживается только в Tello EDU.

За начало осей координат (0 0 0) берется Mission Pad mid1. (TODO check coord)

Если Mission Pad с ID mid1 не обнаружен - выводит ошибку и приземляется.

Если в точке x y z Mission Pad с ID mid2 не обнаружен - выводит ошибку и приземляется.

Неоднозначную работу команды может вызвать слишком близкое расположение двух Mission Pad. (TODO ссылка на область камеры)

Необходимо чтобы был активен поиск Mission Pad с помощью [enable_mission_pads()](https://github.com/Hellsingoff/DJITelloPy#enable_mission_pads), а так же чтобы Mission Pad находился в области видимости камеры дрона. (TODO ссылка на область камеры)

Модуль хотя бы одной из координат x y z должен быть не менее 20, попытка лететь на меньшую дистанцию вызовет ошибку.

Допустимые значения аргументов:
| Аргумент | Данные | Допустимые значения |
|:----------:|:------------------:|:--------:|
| x | int (сантиметры) | -500 - 500 |
| y | int (сантиметры) | -500 - 500 |
| z | int (сантиметры) | -500 - 500 |
| speed | int (сантиметры в секунду) | 10 - 100 |
| yaw | int (градусы) | -360 - 360 |
| mid1 | int (Mission Pad ID) | 1 - 8 |
| mid2 | int (Mission Pad ID) | 1 - 8 |
```python
from djitellopy import Tello # импорт класса управления одним дроном

drone = Tello() # дрон по адресу 192.168.10.1

drone.connect() # подключение

drone.takeoff() # взлёт

# полёт от MP1 на метр вперед (по направлению ракеты на коврике) со скоростью 100 см/с
# после производится поиск MP2 и такой поворот дрона, чтобы разница между направлением дрона и ракетой на MP2 составила 0 градусов
drone.go_xyz_speed(100, 0, 0, 100, 0, 1, 2)

drone.land() # приземление

drone.end() # удаляет drone
```
____
#### land()
Приземление дрона.
```python
from djitellopy import Tello # импорт класса управления одним дроном

drone = Tello() # дрон по адресу 192.168.10.1

drone.connect() # подключение

drone.takeoff() # взлёт

drone.land() # приземление

drone.end() # удаляет drone
```
____
#### move(direction, x)
Полёт дрона параллельно координатным осям - вперед/назад (ось X), влево/вправо (ось Y), вверх/вниз (ось Z).

Требуется два аргумента - направление (str) и расстояние в сантиметрах (int).

Расстояние должно быть не менее 20 сантиметров, попытка полёта на меньшую диистанцию вызовет ошибку.

Допустимые значения аргументов:
| Аргумент | Данные | Допустимые значения |
|:----------:|:------------------:|:--------:|
| direction | str (направление) | 'forward', 'back', 'left', 'right', 'up', 'down' |
| x | int (сантиметры) | 20 - 500 |

Значение аргументов направления:
| Аргумент | Направление |
|:--------:|:------------------:|
| 'forward' | Полет вперед |
| 'back' | Полет назад |
| 'left' | Полет влево |
| 'right' | Полет вправо |
| 'up' | Полет вверх |
| 'down' | Полет вниз |
```python
from djitellopy import Tello # импорт класса управления одним дроном

drone = Tello() # дрон по адресу 192.168.10.1

drone.connect() # подключение

drone.takeoff() # взлёт

drone.move('forward', 50) # полет вперед на 50 сантиметров

drone.move('back', 50) # полет назад на 50 сантиметров

drone.move('left', 50) # полет влево на 50 сантиметров

drone.move('right', 50) # полет вправо на 50 сантиметров

drone.move('up', 50) # полет вверх на 50 сантиметров

drone.move('down', 50) # полет вниз на 50 сантиметров

drone.land() # приземление

drone.end() # удаляет drone
```
____
#### move_back(x)
Полет назад на x сантиметров.

Принимает один аргумент - целое число от 20 до 500.
```python
from djitellopy import Tello # импорт класса управления одним дроном

drone = Tello() # дрон по адресу 192.168.10.1

drone.connect() # подключение

drone.takeoff() # взлёт

drone.move_back(50) # полет назад на 50 сантиметров

drone.land() # приземление

drone.end() # удаляет drone
```
____
#### move_down(x)
Полет вниз на x сантиметров.

Принимает один аргумент - целое число от 20 до 500.
```python
from djitellopy import Tello # импорт класса управления одним дроном

drone = Tello() # дрон по адресу 192.168.10.1

drone.connect() # подключение

drone.takeoff() # взлёт

drone.move_down(50) # полет вниз на 50 сантиметров

drone.land() # приземление

drone.end() # удаляет drone
```
____
#### move_forward(x)
Полет вперед на x сантиметров.

Принимает один аргумент - целое число от 20 до 500.
```python
from djitellopy import Tello # импорт класса управления одним дроном

drone = Tello() # дрон по адресу 192.168.10.1

drone.connect() # подключение

drone.takeoff() # взлёт

drone.move_forward(50) # полет вперед на 50 сантиметров

drone.land() # приземление

drone.end() # удаляет drone
```
____
#### move_left(x)
Полет влево на x сантиметров.

Принимает один аргумент - целое число от 20 до 500.
```python
from djitellopy import Tello # импорт класса управления одним дроном

drone = Tello() # дрон по адресу 192.168.10.1

drone.connect() # подключение

drone.takeoff() # взлёт

drone.move_left(50) # полет влево на 50 сантиметров

drone.land() # приземление

drone.end() # удаляет drone
```
____
#### move_right(x)
Полет вправо на x сантиметров.

Принимает один аргумент - целое число от 20 до 500.
```python
from djitellopy import Tello # импорт класса управления одним дроном

drone = Tello() # дрон по адресу 192.168.10.1

drone.connect() # подключение

drone.takeoff() # взлёт

drone.move_right(50) # полет вправо на 50 сантиметров

drone.land() # приземление

drone.end() # удаляет drone
```
____
#### move_up(x)
Полет вверх на x сантиметров.

Принимает один аргумент - целое число от 20 до 500.
```python
from djitellopy import Tello # импорт класса управления одним дроном

drone = Tello() # дрон по адресу 192.168.10.1

drone.connect() # подключение

drone.takeoff() # взлёт

drone.move_up(50) # полет вверх на 50 сантиметров

drone.land() # приземление

drone.end() # удаляет drone
```
____
#### parse_state(state)
Статический внутренний метод библиотеки для обработки данных, полученных от дрона. Он Вам не нужен.

Принимает один аргумент - строку с данными в особом формате.

Возвращает словарь.
____
#### query_attitude()
Запрашивает у дрона данные о его наклоне по осям X/Y и повороте относительно оси Z.

Работает медленнее, чем запросы [get_pitch()](https://github.com/Hellsingoff/DJITelloPy#get_pitch), [get_roll()](https://github.com/Hellsingoff/DJITelloPy#get_roll) и [get_yaw()](https://github.com/Hellsingoff/DJITelloPy#get_yaw), предоставляющих те же данные.

Возвращает словарь:
| Ключ | Данные | Значение |
|:----:|:------:|:--------:|
| 'pitch' | int (градус) | Наклон по оси X |
| 'roll' | int (градус) | Наклон по оси Y |
| 'yaw' | int (градус) | Поворот относительно оси Z |
```python
from djitellopy import Tello # импорт класса управления одним дроном

drone = Tello() # дрон по адресу 192.168.10.1

drone.connect() # подключение

print(drone.query_attitude()) # выводит весь словарь в "сыром" виде

# выводит весь словарь построчно:
attitude = drone.query_attitude()
for key in attitude:
    print(f'{key}: {attitude[key]}')

# вывод наклона по оси X (результат полностью идентичен get_pitch(), но работает медленнее)
print(drone.query_attitude()['pitch'])

drone.end() # удаляет drone
```
____
#### query_barometer()
Запрашивает у дрона показания встроенного барометра. (TODO единицы измерения)

Работает медленнее запроса [get_barometer()](https://github.com/Hellsingoff/DJITelloPy#get_barometer), предоставляющего те же данные.

Возвращает int.
```python
from djitellopy import Tello # импорт класса управления одним дроном

drone = Tello() # дрон по адресу 192.168.10.1

drone.connect() # подключение

print(drone.query_barometer()) # выводит показания барометра

drone.end() # удаляет drone
```
____
#### query_battery()
Запрашивает у дрона уровень заряда аккумулятора в процентах.

Работает медленнее запроса [get_battery()](https://github.com/Hellsingoff/DJITelloPy#get_battery), предоставляющего те же данные.

Возвращает int.
```python
from djitellopy import Tello # импорт класса управления одним дроном

drone = Tello() # дрон по адресу 192.168.10.1

drone.connect() # подключение

print(drone.query_battery()) # выводит заряд аккумулятора

drone.end() # удаляет drone
```
____
#### query_distance_tof()
Запрашивает у дрона расстояние до препятствия снизу в сантиметрах.

Работает медленнее запроса [get_distance_tof()](https://github.com/Hellsingoff/DJITelloPy#get_distance_tof), предоставляющего те же данные.

Возвращает int.
```python
from djitellopy import Tello # импорт класса управления одним дроном

drone = Tello() # дрон по адресу 192.168.10.1

drone.connect() # подключение

drone.takeoff() # взлет

print(drone.query_distance_tof()) # выводит расстояние до препятствия снизу

drone.land() # приземление

drone.end() # удаляет drone
```
____
#### query_flight_time()
Запрашивает у дрона время с начала текущего полета в секундах.

Работает медленнее запроса [get_flight_time()](https://github.com/Hellsingoff/DJITelloPy#get_flight_time), предоставляющего те же данные.

Возвращает int.
```python
from djitellopy import Tello # импорт класса управления одним дроном

drone = Tello() # дрон по адресу 192.168.10.1

drone.connect() # подключение

drone.takeoff() # взлет

print(drone.query_flight_time()) # выводит время полета

drone.land() # приземление

drone.end() # удаляет drone
```
____
#### query_height()
Запрашивает у дрона высоту относительно координатной оси в сантиметрах.

Работает медленнее запроса [get_height()](https://github.com/Hellsingoff/DJITelloPy#get_height), предоставляющего те же данные.

Возвращает int.
```python
from djitellopy import Tello # импорт класса управления одним дроном

drone = Tello() # дрон по адресу 192.168.10.1

drone.connect() # подключение

drone.takeoff() # взлет

print(drone.query_height()) # выводит высоту

drone.land() # приземление

drone.end() # удаляет drone
```
____
#### query_sdk_version()
Запрашивает у дрона версию поддерживаемого набора команд.

Версия 1.3 соответствует Tello Ryze, а версия 2.0 - Tello EDU.

SDK 2.0 предоставляет дополнительный функционал:
* Работа с Mission Pad:
    * [curve_xyz_speed_mid(x1, y1, z1, x2, y2, z2, speed, mid)](https://github.com/Hellsingoff/DJITelloPy#curve_xyz_speed_midx1-y1-z1-x2-y2-z2-speed-mid)
    * [disable_mission_pads()](https://github.com/Hellsingoff/DJITelloPy#disable_mission_pads)
    * [enable_mission_pads()](https://github.com/Hellsingoff/DJITelloPy#enable_mission_pads)
    * [get_mission_pad_distance_x()](https://github.com/Hellsingoff/DJITelloPy#get_mission_pad_distance_x)
    * [get_mission_pad_distance_y()](https://github.com/Hellsingoff/DJITelloPy#get_mission_pad_distance_y)
    * [get_mission_pad_distance_z()](https://github.com/Hellsingoff/DJITelloPy#get_mission_pad_distance_z)
    * [get_mission_pad_id()](https://github.com/Hellsingoff/DJITelloPy#get_mission_pad_id)
    * [go_xyz_speed_mid(x, y, z, speed, mid)](https://github.com/Hellsingoff/DJITelloPy#go_xyz_speed_midx-y-z-speed-mid)
    * [go_xyz_speed_yaw_mid(x, y, z, speed, yaw, mid1, mid2)](https://github.com/Hellsingoff/DJITelloPy#go_xyz_speed_yaw_midx-y-z-speed-yaw-mid1-mid2)
* Подключение к локальной сети:
    * [connect_to_wifi(ssid, password)](https://github.com/Hellsingoff/DJITelloPy#connect_to_wifissid-password)
* Дополнительные поля для данных обнаруженного Mission Pad:
    * [get_current_state()](https://github.com/Hellsingoff/DJITelloPy#get_current_state)
    * [get_state_field(key)](https://github.com/Hellsingoff/DJITelloPy#get_state_fieldkey)

Возвращает str.
```python
from djitellopy import Tello # импорт класса управления одним дроном

drone = Tello() # дрон по адресу 192.168.10.1

drone.connect() # подключение

print(drone.query_sdk_version()) # выводит версию SDK

drone.end() # удаляет drone
```
____
#### query_serial_number()
Запрашивает у дрона его серийный номер.

Возвращает str.
```python
from djitellopy import Tello # импорт класса управления одним дроном

drone = Tello() # дрон по адресу 192.168.10.1

drone.connect() # подключение

print(drone.query_serial_number()) # выводит серийный номер

drone.end() # удаляет drone
```
____
#### query_speed()
Запрашивает у дрона текущее значение настройки скорости.

Возвращает int.
```python
from djitellopy import Tello # импорт класса управления одним дроном

drone = Tello() # дрон по адресу 192.168.10.1

drone.connect() # подключение

print(drone.query_speed()) # выводит текущее ограничение скорости

drone.end() # удаляет drone
```
____
#### query_temperature()
Запрашивает у дрона его текущую температуру. (TODO check vs get)

Возвращает int.
```python
from djitellopy import Tello # импорт класса управления одним дроном

drone = Tello() # дрон по адресу 192.168.10.1

drone.connect() # подключение

print(drone.query_temperature()) # выводит текущую темрпературу дрона

drone.end() # удаляет drone
```
____
#### query_wifi_signal_noise_ratio()
Запрашивает у дрона текущее качество WiFi соединения. (TODO check ap vs client mode)

Возвращает str. (TODO check lesser is better)
```python
from djitellopy import Tello # импорт класса управления одним дроном

drone = Tello() # дрон по адресу 192.168.10.1

drone.connect() # подключение

print(drone.query_wifi_signal_noise_ratio()) # выводит текущее качество приема

drone.end() # удаляет drone
```
____
#### rotate_clockwise(x)
Поворот дрона по часовой стрелке на угол x.

Аргумент - целое число от 1 до 3600. (TODO check ryze edu 0 negative 360+ 3600+)
```python
from djitellopy import Tello # импорт класса управления одним дроном

drone = Tello() # дрон по адресу 192.168.10.1

drone.connect() # подключение

drone.takeoff() # взлет

drone.rotate_clockwise(90) # поворот на 90 градусов по часовой стрелке

drone.land() # приземление

drone.end() # удаляет drone
```
____
#### rotate_counter_clockwise(x)
Поворот дрона против часовой стрелки на угол x.

Аргумент - целое число от 1 до 3600. (TODO check ryze edu 0 negative 360+ 3600+)
```python
from djitellopy import Tello # импорт класса управления одним дроном

drone = Tello() # дрон по адресу 192.168.10.1

drone.connect() # подключение

drone.takeoff() # взлет

drone.rotate_counter_clockwise(90) # поворот на 90 градусов против часовой стрелки

drone.land() # приземление

drone.end() # удаляет drone
```
____
#### send_command_with_return(command, timeout=RESPONSE_TIMEOUT) (TODO response link)
Выполнение дроном команды из SDK с ожиданием ответа.

Принимает один обязательный и один необязательный аргументы.

Обязательный - строка с командой. Необязательный - время ожидания ответа в секундах (int).

Каждая команда из набора SDK реализована в данной библиотеке.

Общие для Ryze (SDK 1.3) и EDU (SDK 2.0) команды:

| Команда в SDK | Допустимые аргументы | Метод в библиотеке |
|:-------------:|:-----------------:|--------------------|
| command |  | [connect()](https://github.com/Hellsingoff/DJITelloPy#connect) |
| takeoff |  | [takeoff()](https://github.com/Hellsingoff/DJITelloPy#takeoff) |
| land  |  | [land()](https://github.com/Hellsingoff/DJITelloPy#land) |
| streamon |  | [streamon()](https://github.com/Hellsingoff/DJITelloPy#streamon) |
| streamoff |  | [streamoff()](https://github.com/Hellsingoff/DJITelloPy#streamoff) |
| emergency | (TODO response check) | [emergency()](https://github.com/Hellsingoff/DJITelloPy#emergency) |
| up x | 19 < x (int) < 501 | [move_up(x)](https://github.com/Hellsingoff/DJITelloPy#move_upx) |
| down x | 19 < x (int) < 501 | [move_down(x)](https://github.com/Hellsingoff/DJITelloPy#move_downx) |
| left x | 19 < x (int) < 501 | [move_left(x)](https://github.com/Hellsingoff/DJITelloPy#move_leftx) |
| right x | 19 < x (int) < 501 | [move_right(x)](https://github.com/Hellsingoff/DJITelloPy#move_rightx) |
| forward x | 19 < x (int) < 501 | [move_forward(x)](https://github.com/Hellsingoff/DJITelloPy#move_forwardx) |
| back x | 19 < x (int) < 501 | [move_back(x)](https://github.com/Hellsingoff/DJITelloPy#move_backx) |
| cw x | 0 < x < 3601 (TODO check) | [rotate_clockwise(x)](https://github.com/Hellsingoff/DJITelloPy#rotate_clockwisex) |
| ccw x | 0 < x < 3601 (TODO check) | [rotate_counter_clockwise(x)](https://github.com/Hellsingoff/DJITelloPy#rotate_counter_clockwisex) |
|  |  | [](https://github.com/Hellsingoff/DJITelloPy#) |
|  |  | [](https://github.com/Hellsingoff/DJITelloPy#) |
|  |  | [](https://github.com/Hellsingoff/DJITelloPy#) |
|  |  | [](https://github.com/Hellsingoff/DJITelloPy#) |
|  |  | [](https://github.com/Hellsingoff/DJITelloPy#) |
|  |  | [](https://github.com/Hellsingoff/DJITelloPy#) |
|  |  | [](https://github.com/Hellsingoff/DJITelloPy#) |
|  |  | [](https://github.com/Hellsingoff/DJITelloPy#) |
|  |  | [](https://github.com/Hellsingoff/DJITelloPy#) |

____










send_command_with_return(self, command, timeout=7)
Send command to Tello and wait for its response. Internal method, you normally wouldn't call this yourself.

Returns:

Type	Description
bool/str	
str with response text on success, False when unsuccessfull.

Source code in djitellopy/tello.py
send_command_without_return(self, command)
Send command to Tello without expecting a response. Internal method, you normally wouldn't call this yourself.

Source code in djitellopy/tello.py
send_control_command(self, command, timeout=7)
Send control command to Tello and wait for its response. Internal method, you normally wouldn't call this yourself.

Source code in djitellopy/tello.py
send_rc_control(self, left_right_velocity, forward_backward_velocity, up_down_velocity, yaw_velocity)
Send RC control via four channels. Command is sent every self.TIME_BTW_RC_CONTROL_COMMANDS seconds.

Parameters:

Name	Type	Description	Default
left_right_velocity	int	
-100~100 (left/right)

required
forward_backward_velocity	int	
-100~100 (forward/backward)

required
up_down_velocity	int	
-100~100 (up/down)

required
yaw_velocity	int	
-100~100 (yaw)

required
Source code in djitellopy/tello.py
send_read_command(self, command)
Send set command to Tello and wait for its response. Internal method, you normally wouldn't call this yourself.

Source code in djitellopy/tello.py
set_mission_pad_detection_direction(self, x)
Set mission pad detection direction. enable_mission_pads needs to be called first. When detecting both directions detecting frequency is 10Hz, otherwise the detection frequency is 20Hz.

Parameters:

Name	Type	Description	Default
x		
0 downwards only, 1 forwards only, 2 both directions

required
Source code in djitellopy/tello.py
set_speed(self, x)
Set speed to x cm/s.

Parameters:

Name	Type	Description	Default
x	int	
10-100

required
Source code in djitellopy/tello.py
set_wifi_credentials(self, ssid, password)
Set the Wi-Fi SSID and password. The Tello will reboot afterwords.

Source code in djitellopy/tello.py
streamoff(self)
Turn off video streaming.

Source code in djitellopy/tello.py
streamon(self)
Turn on video streaming. Use tello.get_frame_read afterwards. Video Streaming is supported on all tellos when in AP mode (i.e. when your computer is connected to Tello-XXXXXX WiFi ntwork). Currently Tello EDUs do not support video streaming while connected to a wifi network.

Note

If the response is 'Unknown command' you have to update the Tello firmware. This can be done using the official Tello app.

Source code in djitellopy/tello.py
takeoff(self)
Automatic takeoff

Source code in djitellopy/tello.py
udp_response_receiver() staticmethod
Setup drone UDP receiver. This method listens for responses of Tello. Must be run from a background thread in order to not block the main thread. Internal method, you normally wouldn't call this yourself.

Source code in djitellopy/tello.py
udp_state_receiver() staticmethod
Setup state UDP receiver. This method listens for state information from Tello. Must be run from a background thread in order to not block the main thread. Internal method, you normally wouldn't call this yourself.

## Authors

* **Damià Fuentes Escoté**
* **Jakob Löw**
* [and more](https://github.com/damiafuentes/DJITelloPy/graphs/contributors)

## License

This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details