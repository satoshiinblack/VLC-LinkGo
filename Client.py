# UDP broadcast example: https://github.com/ninedraft/python-udp

# Run VLC player from command-line
# vlc bunny.mp4 -f --loop --http-password 1234

import xml.etree.ElementTree as ET
import requests
import socket
import time
import struct

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)  # UDP
clientVlcUrl = 'http://127.0.0.1:8080/requests/status.xml'

client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
client.bind(("", 37020))

time.sleep(10)

while True:

    #get server vlc time
    data, addr = client.recvfrom(1024)
    serverPos = struct.unpack_from("fi", data)[0]
    serverTime = struct.unpack_from("fi", data)[1]
    print("pos: " + str(serverPos) + " | time: " + str(serverTime))

    #get client vlc time
    res =requests.get(clientVlcUrl,
                                     #Lua HTTP Password
                           auth=('', '1234'))
    root = ET.fromstring(res.text)
    clientMoviePos = 0.0
    clientMovieTime = 0
    for position in root.iter('position'):
        clientMoviePos = float(position.text)
    for timeInSec in root.iter('time'):
        clientMovieTime = int(timeInSec.text)

    #time check
    if abs(serverTime-clientMovieTime)>2:
        requests.get(clientVlcUrl + '?command=seek&val=' + str(serverPos*100) + '%25',
                               #Lua HTTP Password
                     auth=('', '1234'))
    else :
        if serverPos > clientMoviePos:
            requests.get(clientVlcUrl + '?command=rate&val=1.02',
                                   #Lua HTTP Password
                         auth=('', '1234'))
        else :
            requests.get(clientVlcUrl + '?command=rate&val=0.98',
                                   #Lua HTTP Password
                         auth=('', '1234'))
