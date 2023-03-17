# Manage System Logs

### syslog file is used as a demo file
```
logs/syslog.log
```

### create csv file of all the errors triggered by users
```
./user_errors_in_system.py
```


### create csv file of all the system error with count 
```
./count_system_errors.py
```


### to create html table of all system error with count run command
```
./csv_to_html.py user_statistics.csv /var/www/html/user_statistics.html
```


### to create html table of all system error with count run command
```
./csv_to_html.py error_emails.csv /var/www/html/error_email.html
```
