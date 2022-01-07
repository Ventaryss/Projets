#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdbool.h>

#define N 100
typedef float hist[N];

float addition (float n1, float n2);
float soustraction (float n1, float n2);
float multiplication (float n1, float n2);
float division (float n1, float n2);
int reste (int n_1, int n_2);
float puissance (float n1, float n2);
float racineCarre (float n2);
int facto (int n_1);
float sinus (float n2);
float cosinus (float n2);
float tangente (float n2);
void creerPile (hist tab);
void empiler (float nb, hist tab, int *n);
void depiler (hist tab, int *n);
int sommet (hist tab, int n);
void remplir (hist tab, int*n);
void affichHist (hist tab, float sommet);
void clear (void);

float addition (float n1, float n2)
{
    float res;

    res = n1+n2;

    return res;
}

float soustraction (float n1, float n2)
{
    float res;

    res = n1-n2;

    return res;
}

float multiplication (float n1, float n2)
{
    float res;

    res = n1*n2;

    return res;
}

float division (float n1, float n2)
{
    float res;

    res = n1/n2;

    return res;
}

int reste (int n_1, int n_2)
{
    int res;

    res = n_1%n_2;

    return res;
}

float puissance (float n1, float n2)
{
    float res;

    res = pow(n1,n2);

    return res;
}

float racineCarre (float n2)
{
    float res;

    res = sqrtf(n2);

    return res;
}

int facto (int n_1)
{
    int res = 1;
    int i;

    for (i = 1; i <= n_1; i++)
    {
        res = res*i;
    }

    return res;
}

float sinus (float n2)
{
    float res;

    res = sin(n2);

    return res;
}

float cosinus (float n2)
{
    float res;

    res = cos(n2);

    return res;
}

float tangente (float n2)
{
    float res;

    res = tan(n2);

    return res;
}

void clear (void)
{    
  while ( getchar() != '\n' );
}

void creerPile (hist tab)
{
    int i;

    for (i=0; i<N; i++)
    {
        tab[i]=-1;
    }
}

void empiler (float nb, hist tab, int *sommet)
{
    *sommet = *sommet+1;
    tab[*sommet] = nb;
}

void depiler (hist tab, int *sommet)
{
    tab[*sommet] = -1;
    *sommet = *sommet-1;
}

int sommet (hist tab, int sommet)
{
    return tab[sommet];
}

void remplir (hist tab, int *sommet)
{
    int nb;

    printf("Souhaitez-vous enregistrer cette valeur dans l'historique ? (0 pour non, 1 pour oui)\n");
    scanf("%d", &nb);

    if (nb==1)
    {
        empiler(nb,tab,sommet);
    }
}

void affichHist (hist tab, float sommet)
{
    int i;

    for (i=1; i<=sommet; i++)
    {
        printf("%.5f\n", tab[i]);
    }
}