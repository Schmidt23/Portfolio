import argparse
import sys
import socket

def scan_ports(target, port):
    try:
        s = socket.socket()
        s.connect((host, port))
    except:
        print(f"no response on {port}")
    else:
        print(f"{target} is open on Port {port}")
    
    s.close()





if __name__ == "__main__":
    #define sysargs
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", help="target host IP")

    args = parser.parse_args()

    if len(sys.argv)==1:
        parser.print_help()
        sys.exit()


    host = args.target
    print(host)

    for i in range(109,114):
        scan_ports(host, i)