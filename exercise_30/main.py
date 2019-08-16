#!/bin/env python36
import sys
import threading
import time


# 单位换算
def unit_conversion(byte):
    byte = int(byte)
    if byte > 1000:
        res = byte / 1024
        if res < 1000:
            res = float('%.2f' % res)
            return str(res) + 'k'
        elif res < 1000 * 1024:
            res = res / 1024
            res = float('%.2f' % res)
            return str(res) + 'm'
        else:
            res = res / (1024 * 1024)
            res = float('%.2f' % res)
            return str(res) + 'g'


def get_net_data(netdev):
    with open('/proc/net/dev', 'r') as f:
        for line in f:
            if line.find(netdev) >= 0:
                receive = line.split(':')[1].split()[0]
                transmit = line.split(':')[1].split()[8]
                return float(receive), float(transmit)


def speed_monitor(netdev):
    while True:
        receive_old, transmit_old = get_net_data(netdev)
        time.sleep(1)
        receive, transmit = get_net_data(netdev)
        print('recevice' + unit_conversion(receive - receive_old) + '/s')
        print('transmit' + unit_conversion(transmit - transmit_old) + '/s')


if __name__ == "__main__":
    if sys.argv[1] == "t":
        receive, transmit = get_net_data(sys.argv[2])
        print(unit_conversion(receive))
        print(unit_conversion(transmit))
    elif sys.argv[1] == "s":
        threading.Thread(target=speed_monitor,args=(sys.argv[2],)).start()
