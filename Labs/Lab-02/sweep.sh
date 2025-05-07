#!/bin/bash

# Nhập dải IP cần quét
network="192.168.195.1-254"

# Tên tệp để lưu kết quả
output_file="sweep.txt"

# Sử dụng Nmap để quét và lưu kết quả
nmap -v -sn $network -oG $output_file

# Kiểm tra kết quả
if [ $? -eq 0 ]; then
    echo "Quét hoàn tất. Kết quả đã được lưu vào $output_file"
else
    echo "Có lỗi xảy ra khi quét"
fi
