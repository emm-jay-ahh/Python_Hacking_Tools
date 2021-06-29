#!/usr/bin/env python3

import subprocess
import optparse

# Function:
# allow displaying help maccas -h or --help
# parse options "-i or --interface and -m or --mac"
# and accepting argument inputs at command line 
# helper text output if missed an argument
def argument_input():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change MAC")
    parser.add_option("-m", "--mac", dest="new_mac_address", help="New MAC address entry. EXAMPLE FORMAT: a3:2e:9c:18:8d:81")
    (options, arguments) = parser.parse_args()
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

#Function:
# print interface entered and mac changes
# bash cmd 'sudo ifconfig {interface} down'     TURN INTERFACE OFF
# bash cmd 'sudo ifconfig {interface} hw ether {new_mac_address}'       CHANGE MAC ADDRESS       
# bash cmd 'sudo ifconfig {interface} up'       TURN INTERFACE ON
def change_mac_address(interface, new_mac_address):
    print(f"\n\tSTART >>>\n\n\tChanging MAC for '{interface}' to '{new_mac_address}'\n\n\tEND <<<")
    subprocess.call(["sudo", "ifconfig", interface, "down"])
    subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", new_mac_address])
    subprocess.call(["sudo", "ifconfig", interface, "up"])


options = argument_input()
change_mac_address(options.interface, options.new_mac_address)
