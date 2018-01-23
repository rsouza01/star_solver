#!/usr/bin/python3


import configparser


def generate_default_config():


    config = configparser.ConfigParser()

    config['EOS'] = {}
    config['EOS']['filename'] = 'eos.csv'


    with open('solver.ini', 'w') as configfile:
        config.write(configfile)


def main():
    generate_default_config()


if __name__ == "__main__":
        main()

