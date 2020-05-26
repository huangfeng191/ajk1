# -*- coding: utf-8 -*-
import time
def YMD(ts, fmt='%Y-%m-%d'):
    return time.strftime(fmt.encode('utf-8'), time.localtime(float(ts))).decode('utf-8')

def YMDHMS(ts, fmt='%Y-%m-%d %H:%M:%S'):
    return time.strftime(fmt , time.localtime(float(ts)))