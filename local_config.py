#encoding=utf-8
import os
import sys

#BASE PATH
if sys.platform == "win32":
    BASE_PATH = os.path.dirname(os.path.abspath(__file__))
else:
    raise SystemError("Module is written for Windows bitches. SO FUCK YOU!")

#SAMPLE OUTPUT CONFIG
SAMPLE_FILENAME = r"sample.csv"
DELIMETER = r';'