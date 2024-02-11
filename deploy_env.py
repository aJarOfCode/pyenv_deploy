import argparse
import os
import sys
import configparser

def read_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config

def parse_args():
    parser = argparse.ArgumentParser(description="This tool helps you quickly deploy your environment (Python only).")
    parser.add_argument('-f', '--file', type=str, help="Specifies the passed file.")
    parser.add_argument('-d', '--directory', type=str, help="Specifies the passed folder.")
    parser.add_argument('--conda', type=bool, default=False, help="Specifies whether to use the conda command.")
    args = parser.parse_args()
    return args
args=parse_args()
def install_requirements(config):
    if args.conda:
        os.popen("conda install --file " + args.directory + "requirements.txt -i "+config.get('mirror','conda_mirror')).read()
    else:
        os.popen("pip install -r " + args.directory + "requirements.txt"+config.get('mirror','pip_mirror')).read()
    os.popen().close()

def freeze_requirements(config):

    os.popen("pip freeze < " + args.file + " > requirements.txt")
    install_requirements(config)

def main():
    config = read_config()
    if args.file:
        freeze_requirements(config)
    if args.directory:
        install_requirements(config)

if __name__ == "__main__":
    main()
