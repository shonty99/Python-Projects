from sys import *
import webbrowser
import re
from urllib.request import urlopen
#from urllib.error import HTTPError
#import urllib.error
#import urllib


def is_connected():
    try:
        urlopen('http://google.com')#,timeout=1
        return True
    except Exception as err:  #urllib.error.HTTPError
        return False
    
def Find(string):
    url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F]))+', string)
    return url

def WebLauncher(path):
    with open(path) as fp:
        for line in fp:
            print(line)
            url = Find(line)
            print(url)
            for str in url:
                webbrowser.open(str,new = 2)

def main():
    print("-------Web Launcher BY Shantanu Sawalkar")

    print("Application name : "+argv[0])

    if (len(argv)!=2):
        print("Error : Invalid number of arguments")
        exit()

    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("This script is used to open URL which are written in one file")
        exit()

    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("Usage : Application name Name_OF_File")
        exit()

    try:
        connected = is_connected()

        if connected:
            WebLauncher(argv[1])
        else:
            print("Unable to connect Internet......")

    except ValueError:
        print("Error : invalid datatype of input")
    except Exception as E:
        print("Error : Invalid input",E)


if __name__ == "__main__":
    main()
