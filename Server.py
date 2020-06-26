# UDP broadcast example: https://github.com/ninedraft/python-udp

# Run VLC player from command-line
# vlc bunny.mp4 -f --loop --http-password 1234

import xml.etree.ElementTree as ET
import requests
import socket
import time
import struct

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
server.settimeout(0.2)
serverVlcUrl = 'http://127.0.0.1:8080/requests/status.xml'
time.sleep(15)

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

    time.sleep(0.2)
