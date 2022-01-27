#/mnt/c/Windows/System32

var="/mnt/c/Users/aubin/OneDrive/Documents/GitHub/Projets/Portfolio/Sentinelle/test"
number_of_words1=`wc --word < $var`

# méthode simple de comptage de mots

# mettre en uniq les pharses en trop
# faire en sorte que dès qu'il y a une modification ne pas écrire encore et encore, mais relancer un autre while

echo "Le nombre de mots est : $number_of_words1"

while true
do
    number_of_words2=`wc --word < $var`

    w1=$number_of_words1
    w2=$number_of_words2

    if test "$w1" -eq "$w2"
    then 
    echo "Le fichier n'a pas été modifié"
    else
        heure=$(date +%H:%M:%S)
        if test "$w1" -gt "$w2"
        then
            nb_supp=$(($w1-$w2))
            echo "Le fichier a été modifié avec suppression de $nb_supp mots le `date +%x` à $heure" >> Resu
        else
            nb_ajout=$(($w2-$w1))
            echo "Le fichier a été modifié avec ajout de $nb_ajout mots le `date +%x` à $heure" >> Resu
        fi
    fi

    sleep 2;
done