#connects to the WiFi network and sync time via NTP
import time
import network
import ntptime
import utime

sta_if = network.WLAN(network.STA_IF)

def wifi_connect(ssid, pwd):
    ''' connect to wifi with provided password and print the result '''
    # activate the interface
    sta_if.active(True)

    # connect it to the network
    sta_if.connect(ssid, pwd)
    
    # check result
    print("Connection attempt to WiFi SSID:", ssid)
    for i in range(0,20):
        if not(sta_if.isconnected()):
            print('.' * i)
            time.sleep(1)
        else:
            break
    print("Wifi connected:", sta_if.isconnected())
    print("Wifi config:", sta_if.ifconfig())


def sync_ntp_time():
    if not(sta_if.active()):
        print("Can't sync NTP. Wifi not active.")
    elif not(sta_if.isconnected()):
        print("Can't sync NTP. Wifi not connected.")
    else:
        ntptime.settime()
        dt = utime.localtime()
        dt = [str(d) for d in dt] # int to str for concat
        print("NTP time loaded:", "-".join(dt[0:3]), ":".join(dt[3:6]))


def connect_wifi():
    ssid = "beacon"
    passwd = "noyfb"
    wifi_connect(ssid, passwd)
    sync_ntp_time()



