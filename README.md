# ad7200_802.11ad-measurement-logs

testing the tp-link ad7200 bandwidth of the 60ghz link in different scenarios.

## command

example:
```
iperf3 -c 192.168.100.2 -i 10 -t 240 -J --logfile ~/logs/03_60cm-front-to-front.json
```
