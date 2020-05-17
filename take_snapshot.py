#!/usr/bin/python
# -*- coding: utf-8 -*-

# Credit to Tom Catullo https://github.com/Tom25



import datetime
import cv2
import os

# Config
stream_url = 'http://192.168.0.XX/cgi-bin/api.cgi?cmd=Snap&channel=0&rs=wuuPhkmUCeI9WG7C&user=xxxxxx&password=xxxx'
filename = "/var/www/html/weewx/conditions1.txt" #Where the weewx conditions are
gardenwx = "/var/www/html/camera/gardenwx.jpg" #Where the Web page image goes

# Determine save location
now = datetime.datetime.now()
date = now.strftime("%Y-%m-%d")
time = now.strftime("%H-%M-%S")
absolute_script_dir = os.path.dirname(os.path.realpath(__file__))
save_dir = absolute_script_dir + '/snapshots/' + date
save_path = save_dir + '/' + time + '.jpg'

# Capture frame from camera stream
cap = cv2.VideoCapture(stream_url)
ret, frame = cap.read()

#Put conditions from weewx onto image

datafile = open(filename)
conditions = datafile.read()


position = (10,1750)
cv2.putText(
     frame, #numpy array on which text is written
     (conditions), #text
     position, #position at which writing has to start
     cv2.FONT_HERSHEY_COMPLEX, #font family
     1.5, #font size
     (255,255,255), #font color
     3) #font stroke

datafile.close()

# Save frame as image
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

cv2.imwrite(save_path, frame)
cv2.imwrite(gardenwx, frame)
