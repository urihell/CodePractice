import requests
import json


class GetConfig:

    def __init__(self, r_json=None, env='-dev'):
        # self.bearer_token = bearer_token
        # self.headers = headers
        # self.endpoint = endpoint'
        self.r_json = r_json
        self.env = env

    def get(self, account_id):
        """
        :param env:
        :param account_id:
        :return: GET json payload of all the account configurations
        """
        bearer_token = '4f090060081cc74a683ecfbfb8fda256a5872abfe2162d2dd44878e3c48b0458'
        headers = {'Content-Type': 'application/json', 'Cache-Control': 'no-cache',
                   'Authorization': 'Bearer ' + bearer_token}
        endpoint = "https://admin-api" + self.env + ".dispatch.me/config/account_dispatcher/"
        r = requests.get(endpoint + account_id, headers=headers)
        r_raw = r.content
        self.r_json = json.loads(r_raw)

    def get_complete(self):
        """
        :param
        :return: Parsed "Cancel Reasons" from account_id
        """
        parsed = json.dumps(self.r_json["app"]["completeReasons"], indent=4, sort_keys=True)
        print("Complete Reasons:\n" + parsed)

    def get_cancel(self):
        """
        :param
        :return: Parsed "Cancel Reasons" from account_id
        """
        parsed = json.dumps(self.r_json["app"]["cancelReasons"], indent=4, sort_keys=True)
        print("Cancel Reasons:\n" + parsed)

    def get_reject(self):
        """
        :param
        :return: Parsed "Reject Reasons" from account_id
        """
        parsed = json.dumps(self.r_json["app"]["rejectReasons"], indent=4, sort_keys=True)
        print("Reject Reasons:\n" + parsed)


class PostConfig:

    def __init__(self, r_json=None, env='-dev'):
        self.r_json = r_json
        self.env = env

    def post(self, account_id, payload=None):
        """
        :param account_id:
        :param env:
        :return: POST json payload of all the account configurations
        """
        bearer_token = '4f090060081cc74a683ecfbfb8fda256a5872abfe2162d2dd44878e3c48b0458'
        headers = {'Content-Type': 'application/json', 'Cache-Control': 'no-cache',
                   'Authorization': 'Bearer ' + bearer_token}
        endpoint = "https://admin-api" + self.env + ".dispatch.me/config/account_dispatcher/"
        r = requests.post(endpoint + account_id, headers=headers, data=payload)
        print(r.text)

    # def post_complete(self, data):
    #     """
    #     :param data:
    #     :return: Update Complete Reasons for account_id
    #     """
    #     r_post = self.r


def main():
    # env = '-' + input("Environment (staging\dev\sandbox): ")
    account_id = input("Account ID: ")
    get_config = GetConfig()
    get_config.get(account_id)
    get_config.get_complete()
    get_config.get_cancel()
    get_config.get_reject()

    lines = []
    while True:
        line = input("Enter a complete reason: ")
        if line:
            lines.append(line)
        else:
            break
    data = lines
    if data is not None:
        payload = json.dumps({"overwrite": False, "config": {"app": {"completeReasons": data}}}, indent=4, sort_keys=True)
        post_config = PostConfig()
        post_config.post(account_id, payload)
    else:
        print("No update was made")
    # print(payload)


main()
