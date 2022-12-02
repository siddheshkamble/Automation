import os
import psutil
import time
from sys import *
import schedule

def ProcessDisplay(log_dir = "LogFiles"):
    listprocess = []

    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass

    separator = "-" * 80
    log_path = os.path.join(log_dir,"SID%s.csv"%(time.ctime()))
    f = open(log_path,'w')
    f.write(separator + "\n")
    f.write("Siddhesh Kamble Process Logger :"+time.ctime() + "\n")
    f.write(separator + "\n")
    
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs = ['pid', 'name', 'username'])
            vms = proc.memory_info().vms / (1024*1024)
            pinfo['vms'] = vms
            listprocess.append(pinfo);
        except(psutil.NoSuchProcess, psutil.AccessDenied,psutil.ZombieProcess):
            pass

    for element in listprocess:

        shifts = len(listprocess)
        for i in range(shifts):
            iMax = vms
            if(iMax > vms):
                listprocess.append(element)
        f.write("%s\n"%element)

def main():
    print("----Siddhesh Kamble----")

    print("Application name :", argv[0])

    if(len(argv) != 2):
        print("Invalid number of arguments")
        exit()
    if((argv[1]=="-h") or (argv[1]=="-H")):
        print("The script is used log record of running process")
        exit()
    if((argv[1]=="-u") or (argv[1]=="-U")):
        print("Usage : ApplicationName AbsolutePath_Of_Directory")
        exit()

    try:
        ProcessDisplay(argv[1])

        schedule.every(1).minutes.do(ProcessDisplay)

        while(True):       
            schedule.run_pending()
            time.sleep(1)

    except ValueError:
        print("Error : Invalid datatype of input")

    except Exception:
        print("Error : Invaild Inputs")

if __name__ == "__main__":
    main()