#!/usr/bin/env python3

import subprocess
import random

interface_name = input("\n\nEnter interface to change MAC of\n\t>>> ")
mac_random = ":".join("%02x"%random.randint(0,255) for x in range(6)) # thanks stackoverflow - get a random MAC

print(f"\n---  Changing Mac Address for {interface_name}  ---\n")
print("  -- OLD --\n")

# run bash commands ifconfig interface_name - view ifconfig before MAC changes
subprocess.call(["ifconfig", interface_name])

# int_name down - hw ether {MAC_RANDOM} - int_name up
subprocess.call(["sudo", "ifconfig", interface_name, "down"])
subprocess.call(["sudo", "ifconfig", interface_name, "hw", "ether", mac_random])
subprocess.call(["sudo", "ifconfig", interface_name, "up"])


print("\n  -- NEW --\n")
# run ifconfig interface_name again
subprocess.call(["ifconfig", interface_name])

print("""

IF ANY ERRORS TRY RE-RUNNING maccas_random.py

###----  MACCAS HAS ENDED  ----###
""")
