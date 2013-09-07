#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import time
import subprocess

while True:
    output = subprocess.check_output(["git", "diff"])
    print("resultat : ", output)
    if output == b'':
        print('Pas de changement')
    else:
        os.system("git add .")
        os.system("make html")

    time.sleep(1)

