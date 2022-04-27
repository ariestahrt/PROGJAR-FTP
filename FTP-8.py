import socket
import user

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 21))
s.settimeout(1.0)

BUFFER_SIZE=4096
COMMANDS = [
    f'USER {user.username}\r\n',
    f'PASS {user.password}\r\n',
    'RMD test2\r\n',
    'QUIT\r\n'
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
                print(code, msg)

            i+=1

    except KeyboardInterrupt as Kiex:
        print("Keyboard Interrupt")
        
s.close()