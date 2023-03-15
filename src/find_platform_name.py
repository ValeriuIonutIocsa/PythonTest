import platform
import socket


def main():
    print()

    platformNode = platform.node()
    print('platform node: ' + str(platformNode))
    socketFqdn = socket.getfqdn()
    print('socket FQDN: ' + str(socketFqdn))

    print()


main()
