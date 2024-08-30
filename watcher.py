
import subprocess
import pyautogui 
import requests
import zipfile
import os
import sys
import time 
import psutil 
import ipaddress
import socket


def setup(location,exe):
    process = subprocess.Popen([exe])
    time.sleep(2)
    pyautogui.click(627,530,duration = 10)  
    pyautogui.click(672,528,duration = 6)
    pyautogui.click(328,458,duration = 16)
    pyautogui.click(606,526,duration = 12)
    pyautogui.click(589,369,duration = 14)
    pyautogui.click(609,531,duration = 4)
    pyautogui.click(741,580,duration = 6)
    pyautogui.click(741,580,duration = 4)
    pyautogui.click(780,141,duration = 2)
    pyautogui.typewrite(location)
    pyautogui.press("enter")
    pyautogui.click(446,464,duration = 4)          
    pyautogui.click(267,228,duration = 20)        
    return True 


def connected(adptr, orefx):
    adapters = psutil.net_if_addrs()
    if adptr not in adapters:
        return False
    addresses = adapters[adptr]
    for address in addresses:
        if address.family == socket.AF_INET:
            ip = address.address
            try:
                if ipaddress.ip_address(ip) in ipaddress.ip_network(orefx, strict=False):                    
                    return True
            except ValueError:
                continue
    return False


def watcher(adptrt,prefx,exe,wdir):
    isRunning = False 
    while True :
        process = None 
        if connected(adptrt,prefx) :
            if not isRunning:  
               process = subprocess.Popen(exe, cwd=wdir , creationflags=subprocess.CREATE_NEW_CONSOLE)   
               isRunning = True
        else:
            if isRunning : 
               subprocess.run(['taskkill', '/F', '/IM', 'nanominer.exe'])
               isRunning = False 
        #time.sleep(1)



if __name__ == "__main__":

    location = 'China'
    exe = "vpn.exe"
    
    setup(location,exe)

    adptr = 'Local Area Connection'
    prefx = '10.10.0.0/16'
    exeh = 'macro.exe'
    wdir = '\\'

    watcher(adptr,prefx,exeh,wdir)