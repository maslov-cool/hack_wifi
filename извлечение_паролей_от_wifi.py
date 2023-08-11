import subprocess
# данная библиотека позволяет создавать новые процессы


def wifi():
    data = subprocess.check_output('netsh wlan show profiles').decode('cp866').split('\n')
    # subprocess.check_output('netsh wlan show profiles') принимает ТОЛЬКО СТРОКУ ИЛИ F-СТРОКУ КАК АРГУМЕНТ запускает процесс в командной строке,
    # который выводит список доступных Wi-Fi сетей(инфа и пароли которых есть в пк) на пк в байтовом формате
    # subprocess.check_output('netsh wlan show profiles').decode('cp866') декодирует из кодировки cp866 в строку
    # subprocess.check_output('netsh wlan show profiles').decode('cp866').split('\n') разбивает строку по символу
    # новой строки

    profiles = [i.split(':')[1][1:-1].strip() for i in data if 'Все профили пользователей' in i]
    # оставляем только названия Wi-Fi

    pass_wifi = ''
    # в ней будем сохранять итоговые данные
    for i in profiles:
        results = subprocess.check_output(f'netsh wlan show profiles {i} key = clear').decode('cp866')\
            .split('\n')
        for j in results:
            if 'Содержимое ключа' in j:
                pass_wifi += f'{i} -- {j.split(":")[1][1:-1].strip()}\n'
    print(pass_wifi)


wifi()





