One Script Car
=======

The one script car, is the a RC-car controlled by a Raspberry Pi, a PS3 dualshock controller, and a python script.

####Pictures and videos:

![alt one script car](https://raw.github.com/iobear/rpi-car/master/pictures/one_script_car_v1.jpg)

<a href="http://www.youtube.com/watch?feature=player_embedded&v=f1-Kq_kkoo0
" target="_blank"><img src="http://img.youtube.com/vi/f1-Kq_kkoo0/0.jpg" 
alt="First test" width="240" height="180" border="10" /></a>

<a href="http://www.youtube.com/watch?feature=player_embedded&v=9JCLskjOuQo
" target="_blank"><img src="http://img.youtube.com/vi/9JCLskjOuQo/0.jpg" 
alt="First test" width="240" height="180" border="10" /></a>


####BT dongles tested

![alt bt-dongle](https://raw.github.com/iobear/rpi-car/master/pictures/bt-dongle.jpg)

```
ID 0a12:0001 Cambridge Silicon Radio, Ltd Bluetooth Dongle (HCI mode)
ID 0cf3:3005 Atheros Communications, Inc. AR3011 Bluetooth
```

####Battery

To power the Pi I'm using a 680mAh, 3.7v battery from a Creative mp3 player. You could use one from a cellphone also, with a ~4v output.
I connect it directly to the 5v GPIO pin, with no protection in between - hint hint. 
The placement of the battery is underneath the Pi, the mileage is not tested yet.

<img src="https://raw.github.com/iobear/rpi-car/master/pictures/rpi_battery.jpg" alt="rpi battery">

The DC motor battery's are the same as the one used from the donor car, 4 x 1.5v.
 The output is connect to the vcc or vms, of the DC controller

<img src="https://raw.github.com/iobear/rpi-car/master/pictures/dc_motor_battery.jpg" alt="rpi battery" height="300" width="400">


####DC controller

I found a L298N DC controller on dx.com, for around 6 usd, you can find one 
<a href="http://dx.com/p/l298n-stepper-motor-driver-controller-board-for-arduino-120542">here</a>
<br /> I think any L298N controller board will work, there is lots of them out there.

#####Connections

```
RPI               L298N
ground(PIN6)  <-> GND
GIPO17(PIN11) <-> IN4
GIPO18(PIN12) <-> IN3
GIPO22(PIN15) <-> IN1
GIPO22(PIN16) <-> IN2

L298N MotorA <-> Back motor
L298N MotorB <-> Front motor
L298N VMS <-> + on battery pack
L298N GND <-> - on battery pack

```

<img src="https://raw.github.com/iobear/rpi-car/master/pictures/l298n_dc_controller.jpg" alt="l298n dc controller"> 



####Wheezy snapshot

If you are lazy or new to Linux, you can download a working snapshot of Raspain "wheezy", with my modifications via torrent.
<a href="https://raw.github.com/iobear/rpi-car/master/one-script-car/wheezy-one_script_car_oct16.zip.torrent">here</a>

The file is 2GB in size when compressed, and 8GB uncompressed. 
 Depending on operating system, there is diffrent ways to copy the image to the card, remember to unzip first.

```
Linux:
ImageWriter or
sudo dd if=path_of_your_image.img of=/dev/sdd bs=1M

MAC:
RasPiWrite or
sudo dd if=path_of_your_image.img of=/dev/diskn bs=1m
```

You can read more about SD-cards and images here: http://elinux.org/RPi_Easy_SD_Card_Setup

The image login is:

    user: pi
    pass: 1234

After first boot, you need to change a few thinges: (Keyboard and BT-dongle/dualshock bonding)

```
sudo dpkg-reconfigure keyboard-configuration
sudo download/sixpair
sudo reboot
```

When rebooted, press the PS button and you should be ready to play. 


####Credits:

Bluetooth:
http://dhoium3009.wordpress.com/raspberry-pi-connecting-multiple-ps3-controllers-via-bluetooth/

Controlling GPIO with Python:
http://pdwhomeautomation.blogspot.dk/2012/11/raspberry-pi-powered-lego-car.html

