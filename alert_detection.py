from send_phone_alert import send_phone_alert
import json
import os
from datetime import datetime
from collections import defaultdict
import time
scan_tracker=defaultdict(list)
def port_scan_detection(src_ip,dst_ip,dst_port):
    current_time=time.time()
    scan_tracker[(src_ip,dst_ip)].append((current_time,dst_port))
    scan_tracker[(src_ip,dst_ip)]=[
        (timestamp,port)
	for timestamp,port in scan_tracker[(src_ip,dst_ip)]
	if current_time-timestamp<=5
    ]
    unique_port={port for timestamp_,port in scan_tracker[(src_ip,dst_ip)]}
    if len(unique_port)==10:
        os.system('clear')
        print("\u26a0\ufe0f POSSIBLE PORT SCAN DETECTED")
        print(f"Source:{src_ip}")
        print(f"Destination:{dst_ip}")
        print(f"No of ports contacted:{len(unique_port)}")
        def log_port_scan(src_ip,dst_ip,unique_port):
            alert={"alert_type":"Port scan detected","message":"A port scan has been detected","Timestamp":datetime.now().strftime("%Y-%m-%d %H:%M:%S"),"Source ip":src_ip,"Destination ip":dst_ip,"Ports_detected":list(unique_port)}
            formatted_alert=f"{alert['message']}:{alert['Ports_detected']}"
            send_phone_alert(formatted_alert)
            try:
                with open ('alert.json','r') as f:
                        alerts=json.load(f)
            except (FileNotFoundError,json.JSONDecodeError):
                alerts=[]
            alerts.append(alert)
            with open('alert.json',"w") as file:
                json.dump(alerts,file,indent=4)
        log_port_scan(src_ip,dst_ip,unique_port)
	
arp={}
def arp_anomaly_detection(src_ip,mac):
    if not src_ip or not mac:
        return
    if src_ip not in arp:
        arp[src_ip]=mac
        return
    old_mac=arp[src_ip]
    os.system('clear')
    if old_mac!=mac:
        print("\U0001F6A8 ARP ANOMALY DETECTED \U0001F6A8")
        print(f"Previous mac: {old_mac}")
        print(f"New mac: {mac}")
        def log_arp_anomaly(old_mac,mac):
            try:
                alert={"alert_type":"ARP anomaly","message":"IP to MAC mapping has been changed","Timestamp":datetime.now().strftime("%Y-%m-%d %H:%M:%S"),"Old mac":old_mac,"New mac":mac}
                send_phone_alert(alert["message"])
                with open ('alert.json','r') as f:
                    alerts=json.load(f)
            except (FileNotFoundError,json.JSONDecodeError):
                alerts=[]
            alerts.append(alert)
            with open('alert.json',"w") as file:
                json.dump(alerts,file,indent=4) 
        log_arp_anomaly(old_mac,mac)
	

