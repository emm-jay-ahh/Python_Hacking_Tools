#!/usr/bin/env python3

import subprocess
import random

def run_ifconfig():
    subprocess.call(["ifconfig", interface_name])

def mac_change():
    # sudo int_name down - hw ether {MAC Change} - int_name up
    print(f"\n---  Changing Mac Address for {interface_name}  ---\n")
    subprocess.call(["sudo", "ifconfig", interface_name, "down"])
    subprocess.call(["sudo", "ifconfig", interface_name, "hw", "ether", mac_random])
    subprocess.call(["sudo", "ifconfig", interface_name, "up"])


interface_name = input("\n\nEnter interface to change MAC of\n\t>>> ")
# thanks stackoverflow random mac generator
mac_random = ":".join("%02x"%random.randint(0,255) for x in range(6))

# run_ifconfig interface_name before MAC is changed
print("\n  -- OLD MAC --\n")
run_ifconfig()

# mac_change
mac_change()

# run ifconfig interface_name again with new MAC
print("\n  -- NEW MAC --\n")
run_ifconfig()

print("""

IF ANY ERRORS TRY RE-RUNNING maccas_random.py

###----  MACCAS HAS ENDED  ----###""")
