# -*- coding: utf-8 -*-
import csv
from math import sqrt

k = 5
#Dictionnaire sous forme Nom Courage , Ambition, Intelligence, Good
student1 = {'Name': 'eleve1', 'Courage': 9, 'Ambition': 2, 'Intelligence': 8, 'Good': 9}
student2 = {'Name': 'eleve2', 'Courage': 9, 'Ambition': 4, 'Intelligence': 8, 'Good': 9}
student3 = {'Name': 'eleve3', 'Courage': 3, 'Ambition': 8, 'Intelligence': 6, 'Good': 3}
student4 = {'Name': 'eleve4', 'Courage': 2, 'Ambition': 3, 'Intelligence': 7, 'Good': 8}

students_features = [] #initialisation de la variable en globale

def create_table(tab):
    with open("Characters.csv", mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=';')
        students = [{key: value.replace('\xa0', ' ') for key, value in element.items()} for element in reader]

    with open("Caracteristiques_des_persos.csv", mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=';')
        tab = [{key: value for key, value in element.items()} for element in reader]

    for student_character in tab:
        for poudlard_character in students:
            if poudlard_character['Name'] == student_character['Name']:
                student_character.update({'House': poudlard_character['House']})
    return tab

def distance(student_one, student_two, methode='euclidienne'):
    """
    Calcule la distance entre 2 élèves en fonctions de leurs caratéristques
    
    entrée : student_one = dictionnaire avec ses caractéristiques d'un 1er élève
             student_two = dictionnaire avec les caractéristiques d'un 2e élève
             
    sortie : La distance entre ces 2 élèves
    """
    return sqrt((int(student_one['Courage']) - int(student_two['Courage'])) ** 2
                + (int(student_one['Ambition']) - int(student_two['Ambition'])) ** 2
                + (int(student_one['Intelligence']) - int(student_two['Intelligence'])) ** 2
                + (int(student_one['Good']) - int(student_two['Good'])) ** 2)






def add_distance(tab, student_selected):
    """
    Ajoute au dictionnaire de l'élève sa distance
    entrée : tab = liste de dictionnaire
             student_selected = chaine de caractère, nom de l'élève référentiel(choisie)
    sortie : la liste mise à jour avec les distances
    """
    for student in tab:
        student['Distance'] = distance(student_selected, student)

    return tab

def pooling(tab, student_selected):
    """
    éxecute la fonction pour calculer et mettre les distances à chaque élèves puis trie le tableau de
    dictionnaire en fonction de la du couple 'Distance' : valeur, pour finir par n'en garder que les premiers jusqu'à k
    entrée : tab = liste de dictionnaire
             student_selected = chaine de caractère, nom de l'élève référentiel(choisie)
    sortie : la liste mise à jour avec seulement les k voisins plus proches
    """
    tab = add_distance(tab, student_selected)
    tab = sorted(tab, key=lambda x: x['Distance'])
    tab = tab[:k]
    return tab


def search_house(neighborhoods):
    """
    Calcul en fonction des k élèves les plus proches la moyenne des maisons et renvoie la maison avec la plus haute
    entrée : neighborhoods = liste de dictionnaire des k élèves les plus proches
    sortie : actual_house = string, la maison qui correspond à l'élève de référence
    """

    actual_house = ""
    houses = {}
    for neighborhood in neighborhoods:
        if neighborhood['House'] in houses:
            houses[neighborhood['House']] += 1
        else:
            houses[neighborhood['House']] = 1
    maximum = 0
    for house, nb in houses.items():
        if nb > maximum:
            maximum = nb
            actual_house = house
    return actual_house


def put_the_sorting_hat(tab, student_selected):
    """
    Coeur du programme, appelle dans l'ordre les différentes fonctions
    entrée : tab = liste de dictionnaire
             student_selected = chaine de caractère, nom de l'élève référentiel(choisie)
    """
    tab = create_table(tab)
    fonction_3 = pooling(tab, student_selected)
    print("Les 5 élèves les plus proches :", *fonction_3, sep='\n-')
    fonction_5 = search_house(fonction_3)
    print("La maison qui lui convient", fonction_5)
    print('\n')

put_the_sorting_hat(students_features, student1)
put_the_sorting_hat(students_features, student2)
put_the_sorting_hat(students_features, student3)
put_the_sorting_hat(students_features, student4)