# Welcome to AK_Tools, Follow me on Telegram: https://t.me/AKHacking1 For more tools

import scapy.all as scapy
import optparse

def get_arguments():
    parser = optparse.OptionParser()
    print("------------------------------------------------------------------------------------------")
    print("   Welcome to AK_Tools, Follow me on Telegram: https://t.me/AKHacking1 For more tools ")
    print("------------------------------------------------------------------------------------------")
    parser.add_option("-r", "--range", dest="network_ip", help="To enter device IP or Network Range")
    options, arguments = parser.parse_args()

    if not options.network_ip:
        parser.error("[-] Please specify an IP Address, -h for help")
    return options

def scan(network_ip):
    arp_request = scapy.ARP(pdst=network_ip)
    arp_broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = arp_broadcast/arp_request
    answered = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    client_list = []
    for ans in answered:
        client_dict = {"ip":ans[1].psrc, "mac":ans[1].hwsrc}
        client_list.append(client_dict)
    return client_list

def display_clients(clients):
    print("IP Address\t\t MAC Address")
    print("-" * 42)
    for client in clients:
        print(client["ip"], "\t\t" ,client["mac"])

options = get_arguments()
client_list = scan(options.network_ip)
display_clients(client_list)