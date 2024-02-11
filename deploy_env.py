import argparse
import os
import sys
import configparser

def read_config():
    config=configparser.ConfigParser()
    config.read('config.ini')
    return config

def configuration_parameter():
    parser = argparse.ArgumentParser(description="This tool helps you quickly deploy your environment (Python only).")
    parser.add_argument('-f','--file', type=str, help="Specifies the passed file.")
    parser.add_argument('-dir','--folder',type=str, help="Specifies the passed folder.")
    parser.add_argument('--conda',type=bool,default=False,help="Specifies whether to use the conda command.")
    args = parser.parse_args()
    return args

args = configuration_parameter()

def Use_requirements():
    config=read_config()
    if args.conda:
        os.popen("conda install --file "+args.folder).read()
    else:
        os.popen("pip install -r "+args.folder).read()

def open_file(file_name):
    os.popen("pip freeze <"+file_name+"> > requirements.txt")
    Use_requirements()

def open_folder():
    try:
        files=os.listdir(args.folder)
        if "requirements.txt" not in files:
            os.popen("cd "+args.folder).read()
            os.popen("pip freeze > requirements.txt")
        Use_requirements()
    except:
        print("Sorry,Folder not found.Check that the path is correct.")


def main():
    args = configuration_parameter()
    if args.file:
        open_file(args.file)
    if args.folder:
        open_folder()

if __name__ == "__main__":
    main()
