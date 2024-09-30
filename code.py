import board
import time
import displayio
import digitalio

import ipaddress
import wifi
import socketpool
import ssl
import adafruit_requests

import terminalio
from adafruit_display_text import label


buttonD0 = digitalio.DigitalInOut(board.D0)
buttonD0.direction = digitalio.Direction.INPUT
buttonD0.pull = digitalio.Pull.UP

buttonD1 = digitalio.DigitalInOut(board.D1)
buttonD1.direction = digitalio.Direction.INPUT
buttonD1.pull = digitalio.Pull.UP

buttonD2 = digitalio.DigitalInOut(board.D2)
buttonD2.direction = digitalio.Direction.INPUT
buttonD2.pull = digitalio.Pull.UP


ssid="xxxxx"
passwd="xxxxx"

def wifi_scan():
    networks = wifi.radio.start_scanning_networks()
    wifi_list = list(networks)
    return wifi_list


def screen_display(network):

    group = displayio.Group()

    signalPercentage = 2 * (network.rssi + 100)
    wifi_name = "" + str(network.ssid)
    pourcentage = " " + str(signalPercentage) + "% " #+ str(network.channel)

    text_area_namewf = label.Label(terminalio.FONT, text=wifi_name, color=0x0000FF, background_color=0xFFFFFF, scale = 2)
    text_area_namewf.x = 30
    text_area_namewf.y = 10
    group.append(text_area_namewf)

    text_area_pourcentage = label.Label(terminalio.FONT, text=pourcentage, color=0x0000FF, background_color=0xFFFFFF, scale = 2)
    text_area_pourcentage.x = 90
    text_area_pourcentage.y = 80
    group.append(text_area_pourcentage)

    board.DISPLAY.root_group = group


wifi_list = wifi_scan()
index = 0


while True:

    if not buttonD1.value:
        wifi_list = wifi_scan()
        print(wifi_list)




    if not buttonD0.value:
        index = ( index - 1) % len(wifi_list)
        time.sleep(0.3)

    if not buttonD2.value:
        index += ( index + 1) % len(wifi_list)
        time.sleep(0.3)

    screen_display(wifi_list[index])

    #board.DISPLAY.root_group = text_area_namewf
    #board.DISPLAY = text_area_pourcentage

    time.sleep(0.01)

    wifi.radio.stop_scanning_networks()
