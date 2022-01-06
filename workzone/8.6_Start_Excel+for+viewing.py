#!/usr/bin/env python3

"""
Start Excel App for viewing your sheets
"""
import os

if __name__ == "__main__":
    # Open workbook
    file_name = "8.6_Open_me.xlsx"
    os.system("start EXCEL.EXE " + file_name)
