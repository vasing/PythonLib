#!/usr/bin/env python3

"""
Creating a Workbook object with OpenPyXL
Saving the workbook to disk
"""
from openpyxl import Workbook

def main():
    #Create the Workbook object
    wb = Workbook()

    # Save the workbook to disc
    wb.save('2.1_Hello_world.xlsx')
    print("Exiting main()")

if __name__ == "__main__":
    main()
