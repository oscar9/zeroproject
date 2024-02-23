
# https://aprs.gids.nl/nmea/
import serial
import time
import string
import pynmea2

while True: 
    port="/dev/ttyAMA0"
    ser=serial.Serial(port,baudrate=9600,timeout=0.5)
    dataout =pynmea2.NMEAStreamReader()
    newdata=ser.readline()
    #print("Next: ", str(newdata[0:6]), " @all. ", str(newdata))
    code = newdata[0:6]
    gpscode = b"$GPRMC"
    #print("Code: ", code, " compare with", gpscode, " -- result: ", code=="$GPRMC")
    if code==gpscode:
        newmsg=pynmea2.parse(newdata.decode("utf-8"))
        lat=newmsg.latitude
        lng=newmsg.longitude
        gps="---- Latitude=" +str(lat) + "and Longitude=" +str(lng)
        print(gps)
