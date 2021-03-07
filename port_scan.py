# -*- encoding: utf-8 -*-
import socket
import pyfiglet
import sys
from datetime import datetime, timedelta
#from timeit import default_timer as timer
from pytictoc import TicToc

ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)


# Defining a target
if len(sys.argv) == 2:
    print(sys.argv[0]) #  test // script-name
    print(sys.argv[1]) #  test // target HOST_IP entered on CLI
    print(len(sys.argv)) # expect 2

    # translate hostname to IPv4
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Please enter at the command line a target IP. ")

# Add Banner
start_time = str(datetime.now())
print("-" * 50)
print("Scanning Target: " + target)
print("Scanning started at:" + start_time )
t = TicToc()  # create TicToc instance
t.tic()       # start timer
print("-" * 50)

try:

    # will scan ports between 1 to port[,n]
    for port in range(1,82):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        # returns an error indicator
        result = s.connect_ex((target,port))
        #check result: zero means succceded;otherwise,returns error indicator,
        # not an exception for errors returned by the C-level connect() call.
        if result == 0:
            print("[+]Port {} is open".format(port))
        s.close()
    t.toc()


except KeyboardInterrupt:
        print("\n Exiting Program. Bye!")
        sys.exit()
except socket.gaierror:
        print("\n Hostname Could Not Be Resolved!")
        sys.exit()
except socket.error:
        print("\ Server not responding!")
        sys.exit()
