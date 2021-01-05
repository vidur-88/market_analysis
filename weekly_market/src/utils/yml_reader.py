import yaml


def get_yml_info(file_path, file_name):
    with open('{}/{}'.format(file_path, file_name)) as stream:
        info = yaml.safe_load(stream)
    return info
