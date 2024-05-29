import yaml


class Config:
    def __init__(self, config_path):
        self.config_path = config_path
        self.cfg = {}
        self.load_config()

    def load_config(self):
        with open(self.config_path) as config:
            try:
                self.cfg = yaml.safe_load(config)
            except yaml.YAMLError as exc:
                print(exc)


cfg = Config('config.yaml')
