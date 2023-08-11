from random import *
from string import *
import pywifi
# Библиотека pywifi - это библиотека для работы с Wi-Fi на языке программирования Python. Она позволяет
# сканировать доступные Wi-Fi сети, подключаться к ним, создавать новые профили и многое другое.
from pywifi import const
#Оператор from pywifi import const импортирует константы, используемые в библиотеке pywifi

def generate_password(length):
    s = ''
    for i in range(length):
        el = [choice(ascii_uppercase), choice(ascii_lowercase), choice(digits)][randrange(3)]
        while el in 'lI10oO':
            el = [choice(ascii_uppercase), choice(ascii_lowercase), choice(digits)][randrange(3)]
        s += el
    return s



wifi = pywifi.PyWiFi()  # создаем объект PyWiFi
ifaces = wifi.interfaces()[0]  # выбираем первый интерфейс Wi-Fi
# Оператор iface = wifi.interfaces()[0] выбирает первый доступный интерфейс Wi-Fi на устройстве.
# Обычно на устройстве может быть несколько интерфейсов Wi-Fi, поэтому мы выбираем первый из них.
# Далее мы будем использовать этот интерфейс для подключения к Wi-Fi сети
profile = pywifi.Profile()  # создаем профиль Wi-Fi
# Профили WiFi сетей - это одна из ключевых фигур в "игре" с беспроводными сетями. Профиль хранит всю информацию, необходимую для успешной установки беспроводного подключения, в том числе способ аутентификации и пароли.
# Профиль создается, когда вы успешно подключаетесь с беспроводной сети.
# указываем название сети
# имя Wi-Fi сети, к которой мы хотим подключиться. SSID (Service Set Identifier) - это уникальное имя Wi-Fi сети, которое используется для идентификации сети в радиовещании. Мы указываем его в профиле для того, чтобы
# библиотека pywifi знала, к какой сети мы хотим подключиться.

# указываем тип защиты и пароль
profile.auth = const.AUTH_ALG_OPEN
# Устанавливает метод аутентификации в открытом режиме.
profile.akm.append(const.AKM_TYPE_WPA2PSK)
# Добавляет метод защиты WPA2-PSK для авторизации на сети.
profile.cipher = const.CIPHER_TYPE_CCMP
# Устанавливает тип шифрования CCMP для защиты передаваемых данных.
profile.key = generate_password(randint(5, 12))
profile.ssid = input('Введите сеть ')

iface.remove_all_network_profiles()  # удаляем все профили Wi-Fi
tmp_profile = iface.add_network_profile(profile)  # добавляем новый профиль Wi-Fi
# Создает временный профиль для подключения к указанной сети и добавляет его в список профилей на устройстве.
print(const.IFACE_CONNECTING)
iface.connect(tmp_profile)  # подключаемся к сети
cnt = 0
# проверяем статус подключения
while iface.status != const.IFACE_CONNECTING:
# const.IFACE_CONNECTING Константа, которая содержит информацию о текущем подключении к сети.
# Это метод объекта интерфейса сети в Python, который возвращает строку, указывающую текущий статус
# подключения к сети (например, "up" или "down"). Это не константа, а функция.
# условие проверяет, что статус подключения к сети не является "connecting" (подключение в процессе)
    print(iface.connect(tmp_profile), iface.status(), const.IFACE_CONNECTING, profile.key)
    if cnt != 0:
        profile.key = generate_password(randint(5, 12))
        iface.connect(tmp_profile)
    cnt += 1
print(iface.status, const.IFACE_CONNECTING, profile.key)
print(f'{profile.ssid} -- {profile.key}')

