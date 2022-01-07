#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <time.h>

#define TAILLETAB 1000
const int TAILLEMAX = 1000;

int aleatoire();

int main()
{
    char chaine[TAILLETAB] = {0};
    char tabalea[20] = {0};
    int decrypt;
    int tab[TAILLETAB] = {0};
    int longchaine = 0, i = 0, compteur = 0;
    int alea;

    printf("Ecrivez le message que vous souhaitez decrypter (%d caracteres maximum autorises)\n", TAILLEMAX);
    fgets(chaine, sizeof(chaine), stdin);

    printf("Entrez la cle de cryptage\n");
    scanf("%d", &decrypt);

    while (chaine[longchaine]!='\n')
    {
        longchaine++;
    }

    for (i = 0; i < longchaine; i++)
    {

        tab[i] = chaine[i];
        
    }

    printf("Chaine decryptee :\n");
    
    for (i = 0; i < longchaine; i++)
    {

        printf("%c", tab[i] - decrypt);
        
    }

    return 0;
}

