import socket


def findIpAddress1():
    hostname = socket.gethostname()
    ipAddress = socket.gethostbyname(hostname)
    return ipAddress


def findIpAddress2():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ipAddress = s.getsockname()[0]
    s.close()
    return ipAddress


def main():
    ipAddress1 = findIpAddress1()
    print('ip address (method 1): ' + ipAddress1)

    ipAddress2 = findIpAddress2()
    print('ip address (method 2): ' + ipAddress2)


main()
