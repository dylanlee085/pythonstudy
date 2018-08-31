#!/usr/bin/env pyhton
# coding: utf-8



import re
from collections import namedtuple

Disk = namedtuple('Disk','major_number minor_number device_name'
                          ' read_count read_merged_count read_sections'
                          ' time_spent_reading write_count write_merged_count'
                          ' write_sections time_spent_write io_requests'
                          ' time_spent_doing_io weighted_time_spent_doing_io'
                  )

def discovery_disk():
    with open('/proc/diskstats', 'r') as f:
        content = str(f.readlines())
        pattern = re.compile(r'[a-z]d[a-z]*')
        disk = re.findall(pattern, content)
    return list(set(disk))

def get_disk_info(device):
    for i in device:
        with open("/proc/diskstats") as f:
            for line in f:
                if line.split()[2] == i:
                    return Disk(*(line.split()))

def main():
    device = discovery_disk()
    disk_info = get_disk_info(device)
#    print disk_info
    print("磁盘写次数：{0}".format(disk_info.write_count))
    print("磁盘写字节数：{0}".format(disk_info.write_sections))
    print("磁盘写延时：{0}".format(disk_info.time_spent_write))
    
if __name__ == '__main__':
    main()
