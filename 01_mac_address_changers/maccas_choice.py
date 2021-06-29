#!/usr/bin/env python3

import subprocess

def run_ifconfig():
    subprocess.call(["ifconfig", interface_name])

def mac_change():
    # sudo int_name down - hw ether {MAC Change} - int_name up
    print(f"\n---  Changing Mac Address for {interface_name}  ---\n")
    subprocess.call(["sudo", "ifconfig", interface_name, "down"])
    subprocess.call(["sudo", "ifconfig", interface_name, "hw", "ether", mac_choice])
    subprocess.call(["sudo", "ifconfig", interface_name, "up"])


interface_name = input("\n\nEnter interface to change MAC of\n\t>>> ")
mac_choice = input('Enter a new MAC address... format "ab:cd:ed:01:23:89"\n\t>>> ')

# run_ifconfig interface_name before MAC is changed 
print("\n\t  -- OLD MAC --\n")
run_ifconfig()

# mac_change
mac_change()

# run ifconfig interface_name again with new MAC
print("\n\t  -- NEW MAC --\n")
run_ifconfig()

print("""

IF ANY ERRORS ABOVE TRY RE-RUNNING maccas_choice.py
THE MAC YOU ENTERED MAY NOT BE ALLOWED
LOOK AT YOUR CURRENT MAC FIRST

###----  MACCAS HAS ENDED  ----###""")
