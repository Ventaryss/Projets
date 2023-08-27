#############
## IMPORTS ##
#############

import speech_recognition as sr
import pyttsx3 as ttx
from urllib.request import urlopen
import subprocess
import webbrowser
import wikipedia
import translators as ts
import datetime as dt


########################################################################################################################

# jeux à faire (fait, mais permettre de quitter le jeu et revenir à la conv) (ne pas relancer la fct chat())
# voix à changer
# appli graphique à créer
# toujours allumé en arrière-plan, mais s'active avec "Atlas" (fait, mais à tester)
# def calcul
# choisir la langue (ENG ou FR pour l'instant)
# proposer une réponse à je m'ennuie (devinette, temps restant avant la fin de la journée etc)
# connecter à un dico
# changer les mots TXT, pas conjugués
# améliorer le pendu avec la diff des mots
# chemins des applications à trouver tout seul
# s'occuper du fait que le mot cherche doit juste être captée dans la phrase
# commandes à mettre idem que speech
# différencier le "ça va ?" du "ça va"
# MAJ Graphique à faire (des espaces entre les discu)
# Ranger et commenter le code
# mettre les directions des fichiers en constantes
# faire en sorte de pouvoir lancer les try directement depuis les constantes
# faire en sorte de ne pas faire un double (ou plus) quit si on rentre dans une autre boucle
# permettre de sortir de la select de tags
# améliorer la reconnaissance des phrases
# faire en sorte que le user ne se perdre pas (préciser s'il est dans la discussion ou dans un jeu par ex
# faire en sorte qu'il reco les mots même avec des petites fautes

########################################################################################################################

###########
## CODES ##
###########

def listen():
    listener = sr.Recognizer()

    with sr.Microphone() as source:

        listener.adjust_for_ambient_noise(source)
        # listener.pause_threshold = 2 #(2*2)

        print("....")

        audio = listener.listen(source)
        try:
            # valid
            quote = listener.recognize_google(audio, language='fr-FR')
        except:
            # google could not validate
            speak("Vous m'en voyez navré mais je ne comprend pas")

    return quote


########################################################################################################################

def speak(text):
    engine = ttx.init()
    if text != None:
        engine.say(text)
        engine.runAndWait()


########################################################################################################################

def internet():
    try:
        urlopen("https://www.google.com", timeout=1)
        return True
    except:
        return False


########################################################################################################################

def applications(commande):
    if commande != None:
        dico_apps = {
            "firefox": ["firefox", "fire fox", "fire foxe"],
            "notion": ["notion", "no tion"],
            "visual studio code": ["vsc", "visual studio code"],
            "discord": ["discord"]
        }
    fini = False
    while not fini:
        for x in dico_apps["firefox"]:
            if x in commande.lower():
                # speak("Ouverture de Firefox .")
                print("Ouverture de Firefox ...")
                subprocess.Popen(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Firefox.lnk", shell=True)
                fini = True
        for x in dico_apps["notion"]:
            if x in commande.lower():
                # speak("Ouverture de Notion .")
                print("Ouverture de Notion ...")
                subprocess.Popen(r"C:\Users\aubin\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Notion.lnk",
                                 shell=True)
                fini = True
        for x in dico_apps["visual studio code"]:
            if x in commande.lower():
                # speak("Ouverture de VSC .")
                print("Ouverture de VSC ...")
                subprocess.Popen(
                    r"C:\Users\aubin\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Visual Studio Code\Visual Studio Code.lnk",
                    shell=True)
                fini = True
        for x in dico_apps["discord"]:
            if x in commande.lower():
                # speak("Ouverture de Discord .")
                print("Ouverture de Discord...")
                subprocess.Popen(
                    r"C:\Users\aubin\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Discord Inc\Discord.lnk",
                    shell=True)
                fini = True


########################################################################################################################

def traducteur(commande):
    if commande != None:
        trad = commande.lower().replace("traduis", "")
        translate = ts.google(trad, to_language='fr')
        # speak("La traduction de "+commande+" est : "+translate)
        print("La traduction de " + commande + " est : " + translate)


########################################################################################################################

# def calcul(command):

########################################################################################################################

def time():
    time = dt.datetime.now()
    # speak(time)
    print(time)


########################################################################################################################

def net(commande):
    if commande != None:
        if 'youtube' in commande.lower():
            recherche = commande.lower().replace("cherche sur youtube", "")
            if len(recherche) != 0:
                # speak("Recherche sur Youtube .")
                print("Recherche sur Youtube ...")
                webbrowser.open("http://www.youtube.com/results?search_query=" + "+".join(recherche), new=2)
        elif "wikipédia" in commande.lower():
            wikipedia.set_lang("fr")
            try:
                recherche = commande.lower().replace("cherche sur wikipédia", "")
                if len(recherche) != 0:
                    resultat = wikipedia.summary(recherche, sentences=1)
                    # speak("Recherche sur Wikipédia .")
                    print("Recherche sur Wikipédia ...")
                    print(resultat)
                    # speak(resultat)
            except:
                # speak("Toutes mes excuses, aucune page n'a été trouvée")
                print("Toutes mes excuses, aucune page n'a été trouvée")
        elif "google" in commande.lower():
            recherche = commande.lower().replace("cherche sur google", "")
            if len(recherche) != 0:
                # speak("Recherche sur Google .")
                print("Recherche sur Google ...")
                webbrowser.open("http://www.google.com/search?q=" + "+".join(recherche), new=2)


########################################################################################################################

def launch_atlas():
    print("Bonjour, mon nom est Atlas, c'est un plaisir de vous aider .")
    speak("Bonjour, mon nom est Atlas, c'est un plaisir de vous aider.")
    close = ["Atlas stop", "stop", "arrêtes-toi", "chut"]
    open = ["ouvre", "ouvrir", "peut-tu ouvrir"]
    cherche = ["cherche sur youtube", "cherche sur wikipédia", "cherche sur google", "cherche",
               "fait moi cette recherche", "peut-tu faire cette recherche"]
    calculs = []
    trad = ["traduit", "peut-tu traduire"]

    actif = True

    while actif:
        if (commande := listen()) is not None:
            if commande == "Atlas":
                for x in range(len(close)):
                    if close[x] in commande.lower():
                        speak("En revoir .")
                        actif = False
                for x in range(len(open)):
                    if open[x] in commande.lower():
                        applications(commande)
                        break
                for x in range(len(cherche)):
                    if cherche[x] in commande.lower():
                        net(commande)
                        break
                for x in range(len(calculs)):
                    if calculs[x] in commande.lower():
                        # calcul(commande)
                        break
                for x in range(len(trad)):
                    if trad[x] in commande.lower():
                        traducteur(commande)
                        break


########################################################################################################################

if __name__ == "__main__":
    launch_atlas()
