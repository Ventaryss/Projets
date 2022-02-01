#/mnt/c/Windows/System32

# avoir une varibale originelle du nombre de mots/cara/lignes
# mots avec s ou non
# faire un switch 
# mélanger les méthodes
# rajouter le comptage de lignes

var="/mnt/c/Users/aubin/OneDrive/Documents/GitHub/Projets/Portfolio/Sentinelle/test"

# méthode simple de comptage de mots

number_of_words1=`wc -w < $var`
w1=$number_of_words1

echo "Le nombre de mots est : $number_of_words1"

number_of_cara1=`wc -m < $var`
c1=$number_of_cara1

echo "Le nombre de caractères est : $number_of_cara1"

while true
do
    number_of_words2=`wc --word < $var`

    w2=$number_of_words2

    number_of_cara2=`wc -m < $var`

    c2=$number_of_cara2

    if test "$w1" -eq "$w2" || test "$c1" -eq "$c2"
    then 
    echo "Le fichier n'a pas été modifié"
    else
        heure=$(date +%H:%M:%S)
        if test "$w1" -gt "$w2" || test "$c1" -gt "$c2"
        then
            if test "$w1" -gt "$w2" && test "$c1" -gt "$c2"
            then  
                nb_suppw=$(($w1-$w2))
                nb_suppc=$(($c1-$c2))
                echo "Le fichier a été modifié avec suppression de $nb_suppw mots et $nb_syppc caractères le `date +%x` à $heure" >> Resu
            elif test "$w1" -gt "$w2"
            then
                nb_suppw=$(($w1-$w2))
                echo "Le fichier a été modifié avec suppression de $nb_suppw mots le `date +%x` à $heure" >> Resu
            elif test "$c1" -gt "$c2"
            then
                nb_suppc=$(($c1-$c2))
                echo "Le fichier a été modifié avec suppression de $nb_suppc caractères le `date +%x` à $heure" >> Resu
            fi
        else
            nb_ajoutw=$(($w2-$w1))
            nb_ajoutc=$(($c2-$c1))
            echo "Le fichier a été modifié avec ajout de $nb_ajoutw mots et $nb_ajoutc caractères le `date +%x` à $heure" >> Resu
        fi
    fi

    sleep 2;

    w1=$number_of_words2
    c1=$number_of_cara2
done

# Méthode plus précise avec les caractères

# number_of-cara1=`wc -m < $var`
# c1=$number_of_cara1
# 
# echo "Le nombre de caractères est : $number_of_cara1"
# 
# while true
# do
#     number_of_cara2=`wc -m < $var`
# 
#     c2=$number_of_cara2
# 
#     if test "$c1" -eq "$c2"
#     then 
#     echo "Le fichier n'a pas été modifié"
#     else
#         heure=$(date +%H:%M:%S)
#         if test "$c1" -gt "$c2"
#         then
#             nb_supp=$(($c1-$c2))
#             echo "Le fichier a été modifié avec suppression de $nb_supp caractères le `date +%x` à $heure" >> Resu
#         else
#             nb_ajout=$(($c2-$c1))
#             echo "Le fichier a été modifié avec ajout de $nb_ajout caractères le `date +%x` à $heure" >> Resu
#         fi
#     fi
# 
#     sleep 2;
# 
#     c1=$number_of_cara2
# done