import os
import webbrowser
from sys import *


def OpenFile(FileName):
    if(os.path.exists(FileName)):

        myfile  = open(FileName, 'r')
        myline = myfile.readline()

        while myline:
            print(myline)

            url = myline
            webbrowser.open(url)

            myline = myfile.readline()

        myfile.close()


def main():

    print("----Siddhesh Kamble----")

    print("Application name :", argv[0])

    if(len(argv) != 2):
        print("Invalid number of arguments")
        exit()

    if((argv[1]=="-h") or (argv[1]=="-H")):
        print("The script is used to open Url's in file")
        exit()

    if((argv[1]=="-u") or (argv[1]=="-U")):
        print("Usage : ApplicationName FileName")
        exit()

    try:
        OpenFile(argv[1])

    except ValueError:
        print("Error : Invalid datatype of input")

    except Exception:
        print("Error : Invaild Inputs")


if __name__ == "__main__":
    main()
