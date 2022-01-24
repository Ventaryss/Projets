#/mnt/c/Windows/System32

$var "./test.odt"

FILESIZE=$(stat -c%s "$var")

echo "le fichier pèse $FILESIZE"

while true
do
    if test $var
    then 
    echo "Le fichier a été modifié"
    else
    echo "Le fichier n'a pas été modifié"
    fi

    sleep 3;
done