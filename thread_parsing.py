# -*- coding: utf-8 -*-
import Queue
import threading
import requests

'''
testing part with files
'''

f_parsed = open("parsed_macs.txt", 'r')
f_out = open("results.txt", "w")

'''
end of part with files
'''
def worker():
    while True:
        mac = q.get()
        page = requests.get('https://login.wi-fi.ru/am/UI/Login?org=mac&service=coa&client_mac='+mac.lower().replace(':','-').strip()+'&ForceAuth=true')
        if u'Введите Ваш номер и подтвердите идентификацию' in page.text:
            #print(mac+'na')
            mac = mac+' not authorized'
        elif "mosmetro_premium" in page.text:
            mac = mac+' is golden!'
            #print(mac+'golden')
        else:
            mac = mac+' is not payed'
        f_out.write(mac+'\n')
        q.task_done()
q = Queue.Queue()

for line in f_parsed:
    q.put(line.strip())

for i in range(5):
    t = threading.Thread(target=worker)
    t.daemon = True
    t.start()

q.join()
f_parsed.close()
f_out.close()
print("DONE")
