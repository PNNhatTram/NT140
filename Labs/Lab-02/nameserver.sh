#!/bin/bash

declare -A domain_ns

domain_ns["hcmus.edu.vn"]="dns2.hcmus.edu.vn server.hcmus.edu.vn"
domain_ns["hcmussh.edu.vn"]="ns1.vdconline.vn ns2.vdconline.vn"
domain_ns["uit.edu.vn"]="nsbak.pavietnam.net ns1.pavietnam.vn ns2.pavietnam.vn"
domain_ns["hcmut.edu.vn"]="dns4.hcmut.edu.vn dns3.hcmut.edu.vn dns2.hcmut.edu.vn dns1.hcmut.edu.vn"
domain_ns["hcmiu.edu.vn"]="hcm-server1.vnn.vn vdc-hn01.vnn.vn"
domain_ns["uel.edu.vn"]="ns1.dns.net.vn ns2.dns.net.vn"
domain_ns["hcmier.edu.vn"]="server.vnuhcm.edu.vn vnuserv.vnuhcm.edu.vn"
domain_ns["vnuhcm.edu.vn"]="server.vnuhcm.edu.vn ns1.vdc2.vn ns2.vdc2.vn vnuserv.vnuhcm.edu.vn"

# Định nghĩa màu
RED="\033[1;31m"
GREEN="\033[1;32m"
BLUE="\033[1;34m"
NC="\033[0m" # Không có màu

check_domain() {
    domain=$1
    nameservers=${domain_ns[$domain]}
    
    if [[ -z "$nameservers" ]]; then
        echo -e "${RED}No nameservers found for $domain${NC}"
        return
    fi
    
    for ns in $nameservers; do
        echo -e "${BLUE}Attempting zone transfer for ${GREEN}$domain${NC} on nameserver ${GREEN}$ns${NC}"
        host -l $domain $ns
    done
}

for domain in "${!domain_ns[@]}"; do
    echo -e "${RED}Checking domain: ${GREEN}$domain${NC}"
    check_domain $domain
    echo
done
