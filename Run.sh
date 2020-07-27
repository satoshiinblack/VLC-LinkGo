#!/bin/sh

#run server
gnome-terminal -e "python3 /home/user/VLC-LinkGo/Server.py"
#/usr/local/bin/python3 Server.py

#run client
#gnome-terminal -e "python3 /home/user/VLC-LinkGo/Client.py"
#/usr/local/bin/python3 Client.py

#run VLC
gnome-terminal -e "vlc /home/user/VLC-LinkGo/movie.mp4 -f --loop --http-password 1234"
#open -a VLC.app --args /Users/lumeiying/VLC-LinkGo/movie.mp4 -f --loop --http-password 1234

exit 0
