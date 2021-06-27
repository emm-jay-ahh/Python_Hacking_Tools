#!/usr/bin/env python3

import subprocess

def run_ifconfig():
    subprocess.call(["ifconfig", interface_name])
    return

def mac_change():
    # sudo int_name down - hw ether {MAC Change} - int_name up
    subprocess.call(["sudo", "ifconfig", interface_name, "down"])
    subprocess.call(["sudo", "ifconfig", interface_name, "hw", "ether", mac_choice])
    subprocess.call(["sudo", "ifconfig", interface_name, "up"])
    return


interface_name = input("\n\nEnter interface to change MAC of\n\t>>> ")
mac_choice = input('Enter a new MAC address... format "AA:BB:CC:11:22:33"\n\t>>> ')
 
print(f"\n---  Changing Mac Address for {interface_name}  ---\n")
print("  -- OLD --\n")

# run_ifconfig interface_name before MAC is changed
run_ifconfig()

# mac_change
mac_change()

print("\n  -- NEW --\n")
# run ifconfig interface_name again with new MAC
run_ifconfig()

print("""

IF ANY ERRORS TRY RE-RUNNING maccas_choice.py

###----  MACCAS HAS ENDED  ----###""")
