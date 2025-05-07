#!/bin/bash

output_file="nslookup_results.txt"

# Xóa file đầu ra nếu tồn tại
if [[ -f "$output_file" ]]; then
    rm "$output_file"
fi

target="www.example.com"

# Lặp 1000 lần thực hiện nslookup
for i in {1..1000}; do
    echo "Number $i:" >> "$output_file"
    nslookup "$target" >> "$output_file" 2>&1
    echo -e "\n----------------------\n" >> "$output_file"
done

echo "Result saved to $output_file"
