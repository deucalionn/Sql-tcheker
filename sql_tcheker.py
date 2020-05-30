import os
import sys
import urllib
import time
import requests


def design():
    print(""" 
    
   _____ ____    __       ______     __         __            
  / ___// __ \  / /      /_  __/____/ /_  ___  / /_____  _____
  \__ \/ / / / / /        / / / ___/ __ \/ _ \/ //_/ _ \/ ___/
 ___/ / /_/ / / /___     / / / /__/ / / /  __/ ,< /  __/ /    
/____/\___\_\/_____/    /_/  \___/_/ /_/\___/_/|_|\___/_/     
                                                              
                   By Deucalion
            
            Discord : Deucalion#0776
            Github  : https://github.com/Baki-Corp

    
    """)

design()

def help():
    print("""
    
            Using sql tcheker : python sql_tcheker.py <url>
            help to print command
    
    
    """)


try:
    target = sys.argv[1]
except:
    help()
    quit()


if target == "help":
    help()
    quit()


to_ping = target.split("/")[0]
prefix = "SQL_Tcheker -->  "
try:
    response = os.system("ping " + to_ping)
    requete = requests.post("https://"+target+"'")
    print()
    print(prefix + "Connection avec la cible en cours ...")
    time.sleep(1)
    b = True
except:
    print(prefix + "Une Erreur est survenue")
    b = False
    
while b:
    if response == 0:
        pingstatus = "Connexion réussi avec la cible"
        print(prefix + pingstatus)
        print(prefix + "Verification de faille SQL en cours ...")
        time.sleep(2)
        try:
            if "mysql" in requete.text.lower():
                print(prefix + "SQL Error detected")
            elif "MySQL Error 1064: You has an error in your SQL syntax" in requete.text.lower():
                print(prefix + 'Error SQL detected')
            elif "You has an error in your SQL syntax" in requete.text.lower():
                print(prefix + "Error SQL detected")
            else:
                print(prefix + "SQL Error not detected")

            break
        except:
            print(prefix + 'Une Erreur est survenue')

    else:
        pingstatus = "Erreur lors de la connexion avec la cible"
        print(prefix + pingstatus)
        break