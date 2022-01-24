#!/usr/local/bin/bash

"Daemon de sécurité :

- vérifie l'ensemble des fichiers en continue
- si il y a eu une modification :

    - où elle a eu lieu (faire en sorte de proposer de copier le lien)
    - quand elle a eu lieu
    - quelle ligne de commande à été utilisée
    - pouvoir revenir à la version non modifiée

    --> rediriger les résultats dans un fichier

- utilisation du forking sur un code source qui check en permanence l'ensemble des fichiers et du système.

C'est à dire faire en sorte de détacher une partie du processus en une sous partie (père et fils) afin de pouvoir améliorer le processus principal en passant par le processus fils.

Un fork désigne un nouveau logiciel créé à partir du code source d'un logiciel existant 
- à ne pas confondre avec un fork : ensemble de données associé à un objet du système de fichiers.
- ni avec l'appel système fork qui permet à un processus d'en créer un nouveau. 

Son existence découle d’un choix politique venant de visions différentes du projet des différents acteurs qui y participe, un acteur décidant alors de créer le fork pour lui imposer les idées qu’il n’a pas pu soumettre au précédent projet, une forme de schisme. 

Si attaque : qu'il/elle liste les processus actifs, voit (peut probable vu le nombre de processus en arrière plan) le daemon, faire en sorte que seul moi puisse toucher à ce processus.

Points à voir :

Solution de facilitée :

- sfc/verifyonly (scan uniquement et vérifie l'intégrité des fichiers systèmes) == plus utile
- sfc/scannow (scan et répare dès que possible) == peut tenter de faire un fork avec cette commande dans un bash pour pouvoir déterminer la date, l'endroit et la ligne de commande utilisée.

Solutions autres : 

- tenter de le faire pour windows et Linux (Linux plus simple)
- voir pour faire en sorte de déterminer ou non si la modification a été illégale ou non "

'

test en C :

#include <stdio.h>
#include <stdlib.h>
#include <dirent.h>

typedef char chaine[61];

int main()
{
    struct dirent *dir;
    // opendir() renvoie un pointeur de type DIR. 
    DIR *d = opendir("."); 
    if (d)
    {
        while ((dir = readdir(d)) != NULL)
        {
            printf("%s\n", dir->d_name);
        }
        closedir(d);
    }
    return 0;
}

void verif(char fichier_a_verifier[], char Ancien_poid[], char Poid_fichier[], chaine nomfic)
{
    fichier_a_verifier = "Emplacement de ton fichier";
    Ancien_poid = FileGetSize(nomfic);

    while (strcmp(Poid_fichier,Ancien_poid)!=0)
        Poid_fichier = FileGetSize(nomfic);

        if (strcmp(Poid_fichier,Ancien_poid)!=0)
        {
            MsgBox(64, "", "Fichier modifier");
            Ancien_poid = FileGetSize(nomfic);
        }
    }
}

//FileGetTime()

void veriff ()
{
    Global $txt = FileRead(/*nomfic*/);
    AdlibRegister("_verif", 5000);
}

void _verif(controle, txt)
{
   Local controle = FileRead(/*nomfic*/);

   if (controle != txt)
   {
       //envoi alerte
   }

   txt = controle
}


/*
FileSetAttrib("Fichier.txt", "-A")

If Not StringInStr(FileGetAttrib("Fichier.txt"), "A") Then
; Le fichier à été modifié
EndIf

'

"test en bash :"

$var="\C:\Users\aubin\OneDrive\Documents\GitHub\Projets\Portfolio\Sentinelle\test.odt"

while true
do

    if test $var
    then 
    echo "Le fichier a été modifié"
    else
    echo "Le fichier n'a pas été modifié"
    fi

    sleep 20m;
done