#!/usr/local/bin/python3
import json, csv, sys, glob

logs = glob.glob('*.json')

with open('measurements.csv', 'w', newline='') as output_file:

    header=['filename', 'timestamp', 'sum_sent-Gbps', 'sum_received-Gbps','sum-sent-retranmits', 'cpu-host_total', 'cpu-remote_total', 'cpu-remote_user', 'cpu-remote_system', 'max_snd_cwnd', 'max_rtt', 'min_rtt', 'mean_rtt']
    writer = csv.DictWriter(output_file, fieldnames=header, delimiter=';')
    writer.writeheader()

    for log in logs:
        input = open(log)
        data = json.load(input)
        writer.writerow({'filename': log,
                     'timestamp': data['start']['timestamp']['time'],
                     'sum_sent-Gbps':format(data['end']['sum_sent']['bits_per_second']/(1000*1000*1000),'.4f'),
                     'sum_received-Gbps':format(data['end']['sum_received']['bits_per_second']/(1000*1000*1000),'.4f'),
                     'sum-sent-retranmits': data['end']['sum_sent']['retransmits'],
                     'cpu-host_total':format(data['end']['cpu_utilization_percent']['host_total'],'.2f'),
                     'cpu-remote_total':format(data['end']['cpu_utilization_percent']['remote_total'],'.2f'),
                     'cpu-remote_user':format(data['end']['cpu_utilization_percent']['remote_user'],'.2f'),
                     'cpu-remote_system':format(data['end']['cpu_utilization_percent']['remote_system'],'.2f'),
                     'max_snd_cwnd':data['end']['streams'][0]['sender']['max_snd_cwnd'],
                     'max_rtt':data['end']['streams'][0]['sender']['max_rtt'],
                     'min_rtt':data['end']['streams'][0]['sender']['min_rtt'],
                     'mean_rtt':data['end']['streams'][0]['sender']['mean_rtt']})

    input.close()
