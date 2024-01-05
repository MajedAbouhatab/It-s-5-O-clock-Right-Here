from usocket import getaddrinfo, socket, SOCK_STREAM
from wifimgr import get_connection
from ScreenText import UpdateLabel
from ussl import wrap_socket
from time import sleep

try:
    get_connection()
    ai = getaddrinfo('www.timeanddate.com', 443, 0, SOCK_STREAM)[0]
    while True:
        s = socket()
        s.connect(ai[-1])
        s = wrap_socket(s, server_hostname='www.timeanddate.com')
        s.write(b'GET /worldclock/ HTTP/1.0\r\nHost: www.timeanddate.com\r\nConnection: close\r\n\r\n')
        HTML=str(s.read())
        Secs=59-int(HTML.split('<strong id=ctu>')[1].split('<')[0].split(':')[-1])
        s.close()
        L=[[l.split('>')[1].split('<')[0],l.split('class=rbi>')[1].split('m<')[0]+'m'] for l in HTML.split('<table ')[1].split('href="/worldclock/') if ' 5:' in l]
        UpdateLabel(False,' . '.join([i[0] for i in L]))
        while Secs != 0:
            for l in L:
                Secs=Secs-1
                if Secs == 0:
                    break
                UpdateLabel(True,l[0] + '\t\t\t' + l[1])
                sleep(1)
except:
    import machine
    machine.reset()
