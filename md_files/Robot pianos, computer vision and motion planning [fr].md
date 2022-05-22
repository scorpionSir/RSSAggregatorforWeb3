![moi et les pianos](https://www.palkeo.com/en/blog/_images/pianos.png)

J’ai eu l’occasion de travailler avec Céleste Boursier-Mougenot (artiste
français) pour sa dernière exposition au musée des abattoirs à Toulouse. En
effet, j’ai fait partie d’une équipe de quatre ingénieurs ([Ken
Hasselman](http://kenh.fr), [Guilhem “Nim” Saurel](http://saurel.me) et
Vincent Angladon), contactés pour travailler sur la partie technique de
l’œuvre _Offroad_.

## Concept

L’œuvre consistait à faire se déplacer trois pianos à queue, dans la plus
grande salle du musée des abattoirs. Les pianos devant se déplacer de manière
autonome, et avoir une trajectoire qui plaise à l’artiste (qualifiée
d’aléatoire, d’animale).

Nous avions approximativement trois mois pour tout réaliser, et avions moins
d’un mois avec un accès au musée, pour tout mettre en place et surtout tester
notre système en conditions réelles ! C’est en réalité une fois au musée que
le plus gros du développement s’est réalisé, c’était donc un véritable rush.
Cette période était particulièrement excitante et sympathique, mais aussi très
stressante : nous avions une deadline (le jour du vernissage de l’exposition),
et nous DEVIONS avoir le système qui tourne parfaitement pour cette date :
impossible de repousser l’échéance ou de rendre un système qui marche mal.

## Suivi des pianos : vision par ordinateur

[![installation des
pianos](https://www.palkeo.com/en/blog/_images/installation-
pianos.jpg)](https://www.palkeo.com/en/_images/installation-pianos.jpg)

Un premier problème s’est posé : avant toute chose, si on veut faire bouger
les pianos dans les limites de la salle (et en prenant potentiellement en
compte les visiteurs), il faut pouvoir connaître leur emplacement, et le
suivre au fur et à mesure du temps.

Une solution peu coûteuse sur laquelle on a décidé de se concentrer fut la
vision par ordinateur : via l’installation de deux caméras grand angle, nous
avons pu couvrir toute la pièce.

Toutefois, la conception d’un algorithme de détection des pianos s’est avéré
extrêmement difficile, pour la simple raison que le sol réléchissait très bien
la lumière, et la surface vernie des pianos également. Ainsi, en fonction de
leur emplacement dans la pièce leur couleur vue par la caméra changeait, et,
dans certaines situations on se trouvait avec un piano qui avait une couleur
très proche de celle du sol.

La solution que l’on a finalement retenue a le mérite d’être relativement
simple, et assez robuste : tout d’abord, on va conserver pour chaque piano la
forme de son contour, on appellera cette forme le « masque » du piano.

Avant de lancer l’algorithme, il faudra positionner le masque du piano (son
contour) sur la position réelle du piano en question sur l’image renvoyée par
les caméras.

Ensuite, le procédé est itératif. Pour chaque nouvelle image, on va calculer
les contours de l’image (via les gradients, nous avons utilisé l’algorithme «
Canny » d’openCV), puis essayer de déplacer légèrement l’image du masque de
chaque piano pour qu’elle colle le mieux possible sur les contours détectés de
l’image.

Pour faire cela, on va essayer de déplacer/tourner chaque masque d’un cran
dans toutes les directions, puis calculer l’écart aux contours : pour chaque
pixel du contour du masque, on calcule sa distance au contour le plus proche
détecté sur l’image. En sommant toutes ces distances, on obtient l’écart aux
contours de l’image. Si on trouve un déplacement du masque qui réduit cet
écart, on recommence depuis cette position jusqu’à atteindre un minimum local.

Puisque rien ne vaut un bon exemple, voici une vidéo montrant l’algorithme en
action :

Toutefois, cet algorithme a deux inconvénients majeurs :

  * L’initialisation doit se faire à la main en mettant le masque sur le piano.

  * Si, pour des raisons, un masque vient à quitter un piano, il va se mettre à se balader sur l’image (ou pire, se coller sur un autre piano), et le système perdra complètement le piano que ce masque était censé suivre.

## Déplacement des pianos

Un autre problème crucial sur lequel je me suis penché est la gestion des
déplacements des pianos. Il s’agit donc de « motion planning », domaine de
recherche pour lequel le problème type est le problème du déménageur de
pianos, quelle coincidence !

Ce fût particulièrement compliqué d’arriver à aboutir à quelque chose plaisant
à l’artiste car si on sait comment amener un objet d’un point A à un point B
(même avec de fortes contraintes, des obstacles…), on sait moins faire bouger
un objet de manière aléatoire, sachant que ses mouvements doivent êtres «
esthétiques », et plaire à l’artiste !

Nous avions donc commencé par une machine à état faisant se déplacer les
pianos, et non seulement les mouvements étaient complètement « robotiques »,
mais en plus nous avons rencontré des problèmes d’exclusion mutuelle quand
deux pianos proches étaient en train de faire demi-tour et s’arrêtaient,
chacun attendant que l’autre parte pour continuer sa manœuvre.

La solution fut alors une solution connue en motion planning : utiliser un
champ de potentiels ! En effet, il a suffit de modéliser un champ de
potentiels dont les pianos suivraient le gradient (un relief dont les pianos
descendraient les pentes !), et de donner aux pianos un mouvement naturel vers
l’avant quand ils sont sur du plat, et voilà ! Arrivant près d’un mur, les
pianos se retrouvent face à une grosse montée, et finissent forcément par
ralentir, se retourner et redescendre la pente.

Là où cette solution devient particulièrement élégante, et qu’il est possible
de modéliser les pianos par des bosses dans le relief (voire des creux),
permettant à chaque piano d’éviter les autres, ou d’en être attiré ! On
obtient donc au final un comportement très sympathique, et assez imprévisible.

D’ailleurs, il a été très intéressant de remarquer que dans notre simulateur,
les pianos se mettaient à tourner en rond dans une position d’équilibre
mutuel. Alors qu’en vrai, celà n’arrive jamais. Merci le monde réel qui est
truffé d’imperfections, et notre PID grossier pour asservir les moteurs des
pianos, qui a tout intérêt à le rester.

## Résultat final

Vue par nos caméras :

Vue par un humain au musée :

Et en bonus, un article du monde sur les pianos : [`article-
pianos.pdf`](https://www.palkeo.com/en/blog/_downloads/59a3e8ee285d015355ea17fecef1d60a/article-
pianos.pdf).

En conclusion, c’était donc un projet extrêmement intéressant, aussi bien sur
le plan technique que sur le plan humain.

