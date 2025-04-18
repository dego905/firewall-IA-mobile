#!/bin/bash
netstat -tulnp | awk '{print $4, $7}' > conn_raw.csv
ps aux --sort=-%cpu > process_list.txt
python ai_detect.py
echo "Actividades sospechosas detectadas: $(date)" >> decision.log
while true; do
  netstat -tulnp | awk '{print $4, $7}' >> conn_raw.csv
  ps aux --sort=-%cpu >> process_list.txt
  sleep 10
done
