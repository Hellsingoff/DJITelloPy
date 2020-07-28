# DJITelloPy
DJITelloPy - библиотека для Python 3.5 и выше, реализующая все команды, доступные в официальном [Tello SDK](https://dl-cdn.ryzerobotics.com/downloads/tello/20180910/Tello%20SDK%20Documentation%20EN_1.3.pdf) и [Tello EDU SDK](https://dl-cdn.ryzerobotics.com/downloads/Tello/Tello%20SDK%202.0%20User%20Guide.pdf).

Установка через pip
```
pip3 install https://github.com/Hellsingoff/DJITelloPy/archive/master.zip
```

## Использование

### Управление одним дроном

**Tello** - класс, реализующий управление одним дроном.

По умолчанию инициализация не трует аргументов, при этом IP дрона используется стандартный - 192.168.10.1, как при подключении к дрону по Wi-Fi. 

Если дрон подключен к локальной сети - при инициализации класса нужно как аргумент указать строку, содержащую IP дрона:
```python
from djitellopy import Tello

drone1 = Tello() # дрон по адресу 192.168.10.1

drone2 = Tello('192.168.1.220') # дрон по адресу 192.168.1.220
```

### Методы класса Tello

+ **connect()**
Вход в режим управления командами.
```python
from djitellopy import Tello

drone = Tello() # дрон по адресу 192.168.10.1

drone.connect() # подключение
```
+ **connect_to_wifi(ssid, password)**
Подключение дрона к существующей локальной сети по Wi-Fi.

Первый аргумент - имя сети, второй аргумент - её пароль.

После выполнения команды дрон перезагрузится и подключится к указанной сети.

Команда поддерживается только Tello EDU.
```python
from djitellopy import Tello

drone = Tello() # дрон по адресу 192.168.10.1, мы подключились к создаваемой дроном точке доступа.

drone.connect() # подключение к дрону

drone.connect_to_wifi('example', 'pass') # дрон перезагрузится и подключится к точке example с паролем pass
```

+ **curve_xyz_speed(x1, y1, z1, x2, y2, z2, speed)**
Полёт по дуге (части окружности).

Летит в относительные координаты x2 y2 z2 через x1 y1 z1 со скоростью speed сантиметров в секунду.

Обе координаты указываются в сантиметрах относительно текущего положения, то есть дрон считается точкой начала координатных осей (0 0 0).

Движение по оси X - вперед. По оси Y - влево. По оси Z - вверх.

Координаты x2 y2 z2, x1 y1 z1 и текущее расположение дрона (координаты 0 0 0) должны находиться на окружности радиусом 0.5-10 метров.

Если такую окружность найти не удалось или её радиус не входит в допустимые значения - дрон отправит сообщение об ошибке и сядет.

Both points are relative to the current position
The current position and both points must form a circle arc.
If the arc radius is not within the range of 0.5-10 meters, it raises an Exception
x1/x2, y1/y2, z1/z2 can't both be between -20-20 at the same time, but can both be 0.
Parameters:

Name	Type	Description	Default
x1	int	
-500-500

required
x2	int	
-500-500

required
y1	int	
-500-500

required
y2	int	
-500-500

required
z1	int	
-500-500

required
z2	int	
-500-500

required
speed	int	
10-60

required
Source code in djitellopy/tello.py
curve_xyz_speed_mid(self, x1, y1, z1, x2, y2, z2, speed, mid)
Fly to x2 y2 z2 in a curve via x2 y2 z2. Speed defines the traveling speed in cm/s.

Both points are relative to the mission pad with id mid.
The current position and both points must form a circle arc.
If the arc radius is not within the range of 0.5-10 meters, it raises an Exception
x1/x2, y1/y2, z1/z2 can't both be between -20-20 at the same time, but can both be 0.
Parameters:

Name	Type	Description	Default
x1	int	
-500-500

required
y1	int	
-500-500

required
z1	int	
-500-500

required
x2	int	
-500-500

required
y2	int	
-500-500

required
z2	int	
-500-500

required
speed	int	
10-60

required
mid	int	
1-8

required
Source code in djitellopy/tello.py
disable_mission_pads(self)
Disable mission pad detection

Source code in djitellopy/tello.py
emergency(self)
Stop all motors immediately.

Source code in djitellopy/tello.py
enable_mission_pads(self)
Enable mission pad detection

Source code in djitellopy/tello.py
end(self)
Call this method when you want to end the tello object

Source code in djitellopy/tello.py
flip(self, direction)
Do a flip maneuver. Users would normally call one of the flip_x functions instead.

Parameters:

Name	Type	Description	Default
direction	str	
l (left), r (right), f (forward) or b (back)

required
Source code in djitellopy/tello.py
flip_back(self)
Flip backwards.

Source code in djitellopy/tello.py
flip_forward(self)
Flip forward.

Source code in djitellopy/tello.py
flip_left(self)
Flip to the left.

Source code in djitellopy/tello.py
flip_right(self)
Flip to the right.

Source code in djitellopy/tello.py
get_acceleration_x(self)
X-Axis Acceleration

Returns:

Type	Description
float	
float: acceleration

Source code in djitellopy/tello.py
get_acceleration_y(self)
Y-Axis Acceleration

Returns:

Type	Description
float	
float: acceleration

Source code in djitellopy/tello.py
get_acceleration_z(self)
Z-Axis Acceleration

Returns:

Type	Description
float	
float: acceleration

Source code in djitellopy/tello.py
get_barometer(self)
Get current barometer measurement in cm This resembles the absolute height. See https://en.wikipedia.org/wiki/Altimeter

Returns:

Type	Description
int	
int: barometer measurement in cm

Source code in djitellopy/tello.py
get_battery(self)
Get current battery percentage

Returns:

Type	Description
int	
int: 0-100

Source code in djitellopy/tello.py
get_current_state(self)
Call this function to attain the state of the Tello. Returns a dict with all fields. Internal method, you normally wouldn't call this yourself.

Source code in djitellopy/tello.py
get_distance_tof(self)
Get current distance value from TOF in cm

Returns:

Type	Description
int	
int: TOF distance in cm

Source code in djitellopy/tello.py
get_flight_time(self)
Get the time the motors have been active in seconds

Returns:

Type	Description
int	
int: flight time in s

Source code in djitellopy/tello.py
get_frame_read(self)
Get the BackgroundFrameRead object from the camera drone. Then, you just need to call backgroundFrameRead.frame to get the actual frame received by the drone.

Returns:

Type	Description
BackgroundFrameRead	
BackgroundFrameRead

Source code in djitellopy/tello.py
get_height(self)
Get current height in cm

Returns:

Type	Description
int	
int: height in cm

Source code in djitellopy/tello.py
get_highest_temperature(self)
Get highest temperature

Returns:

Type	Description
int	
float: highest temperature (°C)

Source code in djitellopy/tello.py
get_lowest_temperature(self)
Get lowest temperature

Returns:

Type	Description
int	
int: lowest temperature (°C)

Source code in djitellopy/tello.py
get_mission_pad_distance_x(self)
X distance to current mission pad Only available on Tello EDUs after calling enable_mission_pads

Returns:

Type	Description
int	
int: distance in cm

Source code in djitellopy/tello.py
get_mission_pad_distance_y(self)
Y distance to current mission pad Only available on Tello EDUs after calling enable_mission_pads

Returns:

Type	Description
int	
int: distance in cm

Source code in djitellopy/tello.py
get_mission_pad_distance_z(self)
Z distance to current mission pad Only available on Tello EDUs after calling enable_mission_pads

Returns:

Type	Description
int	
int: distance in cm

Source code in djitellopy/tello.py
get_mission_pad_id(self)
Mission pad ID of the currently detected mission pad Only available on Tello EDUs after calling enable_mission_pads

Returns:

Type	Description
int	
int: -1 if none is detected, else 1-8

Source code in djitellopy/tello.py
get_pitch(self)
Get pitch in degree

Returns:

Type	Description
int	
int: pitch in degree

Source code in djitellopy/tello.py
get_roll(self)
Get roll in degree

Returns:

Type	Description
int	
int: roll in degree

Source code in djitellopy/tello.py
get_speed_x(self)
X-Axis Speed

Returns:

Type	Description
int	
int: speed

Source code in djitellopy/tello.py
get_speed_y(self)
Y-Axis Speed

Returns:

Type	Description
int	
int: speed

Source code in djitellopy/tello.py
get_speed_z(self)
Z-Axis Speed

Returns:

Type	Description
int	
int: speed

Source code in djitellopy/tello.py
get_state_field(self, key)
Get a specific sate field by name. Internal method, you normally wouldn't call this yourself.

Source code in djitellopy/tello.py
get_temperature(self)
Get average temperature

Returns:

Type	Description
float	
float: average temperature (°C)

Source code in djitellopy/tello.py
get_udp_video_address(self)
Internal method, you normally wouldn't call this youself.

Source code in djitellopy/tello.py
get_video_capture(self)
Get the VideoCapture object from the camera drone. Users usually want to use get_frame_read instead.

Returns:

Type	Description
VideoCapture

Source code in djitellopy/tello.py
get_yaw(self)
Get yaw in degree

Returns:

Type	Description
int	
int: yaw in degree

Source code in djitellopy/tello.py
go_xyz_speed(self, x, y, z, speed)
Fly to x y z relative to the current position. Speed defines the traveling speed in cm/s.

Parameters:

Name	Type	Description	Default
x	int	
20-500

required
y	int	
20-500

required
z	int	
20-500

required
speed	int	
10-100

required
Source code in djitellopy/tello.py
go_xyz_speed_mid(self, x, y, z, speed, mid)
Fly to x y z relative to the mission pad with id mid. Speed defines the traveling speed in cm/s.

Parameters:

Name	Type	Description	Default
x	int	
-500-500

required
y	int	
-500-500

required
z	int	
-500-500

required
speed	int	
10-100

required
mid	int	
1-8

required
Source code in djitellopy/tello.py
go_xyz_speed_yaw_mid(self, x, y, z, speed, yaw, mid1, mid2)
Fly to x y z relative to mid1. Then fly to 0 0 z over mid2 and rotate to yaw relative to mid2's rotation. Speed defines the traveling speed in cm/s.

Parameters:

Name	Type	Description	Default
x	int	
-500-500

required
y	int	
-500-500

required
z	int	
-500-500

required
speed	int	
10-100

required
yaw	int	
-360-360

required
mid1	int	
1-8

required
mid2	int	
1-8

required
Source code in djitellopy/tello.py
land(self)
Automatic land

Source code in djitellopy/tello.py
move(self, direction, x)
Tello fly up, down, left, right, forward or back with distance x cm. Users would normally call one of the move_x functions instead.

Parameters:

Name	Type	Description	Default
direction	str	
up, down, left, right, forward or back

required
x	int	
20-500

required
Source code in djitellopy/tello.py
move_back(self, x)
Fly x cm backwards.

Parameters:

Name	Type	Description	Default
x	int	
20-500

required
Source code in djitellopy/tello.py
move_down(self, x)
Fly x cm down.

Parameters:

Name	Type	Description	Default
x	int	
20-500

required
Source code in djitellopy/tello.py
move_forward(self, x)
Fly x cm forward.

Parameters:

Name	Type	Description	Default
x	int	
20-500

required
Source code in djitellopy/tello.py
move_left(self, x)
Fly x cm left.

Parameters:

Name	Type	Description	Default
x	int	
20-500

required
Source code in djitellopy/tello.py
move_right(self, x)
Fly x cm right.

Parameters:

Name	Type	Description	Default
x	int	
20-500

required
Source code in djitellopy/tello.py
move_up(self, x)
Fly x cm up.

Parameters:

Name	Type	Description	Default
x	int	
20-500

required
Source code in djitellopy/tello.py
parse_state(state) staticmethod
Parse a state line to a dictionary Internal method, you normally wouldn't call this yourself.

Source code in djitellopy/tello.py
query_attitude(self)
Query IMU attitude data. Using get_pitch, get_roll and get_yaw is usually faster.

Returns:

Type	Description
dict	
{'pitch': int, 'roll': int, 'yaw': int}

Source code in djitellopy/tello.py
query_barometer(self)
Get barometer value (cm) Using get_barometer is usually faster.

Returns:

Type	Description
int	
int: 0-100

Source code in djitellopy/tello.py
query_battery(self)
Get current battery percentage via a query command Using get_battery is usually faster

Returns:

Type	Description
int	
int: 0-100 in %

Source code in djitellopy/tello.py
query_distance_tof(self)
Get distance value from TOF (cm) Using get_distance_tof is usually faster.

Returns:

Type	Description
int	
float: 30-1000

Source code in djitellopy/tello.py
query_flight_time(self)
Query current fly time (s). Using get_flight_time is usually faster.

Returns:

Type	Description
int	
int: Seconds elapsed during flight.

Source code in djitellopy/tello.py
query_height(self)
Get height in cm via a query command. Using get_height is usually faster

Returns:

Type	Description
int	
int: 0-3000

Source code in djitellopy/tello.py
query_sdk_version(self)
Get SDK Version

Returns:

Type	Description
str	
str: SDK Version

Source code in djitellopy/tello.py
query_serial_number(self)
Get Serial Number

Returns:

Type	Description
str	
str: Serial Number

Source code in djitellopy/tello.py
query_speed(self)
Query speed setting (cm/s)

Returns:

Type	Description
int	
int: 1-100

Source code in djitellopy/tello.py
query_temperature(self)
Query temperature (°C). Using get_temperature is usually faster.

Returns:

Type	Description
int	
int: 0-90

Source code in djitellopy/tello.py
query_wifi_signal_noise_ratio(self)
Get Wi-Fi SNR

Returns:

Type	Description
str	
str: snr

Source code in djitellopy/tello.py
rotate_clockwise(self, x)
Rotate x degree clockwise.

Parameters:

Name	Type	Description	Default
x	int	
1-360

required
Source code in djitellopy/tello.py
rotate_counter_clockwise(self, x)
Rotate x degree counter-clockwise.

Parameters:

Name	Type	Description	Default
x	int	
1-3600

required
Source code in djitellopy/tello.py
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