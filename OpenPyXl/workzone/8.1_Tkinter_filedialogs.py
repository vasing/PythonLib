#!/usr/bin/env python3

"""
Open file and save file dialogs with tkinter
Icon by Paulo Ruberto
http://www.iconarchive.com/show/custom-round-yosemite-icons-by-pauloruberto/Python-icon.html

If you are using VSCode:
1) add root.mainloop() as the last line in the script, and 
2) comment out root.withdraw() as you will need to 'X' out of this window otherwise VSCode will hang.
Thank you James Strayer for the comment about this!
"""
import tkinter as tk
from tkinter import filedialog
from os import getcwd
from openpyxl import load_workbook

if __name__ == "__main__": 
    root = tk.Tk()
    root.withdraw() # Hides the root window
    #root.wm_iconbitmap('py.ico')
    
    root.filename =  filedialog.asksaveasfilename(initialdir=getcwd(),\
                                                  title = "Select file",\
                                                  filetypes = (("png files","*.png"),\
                                                               ("all files","*.*")))

    print ("Save as file path:", root.filename)

##    root.filename =  filedialog.askopenfilename(initialdir=getcwd(),\
##                                                title = "Select file",\
##                                                filetypes = (("Excel workbooks","*.xlsx"),\
##                                                             ("all files","*.*")))
##    print ("Open file path:", root.filename)
##
##    
##    wb = load_workbook(root.filename)
##    print("Sheets in workbook", wb.worksheets)
