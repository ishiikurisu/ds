import os
import subprocess

class House:
    def __init__(self, repo):
        self.local = False
        self.commands = []
        self.repo = repo

    def add_command(self, command):
        self.commands.append(command)

    def build(self):
        house_config = 'src/{0}/house.yml'.format(self.repo)
        config = "---\nbuild:\n  local: {0}\n  commands:\n".format('true' if self.local else 'false')
        for command in self.commands:
            config += "  - {0}\n".format(command)
        config += '...\n'
        with open(house_config, 'w') as fp:
            fp.write(config)
        subprocess.call(['house', 'build', self.repo])
        os.remove(house_config)
