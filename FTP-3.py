import socket
import user

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
    "LIST\r\n",
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
            s.send(cmd.encode('utf-8'))

            # Always waiting all response from FTP Sock
            while True:
                try:
                    resp = s.recv(BUFFER_SIZE).decode()
                    if len(resp) == 0:
                        break
                except Exception as ex:
                    break

                # print("RESP", resp)
                code,msg = parse_resp(resp.strip())
                # print(code, msg)

                if "Entering Passive Mode" in msg:
                    # print("Connecting to passive mode")
                    datas = msg.strip().split("(")[1].split(")")[0].split(",")
                    p1,p2 = int(datas[-2]), int(datas[-1])
                    data_port = p1 * 256 + p2

                    DATA_SOCK.connect(('localhost', data_port))
            
            # Also waiting all response from DataSock if available
            while True:
                try:
                    resp = DATA_SOCK.recv(4096).decode().rstrip()
                    if len(resp) == 0:
                        break

                    for dirname in resp.split("\r\n"):
                        print(f"{dirname.split(' ')[-1]}")
                    DATA_SOCK.close()
                except Exception as ex:
                    break
            i+=1

    except KeyboardInterrupt as Kiex:
        print("Keyboard Interrupt")
        
s.close()