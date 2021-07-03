#!/usr/bin/env python3

import subprocess
import argparse
import re

# Function HELP AND ARG INPUT:
# allow displaying help maccas -h or --help
# parse options "-i or --interface and -m or --mac"
# and accepting argument inputs at command line 
# helper text output if missed an argument
def argument_input():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--interface", dest="interface", help="Interface to change MAC")
    parser.add_argument("-m", "--mac", dest="new_mac_address", help="New MAC address entry. EXAMPLE FORMAT: a3:2e:9c:18:8d:81")
    options = parser.parse_args()
    if not options.interface:
        parser.error("\n\n\tALERT >>>\
        \n\n\tMESSAGE:\tInterface missing\
        \n\tRUN:\t\tifconfig \
        \n\tEXAMPLE:\tinterface could be 'eth0' or 'wlan0'\
        \n\tCOMMAND:\tmaccas -i eth0 -m 01:ab:cd:ef:23:89\
        \n\tSEE:\t\tmaccas -h or --help\
        \n\n\tEND <<<")
    elif not options.new_mac_address:
        parser.error("\n\n\tALERT >>>\
        \n\n\tMESSAGE:\tMAC address missing\
        \n\tRUN:\t\tifconfig\
        \n\tEXAMPLE:\tmac address 'aa:bb:bb:11:22:33'\
        \n\tCOMMAND:\tmaccas -i eth0 -m 01:ab:cd:ef:23:89\
        \n\tSEE:\t\tmaccas -h or --help\
        \n\n\tEND <<<")
    return options

#Function ALTER MAC ADDRESS:
# print interface entered and mac changes
# bash cmd 'sudo ifconfig {interface} down'                             TURN INTERFACE OFF
# bash cmd 'sudo ifconfig {interface} hw ether {new_mac_address}'       CHANGE MAC ADDRESS       
# bash cmd 'sudo ifconfig {interface} up'                               TURN INTERFACE ON
def change_mac_address(interface, new_mac_address):
    print(f"\n\tSTART >>>\n\n\tPROCESS: MAC Address for '{interface}' to '{new_mac_address}'\n\n\tEND <<<")
    subprocess.call(["sudo", "ifconfig", interface, "down"])
    subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", new_mac_address])
    subprocess.call(["sudo", "ifconfig", interface, "up"])

def print_current_mac(interface):
    # print output of the curretn MAC
    cmd_ifconfig_interface = subprocess.check_output(["ifconfig", interface])
    search_result_mac_address = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(cmd_ifconfig_interface))

    if search_result_mac_address:
        return search_result_mac_address.group(0)
    else:
        print("ERROR:  Unable to read MAC address")

options = argument_input()

current_mac = print_current_mac(options.interface)
print(f"\n\n\tCURRENT: {current_mac}")

change_mac_address(options.interface, options.new_mac_address)

current_mac = print_current_mac(options.interface)
if current_mac == options.new_mac_address:
    print(f"\tSUCCESS: The mac address has been updated to {current_mac}\n")
else:
    print("\n\tERROR: The mac address has not changed\n")
