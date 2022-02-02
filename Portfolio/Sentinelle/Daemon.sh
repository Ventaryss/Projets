#/mnt/c/Windows/System32

# avoir une varibale originelle du nombre de mots/cara/lignes
# mots avec s ou non

var="/mnt/c/Users/aubin/OneDrive/Documents/GitHub/Projets/Portfolio/Sentinelle/test"

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

    if test "$w1" -eq "$w2" && test "$c1" -eq "$c2"
    then 
    clear
    echo "Le fichier n'a pas été modifié"
    sleep 0.2
    else
        heure=$(date +%H:%M:%S)
        if test "$w1" -gt "$w2" || test "$c1" -gt "$c2"
        then
            if test "$w1" -gt "$w2" && test "$c1" -gt "$c2"
            then  
                nb_suppw=$(($w1-$w2))
                nb_suppc=$(($c1-$c2))
                echo "Le fichier a été modifié avec suppression de $nb_suppw mots et $nb_suppc caractères le `date +%x` à $heure" >> Resu
            elif test "$w1" -gt "$w2"
            then
                nb_suppw=$(($w1-$w2))
                echo "Le fichier a été modifié avec suppression de $nb_suppw mots le `date +%x` à $heure" >> Resu
            elif test "$c1" -gt "$c2"
            then
                nb_suppc=$(($c1-$c2))
                echo "Le fichier a été modifié avec suppression de $nb_suppc caractères le `date +%x` à $heure" >> Resu
            fi
        elif test "$w1" -lt "$w2" || test "$c1" -lt "$c2"
        then 
            if test "$w1" -lt "$w2" && test "$c1" -lt "$c2"
            then
                nb_ajoutw=$(($w2-$w1))
                nb_ajoutc=$(($c2-$c1))
                echo "Le fichier a été modifié avec ajout de $nb_ajoutw mots et $nb_ajoutc caractères le `date +%x` à $heure" >> Resu
            elif test "$w1" -lt "$w2"
            then
                nb_ajoutw=$(($w2-$w1))
                echo "Le fichier a été modifié avec ajout de $nb_ajoutw mots le `date +%x` à $heure" >> Resu
            elif test "$c1" -lt "$c2"
            then
                nb_ajoutc=$(($c2-$c1))
                echo "Le fichier a été modifié avec ajout de $nb_ajoutc caractères le `date +%x` à $heure" >> Resu
            fi
        fi
    fi

    sleep 1;

    w1=$number_of_words2
    c1=$number_of_cara2
done