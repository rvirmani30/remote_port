import socket
from datetime import datetime
from pyfiglet import Figlet 


#Displaying Banner
custom_fig = Figlet(font='graffiti')
print(custom_fig.renderText('Port Scan!!'))

#Enter target IP/FQDN and Port number to scan.
remote_server_ip = input("Enter the remote host IP or FQDN \n")
remote_server_port = int(input("Enter the port number(s) \n"))

#Timestamp of scan initiated
print ("Scanning started at:" + str(datetime.now()))

def connection_initiated():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        scan_remote = sock.connect((remote_server_ip, remote_server_port))
        sock.settimeout(1)
        if scan_remote ==0:
            print("Port is Open")
        else:
            print("Port is closed")
            sock.close()
    except socket.error:
        print("Couldn't connect to host on the specified port",remote_server_port)
    except socket.timeout:
        print("Connection timedout")
    except KeyboardInterrupt:
        print("Connection was closed by the user. You pressed ctrl+c")

connection_initiated()