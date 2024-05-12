import subprocess
import pyfiglet
import optparse
import re
text = "SIR RA3D"
ascii_art = pyfiglet.figlet_format(text, font="slant")

print(ascii_art)
def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="network_interface", help="This is for network interface ")
    parser.add_option("-m", "--mac", dest="new_mac", help="This is for MAC Address ")
    options, arguments = parser.parse_args()

    if not options.network_interface:
        print("[-] Specify an interface please, type -h for help ")
        exit()

    if not options.new_mac:
        print("[-] Specify MAC Address , type -h for help")
        exit()

    return options


def mac_changer(network_interface, new_mac):
    subprocess.call(" ifconfig " + network_interface + " down ", shell=True)
    subprocess.call(" ifconfig " + network_interface + " hw ether " + new_mac, shell=True)
    subprocess.call(" ifconfig " + network_interface + " up", shell=True)
    print("[+] Changing MAC Address for " + network_interface + " to " + new_mac)


def get_mac(network_interface):
    ifconfig_result = subprocess.check_output("ifconfig " + network_interface, shell=True).decode("UTF-8")

    mac_address = re.search("\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    return mac_address[0]


options = get_arguments()
mac_changer(options.network_interface, options.new_mac)
mac_address = get_mac(options.network_interface)

if mac_address == options.new_mac:
    print("[+] Mac address has changed successfully " + options.new_mac)
else:
    print("Something went wrong............")
