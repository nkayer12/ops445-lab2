#!/usr/bin/env python3

# Author: Narendra Ayer
# Author ID: nkayer
# Date Created: 2025/05/16

import sys

if len(sys.argv) == 2:
    timer = int(sys.argv[1])
else:
    timer = 3

while timer > 0:
    print(timer)
    timer -= 1

print("blast off!")

