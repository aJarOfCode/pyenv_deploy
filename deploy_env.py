import argparse
import os
import pkg_resources
import configparser

def read_config():
    config=configparser.ConfigParser()
    config.read('config.ini')
    return config

def is_model_installed(model_name):
    return any(dist.key == model_name for dist in pkg_resources.working_set)

def configuration_parameter():
    parser = argparse.ArgumentParser(description="This tool helps you quickly deploy your environment (Python only).")
    parser.add_argument('-f','--file', type=str, help="Specifies the passed file.")
    parser.add_argument('-dir','--folder',type=str, help="Specifies the passed folder.")
    parser.add_argument('--conda',type=bool,default=False,help="Specifies whether to use the conda command.")
    args = parser.parse_args()
    return args

args = configuration_parameter()
def open_file(file_name):
    config=read_config()
    with open(file_name, 'r', encoding='utf-8') as file:
        data = file.readlines()
    for line in data:
        if "import"in line:
            model_name=line.split(" ")[1].split(".")[0]
            if not is_model_installed(model_name):
                cmd="pip install "+model_name+" -i "+config.get("mirror","pip_mirror") if not args.conda else "conda install "+model_name+" -c "+config.get("mirror","conda_mirror")
                print(cmd)
                os.popen(cmd).read()
                print("Successfully installed "+model_name)

def open_folder():
    try:
        files=os.listdir(args.folder)
        for file in files:
            if file.endswith(".py"):
                print("Opening "+file)
                open_file(os.path.join(args.folder, file))
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

