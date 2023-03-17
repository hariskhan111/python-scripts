#!/usr/bin/env python3
import re 
import operator
import csv 

def find_error(log_file):
    file1 = open(log_file, 'r')
    errors = {}
    while True:
        line = file1.readline()

        if not line:
            break
        else:
            error_exist = re.search(r"ticky: ([\w ]*) ([\w ]*)", line)
            if error_exist:
                error_type = error_exist.group(1)
                log_error = error_exist.group(1)
                log_error = log_error.strip()
                errors[log_error] = errors.get(log_error,0) + 1

    errors = sorted(errors.items(), key = operator.itemgetter(1), reverse=True)
    return errors

def create_csv(errors):
    fieldnames = ['Error', 'Count']
    with open('error_message.csv','w', encoding='UTF8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer = writer.writerows(errors)

if __name__ == "__main__":
  errors = find_error("/home/ilsa/my-folder/python-scripts/managing-sys-logs/logs/syslog.log")
rows = []
for key, value in errors:
    temp = {}
    temp['Error'] = key
    temp['Count'] = value
    rows.append(temp)

create_csv(rows)