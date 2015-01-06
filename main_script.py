#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Authors:
	Coraline MARIE

:Date:
	2015/1/6
"""

import sys
import os
import codecs
import glob
from functions import *


if __name__ == "__main__":

    ###############################
    #   Variables de traitement   #
    ###############################
    # True pour traiter, False sinon

    pretraitement = False
    emergent_motif_extraction = True


    ##############################
    #  Prétraitement des corpus  #
    ##############################

    if pretraitement == True:
        pretraitement_funct("data/train_LinkinPark.txt")
        pretraitement_funct("data/train_BreakingBenjamin.txt")
        pretraitement_funct("data/train_DaftPunk.txt")
    for file_to_clean in glob.glob("data/test_LinkinPark/*"):
        pretraitement_funct(file_to_clean)
    for file_to_clean in glob.glob("data/test_BreakingBenjamin/*"):
        pretraitement_funct(file_to_clean)
    for file_to_clean in glob.glob("data/test_DaftPunk/*"):
        pretraitement_funct(file_to_clean)


    ####################################
    #  Extraction de motifs émergents  #
    ####################################

    if emergent_motif_extraction == True:
        affichage(1)
        emergent_motif_extraction_funct(1)
        affichage(0)

