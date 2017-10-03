#!/usr/bin/env python

import subprocess
from pprint import pprint

def reboot_ec2_instance(process=None):
    """
    To reboot the host machine ones in a week
    :param process:
    :return:
    """
    cassandra_process = subprocess.Popen(process, stdout=subprocess.PIPE, shell=True)
    out, err = cassandra_process.communicate()
    pprint (out, err)


def main():
    reboot = 'reboot'
    reboot_ec2_instance(reboot)

if __name__ == "__main__":
    main()
