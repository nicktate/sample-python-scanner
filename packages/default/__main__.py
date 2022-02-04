import sys
import socket
import requests
from datetime import datetime

def main(args):
    name = args.get('name', "World")
    name = name if name else "World"
    message = "Hello, " + name + "!";
    print(message)

    target = '0.0.0.0'

    # Add Banner
    print("-" * 50)
    message += "\n-" * 50
    print("Scanning Target: " + target)
    message += "\nScanning Target: " + target
    print("Scanning started at:" + str(datetime.now()))
    message += "\nScanning started at:" + str(datetime.now()) + "\n"
    print("-" * 50)
    message += "-" * 50

    try:

        # will scan ports between 1 to 65,535
        for port in range(1,65535):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)

            # returns an error indicator
            result = s.connect_ex((target,port))
            if result ==0:
                print("Port {} is open".format(port))
                message += "\nPort {} is open".format(port)
                url = "http://0.0.0.0:{}".format(port)
                resp = requests.get(url)
                print("\nresp: " + resp.text)
            s.close()

    except KeyboardInterrupt:
            print("\n Exiting Program !!!!")
            message += "\n Exiting Program !!!!"
            sys.exit()
    except socket.gaierror:
            print("\n Hostname Could Not Be Resolved !!!!")
            message += "\n Hostname Could Not Be Resolved !!!!"
            sys.exit()
    except socket.error:
            print("\ Server not responding !!!!")
            message += "\ Server not responding !!!!"
            sys.exit()

    return {
        "body": {"message": message}
    }

