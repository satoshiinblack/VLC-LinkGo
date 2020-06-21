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

# Enable port reusage so we will be able to run multiple clients and servers on single (host, port).
# Do not use socket.SO_REUSEADDR except you using linux(kernel<3.9): goto https://stackoverflow.com/questions/14388706/how-do-so-reuseaddr-and-so-reuseport-differ for more information.
# For linux hosts all sockets that want to share the same address and port combination must belong to processes that share the same effective user ID!
# So, on linux(kernel>=3.9) you have to run multiple servers and clients under one user to share the same (host, port).
# Thanks to @stevenreddie
#client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)

# Enable broadcasting mode
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
