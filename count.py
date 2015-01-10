#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Authors:
	Coraline MARIE

:Date:
	2015/1/10
"""

import sys
import os
import codecs
import glob


if __name__ == "__main__":

	line_counter = 0
	word_counter = 0
	for file_name in glob.glob("/home/coraline/Documents/RI/RI_Project/data/test_LinkinPark/*"):
		line_counter = line_counter + os.system("wc -l " + file_name)
		word_counter = word_counter + os.system("wc -w " + file_name)
	print line_counter
	print word_counter
