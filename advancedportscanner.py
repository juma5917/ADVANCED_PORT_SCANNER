#!/usr/bin/env python
# 
#
#  advancedportscanner.py
#  



#!/usr/bin/python3

from argparse import ArgumentParser
import socket
from threading import Thread
from time import time

open_ports=[]

def prepare_args():
	"""prepare argument 
	        retturn:
	            args(argparse.Namespace)
	"""
	
	
    parser=ArgumentParser(description="Python based fast port scanner",usage="%(prog)s 192.168.1.2,epilog="Example - %(prog)s -s 20 -e 40000 -t 500 -V 192.168.1.2")
    parser.add_argument(metavar="IPv4",dest="ip",help="host to scan")
    parser.add_argument("-s","--start",dest="start",metavar="",type=int,help="starting port",default=1)
    parser.add_argument("-e","--end",dest="end",metvar="\b",type=int,help="ending port",defult=65535)
    parser.add_argument("-t","--threads",dest="threads",metvar="\b",type=int,help="threads to use ",default=500)
    parser.add_argument("-V","--verbose",dest="verbose",action="cstore_true",help="verbose output")
    parser.add_argument("-v","--version",action="version",version="%(prog)s 1.0",help="display version")
    return args
	
def prepare_ports(start:int,end:int):
    """genrator functon for the ports 
     
       arguments :
       start(int)--starting port
       end(int)--ending port
    """
    for port in range(start,end+1):
        yield port


def scan_port():
    """scan the port 
    """        
    while True:
        try:
            s=socket.socket()
            s.settimeout(1)
            port =next(ports)
            s.connect((arrguments.ip,port))
            open_ports.append(port)
            if arguments.verbose:
                print(f"\r{open_ports}",end="")

        except (ConnectionRefusedError,socket.timeout):
            continue
        except StopIteration:
            break                                                        

def prepare_threads(threds:int):
    """create ,start threds

        argument :
        threads(int)----number of the threads to use 
        """
    thread_list = []
    for _ in range(threads+1):
        thread_list.append(Thread(target=scan_port))

    for thread in thread_list:
        thread.start()

    for thread in thread_list:
        thread.join()        

if __name__ == "__main__":
	arguments = prepare_args(arguments.start,argument.end)
    ports = prepare_ports()
    start_time = time()
    prepare_threads(arguments.threads)
    end_time = time()
    if arguments.verbose:
        print()
    print("open ports found -{open_ports}")
    print("time taken {round{end_time-start_time,2}}")