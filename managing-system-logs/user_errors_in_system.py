#!/usr/bin/env python3
import re 
import operator
import csv 
from pathlib import Path
import os

def find_error(log_file):
    file1 = open(log_file, 'r')
    errors = {}
    while True:
        line = file1.readline()

        if not line:
            break
        else:
            #get username
            error_exist = re.search(r"\((.*?)\)", line)
            if error_exist:
                user = error_exist.group(1)

            #get error type and error 
            error_exist = re.search(r"ticky: ([\w ]*) ([\w ]*)", line)
            if error_exist:
                error_type = error_exist.group(1).split(' ')[0]
                error_type = error_type.strip()
                print(error_type)
                if error_type == 'INFO':
                    has_user = errors.get(user, None)
                    if has_user:
                        errors[user]['INFO'] = errors[user].get('INFO', 0) + 1
                    else:
                        errors[user] = {'INFO':1, 'ERROR':0}
                if error_type== 'ERROR':
                    has_user = errors.get(user, None)
                    if has_user:
                        errors[user]['ERROR'] = errors[user].get('ERROR', 0) + 1
                    else:
                        errors[user] = {'INFO':0, 'ERROR':1}


    errors =  sorted(errors.items(), key=operator.itemgetter(0))
    return errors

def create_csv(errors):
    fieldnames = ['Username', 'INFO', 'ERROR']
    with open('user_statistics.csv','w', encoding='UTF8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer = writer.writerows(errors)

if __name__ == "__main__":
    errors = find_error(os.getcwd() + "/logs/syslog.log")

rows = []
for key, value in errors:
    temp = {}
    temp['Username'] = key
    temp['INFO'] = value.get('INFO')
    temp['ERROR'] = value.get('ERROR')
    rows.append(temp)

create_csv(rows)