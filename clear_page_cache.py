#!/usr/bin/env python

import subprocess
from pprint import pprint

def clear_page_cache(process=None):
    """
    To clear the page cache from the host machine
    :param process:
    :return:
    """
    cassandra_process = subprocess.Popen(process, stdout=subprocess.PIPE, shell=True)
    out, err = cassandra_process.communicate()
    pprint (out, err)


def main():
    clean_cache = 'sync; sync; echo 1 > /proc/sys/vm/drop_caches; free'
    clear_page_cache(clean_cache)


if __name__ == "__main__":
    main()
