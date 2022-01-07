#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <time.h>

#define TAILLETAB 2000
const int TAILLEMAX = 2000;

int aleatoire();

int main()
{
    char chaine[TAILLETAB] = {0};
    char tabalea[20] = {0};
    int tab[TAILLETAB] = {0};
    int longchaine = 0, i = 0, compteur = 0;
    int alea;

    printf("Ecrivez le message que vous souhaitez crypter (%d caracteres maximum autorises)\n", TAILLEMAX);
    fgets(chaine, sizeof(chaine), stdin);

    while (chaine[longchaine]!='\n')
    {
        longchaine++;
    }

    for (i = 0; i < longchaine; i++)
    {

        tab[i] = chaine[i];
        
    }

    printf("Chaine cryptee :\n");

    alea = aleatoire();
    

    for (i = 0; i < longchaine; i++)
    {

        printf("%c", tab[i] + alea);
        
    }

    printf("\nclee de cryptage : %d\n", alea);

    return 0;
}

int aleatoire()
{
    srand(time(NULL));

    int nbAleatoire = 10 + rand()%(127+1-10);

    return nbAleatoire;
}