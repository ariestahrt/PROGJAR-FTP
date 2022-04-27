import socket
import user
from _thread import *

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 21))
s.settimeout(1.0)

DATA_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
DATA_SOCK.settimeout(1.0)
BUFFER_SIZE=4096

COMMANDS = [
    f'USER {user.username}\r\n',
    f'PASS {user.password}\r\n',
    'TYPE I\r\n',
    "PASV\r\n",
    "STOR ty2.jpeg\r\n",
    "THIS IS BYTES OF ty2.jpeg\r\n",
    "QUIT\r\n"
    ]

def parse_resp(msg):
    resp_code = msg[:3]
    resp_msg = msg[4:]
    return resp_code, resp_msg

i = 1
while True:
    try:
        if i > len(COMMANDS):
            s.close()
            break
        else:
            cmd = COMMANDS[i-1]
            # print("CMD", cmd.rstrip())
            if "STOR" in COMMANDS[i-2].split(" ")[0]:
                # print("SENDING FILES")
                with open("E:/ty.jpeg", "rb") as f:
                    while True:
                        # read the bytes from the file
                        bytes_read = f.read(BUFFER_SIZE)
                        # print(bytes_read)
                        if not bytes_read:
                            break
                        DATA_SOCK.send(bytes_read)    
                # print("SENDING FILES DONE")
                DATA_SOCK.close()

            else:
                # print("SENDING", cmd.rstrip())
                s.send(cmd.encode('utf-8'))

                # Always waiting all response
                while True:
                    try:
                        resp = s.recv(BUFFER_SIZE).decode()
                        if len(resp) == 0:
                            break
                    except Exception as ex:
                        break

                    # print("RESP", resp)
                    code,msg = parse_resp(resp.strip())
                    print(code, msg)

                    if "Entering Passive Mode" in msg:
                        # print("Connecting to passive mode")
                        datas = msg.strip().split("(")[1].split(")")[0].split(",")
                        p1,p2 = int(datas[-2]), int(datas[-1])
                        data_port = p1 * 256 + p2

                        DATA_SOCK.connect(('localhost', data_port))

            i+=1

    except KeyboardInterrupt as Kiex:
        print("Keyboard Interrupt")
        
s.close()