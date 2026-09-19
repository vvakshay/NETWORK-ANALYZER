from alert_detection import port_scan_detection,arp_anomaly_detection
from device_lookup import load_database,get_vendor
from scapy.all import sniff,IP,TCP,UDP,ICMP,ARP,Ether
database=load_database()
def packet_handler(packets):
	if Ether in packets:
		source_mac=packets[Ether].src
		dest=packets[Ether].dst
		source=get_vendor(source_mac,database)
		destination=get_vendor(dest,database)
		print("Source mac:",source_mac)
		print("Source Vendor:",source)
		print("Destination mac:",dest)
		print("Destination vendor:",destination)
	if IP in packets:
		src_ip=packets[IP].src
		dst_ip=packets[IP].dst
		print(f"Source:{src_ip}")
		print(f"Destination:{dst_ip}")
		if TCP in packets:
			print("Protocol: TCP")
			srce=packets[TCP].sport
			dst_port=packets[TCP].dport
			print(f"Source port {srce}")
			print(f"Destination port {dst_port}")
			print("-"*40)
			port_scan_detection(src_ip,dst_ip,dst_port)
		elif UDP in packets:
			print("Protocol: UDP")
			print(f"Source port {packets[UDP].sport}")
			print(f"Destination port {packets[UDP].dport}")
			print("-"*40)
		elif ICMP in packets:
			print("Protocol: ICMP")
			print("-"*40)
	elif ARP in packets:
		print("Protocol: ARP")
		print(f"Source ip {packets[ARP].psrc}")
		print(f"Destination ip {packets[ARP].pdst}")
		print(f"Source mac {packets[ARP].hwsrc}")
		print(f"Destination mac {packets[ARP].hwdst}")
		arp_anomaly_detection(packets[ARP].psrc,packets[ARP].hwsrc)
		print("-"*40)
def start_sniffing():
	print("Starting packet capture")
	print("Press ctrl+c to stop this  process")
#Call the function whenever it captures a packet 
	sniff(prn=packet_handler,store=False)
