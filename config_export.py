#!/usr/bin/env/ python

from config_service import ConfigClient
import csv
import os

# Update to current directory
os.chdir(os.getcwd())

# Call ConfigClient class
cc = ConfigClient()

# Collect input to retrieve config
cc.environment_input()
cc.admin_token_input()
cc.account_input()
cc.entity_input()

# Retrieve config report
report = cc.get_account_config_report()

# Export config report to a csv file
with open('config_report.csv', 'w') as cr:
    writer = csv.writer(cr)
    print('\nCreating config_report.csv...\n')
    for key, value in report.items():
        writer.writerow([key, value])
    print('Saving config_report.csv to: %s ' % os.getcwd())




