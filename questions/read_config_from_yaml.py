import yaml

#Q: How would you design a Python utility to dynamically read configurations
# from different environments (dev, qa, prod)?

def read_config_from_yaml():
    with open('config.yaml', 'r') as f:
        config = yaml.safe_load(f)
    return config


def get_config_for_env():
    config = read_config_from_yaml()
    print(config["environments"]["dev"]["api_url"])

get_config_for_env()