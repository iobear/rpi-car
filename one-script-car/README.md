One Script Car
=======

The one script car, is the a RC-car controlled by a Raspberry Pi, a PS3 dualshock controller, and a python script.

####How it looks:

<a href="http://www.youtube.com/watch?feature=player_embedded&v=f1-Kq_kkoo0
" target="_blank"><img src="http://img.youtube.com/vi/f1-Kq_kkoo0/0.jpg" 
alt="First test" width="240" height="180" border="10" /></a>

####Wheezy snapshot

If you are lazy or new to Linux, you can download a working snapshot of Raspain "wheezy", with my modifications via torrent.
<a href="https://raw.github.com/iobear/rpi-car/master/one-script-car/wheezy-one_script_car_oct16.zip.torrent">here</a>

login:

    user: pi
    pass: 1234

You need to change a few thinges: (Keyboard, BT-dongle/dualshock bonding)


```
sudo dpkg-reconfigure keyboard-configuration
sudo download/sixpair
```



####Credits:

Bluetooth:
http://dhoium3009.wordpress.com/raspberry-pi-connecting-multiple-ps3-controllers-via-bluetooth/

Controlling GPIO with Python:
http://pdwhomeautomation.blogspot.dk/2012/11/raspberry-pi-powered-lego-car.html

