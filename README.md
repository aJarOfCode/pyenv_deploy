# Python Environment Deployment Tool

This is a tool for quickly deploying Python environments. It helps you install all the required libraries and dependencies easily. Just provide a Python file containing the required libraries, and then run this tool, it will automatically install all the required libraries.

## Requirements

Make sure Python 3.x is installed.

## Usage

1. First, make sure `argparse` library is installed. If not, install it using the following command:

```
pip install argparse
```

2. Create a Python file containing the required libraries, such as `requirements.py`:

```
import numpy
import pandas
import matplotlib
```

3. Run this tool, passing the `-f` or `--file` parameter to specify the `requirements.py` file, and the `-dir` or `--folder` parameter to specify the folder containing the Python file. For example:

```
python deploy_env.py -f requirements.py -dir my_python_project
```

Or, if you want to use `conda` command to install libraries, add the `--conda` parameter(Before doing this, make sure you're inside your Anaconda environment.):

```
python deploy_env.py -f requirements.py -dir my_python_project --conda
```

4. To configure the image source, go to config.ini.
## Example

Suppose you have a file named `requirements.py` with the following content:

```
import numpy
import pandas
import matplotlib
```

Then, you want to install these libraries in a folder named `my_python_project`. Run the following command:

```
python deploy_env.py -f requirements.py -dir my_python_project
```

This will automatically install all the required libraries.

