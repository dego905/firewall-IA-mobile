#!/data/data/com.termux/files/usr/bin/bash

IFS=$'\n'
LOG=".conn_hash.log"
RAW=".conn_raw.csv"
DECISION=".decision.log"
TMP=".tmp_net"
touch $LOG $RAW $DECISION

termux-toast "Firewall con IA iniciado"

while true; do
netstat -tnp | grep ESTABLISHED > $TMP
while read -r line; do
ip=$(echo $line | awk '{print $5}' | cut -d: -f1)
pid=$(echo $line | awk '{print $7}' | cut -d/ -f1)
pname=$(ps -p $pid | awk 'NR==2 {print $1}')
hash=$(echo "$ip$pname" | sha256sum | cut -d" " -f1)
if ! grep -q "$hash" $LOG; then
echo "$hash" >> $LOG
echo "$(date +%s),$ip,$pname" >> $RAW
python3 ai_detect.py "$ip" "$pname"
decision=$(tail -n 1 $DECISION)
if [[ "$decision" == *"anomalo"* ]]; then
termux-vibrate -d 300
termux-toast "Conexión anómala detectada"
kill -9 $(ps | grep "$pname" | awk '{print $2}' | head -n 1) 2>/dev/null
fi
fi
done < $TMP
sleep 3
done
