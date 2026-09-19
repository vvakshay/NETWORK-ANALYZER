🔐 Network Analyzer

A real-time Python-based network security monitoring and analysis tool that captures network packets, identifies network devices and protocols, detects suspicious activity, logs security events, and sends real-time alerts to a mobile phone.

🚀 Features

- 📡 Real-time packet sniffing using Scapy
- 🌐 Source and destination IP analysis
- 🔌 Protocol and packet-type identification
- 🖥️ MAC address analysis
- 🏷️ MAC vendor/device identification
- 🚨 Port scan detection
- ⚠️ ARP anomaly detection
- 📝 Security alert logging
- 📱 Real-time mobile notifications
- 🔔 Automated security alerts

🔎 Detection Capabilities

Port Scan Detection

Tracks connection attempts and destination ports to identify patterns that may indicate port-scanning or reconnaissance activity.

ARP Anomaly Detection

Monitors ARP traffic and identifies unusual ARP behavior that may indicate network anomalies or potential ARP-based attacks.

Alert Logging

Security events are recorded in an alert log, creating a history of detected events that can be reviewed for further analysis.

Mobile Alerts

When a suspicious event is detected, the analyzer sends a real-time notification to a mobile phone, allowing security events to be monitored remotely.

⚙️ How It Works

Network Traffic
       ↓
Packet Sniffer
       ↓
Packet Analysis
       ↓
┌──────────────────────────────┐
│ IP / MAC Analysis            │
│ Protocol Identification      │
│ Device Identification        │
│ Port Scan Detection          │
│ ARP Anomaly Detection        │
└──────────────────────────────┘
       ↓
  Security Event
       ↓
 ┌───────────────┐
 │               │
 ↓               ↓
Alert Log    Mobile Alert

🛠️ Technologies

- Python
- Scapy
- Linux
- Packet Sniffing
- Network Traffic Analysis
- ARP Analysis
- Port Scan Detection
- Security Event Logging
- Mobile Notifications

📂 Project Structure

Network-Analyzer/
│
├── main.py
├── sniffer.py
├── device_lookup.py
├── port_scan_detection.py
├── arp_anomaly_detection.py
├── alert_phone.py
└── README.md

▶️ Installation

Clone the repository:

git clone https://GitHub.com/vvakshay/NETWORK-ANALYZER.git
cd Network-Analyzer

Install the required dependency:

pip install scapy

Run the analyzer:

sudo python3 main.py

«Root/administrator privileges may be required for packet capture depending on the operating system and network interface configuration.

A corresponding security event is written to the alert log and can trigger a mobile notification.

🎯 Project Objectives

This project was built to gain practical experience in:

- Network packet analysis
- Network monitoring
- Python-based security automation
- ARP behavior analysis
- Port-scan detection
- Security event logging
- Real-time security alerting

🔮 Future Improvements

- DNS traffic analysis
- Additional network attack detection
- Threat intelligence integration
- Machine-learning-based anomaly detection
- Web-based monitoring dashboard
- Advanced traffic visualization
- Centralized security event management

⚠️ Ethical Use

This project is intended for educational purposes and authorized security monitoring only.

Only capture or analyze traffic on networks and devices that you own or have explicit permission to monitor.

👨‍💻 Author

Akshay V V

B.Tech CSE — Cyber Security

Built as a hands-on project exploring network security, packet analysis, anomaly detection, security logging, and automated alerting.
