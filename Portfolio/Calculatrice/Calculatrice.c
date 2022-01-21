#include <stdlib.h>
#include <stdio.h>  
#include <string.h>
#include <math.h>
#include "Calculatrice-Proc.h"

const char STOP1 = ':'; 
const char STOP2 = '.';

#define PI 3.14159265358979323846264338;

int main ()
{
    int choix, i, n_1, n_2, resu_, sommet = 0;
    float n1, n2, resu;
    char signe, chariot, help, histo;

    hist tab;

    printf("Bonjour, je suis votre Calculatrice, veuillez choisir le type de calcul que vous souhaitez !\n");
    printf("1. Calculs basiques\n");
    printf("2. Calculs geometriques\n");
    printf("3. Calculs de factorielles\n");
    printf("4. Calculs de racines\n");
    printf("5. Calculs specifiques (reste)\n");
    printf("6. Historiques de vos derniers calculs\n");
    printf("7. help\n");
    scanf("%d%c", &choix, &chariot);

    while (choix!=STOP2)
    {
        switch (choix)
        {
            case 1 : 

            printf("Entrez votre calcul\n");
            scanf("%f%c%f", &n1, &signe, &n2);

                while (signe!=STOP1)
                {
                    switch (signe)
                    {   
                        case '+' : 
                        resu = addition (n1, n2);
                        printf("%.3f\n", resu); 
                        
                        empiler(resu, tab, &sommet); break;

                        case '-' :
                        resu = soustraction (n1, n2);
                        printf("%.3f\n", resu);

                        empiler(resu, tab, &sommet); break;

                        case '*' :
                        resu = multiplication (n1, n2);
                        printf("%.3f\n", resu);
                        
                        empiler(resu, tab, &sommet); break;

                        case '/' :
                        resu = division (n1, n2);
                        printf("%.3f\n", resu);
                        
                        empiler(resu, tab, &sommet); break; 

                        case '^' :
                        resu = puissance (n1, n2);
                        printf("%.3f\n", resu);
                        
                        empiler(resu, tab, &sommet); break;  

                        default : 
                        printf("La Synthaxe est incorrecte, veuillez reessayer\n"); break;
                    } 

                    printf("Entrez votre calcul\n");
                    scanf("%f%c%f", &n1, &signe, &n2);
                }
                break;

            case 2 :

            printf("Entrez votre type de calcul (s pour sinus, c pour cosinus, et t pour tangente)\n");
            scanf("%c", &signe);

                while (signe!=STOP1)
                {
                    switch (signe)
                    {
                        case 's' :
                        printf("Entrez votre nombre :\n");
                        scanf("%f", &n2);

                        clear();

                        resu = sinus (n2);

                        printf("%.3f\n", resu = sin(n2));
                        
                        empiler(resu, tab, &sommet); break;

                        case 'c' :
                        printf("Entrez votre nombre :\n");
                        scanf("%f", &n2);

                        clear();

                        resu = cosinus (n2);

                        printf("%.3f\n", resu);
                        
                        empiler(resu, tab, &sommet); break;

                        case 't' : 
                        printf("Entrez votre nombre :\n");
                        scanf("%f", &n2);

                        clear();

                        resu = tangente (n2);

                        printf("%.3f\n", resu);
                        
                        empiler(resu, tab, &sommet); break;

                        default : 
                        printf("La Synthaxe est incorrecte, veuillez reessayer\n"); break;
                    }

                    printf("Entrez votre type de calcul (s pour sinus, c pour cosinus, et t pour tangente)\n");
                    scanf("%c", &signe);
                }
                break;

            case 3 :

            printf("Entrez votre calcul\n");
            scanf("%d%c", &n_1, &signe);

                while (signe!=STOP1)
                {
                    switch (signe)
                    {
                        case '!' :
                        resu_ = facto (n_1);

                        printf("%d\n", resu_);
                        
                        empiler(resu_, tab, &sommet); break;

                        default : 
                        printf("La Synthaxe est incorrecte, veuillez reessayer\n"); break;
                    }

                    printf("Entrez votre calcul\n");
                    scanf("%d%c", &n_1, &signe);
                }
                break;

            case 4 :

            printf("Entrez votre calcul\n");
            scanf("%c%f", &signe, &n2);

                while (signe!=STOP1) 
                {
                    switch (signe)
                    {
                        case 'V' :
                        resu = racineCarre(n2);

                        printf("%.3f\n", resu);
                        
                        empiler(resu, tab, &sommet); break;

                        default : 
                        printf("La Synthaxe est incorrecte, veuillez reessayer\n"); break;
                    }

                    printf("Entrez votre calcul\n");
                    scanf("%c%f", &signe, &n2);
                }
                break;

            case 5 :

            printf("Entrez votre calcul\n");
            scanf("%d%c%d", &n_1, &signe, &n_2);

                while (signe!=STOP1)
                {
                    switch (signe)
                    {
                        case '%' : 
                        resu_ = reste (n_1, n_2);
                        printf("%d\n", resu_);
                        
                        empiler(resu_, tab, &sommet); break;
                        
                        default : 
                        printf("La Synthaxe est incorrecte, veuillez reessayer\n"); break;
                    }

                    printf("Entrez votre calcul\n");
                    scanf("%d%c%d", &n_1, &signe, &n_2);
                }
                break; 
  
            case 6 :

            while (histo!='q')
            {
                printf("Bienvenue dans votre historique\n");
                printf("Voici les resultats de vos derniers calculs :\n");

                affichHist(tab, sommet);

                printf("Entrez 'q' pour sortir et revenir au menu\n");
                scanf("%c", &histo);
                break;
            }

            case 7 :

            while (help!='q')
            {
                printf("Voici la page des commandes specifiques a cette calculatrice :\n");
                printf("- Pour PI, mettez simplement : PI\n");
                printf("- Pour une racine carree, mettez un 'V' juste avant le nombre\n");
                printf("- Lorsque vous etes dans un type de calcul specifique, mettez un '%c' a la place du signe pour revenir au menu (1%c1 par exemple)\n", STOP2, STOP2);
                printf("- Si vous souhaitez sortir completement de la calculatrice, mettez un '%c' a la place du choix\n", STOP1, STOP1);
                printf("Entrez 'q' pour sortir et revenir au menu\n");
                scanf("%c", &help);
                break;
            }
        }

        printf("Bonjour, je suis votre Calculatrice, veuillez choisir le type de calcul que vous souhaitez !\n");
        printf("1. Calculs basiques\n");
        printf("2. Calculs geometriques\n");
        printf("3. Calculs de factorielles\n");
        printf("4. Calculs de racines\n");
        printf("5. Calculs specifiques (reste)\n");
        printf("6. Historiques de vos derniers calculs\n");
        printf("7. help\n");
        scanf("%d%c", &choix, &chariot);
    }

    return 0;
}