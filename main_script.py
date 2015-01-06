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
    emergent_motif_extraction = False


    ##############################
    #  Prétraitement des corpus  #
    ##############################

    if pretraitement == True:
        affichage(1)
        pretraitement_funct("data/train_LinkinPark.txt")
        pretraitement_funct("data/train_BreakingBenjamin.txt")
        pretraitement_funct("data/train_DaftPunk.txt")
        for file_to_clean in glob.glob("data/test_LinkinPark/*"):
            pretraitement_funct(file_to_clean)
        for file_to_clean in glob.glob("data/test_BreakingBenjamin/*"):
            pretraitement_funct(file_to_clean)
        for file_to_clean in glob.glob("data/test_DaftPunk/*"):
            pretraitement_funct(file_to_clean)
        affichage(0)


    ####################################
    #  Extraction de motifs émergents  #
    ####################################

    if emergent_motif_extraction == True:
        affichage(2)
        emergent_motif_extraction_funct(1)
        emergent_motif_extraction_funct(2)
        emergent_motif_extraction_funct(3)
        emergent_motif_extraction_funct(4)
        emergent_motif_extraction_funct(5)
        emergent_motif_extraction_funct(6)
        affichage(0)


    #############################################
    # Classification sur le premier classifieur #
    #############################################
        #création d'un vecteur de contexte pour chaque fichier de motifs émergents
        #création d'un vecteur de contexte pour chaque fichier test
        #comparaison entre les vecteurs avec le cosinus

    #first_class_funct(0,1)
    #first_class_funct(0,2)
    #first_class_funct(0,3)
    #first_class_funct(0,4)
    first_class_funct(0,5)
    #first_class_funct(0,6)
    #first_class_funct(5,1)
    #first_class_funct(5,2)
    #first_class_funct(5,3)
    #first_class_funct(5,4)
    #first_class_funct(5,5)
    #first_class_funct(5,6)






    ###############################################
    # Classification sur le deuxième  classifieur #
    ###############################################

    ###############################################
    # Classification sur le troisième classifieur #
    ###############################################