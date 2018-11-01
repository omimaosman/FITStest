#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 10:08:05 2018

@author: skoushan
"""

from astropy.io import fits
import argparse
import os

path = '/Users/skoushan/Desktop/SciCoder-2018-Perth/Data Files/spectra/'
allfiles = os.listdir(path)

for file in allfiles:    
    hdu_list = fits.open(path+file)
    num_hdus = len(hdu_list)
    mytype = hdu_list.info()
    filetype = type(file)
    print("This file has {} HDUs and having {} type.".format(num_hdus,filetype))


########################


# hdu_list[1].header
    # hdu_list.info()

#parser = argparse.ArgumentParser(description="This program does stuff",
#							    usage="name_of_script ...",
#							    epilog="this is text added to the end of the help")

#parser.add_argument('-f', '--file',
#					help="File to open.",
#					type=argparse.FileType('r'))
#args = parser.parse_args()

# Raises an error if the file is not available, or,
# interestingly, not readable (e.g. insufficient 
# permission).

# file is already open; use the "with" construct
# to make sure it gets closed

#with args.file as file:
	# print contents of file
#	print(file.read())