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
import glob


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
        print(color.BOLD + "\n\nPRETRAITEMENT DES CORPUS:" + color.END)
    elif num == 2:
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



######################################
# Création des vecteurs de contextes #
######################################

def creation_context_vector(file_name_song, file_name_train):
    vector_dic = {}
    file_song = codecs.open(file_name_song, "r", "utf-8")
    file_train = codecs.open(file_name_train, "r", "utf-8")

    for line in file_song.readlines():
        motif_song_lst = line.split("\t")[0].split("{")
        motif_song = ""
        for element in motif_song_lst:
            if element != "":
                motif_song = motif_song + element.rstrip("}") + ";"
        vector_dic[motif_song] = 0
    for line in file_train.readlines():
        if line.rstrip("\n") in vector_dic.keys():
            vector_dic[line.rstrip("\n")] += 1
    file_song.close()
    file_train.close()
    return vector_dic



###############################
#           Calculs           #
###############################

###    cosine    ###
#    calcul le cosinus entre deux dictionnaires
#    v1 et v2 sont les deux vecteurs de contextes liste('mot':frequence)
def cosine(v1, v2):
    if len(v2.keys()) == 0:
        return 0.0

    v1v2 = 0
    v1v1 = 0
    v2v2 = 0
    for attr in set(v1.keys() + v2.keys()):
        if attr in v1:
            attr1 = v1[attr]
        else:
            attr1 = 0

        if attr in v2:
            attr2 = v2[attr]
        else:
            attr2 = 0

        v1v2 += (attr1 * attr2)
        v1v1 += (attr1 * attr1)
        v2v2 += (attr2 * attr2)
    return v1v2 / (math.sqrt(v1v1) * math.sqrt(v2v2))


def somme_vec(v1):
    somme = 0
    for element in v1.keys():
        somme = somme + v1[element]
    return somme



