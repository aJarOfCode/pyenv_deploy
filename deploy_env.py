import argparse
import os
def configuration_parameter():
    parser = argparse.ArgumentParser(description="This tool helps you quickly deploy your environment (Python only).")
    parser.add_argument('-f','--file', type=str, help="Specifies the passed file.")
    parser.add_argument('-dir','--folder',type=str, help="Specifies the passed folder.")
    parser.add_argument('--conda',type=bool,default=False,help="Specifies whether to use the conda command.")
    args = parser.parse_args()
    return args
def open_file():
    args = configuration_parameter()
    file_name = args.file
    with open(file_name, 'r') as file:
        data = file.readlines()
    for line in data:
        if "import"in line:
            model_name=line.split(" ")[1]
            if args.conda:
                cmd="conda install "+model_name
            else:
                cmd="pip install "+model_name
            print(cmd)
            os.popen(cmd).read()
            print("Successfully installed "+model_name)
def open_folder():
    args = configuration_parameter()
    folder_dir = args.folder
    try:
        files=os.listdir(folder_dir)
        for file in files:
            if file.endswith(".py"):
                open_file(file)
    except:
        print("Sorry,Folder not found.Check that the path is correct.")
def main():
    open_file()

if __name__ == "__main__":
    main()