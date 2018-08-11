import json
import requests


class GetConfig:

    def __init__(self, env=None):
        self.env = env

    def get(self, account_id, entity, admin_token):
        """
        :param entity:
        :param admin_token:
        :param account_id:
        :return: GET json payload of all the account configurations
        """

        headers = {'Content-Type': 'application/json', 'Cache-Control': 'no-cache',
                   'Authorization': 'Bearer ' + admin_token}
        endpoint = 'https://admin-api' + self.env + '.dispatch.me/config/account_'
        r = requests.get(endpoint + entity + '/' + account_id, headers=headers)
        r_raw = r.content
        config_dict = json.loads(r_raw)
        return config_dict

    def get_report(self, account_id, entity, admin_token):
        """
        :param entity:
        :param admin_token:
        :param account_id:
        :return: GET report json payload of all the account configurations
        """

        headers = {'Content-Type': 'application/json', 'Cache-Control': 'no-cache',
                   'Authorization': 'Bearer ' + admin_token}
        endpoint = 'https://admin-api' + self.env + '.dispatch.me/config/account_'
        r = requests.get(endpoint + entity + '/' + account_id + '?report=true', headers=headers)
        r_raw = r.content
        report_dict = json.loads(r_raw)
        return report_dict

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


class PostConfig:

    def __init__(self, env=None):
        self.env = env

    def post_config(self, account_id, entity, admin_token, config_value=None):
        """
        :param config_value:
        :param entity:
        :param admin_token:
        :param account_id:
        :return: POST json payload of all the account configurations
        """

        config_dumps = json.dumps({"overwrite": False, "config": config_value}, indent=4, sort_keys=True)
        headers = {'Content-Type': 'application/json', 'Cache-Control': 'no-cache',
                   'Authorization': 'Bearer ' + admin_token}
        endpoint = 'https://admin-api' + self.env + '.dispatch.me/config/account_'
        post = requests.post(endpoint + entity + '/' + account_id, headers=headers, data=config_dumps)

        print(config_dumps + '\n')
        print(post.text + '\n')


def main():
    global post_values

    while 1:
        env1 = input('\n\n\nCopy settings FROM:\n- Dev\n- Staging\n- Sandbox\n(Choose environment): ').lower()

        if env1.isalpha():
            break
        else:
            print('\n Please use alphabetic characters.')
            continue
    bearer_token1 = input('\nEnter admin bearer token: ')

    while 1:
        account_id1 = input('Account ID: ')

        if account_id1.isdigit():
            break
        else:
            print('\nPlease use numeric characters.')
            continue

    while 1:
        entity1 = input('\n Account entity (dispatcher/technician/customer): ')

        if entity1 == 'dispatcher' or entity1 == 'technician' or entity1 == 'customer':
            break
        else:
            print('\nPlease pick a valid entity.')
            continue

    raw_config = GetConfig('-' + env1)
    config = raw_config.get(account_id1, entity1, bearer_token1)
    config_json = json.dumps({"overwrite": False, "config": raw_config.get(account_id1, entity1, bearer_token1)},
                             indent=4,
                             sort_keys=True)
    config_report = raw_config.get_report(account_id1, entity1, bearer_token1)

    print(config_json)
    print('\n\n***SETTINGS SAVED IN MEMORY***')

    while 1:
        env2 = input('\n\n\nCopy settings TO:\n- Dev\n- Staging\n- Sandbox\n(Choose environment): ').lower()

        if env2.isalpha():
            break
        else:
            print('\n Please use alphabetic characters.')
            continue
    bearer_token2 = input('\nEnter admin bearer token: ')

    while 1:
        account_id2 = input('Account ID: ')

        if account_id2.isdigit():
            break
        else:
            print('\nPlease use numeric characters.')
            continue

    while 1:
        entity2 = input('\n Account entity (dispatcher/technician/customer): ')

        if entity2 == 'dispatcher' or entity2 == 'technician' or entity2 == 'customer':
            break
        else:
            print('\nPlease pick a valid entity.')
            continue

    proceed = input('Are you sure you want to copy the settings from %s to %s? (y/n) [ENTER=Abort]? ' % (
            env1.upper(), env2.upper()))

    if proceed == 'y' or proceed == 'yes' or proceed == 'Yes':
        post_values = {}
        for item in config_report:
            if not config_report[item]["inherited"]:
                config_value = raw_config.get_dictionary_value(config, item)
                raw_config.set_dictionary_value(post_values, item, config_value)
    else:
        print('\nOperation stopped\n')

    post_config = PostConfig('-' + env2)
    post_config.post_config(account_id2, entity2, bearer_token2, post_values)


if __name__ == '__main__':
    main()
