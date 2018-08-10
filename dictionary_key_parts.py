def get_dictionary_value(dictionary, key):
    key_parts = key.split(".")

    current_value = dictionary

    for key_part in key_parts:
        current_value = current_value[key_part]


    return current_value

def set_dictionary_value(dictionary, key, value):
    key_parts = key.split(".")
    last_key = key_parts.pop()

    current_dictionary = dictionary

    for key_part in key_parts:
        if key_part not in current_dictionary:
            current_dictionary[key_part] = {}

        current_dictionary = current_dictionary[key_part]

    current_dictionary[last_key] = value

report = {
    "app.canSeeAddAJob": {
        "inherited": True
    },
    "app.canSeeBilling": {
        "inherited": False
    },
    "app.canSeeInbox": {
        "inherited": False
    },
    "notifications.email.events.appointment__assigned": {
        "inherited": False
    },
    "notifications.email.events.job__created": {
        "inherited": True
    }
}

config = {
    "app": {
        "canSeeAddAJob": True,
        "canSeeBilling": True,
        "canSeeInbox": False
    },
    "notifications": {
        "email": {
            "events": {
                "appointment__assigned": {
                    "template": {
                        "body": "Test Template",
                        "when": "always"
                    }
                },
                "job__created": {
                    "template": {
                        "body": "Test Template",
                        "when": "never"
                    }
                }
            }
        }
    }
}

post_values = {}

for item in report:
    if report[item]["inherited"] == False:
        config_value = get_dictionary_value(config, item)

        set_dictionary_value(post_values, item, config_value)

print(post_values)