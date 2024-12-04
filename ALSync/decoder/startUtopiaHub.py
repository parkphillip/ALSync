

import subprocess
import os
from time import sleep

def run(label='', logdir=None):
    pydir = os.path.dirname(os.path.abspath(__file__)) # mindaffectBCI/decoder/startUtopiaHub.py
    bindir = os.path.join(pydir,'..','hub') 

    # make the logs directory if not already there
    if logdir is None:
        logdir=os.path.join(bindir,'../../logs')
    if not os.path.exists(logdir):
        try:
            os.makedirs(logdir)
        except:
            print("Error making the log directory {}.... ignoring".format(logdir))

    # command to run the java hub
    cmd = ("java","-jar","UtopiaServer.jar")
    # args to pass to the java hub
    if label is not None:
        logfile = "mindaffectBCI_{}.txt".format(label)
    else:
        logfile = "mindaffectBCI.txt"
    args = ("8400","0",os.path.join(os.path.expanduser(logdir),logfile))

    # run the command, waiting until it has finished
    print("Running command: {}".format(cmd+args))
    utopiaHub = subprocess.Popen(cmd + args, cwd=bindir, shell=False)#,
                               #stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    sleep(1)
    return utopiaHub

if __name__=="__main__":
    run()