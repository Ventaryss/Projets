#/mnt/c/Windows/System32

var="/mnt/c/Users/aubin/OneDrive/Documents/GitHub/Projets/Portfolio/Sentinelle/test"
number_of_words1=`wc --word < $var`

# méthode simple de comptage de mots
# fichier qui s'écrase 
# date et heure à faire

echo "Le nombre de mots est : $number_of_words1"

while true
do
    number_of_words2=`wc --word < $var`

    if test "$number_of_words1" -eq "$number_of_words2"
    then 
    echo "Le fichier n'a pas été modifié"
    else
        if test "$number_of_words1" -gt "$number_of_words2"
        then
            nb_supp=${number_of_words1}-${number_of_words2}
            echo "Le fichier a été modifié avec suppression de $nb_supp mots le $date à $heure" > Resu
        else
            nb_ajout=$number_of_words2-$number_of_words1
            echo "Le fichier a été modifié avec ajout de $nb_ajout mots le $date à $heure" > Resu
        fi
    fi

    sleep 2;
done