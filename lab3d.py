#!/usr/bin/env python3
'''Lab 3 function to return free disk space on Linux system's root directory'''
# Author ID: spaudel11

import subprocess

def free_space():
    command = "df -h | grep '/$' | awk '{print $4}'"
    result = subprocess.run(command, shell=True, capture_output=True, text=True, encoding='utf-8')
    return result.stdout.strip()

if __name__ == '__main__':
    print(free_space())
