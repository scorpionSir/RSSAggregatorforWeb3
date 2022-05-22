# Introduction to Python [fr]¶

Cette page a servi de support pour les formations Python d’[INP-
net](http://inp-net.bde.inp-toulouse.fr/).

## Préambule¶

### Mémo syntaxe¶

    
    
    for i in range(10):
        if i % 2 == 0:
            print("%s est pair !" % i)
        else:
            print("%s est impair !" % i)
    

La boucle `for` parcours une liste d’éléments. `range(10)` renvoie une liste
avec 10 éléments : `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`.

### S’amuser avec Turtle¶

Pour une sympathique démonstration, taper ceci dans une console :

    
    
    python -m turtle
    

Puis, pour vous amuser, exécutez `python` dans une console, et tapez :

    
    
    import turtle
    turtle.forward(10)
    

Une fenêtre va s’ouvrir, avec votre tortue. Vous pouvez ensuite vous amuser
avec `turtle.forward` et `turtle.right` ou `turtle.left`. Essayez de mettre
des boucles for !

    
    
    for i in range(1,1000):
        turtle.forward(10)
        turtle.right(1000 / float(i))
    

## Épreuves¶

### Épreuve 1¶

Trouvez la somme des nombres compris entre 10 et 1000 inclus, qui sont
divisibles par 7.

Indice : utilisez le modulo (opérateur `%`).

Trop facile ? Faites-le en une ligne !

### Épreuve 2¶

#### Intro¶

Avant de vous lancer, téléchargez ce fichier :
[`hp1.txt`](../_downloads/e53210327b82b0df62b61d2089134439/hp1.txt). Essayez
de comprendre et de jouer avec ce script :

    
    
    import matplotlib.pyplot as plt
    
    texte = open('hp1.txt').read()
    mots = texte.split()
    
    d = {'pierre': [], 'poudlard': [], 'flamel': [], 'dudley': []}
    
    for i, mot in enumerate(mots):
        for m, l in d.items():
            if m in mot.lower():
                l.append(i)
    
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    
    for i, (m, l) in enumerate(d.items()):
        ax.plot(l, [1*i]*len(l), 'o', label=m)
    
    plt.legend()
    plt.draw()
    plt.show()
    

Qui donne des résultats comme :

[![../_images/hp.svg](../_images/hp.svg)](../_images/hp.svg)

#### Épreuve¶

L’utilisateur donne un mot, et vous devez lui dire quels sont les mots qui
suivent le plus souvent ce mot, dans Harry Potter 1.

Indice : Utilisez `raw_input()` pour demander le mot et le récupérez. Utilisez
les dictionnaires pour stocker un compteur pour chaque mot. La fonction
`sort()` pourra vous être utile à la fin.

Trop facile ? Découper les mots grace aux espaces, c’est sale. On se retrouve
avec des mots contenant des virgules ou autre ponctuation. Faites un truc
prope.

### Épreuve 3¶

Vous vous rappelez du module « turtle » ? Faites un petit programme qui écoute
sur le réseau, et permet à n’importe qui de déplacer la tortue sur votre
écran, en envoyant des commandes simples.

Indice : Pour la programmation réseau, vous aurez besoin des « sockets ». Vous
trouverez facilement des petits exemples sur le web. La commande « netcat »
vous permettra de tester votre programme en vous connectant dessus.

Trop facile ? Supportez plusieurs connexions en même temps. Si vous êtes
motivés, supportez-en des dizaines de milliers (oubliez les
processus/threads).

### Épreuve 4¶

Faites-donc un petit serveur web dynamique avec
[Flask](http://flask.pocoo.org/), qui affiche le nombre d’utilisateurs
connectés sur la machine.

Indice : Vous aurez besoin d’installer Flask, avec le système de
[virtualenv](http://www.virtualenv.org) (pour les machines de l’N7). La
commande `w` vous permettra de connaître les utilisateurs connectés sur la
machine.

Trop facile ? Ajoutez un formulaire sur votre page web, pour envoyer des
messages à tous les utilisateurs connectés sur la machine !

Previous: [ Sphinx for a personal website/wiki [fr] ](sphinx.html)   Next: [
Pourquoi les nerds sont impopulaires ? ](../thoughts/nerds.html)

### [palkeo](../index.html)

  * [Projects](../projets/index.html)
  * [Blog articles](index.html)
  * [Links](http://links.palkeo.com)
  * [Repository](http://repo.palkeo.com/)
  * [About](../about.html)

##  03 November 2013

  * Language: [French](language/french.html)
  * Tag: [python](tag/python.html)

(C)2020, palkeo.

