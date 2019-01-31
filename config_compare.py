from config_service import ConfigClient as cc
import json


env_a = cc()
env_a.environment_input()
env_a.admin_token_input()
env_a.account_input()
env_a.entity_input()
config_report_a = env_a.get_account_config_report()

print(config_report_a)

env_b = cc()
env_b.environment_input()
env_b.admin_token_input()
env_b.account_input()
env_b.entity_input()
config_report_b = env_a.get_account_config_report()
print(config_report_b)

for i,x in config_report_a:
    print(i)
#
#
# for i,j in enumerate(config_report_a):
#     for x,y in enumerate(config_report_b):
#         if y[x] == j[i]:
#             print("MATCH")


# env_b = ConfigClient.get_account_config_report()



