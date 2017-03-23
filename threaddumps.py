import sys
import time as systime
import datetime as sdt

dt = str(sdt.date.today())
waittime = 10
counter = 6

try :
        connect('username','password','t3://admin-host:admin-port')
        serverNames = cmo.getServers()
        domainRuntime()
        for name in serverNames:
                cd("/ServerRuntimes/" + name.getName())
                i = 0
                dump = StringBuffer("***\n")
                while i < counter :
                        dump = dump.append(str(threadDump()))
                        systime.sleep(waittime)
                        i = i+1
                op = open("/opt/app/scripts/threaddumps-using-wlst/"+str(name.getName())+"-"+dt,"w")
                print >> op, dump
        disconnect()
        exit()
except :
        print 'An error occured while generating threaddump'
        dumpStack()