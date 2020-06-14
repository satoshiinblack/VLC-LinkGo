# UDP broadcast example: https://github.com/ninedraft/python-udp

# Run VLC player from command-line
# vlc bunny.mp4 -f --loop --http-password 1234

import xml.etree.ElementTree as ET
import requests
import socket
import time
import struct

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
serverVlcUrl = 'http://127.0.0.1:8080/requests/status.xml'

# Enable port reusage so we will be able to run multiple clients and servers on single (host, port).
# Do not use socket.SO_REUSEADDR except you using linux(kernel<3.9): goto https://stackoverflow.com/questions/14388706/how-do-so-reuseaddr-and-so-reuseport-differ for more information.
# For linux hosts all sockets that want to share the same address and port combination must belong to processes that share the same effective user ID!
# So, on linux(kernel>=3.9) you have to run multiple servers and clients under one user to share the same (host, port).
# Thanks to @stevenreddie
#server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)

# Enable broadcasting modeB
server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

# Set a timeout so the socket does not block
# indefinitely when trying to receive data.
server.settimeout(0.2)

while True:

    res =requests.get(serverVlcUrl,
                                     #Lua HTTP Password
                           auth=('', '1234'))
    root = ET.fromstring(res.text)
    serverPos = 0.0
    serverTime = 0
    for position in root.iter('position'):
        serverPos = float(position.text)
    for timeInSec in root.iter('time'):
        serverTime = int(timeInSec.text)

    server.sendto( struct.pack("fi", serverPos, serverTime)  , ("<broadcast>", 37020))
    print("pos: " + str(serverPos) + " | time: " + str(serverTime))

    time.sleep(0.1)
