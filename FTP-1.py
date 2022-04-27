import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 21))

def parse_resp(msg):
    resp_code = msg[:3]
    resp_msg = msg[4:]
    return resp_code, resp_msg

resp = s.recv(4096).decode()
code,msg = parse_resp(resp.strip())
# print(code, msg)

# Print First Line Response
print(msg.split("\r\n")[0])

s.close()