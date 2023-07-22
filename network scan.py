import socket
import argparse
import sys
from datetime import datetime
from pyfiglet import Figlet


#Displaying Banner
#custom_fig = Figlet(font='graffiti')
#print(custom_fig.renderText('Port Scan!!'))


#Timestamp of scan initiated
start_time = datetime.now()
print ("Scanning started at:" + str(datetime.now()))

#Port scan time calculation.
def time_calculate(start_time):
    end_time = datetime.now()
    total_time = end_time - start_time
    total_time_in_seconds = total_time.total_seconds()
    if not start_time > end_time:
        print("Total time taken for the scan to complete is: " + str(total_time_in_seconds) + " seconds." )

#Checking if the port is open or closed.
def connection_initiated(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        if sock.connect ==0:
            print("Port is Open")
        else:
            print("Port is closed")
            sock.close()
    except socket.error:
        print("Couldn't connect to host on the specified port",port)
    except socket.timeout:
        print("Connection timedout")
    except KeyboardInterrupt:
        print("Connection was closed by the user. You pressed ctrl+c")

def scanparser():
    #setup argument parsing
    scan_parser = argparse.ArgumentParser(description='Port Scan initiated.')
    scan_parser.add_argument('-H', '--Host', help='Host to scan', type=str, required=True, dest='Host')
    scan_parser.add_argument('-P', '--Port', help='Port range to scan', type=int, required=True, dest='Port')
    scan_parser.add_argument('-U', help='UDP protocol', type=str)
    scan_parser.add_argument('-T', help='TCP Protocol', type=str)
    argparse_call = scan_parser.parse_args()
    host = argparse_call.Host
    port = argparse_call.Port

    connection_initiated(host,port)

if __name__ == '__main__':
    scanparser()
    time_calculate(start_time)

# host, port_range = argparse.host, argparse.port_range
# start_port, end_port = port_range.split(",")
# start_port, end_port = int(start_port), int(end_port)
# ports = [p for p in range(start_port, end_port)]import socket
