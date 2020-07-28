# VLC-LinkGo
## Demo Video
[![](http://img.youtube.com/vi/lGw4BSwcrNU/0.jpg)](http://www.youtube.com/watch?v=lGw4BSwcrNU "")<br />
https://www.youtube.com/watch?v=lGw4BSwcrNU
## What is a multi-channel video installation
### Definition
![What is a multi-channel video installation](/Snapshots/what_is_a_multi-channel_video_installation.png)<br />
Source: [Electronic Arts Intermix](https://www.eai.org/resourceguide/exhibition/installation/basicquestions.html#QUESTION2)<br />
<br />
## Requirements
VLC player 3.0 above (please enable the web interface https://wiki.videolan.org/Documentation:Modules/http_intf/)<br />
Python 3
<br />
<br />
These python scripts test ok(via Wi-fi) on : <br />
* Raspberry Pi 3 Model B 1GB Ram with Raspberry Pi OS (Release date: 2020-05-27) (Full HD Video,30fps is fine)
* Raspberry Pi Model B 512 MB RAM with Raspberry Pi OS (Release date: 2020-05-27) (Full HD Video,24fps is fine)
* PC with Ubuntu 20.04LTS/Ubuntu 18.04LTS/ Windows 10
* MacbookPro with Mojave 10.04

## Motivation
![已經超過八年了～今天還有藝術家跟我討論這問題～](/Snapshots/Snapshot_theReasonOfDoingThis.png)<br />
<br />
我在網路上看到這篇貼文「[已經超過八年了～今天還有藝術家跟我討論這問題～](https://www.facebook.com/honki/posts/10157377229111375)」，我覺得有點不敢置信...。<br />
所以動手寫了python+vlc 影片同步的程式。<br />

## To-do


## Tutorial
運作原理是，先用VLC撥放需要同步的影片。<br />
再用python script去偵測(UDP 廣播)同一個網段裡主畫面(Master)的時間，並即時調整(透過Http介面)本機影片(Slave)的時間。<br />


### Master
<code>
vlc /home/user/VLC-LinkGo/movie.mp4 -f --loop --http-password 1234
python3 /home/user/VLC-LinkGo/Server.py
</code>

### Slave
<code>
vlc /home/user/VLC-LinkGo/movie.mp4 -f --loop --http-password 1234
python3 /home/user/VLC-LinkGo/Client.py
</code>


## About
因為我在林口寫多頻道影片同步的程式，透過VLC實現，故此專案稱之VLC-LinkGo。
