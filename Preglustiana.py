import os
import json
import requests
from colorama import Fore, init

init(autoreset=True)

dictionnary_ps_fr = {}
dictionnary_fr_ps = {}

DictionnaryExist = 0

def load_dictionnary():
    global dictionnary_ps_fr, dictionnary_fr_ps, DictionnaryExist
    path = os.path.join(os.getenv('APPDATA'), 'KFCgaming', 'PregluFrench', 'DictionnaryPSFR.json')
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as file:
            dictionnary = json.load(file)
            dictionnary_fr_ps = dictionnary
            dictionnary_ps_fr = {v: k for k, v in dictionnary.items()}
        DictionnaryExist = 1
    else:
        input(Fore.RED + "Dictionnaire Introuvable. Veuillez l'Installer via l'option 3...")
        os.system('cls' if os.name == 'nt' else 'clear')
        DictionnaryExist = 2

def translate_word(word, dictionnary):
    lower_word = word.lower()
    translated_word = dictionnary.get(lower_word, word)
    if word[0].isupper():
        translated_word = translated_word.capitalize()
    return translated_word

def TranslateFRtoPS():
    sentence = input("Phrases/Mots >  ")
    translated_sentence = ' '.join([translate_word(word, dictionnary_fr_ps) for word in sentence.split()])
    print(Fore.GREEN + translated_sentence)
    input()
    Menu()

def TranslatePStoFR():
    sentence = input("Phrases/Mots >  ")
    translated_sentence = ' '.join([translate_word(word, dictionnary_ps_fr) for word in sentence.split()])
    print(Fore.GREEN + translated_sentence)
    input()
    Menu()

def Setup():
    url = "https://raw.githubusercontent.com/KFCgaming/Preglustiana/main/DIctionnaryPSFR.json"
    response = requests.get(url)
    if response.status_code == 200:
        path = os.path.join(os.getenv('APPDATA'), 'KFCgaming', 'PregluFrench')
        os.makedirs(path, exist_ok=True)
        with open(os.path.join(path, 'DictionnaryPSFR.json'), 'wb') as file:
            file.write(response.content)
        print(Fore.GREEN + "Fichier du Dictionnaire Installé !")
    else:
        print(Fore.RED + "Problème est survenu lors du Téléchargement du Dictionnaire...")
    
    input()
    Menu()

def Menu():
    load_dictionnary()
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.LIGHTBLUE_EX + """  ____  ____     ___     _____ ____    _____                    _       _             
 |  _ \/ ___|   ( _ )   |  ___|  _ \  |_   _| __ __ _ _ __  ___| | __ _| |_ ___  _ __ 
 | |_) \___ \   / _ \/\ | |_  | |_) |   | || '__/ _` | '_ \/ __| |/ _` | __/ _ \| '__|
 |  __/ ___) | | (_>  < |  _| |  _ <    | || | | (_| | | | \__ \ | (_| | || (_) | |   
 |_|   |____/   \___/\/ |_|   |_| \_\   |_||_|  \__,_|_| |_|___/_|\__,_|\__\___/|_|   
                                                                                      """) #Title
    if DictionnaryExist == 1:
        print(Fore.LIGHTBLUE_EX + """ 
        ╔════════════════════════════════════════════════════════════════════╗
        ║                               Menu                                 ║
        ║                                                                    ║
        ║    1. Traduire du FR au Preglustiana                               ║
        ║                                                                    ║
        ║    2. Traduire du Preglustiana au FR                               ║
        ║                                                                    ║
        ║    3. Installer le Dictionnaire                                    ║
        ║                                                                    ║
        ║                                                                    ║
        ║    -- Crée par KFCgaming      (Github)                             ║
        ║                                                                    ║
        ╚════════════════════════════════════════════════════════════════════╝ """) # Menu
    else:
        print(Fore.LIGHTYELLOW_EX + """ 
        ╔════════════════════════════════════════════════════════════════════╗
        ║                               Menu                                 ║
        ║                                                                    ║
        ║    1. Traduire du FR au Preglustiana  |  Dictionnaire Introuvable  ║
        ║                                                                    ║
        ║    2. Traduire du Preglustiana au FR  |  Dictionnaire Introuvable  ║
        ║                                                                    ║
        ║    3. Installer le Dictionnaire                                    ║
        ║                                                                    ║
        ║                                                                    ║
        ║    -- Crée par KFCgaming      (Github)                             ║
        ║                                                                    ║
        ╚════════════════════════════════════════════════════════════════════╝ """) # Menu
    Choose = input(">  ")
    
    if Choose == "1":
        if DictionnaryExist == 1:
            TranslateFRtoPS()
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            input(Fore.RED + "Dictionnaire non chargé, Veuillez lancer l'installation du Dictionnaire...")
            os.system('cls' if os.name == 'nt' else 'clear')
    elif Choose == "2":
        if DictionnaryExist == 1:
            TranslatePStoFR()
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            input(Fore.RED + "Dictionnaire non chargé, Veuillez lancer l'installation du Dictionnaire...")
            os.system('cls' if os.name == 'nt' else 'clear')
    elif Choose == "3":
        Setup()
        load_dictionnary()
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        input(Fore.RED + "Option Inconnu... Veuillez taper une Option valide.")
        os.system('cls' if os.name == 'nt' else 'clear')
        Menu()

Menu()
