# Importing Nessacary Libaries.
import network
import time
from math import sin
from umqtt.simple import MQTTClient
# WiFi credentials
wifi_ssid = "youcannothavemywifi"
wifi_password = "normypassword"
# Connecting to WiFi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(wifi_ssid, wifi_password)
# Waits for connection
while wlan.isconnected() == False:
    print('Waiting for a connection...')
    time.sleep(1)
print("Connected to", wifi_ssid)
