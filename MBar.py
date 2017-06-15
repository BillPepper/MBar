from time import strftime, gmtime
from subprocess import call
import time
import psutil
import subprocess


# enableViewOne = True
# enableViewTwo = True
# activeView = 0
# interval = 5
outputEnabled = True


def getTime():
    return strftime("%H:%M:%S", time.localtime())


def getDate():
    return strftime("%d %b %Y", gmtime())


def getDay():
    return strftime("%a", gmtime())


def getCPUUsage():
    return psutil.cpu_percent(percpu=False)


def getInstalledMemory():
    return psutil.virtual_memory().total


def getUsedMemory():
    return psutil.virtual_memory().used


def bytes2human(n):
    # http://code.activestate.com/recipes/578019
    # '95.4M'
    symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    prefix = {}
    for i, s in enumerate(symbols):
        prefix[s] = 1 << (i + 1) * 10
    for s in reversed(symbols):
        if n >= prefix[s]:
            value = float(n) / prefix[s]
            return '%.1f%s' % (value, s)
    return "%sB" % n


def getBattery():
    acpiCmd = ["acpi", "-b"]
    proc = subprocess.check_output(acpiCmd).split(" ")
    return proc[3].strip(",")


def getIP():
    ipCmd = ["hostname", "-I"]
    proc = subprocess.check_output(ipCmd).split(" ")
    return proc[0]


def renderViewOne():
    outString = "cpu: " + str(getCPUUsage()) + " | " + \
        "mem: " + str(bytes2human(getUsedMemory())) + " / " + \
        str(bytes2human(getInstalledMemory())) + " | batt: " + \
        getBattery() + " | ip: " + \
        getIP() + " | " + \
        getDay() + ", " + \
        getDate() + " | " + \
        getTime()

    if (outputEnabled):
        print(str(outString))

    return outString


def renderViewTwo():
    outString = "Testting my tool"
    return outString


def updateBar(line):
    call(["xsetroot", "-name", line])


while (True):
    updateBar(renderViewOne())

    time.sleep(1)
'''
    if (activeView == 0):
        updateBar(renderViewOne())
        activeView = 1
    else:
        updateBar(renderViewTwo())
        activeView = 0

    interval = interval -1

'''
