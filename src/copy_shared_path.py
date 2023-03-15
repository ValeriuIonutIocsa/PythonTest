import os.path
import socket
import sys
import pyperclip
import utils.logger as logger


def findIpAddress():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ipAddress = s.getsockname()[0]
    s.close()
    return ipAddress


def main():
    if sys.argv.__len__() < 2:
        logger.printError()
        logger.printError("not enough CLI arguments!")
        logger.printError()
        exit(0)

    print()

    path = sys.argv[1]
    print(path)

    index = path.index('\\')
    ipAddress = findIpAddress()
    sharedPath = '\\\\' + ipAddress + path[index:]
    print(sharedPath)

    isFileFlag = os.path.isfile(sharedPath)
    isDirFlag = os.path.isdir(sharedPath)
    fileExists = isFileFlag or isDirFlag
    print('File exists: ' + str(fileExists))

    clipboardPath = sharedPath if fileExists else path
    pyperclip.copy(clipboardPath)
    print('Copied:' + os.linesep + clipboardPath)
    print()


main()
