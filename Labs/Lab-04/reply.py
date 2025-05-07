from scapy.all import *

dns_query = DNSQR(qname="www.example.net")
dns = DNS(id=0xAAAA, qr=0, qdcount=1, ancount=0, nscount=0, arcount=0, qd=dns_query)

ip = IP(dst='192.168.195.138', src='192.168.195.139')
udp = UDP(dport=53, sport=2052, chksum=0)

request = ip/udp/dns

send(request)