import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 21))

# commands = ['USER ariesta\r\n', 'PASS heart123\r\n', 'TYPE I\r\n', 'EPSV\r\n', 'MLSD\r\n', 'QUIT\r\n']

def parse_resp(msg):
    resp_code = msg[:3]
    resp_msg = msg[4:]
    return resp_code, resp_msg

# for cmd in commands:
#     s.send(cmd.encode('utf-8'))
#     resp = s.recv(4096).decode()
#     # print(resp.strip())
#     code,msg = parse_resp(resp.strip())
#     print(code, msg)

resp = s.recv(4096).decode()
# print(resp.strip())
code,msg = parse_resp(resp.strip())
print(code, msg)

s.close()