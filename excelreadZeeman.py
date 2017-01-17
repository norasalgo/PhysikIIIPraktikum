# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 13:27:57 2016

@author: Nora
"""

import xlrd
file_location="/Users/Nora/Dropbox/Dokumente/Studium/PhysikIII/Praktikum/Zeeman.xlsx"
workbook=xlrd.open_workbook(file_location)
sheet=workbook.sheet_by_index(0)



def machliste(z1,z2,s):
    a=[]
    for z in range(z1,z2):
        a.append(sheet.cell_value(z,s))

    return a


