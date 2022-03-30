from browser import document, html
from browser.html import TABLE, TR, TH, TD
import math
document["chargement"].style.display = "none"
document["partie_1"].style.display = "inline"

with open("CSV/Characters.csv", mode='r', encoding='utf-8') as f:
    lines = f.readlines()
    students = []
    key_line = lines[0].strip()
    keys = key_line.split(';')
    for line in lines[1:]:
        line = line.strip()
        line = line.replace('\xa0', ' ')
        values = line.split(';')
        dic = {}
        for i in range(len(keys)):
            dic[keys[i]] = values[i].strip()
        students.append(dic)

with open("CSV/Caracteristiques_des_persos.csv", mode='r', encoding='utf-8') as f:
    lines = f.readlines()
    tab = []
    key_line = lines[0].strip()
    keys = key_line.split(';')
    for line in lines[1:]:
        line = line.strip()
        line = line.replace('\xa0', ' ')
        values = line.split(';')
        dic = {}
        for i in range(len(keys)):
            dic[keys[i]] = values[i].strip()
        tab.append(dic)

for student_character in tab:
    for poudlard_character in students:
        if poudlard_character['Name'] == student_character['Name']:
            student_character.update({'House': poudlard_character['House']})

with open("CSV/QuestionnaireNSI.csv", mode='r', encoding='utf-8') as f:
    lines = f.readlines()
    reader = []
    key_line = lines[0].strip()
    keys = key_line.split(';')
    for line in lines[1:]:
        line = line.strip()
        line = line.replace('\xa0', ' ')
        values = line.split(';')
        dic = {}
        for i in range(len(keys)):
            dic[keys[i]] = values[i].strip()
        reader.append(dic)
questions = [element['Question'] for element in reader]

val_courage = 5
val_ambition = 5
val_intelligence = 5
val_good = 5
compteur = 0
new_student = {}
document["question"].textContent = questions[0]

def affichage(ev):
    display = document["partie_2"].style.display
    document["partie_2"].style.display = "inline" if display == "none" else "none"
    document["partie_1"].style.display = "none"
document["start"].bind("click", affichage)

def change_reponses():
    global compteur, new_student
    reponses_A = [element['ReponseA'] for element in reader]
    reponses_B = [element['ReponseB'] for element in reader]
    reponses_C = [element['ReponseC'] for element in reader]
    reponses_D = [element['ReponseD'] for element in reader]
    document["bouton1"].textContent = f'A) {reponses_A[compteur]}'
    document["bouton2"].textContent = f'B) {reponses_B[compteur]}'
    document["bouton3"].textContent = f'C) {reponses_C[compteur]}'
    document["bouton4"].textContent = f'D) {reponses_D[compteur]}'
    document["progression"].value += 25
    if compteur == 16:
        print(val_courage)
        print(val_ambition)
        print(val_intelligence)
        print(val_good)
        new_student = {'Name': "", 'Courage': val_courage, 'Ambition': val_ambition, 'Intelligence': val_intelligence,
                       'Good': val_good}
        put_the_sorting_hat(tab, new_student, 5)

change_reponses()

def change_texte1(ev):
    global compteur, questions, val_ambition, val_courage, val_good, val_intelligence
    val_reponses_A = [element['Valeur reponse A'] for element in reader]

    if compteur > 3 and compteur < 8:
        val_ambition += float(val_reponses_A[compteur])
    elif compteur > 7 and compteur < 12:
        val_intelligence += float(val_reponses_A[compteur])
    elif compteur > 11:
        val_good += float(val_reponses_A[compteur])
    else:
        val_courage += float(val_reponses_A[compteur])
    compteur += 1
    document["question"].textContent = questions[compteur]
    change_reponses()
document["bouton1"].bind("click", change_texte1)


def change_texte2(ev):
    global compteur, questions, val_ambition, val_courage, val_good, val_intelligence
    val_reponses_B = [element['Valeur reponse B'] for element in reader]
    if compteur > 3 and compteur < 8:
        val_ambition += float(val_reponses_B[compteur])
    elif compteur > 7 and compteur < 12:
        val_intelligence += float(val_reponses_B[compteur])
    elif compteur > 11:
        val_good += float(val_reponses_B[compteur])
    else:
        val_courage += float(val_reponses_B[compteur])
    compteur += 1
    document["question"].textContent = questions[compteur]
    change_reponses()
document["bouton2"].bind("click", change_texte2)


def change_texte3(ev):
    global compteur, questions, val_ambition, val_courage, val_good, val_intelligence
    val_reponses_C = [element['Valeur reponse C'] for element in reader]
    if compteur > 3 and compteur < 8:
        val_ambition += float(val_reponses_C[compteur])
    elif compteur > 7 and compteur < 12:
        val_intelligence += float(val_reponses_C[compteur])
    elif compteur > 11:
        val_good += float(val_reponses_C[compteur])
    else:
        val_courage += float(val_reponses_C[compteur])
    compteur += 1
    document["question"].textContent = questions[compteur]
    change_reponses()
document["bouton3"].bind("click", change_texte3)


def change_texte4(ev):
    global compteur, questions, val_ambition, val_courage, val_good, val_intelligence
    val_reponses_D = [element['Valeur reponse D'] for element in reader]
    if compteur > 3 and compteur < 8:
        val_ambition += float(val_reponses_D[compteur])
    elif compteur > 7 and compteur < 12:
        val_intelligence += float(val_reponses_D[compteur])
    elif compteur > 11:
        val_good += float(val_reponses_D[compteur])
    else:
        val_courage += float(val_reponses_D[compteur])
    compteur += 1
    document["question"].textContent = questions[compteur]
    change_reponses()

document["bouton4"].bind("click", change_texte4)


def distance(student_one, student_two, methode='euclidienne'):
    return math.sqrt((int(student_one['Courage']) - int(student_two['Courage'])) ** 2
                     + (int(student_one['Ambition']) - int(student_two['Ambition'])) ** 2
                     + (int(student_one['Intelligence']) - int(student_two['Intelligence'])) ** 2
                     + (int(student_one['Good']) - int(student_two['Good'])) ** 2)


def add_distance(tab, student_selected):
    for student in tab:
        student['Distance'] = distance(student_selected, student)
    return tab


def pooling(tab, student_selected, k):
    tab = add_distance(tab, student_selected)
    tab = sorted(tab, key=lambda x: x['Distance'])
    tab = tab[:k]
    return tab


def search_house(neighborhoods):
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


def put_the_sorting_hat(tab, student_selected, k):
    neighborhood_tab = pooling(tab, student_selected, k)
    student_house = str(search_house(neighborhood_tab))
    table = TABLE()
    keys = []
    values = [[], [], [], [], []]
    i = 0
    for cle in neighborhood_tab[0].keys():
        keys.append(cle)
    for neighborhood in neighborhood_tab:
        for valeur in neighborhood.values():
            values[i].append(valeur)
        i += 1
    table <= TR(TH(keys[i]) for i in range(len(keys)))
    for liste in values:
        table <= TR(TD(liste[i]) for i in range(len(liste)))
    document['tableau'] <= table
    document[student_house].style.display = 'inline'
    document['maison'].textContent = student_house
    document['partie_2'].style.display = "none"
    document['partie_3'].style.display = 'inline'


