#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Authors:
    Coraline MARIE

:Date:
    2014/10/12
"""
import re
import sys
import os
import codecs


###############################
#     Organistion du code     #
###############################


###    color    ###
#    mise en forme du texte
class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


###    affichage    ###
#    affiche dans la console des textes sur l'exécution du programme
def affichage(num):
    if num == 404:
        print(color.RED + "\nERREUR" + color.END)
    elif num == 0:
        print("                                 " + color.GREEN + " > done" + color.END)
    elif num == 1:
        print(color.BOLD + "\n\nEXTRACTION DE MOTIF EMERGENTS :" + color.END)


##############################
#  Prétraitement des corpus  #
##############################

def pretraitement_funct(file_name):
    file_to_clean = codecs.open(file_name, "r", "utf-8")
    contenu = file_to_clean.read()
    file_to_clean.close()
    file_to_clean = codecs.open(file_name, "w", "utf-8")
    file_to_clean.write(contenu.lower())
    file_to_clean.close()

####################################
#  Extraction de motifs émergents  #
####################################

def emergent_motif_extraction_funct(param):
    #ouverture des fichiers
    file_name = "data/motif/param_" + str(param) + "/LinkinPark"
    file_motif_LinkinPark = codecs.open(file_name, "r", "utf-8")
    file_name = "data/motif/param_" + str(param) + "/BreakingBenjamin"
    file_motif_BreakingBenjamin = codecs.open(file_name, "r", "utf-8")
    file_name = "data/motif/param_" + str(param) + "/DaftPunk"
    file_motif_DaftPunk = codecs.open(file_name, "r", "utf-8")

    #création des structures de données contenant les motifs
    motif_LinkinPark_lst = []
    for line in file_motif_LinkinPark.readlines():
        motif_LinkinPark_lst.append(line.split("\t")[0])
    motif_BreakingBenjamin_lst = []
    for line in file_motif_BreakingBenjamin.readlines():
        motif_BreakingBenjamin_lst.append(line.split("\t")[0])
    motif_DaftPunk_lst = []
    for line in file_motif_DaftPunk.readlines():
        motif_DaftPunk_lst.append(line.split("\t")[0])

    #fermeture des fichiers
    file_motif_LinkinPark.close()
    file_motif_BreakingBenjamin.close()
    file_motif_DaftPunk.close()

    #création du premier fichier de motif emergents : LinkinPark/BreakingBenjamin
    file_name = "data/classifieur/param_" + str(param) + "/classifieur_1/EM1"
    file_EM1 = codecs.open(file_name, "w", "utf-8")
    for element in motif_LinkinPark_lst:
        if not element in motif_BreakingBenjamin_lst:
            tmp_lst = element.split("{")
            for element_tmp in tmp_lst:
                if element_tmp != "":
                    file_EM1.write(element_tmp.rstrip("}"))
                    file_EM1.write(";")
            file_EM1.write("\n")
    file_EM1.close()

    #création du second fichier de motif émergents : BreakingBenjamin/LinkinPark
    file_name = "data/classifieur/param_" + str(param) + "/classifieur_1/EM2"
    file_EM2 = codecs.open(file_name, "w", "utf-8")
    for element in motif_BreakingBenjamin_lst:
        if not element in motif_LinkinPark_lst:
            tmp_lst = element.split("{")
            for element_tmp in tmp_lst:
                if element_tmp != "":
                    file_EM2.write(element_tmp.rstrip("}"))
                    file_EM2.write(";")
            file_EM2.write("\n")
    file_EM2.close()

    #création du troisième fichier de motif émergents : LinkinPark/DaftPunk
    file_name = "data/classifieur/param_" + str(param) + "/classifieur_2/EM3"
    file_EM3 = codecs.open(file_name, "w", "utf-8")
    for element in motif_LinkinPark_lst:
        if not element in motif_DaftPunk_lst:
            tmp_lst = element.split("{")
            for element_tmp in tmp_lst:
                if element_tmp != "":
                    file_EM3.write(element_tmp.rstrip("}"))
                    file_EM3.write(";")
            file_EM3.write("\n")
    file_EM3.close()

    #création du quatrième fichier de motif émergents : DaftPunk/LinkinPark
    file_name = "data/classifieur/param_" + str(param) + "/classifieur_2/EM4"
    file_EM4 = codecs.open(file_name, "w", "utf-8")
    for element in motif_DaftPunk_lst:
        if not element in motif_LinkinPark_lst:
            tmp_lst = element.split("{")
            for element_tmp in tmp_lst:
                if element_tmp != "":
                    file_EM4.write(element_tmp.rstrip("}"))
                    file_EM4.write(";")
            file_EM4.write("\n")
    file_EM4.close()

    #création du cinquième fichier de motif émergents : LinkinPark/BreakingBenjamin et DaftPunk
    file_name = "data/classifieur/param_" + str(param) + "/classifieur_3/EM5"
    file_EM5 = codecs.open(file_name, "w", "utf-8")
    for element in motif_LinkinPark_lst:
        if not element in motif_BreakingBenjamin_lst and not element in motif_DaftPunk_lst:
            tmp_lst = element.split("{")
            for element_tmp in tmp_lst:
                if element_tmp != "":
                    file_EM5.write(element_tmp.rstrip("}"))
                    file_EM5.write(";")
            file_EM5.write("\n")
    file_EM5.close()

    #création du sixième fichier de motif émergents : BreakingBenjamin/LinkiPark et DaftPunk
    file_name = "data/classifieur/param_" + str(param) + "/classifieur_3/EM6"
    file_EM6 = codecs.open(file_name, "w", "utf-8")
    for element in motif_BreakingBenjamin_lst:
        if not element in motif_LinkinPark_lst and not element in motif_DaftPunk_lst:
            tmp_lst = element.split("{")
            for element_tmp in tmp_lst:
                if element_tmp != "":
                    file_EM6.write(element_tmp.rstrip("}"))
                    file_EM6.write(";")
            file_EM6.write("\n")
    file_EM6.close()

    #création du septième fichier de motif émergents : DaftPunk/ LinkinPark et BreakingBenjamin
    file_name = "data/classifieur/param_" + str(param) + "/classifieur_3/EM7"
    file_EM7 = codecs.open(file_name, "w", "utf-8")
    for element in motif_DaftPunk_lst:
        if not element in motif_BreakingBenjamin_lst and not element in motif_LinkinPark_lst:
            tmp_lst = element.split("{")
            for element_tmp in tmp_lst:
                if element_tmp != "":
                    file_EM7.write(element_tmp.rstrip("}"))
                    file_EM7.write(";")
            file_EM7.write("\n")
    file_EM7.close()