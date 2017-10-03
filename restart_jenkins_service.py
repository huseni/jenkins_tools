#!/usr/bin/env python

import subprocess
from pprint import pprint

def restartJenkinsInstance(process=None):
    """
    To reboot the restart jenkins service ones in a week
    :param process:
    :return:
    """
    process = subprocess.Popen(process, stdout=subprocess.PIPE, shell=True)
    out, err = process.communicate()
    pprint (out, err)


def main():
    restart = 'service jenkins restart'
    restartJenkinsInstance(restart)

if __name__ == "__main__":
    main()
