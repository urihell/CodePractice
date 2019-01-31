#!/usr/bin/env/ python

from config_service import ConfigClient
import csv
import os

os.chdir(os.getcwd())
# os.chdir('/Users/urieldabby/Downloads/')
cc = ConfigClient()

cc.environment_input()
cc.admin_token_input()
cc.account_input()
cc.entity_input()
report = cc.get_account_config_report()
print(report)

with open('config_report.csv', 'w') as cr:
    writer = csv.writer(cr)
    print('\nCreating config_report.csv...\n')
    for key, value in report.items():
        writer.writerow([key, value])
    print('Saving config_report.csv to: %s ' % os.getcwd())




