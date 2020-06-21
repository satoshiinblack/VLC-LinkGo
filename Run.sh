#!/bin/sh

gnome-terminal -e "python3 /home/user/VLC-LinkGo/Server.py"
gnome-terminal -e "vlc /home/user/VLC-LinkGo/movie.mp4 -f --loop --http-password 1234"

exit 0
