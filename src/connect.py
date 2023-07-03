import network
import credentials

def connectToNetwork():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print("connecting to network...")
        sta_if.active(True)
        sta_if.connect(credentials.SSID, credentials.WIFI_PASSWORD)
        while not sta_if.isconnected():
            pass
    ip = sta_if.ifconfig()[0]
    return ip