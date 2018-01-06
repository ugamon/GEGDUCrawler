#encoding=utf-8
import os
import sys

#BASE PATH
if sys.platform == "win32":
    BASE_PATH = os.path.join(*os.path.dirname(os.path.abspath(__file__)).split('\\')[:-1])
else:
    raise SystemError("Module is written for Windows bitches. SO FUCK YOU!")

#SAMPLE OUTPUT CONFIG
SAMPLE_FILENAME = r"sample.csv"
DELIMETER = r';'