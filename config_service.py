import json
import requests


class ConfigClient:

    def __init__(self, env=None, admin_token=None, account_id=None, entity=None):
        self.env = env
        self.account_id = account_id
        self.entity = entity
        self.admin_token = admin_token

    def __str__(self):
        return 'Environment: {}\nAdmin token: {}\nAccount ID: {}\nEntity: {}'.format(self.env, self.admin_token,
                                                                                     self.account_id, self.entity)

# Retrieve account configurations
    def get_account_config(self):
        """
        :return: GET json payload of account configurations
        """

        headers = {'Content-Type': 'application/json', 'Cache-Control': 'no-cache',
                   'Authorization': 'Bearer ' + self.admin_token}
        if self.env is None:
            endpoint = 'https://admin-api.dispatch.me/config/account_'
        else:
            endpoint = 'https://admin-api{}.dispatch.me/config/account_{}/{}'.format(self.env, self.entity,
                                                                                     self.account_id)
        r = requests.get(endpoint, headers=headers)
        config_dict = r.json()
        # config_dict = json.loads(r_raw)
        if 'error' in config_dict and config_dict['error'] == 'Unauthorized':
            print("Invalid bearer token!")
            exit()
        else:
            return config_dict

# Retrieve a report of account configurations (with inherited flag)
    def get_account_config_report(self):
        """
        :return: GET report json payload of all the account configurations
        """

        headers = {'Content-Type': 'application/json', 'Cache-Control': 'no-cache',
                   'Authorization': 'Bearer ' + self.admin_token}
        if self.env is None:
            endpoint = 'https://admin-api.dispatch.me/config/account_'
        else:
            endpoint = 'https://admin-api{}.dispatch.me/config/account_{}/{}'.format(self.env, self.entity,
                                                                                     self.account_id)
        r = requests.get(endpoint + '?report=true', headers=headers)
        report_dict = r.json()
        return report_dict

# Put values returned
    def get_dictionary_value(self, dictionary, key):
        """
        :param dictionary:
        :param key:
        :return: split json fields and add to a list
        """

        key_parts = key.split(".")

        current_value = dictionary

        for key_part in key_parts:
            current_value = current_value[key_part]

        return current_value

    def set_dictionary_value(self, dictionary, key, value):
        """
        :param dictionary:
        :param key:
        :param value:
        :return:
        """

        key_parts = key.split(".")
        last_key = key_parts.pop()

        current_dictionary = dictionary

        for key_part in key_parts:
            if key_part not in current_dictionary:
                current_dictionary[key_part] = {}

            current_dictionary = current_dictionary[key_part]

        current_dictionary[last_key] = value

    def post_config_to_destination(self, config_value=None):
        """
        :param config_value:
        :return: POST json payload of all the account configurations
        """

        config_dumps = json.dumps({"overwrite": False, "config": config_value}, indent=4, sort_keys=True)
        headers = {'Content-Type': 'application/json', 'Cache-Control': 'no-cache',
                   'Authorization': 'Bearer ' + self.admin_token}
        endpoint = 'https://admin-api{}.dispatch.me/config/account_{}/{}'.format(self.env, self.entity, self.account_id)

        post = requests.post(endpoint, headers=headers, data=config_dumps)
        # post_response=post.text
        if '{"error":"Unauthorized"}' in post.text:
            print("Invalid bearer token!")
            exit()
        else:
            print(config_dumps + '\n')
            print(post.text + '\n')

    def environment_input(self):
        """
        :return: takes environment input and validates against existing environments
        """

        while 1:
            self.env = input(
                '\nEnvironment:\n- Dev\n- Staging\n- Sandbox\n- Production \n(Choose environment): ').lower()

            if self.env in ['dev', 'staging', 'sandbox', 'production']:
                if self.env == 'production':
                    return None
                else:
                    self.env = '-' + self.env
                    return self.env

            else:
                print('\n Not a valid environment!')
                continue

    def admin_token_input(self):
        """
        :return: takes environment bearer_token
        """
        self.admin_token = input('\nEnter admin bearer token: ')
        return self.admin_token

    def account_input(self):
        """
        :return: takes an account id and validate it is numerical
        """
        while 1:
            self.account_id = input('Account ID: ')

            if self.account_id.isdigit():
                return self.account_id

            else:
                print('\nNot a valid account ID!.')
                continue

    def entity_input(self):
        """
        :return: takes entity role and validates it.
        """

        while 1:
            self.entity = input('\n Account entity (dispatcher/technician/customer): ')

            if self.entity in ['dispatcher', 'technician', 'customer']:
                return self.entity

            else:
                print('\nNot a valid entity role!')
                continue

    def check_inheritance(self, proceed=None, config_report=None, config=None):
        """
        :param proceed:
        :param config_report:
        :param config:
        :return: checks if proceed = y and checks for inherited configs
        """
        global post_values
        if proceed in ['y', 'yes', 'Yes', 'YES']:
            post_values = {}
            for item in config_report:
                if not config_report[item]["inherited"]:
                    config_value = self.get_dictionary_value(config, item)
                    self.set_dictionary_value(post_values, item, config_value)
        else:
            print('\nOperation stopped\n')
        return post_values

    def backup_destination_config(self):
        headers = {'Content-Type': 'application/json', 'Cache-Control': 'no-cache',
                   'Authorization': 'Bearer ' + self.admin_token}
        if self.env is None:
            endpoint = 'https://admin-api.dispatch.me/config/account_'
        else:
            endpoint = 'https://admin-api{}.dispatch.me/config/account_{}/{}'.format(self.env, self.entity,
                                                                                     self.account_id)
        r = requests.get(endpoint, headers=headers)
        config_dict = r.text
        # config_dict = json.loads(r_raw)
        with open('{}_config_backup.json'.format(self.env), 'w') as backup:
            backup.write(config_dict)
        print("Config backup created")

    def backup_destination_config_report(self):
        headers = {'Content-Type': 'application/json', 'Cache-Control': 'no-cache',
                   'Authorization': 'Bearer ' + self.admin_token}
        if self.env is None:
            endpoint = 'https://admin-api.dispatch.me/config/account_'
        else:
            endpoint = 'https://admin-api{}.dispatch.me/config/account_{}/{}'.format(self.env, self.entity,
                                                                                     self.account_id)
        r = requests.get(endpoint + '?report=true', headers=headers)
        report_dict = r.text
        with open('{}_config_backup_report.json'.format(self.env), 'w') as backup:
            backup.write(report_dict)
        print("Config report backup created")



def main():
    env_a = ConfigClient()
    env_a.environment_input()
    env_a.admin_token_input()
    env_a.account_input()
    env_a.entity_input()
    config = env_a.get_account_config()
    config_report = env_a.get_account_config_report()
    print('\n\n***SOURCE CONFIGURATIONS SAVED IN MEMORY***')

    env_b = ConfigClient()
    env_b.environment_input()
    env_b.admin_token_input()
    env_b.account_input()
    env_b.entity_input()

    # process = ConfigClient()
    proceed = input(
        'Are you sure you want to copy the configurations from {} to {}? (y/n) [ENTER=Abort]? '.format(env_a.env.upper(),
                                                                                                 env_b.env.upper()))
    env_b.backup_destination_config()
    env_a.backup_destination_config_report()
    post_values = env_a.check_inheritance(proceed, config_report, config)
    env_b.post_config_to_destination(post_values)

    # print(post_values)


if __name__ == '__main__':
    main()