def first_class_funct(gap,param):

    #premier Classifieur
    print "PREMIER CLASSIFIEUR LINKINPARK"
    file_test_name = "data/motif/testgap" + str(gap) + "/test_LinkinPark/*"
    file_train1_name = "data/classifieur/param_"+ str(param) + "/classifieur_1/EM1"
    file_train2_name = "data/classifieur/param_"+ str(param) + "/classifieur_1/EM2"
    for file_test in glob.glob(file_test_name):
        song1_vc = creation_context_vector(file_test,file_train1_name)
        somme1 = somme_vec(song1_vc)
        song2_vc = creation_context_vector(file_test,file_train2_name)
        somme2 = somme_vec(song2_vc)
        if somme1 > somme2:
            print file_test.split("/")[-1], " est de LinkinPark"
        elif somme1 < somme2:
            print file_test.split("/")[-1], " est de BreakingBenjamin"
        else:
            print file_test.split("/")[-1], " on ne sait pas"

    print "PREMIER CLASSIFIEUR BREAKINGBENJAMIN"
    file_test_name = "data/motif/testgap" + str(gap) + "/test_BreakingBenjamin/*"
    file_train1_name = "data/classifieur/param_"+ str(param) + "/classifieur_1/EM1"
    file_train2_name = "data/classifieur/param_"+ str(param) + "/classifieur_1/EM2"
    for file_test in glob.glob(file_test_name):
        song1_vc = creation_context_vector(file_test,file_train1_name)
        somme1 = somme_vec(song1_vc)
        song2_vc = creation_context_vector(file_test,file_train2_name)
        somme2 = somme_vec(song2_vc)
        if somme1 > somme2:
            print file_test.split("/")[-1], " est de LinkinPark"
        elif somme1 < somme2:
            print file_test.split("/")[-1], " est de BreakingBenjamin"
        else:
            print file_test.split("/")[-1], " on ne sait pas"

    print "DEUXIEME CLASSIFIEUR LINKINPARK"
    file_test_name = "data/motif/testgap" + str(gap) + "/test_LinkinPark/*"
    file_train1_name = "data/classifieur/param_"+ str(param) + "/classifieur_2/EM3"
    file_train2_name = "data/classifieur/param_"+ str(param) + "/classifieur_2/EM4"
    for file_test in glob.glob(file_test_name):
        song1_vc = creation_context_vector(file_test,file_train1_name)
        somme1 = somme_vec(song1_vc)
        song2_vc = creation_context_vector(file_test,file_train2_name)
        somme2 = somme_vec(song2_vc)
        if somme1 > somme2:
            print file_test.split("/")[-1], " est de LinkinPark"
        elif somme1 < somme2:
            print file_test.split("/")[-1], " est de DaftPunk"
        else:
            print file_test.split("/")[-1], " on ne sait pas"

    print "DEUXIEME CLASSIFIEUR DAFTPUNK"
    file_test_name = "data/motif/testgap" + str(gap) + "/test_DaftPunk/*"
    file_train1_name = "data/classifieur/param_"+ str(param) + "/classifieur_2/EM3"
    file_train2_name = "data/classifieur/param_"+ str(param) + "/classifieur_2/EM4"
    for file_test in glob.glob(file_test_name):
        song1_vc = creation_context_vector(file_test,file_train1_name)
        somme1 = somme_vec(song1_vc)
        song2_vc = creation_context_vector(file_test,file_train2_name)
        somme2 = somme_vec(song2_vc)
        if somme1 > somme2:
            print file_test.split("/")[-1], " est de LinkinPark"
        elif somme1 < somme2:
            print file_test.split("/")[-1], " est de DaftPunk"
        else:
            print file_test.split("/")[-1], " on ne sait pas"

    print "TROISIEME CLASSIFIEUR LINKINPARK"
    file_test_name = "data/motif/testgap" + str(gap) + "/test_LinkinPark/*"
    file_train1_name = "data/classifieur/param_"+ str(param) + "/classifieur_3/EM5"
    file_train2_name = "data/classifieur/param_"+ str(param) + "/classifieur_3/EM6"
    file_train3_name = "data/classifieur/param_"+ str(param) + "/classifieur_3/EM7"
    for file_test in glob.glob(file_test_name):
        song1_vc = creation_context_vector(file_test,file_train1_name)
        somme1 = somme_vec(song1_vc)
        song2_vc = creation_context_vector(file_test,file_train2_name)
        somme2 = somme_vec(song2_vc)
        song3_vc = creation_context_vector(file_test,file_train3_name)
        somme3 = somme_vec(song3_vc)
        if somme1 > somme2 :
            if somme1 > somme3 :
                print file_test.split("/")[-1], " est de LinkinPark"
            elif somme3 > somme1 :
                print file_test.split("/")[-1], " est de DaftPunk"
            else :
                print file_test.split("/")[-1], " est soit de LP, soit de DP"
        elif somme2 > somme1 :
            if somme2 > somme3 :
                print file_test.split("/")[-1], " est de BreakingBenjamin"
            elif somme3 > somme2 :
                print file_test.split("/")[-1], " est de DaftPunk"
            else :
                print file_test.split("/")[-1], " est soit de BB, soit de DP"
        elif somme3 > somme1 :
            print file_test.split("/")[-1], " est de DaftPunk"
        else :
            print file_test.split("/")[-1], " est soit de LP, soit de BB"

    print "TROISIEME CLASSIFIEUR BREAKINGBENJAMIN"
    file_test_name = "data/motif/testgap" + str(gap) + "/test_BreakingBenjamin/*"
    file_train1_name = "data/classifieur/param_"+ str(param) + "/classifieur_3/EM5"
    file_train2_name = "data/classifieur/param_"+ str(param) + "/classifieur_3/EM6"
    file_train3_name = "data/classifieur/param_"+ str(param) + "/classifieur_3/EM7"
    for file_test in glob.glob(file_test_name):
        song1_vc = creation_context_vector(file_test,file_train1_name)
        somme1 = somme_vec(song1_vc)
        song2_vc = creation_context_vector(file_test,file_train2_name)
        somme2 = somme_vec(song2_vc)
        song3_vc = creation_context_vector(file_test,file_train3_name)
        somme3 = somme_vec(song3_vc)
        if somme1 > somme2 :
            if somme1 > somme3 :
                print file_test.split("/")[-1], " est de LinkinPark"
            elif somme3 > somme1 :
                print file_test.split("/")[-1], " est de DaftPunk"
            else :
                print file_test.split("/")[-1], " est soit de LP, soit de DP"
        elif somme2 > somme1 :
            if somme2 > somme3 :
                print file_test.split("/")[-1], " est de BreakingBenjamin"
            elif somme3 > somme2 :
                print file_test.split("/")[-1], " est de DaftPunk"
            else :
                print file_test.split("/")[-1], " est soit de BB, soit de DP"
        elif somme3 > somme1 :
            print file_test.split("/")[-1], " est de DaftPunk"
        else :
            print file_test.split("/")[-1], " est soit de LP, soit de BB"

    print "TROISIEME CLASSIFIEUR DAFTPUNK"
    file_test_name = "data/motif/testgap" + str(gap) + "/test_DaftPunk/*"
    file_train1_name = "data/classifieur/param_"+ str(param) + "/classifieur_3/EM5"
    file_train2_name = "data/classifieur/param_"+ str(param) + "/classifieur_3/EM6"
    file_train3_name = "data/classifieur/param_"+ str(param) + "/classifieur_3/EM7"
    for file_test in glob.glob(file_test_name):
        song1_vc = creation_context_vector(file_test,file_train1_name)
        somme1 = somme_vec(song1_vc)
        song2_vc = creation_context_vector(file_test,file_train2_name)
        somme2 = somme_vec(song2_vc)
        song3_vc = creation_context_vector(file_test,file_train3_name)
        somme3 = somme_vec(song3_vc)
        if somme1 > somme2 :
            if somme1 > somme3 :
                print file_test.split("/")[-1], " est de LinkinPark"
            elif somme3 > somme1 :
                print file_test.split("/")[-1], " est de DaftPunk"
            else :
                print file_test.split("/")[-1], " est soit de LP, soit de DP"
        elif somme2 > somme1 :
            if somme2 > somme3 :
                print file_test.split("/")[-1], " est de BreakingBenjamin"
            elif somme3 > somme2 :
                print file_test.split("/")[-1], " est de DaftPunk"
            else :
                print file_test.split("/")[-1], " est soit de BB, soit de DP"
        elif somme3 > somme1 :
            print file_test.split("/")[-1], " est de DaftPunk"
        else :
            print file_test.split("/")[-1], " est soit de LP, soit de BB"