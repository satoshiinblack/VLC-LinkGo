#!/bin/sh

#run VLC
gnome-terminal -e "vlc /home/user/VLC-LinkGo/movie.mp4 -f --loop --http-password 1234"
#open -a VLC.app --args /Users/lumeiying/VLC-LinkGo/movie.mp4 -f --loop --http-password 1234

#run server script
gnome-terminal -e "python3 /home/user/VLC-LinkGo/Server.py"
#/usr/local/bin/python3 Server.py

#run client script
#gnome-terminal -e "python3 /home/user/VLC-LinkGo/Client.py"
#/usr/local/bin/python3 Client.py


exit 0
