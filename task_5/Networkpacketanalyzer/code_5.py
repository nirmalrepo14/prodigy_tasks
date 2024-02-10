import scapy.all as scapy

def sniff_packets(interface=None):
    print("[+] Sniffing Packets...")

    # Start sniffing packets
    if interface:
        scapy.sniff(iface=interface, store=False, prn=process_packet)
    else:
        scapy.sniff(store=False, prn=process_packet)

def process_packet(packet):
    # Extract relevant information from the packet
    if packet.haslayer(scapy.IP):
        ip_src = packet[scapy.IP].src
        ip_dst = packet[scapy.IP].dst
        protocol = packet[scapy.IP].proto

        print(f"[*] Source IP: {ip_src} | Destination IP: {ip_dst} | Protocol: {protocol}")

        # If packet has TCP layer
        if packet.haslayer(scapy.TCP):
            payload = packet[scapy.TCP].payload
            print(f"    [+] TCP Payload: {payload}")

        # If packet has UDP layer
        elif packet.haslayer(scapy.UDP):
            payload = packet[scapy.UDP].payload
            print(f"    [+] UDP Payload: {payload}")

        # If packet has ICMP layer
        elif packet.haslayer(scapy.ICMP):
            payload = packet[scapy.ICMP].payload
            print(f"    [+] ICMP Payload: {payload}")

        # If packet has other layers
        else:
            payload = packet.payload
            print(f"    [+] Other Payload: {payload}")

# Main function
def main():
    # Specify the network interface to sniff on (e.g., 'eth0')
    interface = None

    # Start sniffing packets
    sniff_packets(interface)

# Execute main function
if __name__ == "__main__":
    main()

