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


class Inputs:

    def __init__(self):

        pass

    def environment(self):

        while 1:
            env = input('\n\n\nEnvironment:\n- Dev\n- Staging\n- Sandbox\n(Choose environment): ').lower()

            if env in ['dev', 'staging', 'sandbox']:
                return env

            else:
                print('\n Not a valid environment!')
                continue

    def bearer_token(self):

        bearer_token = input('\nEnter admin bearer token: ')
        return bearer_token

    def account(self):

        while 1:
            account_id = input('Account ID: ')

            if account_id.isdigit():
                return account_id

            else:
                print('\nNot a valid account ID!.')
                continue

    def entity(self):

        while 1:
            entity_role = input('\n Account entity (dispatcher/technician/customer): ')

            if entity_role in ['dispatcher', 'technician', 'customer']:
                return entity_role

            else:
                print('\nNot a valid entity role!')
                continue

    def proceed(self, proceed, config_report, raw_config, config):
        global post_values
        if proceed in ['y', 'yes', 'Yes', 'YES']:
            post_values = {}
            for item in config_report:
                if not config_report[item]["inherited"]:
                    config_value = raw_config.get_dictionary_value(config, item)
                    raw_config.set_dictionary_value(post_values, item, config_value)
        else:
            print('\nOperation stopped\n')
        return post_values


def main():
    inputs = Inputs()
    env1 = inputs.environment()

    bearer_token1 = inputs.bearer_token()
    account_id1 = inputs.account()
    entity1 = inputs.entity()
    raw_config = GetConfig('-' + env1)
    config = raw_config.get(account_id1, entity1, bearer_token1)

    config_json = json.dumps({"overwrite": False, "config": raw_config.get(account_id1, entity1, bearer_token1)},
                             indent=4,
                             sort_keys=True)
    config_report = raw_config.get_report(account_id1, entity1, bearer_token1)

    print(config_json)
    print('\n\n***SETTINGS SAVED IN MEMORY***')

    env2 = inputs.environment()
    bearer_token2 = inputs.bearer_token()
    account_id2 = inputs.account()
    entity2 = inputs.entity()

    proceed = input('Are you sure you want to copy the settings from %s to %s? (y/n) [ENTER=Abort]? ' % (
        env1.upper(), env2.upper()))
    post_values = inputs.proceed(proceed, config_report, raw_config, config)

    post_config = PostConfig('-' + env2)
    post_config.post_config(account_id2, entity2, bearer_token2, post_values)


if __name__ == '__main__':
    main()
