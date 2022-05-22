# Un Firefox qui respecte votre vie privée¶

Quand on est soucieux de sa vie privé / confidentialité sur le web, on peut
facilement tomber dans deux extrêmes :

  * installer AdBlock (ou éventuellement Ghostery), et se dire que ça suffira

  * utiliser une extension comme NoScript, et voire sa navigation rendue pénible sur pas mal de sites…

Nous allons voir plusieurs extensions (ou configurations), qui vont permettre
de rendre Firefox plutôt discret, tout en ayant pour but de nuire le moins
possible à la navigation.

Pour cela, je vais présenter étape par étape, les différents éléments
susceptibles de nuire à votre vie privée, et des outils pour y remédier.

## Le referer HTTP¶

Chaque fois que vous cliquez sur un lien, votre navigateur enverra un [en-tête
HTTP](http://www.alsacreations.com/astuce/lire/1152-en-tetes-http.html) au
site sur lequel vous allez, en lui indiquant de quelle page vous venez. De la
même façon, pour toutes les ressources (images, scripts…) que votre navigateur
charge sur une page, il indique la page en question.

C’est ainsi que si vous mettez une innocente image dans la signature de vos
messages sur un forum, vous pouvez très facilement suivre des internautes, en
regardant de quelles pages ils viennent à chaque fois qu’ils chargent cette
image. Inutile de vous parler des boutons « +1 » et « Like »…

Il est possible de supprimer tout simplement cet en-tête de vos requêtes.
Malheureusement, certains sites ont besoin du referer pour fonctionner,
souvent car ils font des vérifications de sécurité dessus (souvent pour éviter
les attaques CSRF).

Pour parer à cela tout en ne cassant pas certains sites, je vous conseille
l’excellent [Smart Referer](https://addons.mozilla.org/en-
us/firefox/addon/smart-referer/). L’avantage principal de cette extension est
qu’elle enverra le referer correct seulement dans le cas où vous faites une
requête destiné au site sur lequel vous êtes déjà.

Du coup, toutes les vérifications de sécurité passent, et vous y gagnez
énormément en confidentialité :)

## Les cookies¶

![../_images/cookie-trash.jpg](../_images/cookie-trash.jpg)

Comme vous le savez sûrement, les cookies c’est mal. Et pourtant, c’est
totalement inconcevable de les désactiver : énormément de sites en ont besoin
pour fonctionner.

Une première solution de mitigation est d’aller indiquer à Firefox de ne
jamais accepter les cookies tiers (dans l’onglet vie privé des préférences).
Ainsi, seul les cookies du site sur lequel vous êtes seront acceptés : aucune
régie de pub externe ne pourra pas vous poser des cookies.

Mais bon, vous aurez toujours un bon paquet de cookies posés par des sites qui
ne sont pas censés retenir des choses sur vous.

Heureusement, il existe [Self-Destructing
Cookies](https://addons.mozilla.org/en-US/firefox/addon/self-destructing-
cookies/) ! Cette extension va tout simplement laisser les sites poser des
cookies pendant votre navigation, mais les supprimera dès que vous aurez
terminé de naviguer sur le site (bien évidemment, vous pouvez faire des
exceptions).

Simple et efficace :)

## Flash¶

Too bad : les plugins Flash disposent de leur propre moyen de stocker des
données.

Si on rajoute à ça le fait qu’ils sont un bon vecteur d’infection (et de
ralentissement de PC :p), il est bon de ne pas les exécuter à tort et à
travers.

Pour régler ce problème, il suffit de sélectionner « Demander pour activer »,
dans la liste déroulante qui se situe à droite de la liste des plugins de
Firefox.

Et voilà, maintenant il vous suffit de cliquer sur la zone ou devrait être
votre vidéo de chatons, pour lancer Flash. Il est évidemment possible
d’ajouter certains sites en liste blanche.

## HTTPS Everywhere !¶

Parce que beaucoup de sites disposent d’une version sécurisée (HTTPS), mais
fonctionnent par défaut sur la version non chiffrée, l’EFF a développé une
petite extension, [HTTPS Everywhere](https://www.eff.org/https-everywhere),
qui vous passera automatiquement sur la version chiffrée des sites sur
lesquels elle est disponible.

## Les redirections¶

Sur de nombreux sites, quand vous cliquez sur un lien externe, vous passez
d’abord par une page de ce site qui vous redirige ensuite vers le site en
question (généralement à des fins de statistiques).

Le site connaît donc les liens externe sur lesquels vous cliquez, et cette
redirection ralentit votre navigation.

Pour éviter cela, il existe [Redirect
Cleaner](https://addons.mozilla.org/fr/firefox/addon/redirect-cleaner/), qui
remplace les liens de redirection par un lien vers la [destination
finale](https://fr.wikipedia.org/wiki/Destination_finale).

## L’empreinte du navigateur¶

Des outils comme [Panopticlick](https://panopticlick.eff.org/) nous montrent
que chaque navigateur a une empreinte bien à lui :

  * son [User-Agent](https://fr.wikipedia.org/wiki/User-agent) donne des informations sur votre système d’exploitation, sa version…

  * d’autres en-têtes HTTP, comme « Accept-Language » donnent aussi des informations sur vous.

  * en Javascript, on peut ensuite récupérer votre résolution, la liste des plugins, polices… ce qui donne énormément d’informations.

Ceci est assez dur à éviter, mais il existe quelques parades :

  * [FireGloves](https://addons.mozilla.org/en-US/firefox/addon/firegloves/), essaie de régler le problème en interdisant l’accès à la plupart de ces données.

  * Une extension comme NoScript (dont je parle plus bas), a l’avantage d’éviter les fuites dues au Javascript.

  * [Modify Headers](https://addons.mozilla.org/fr/firefox/addon/modify-headers/), vous permet de modifier/supprimer les en-têtes HTTP trop bavardes.

  * [Masking Agent](https://addons.mozilla.org/en-us/firefox/addon/masking-agent/) peut masquer votre système d’exploitation de votre user-agent.

Toutefois, gardez en tête que toutes les modifications que vous faites
pourront vous faire sortir encore plus de la masse : avoir le Javascript
désactivé est peu commun, et avoir un user-agent absent ou tout modifié peut
aussi être quelque chose qui vous rend tout à fait unique…

## Une couche de spoofing ?¶

### De l’adresse IP¶

Si vous voulez vous amuser, vous pouvez installer une extension comme [Modify
Headers](https://addons.mozilla.org/fr/firefox/addon/modify-headers/), et vous
amuser à rajouter des headers du genre « X-Forwarded-For », « Client-IP »… en
mettant une IP bidon (c’est le principe de
[IPFuck/IPFlood](https://addons.mozilla.org/fr/firefox/addon/ipflood/)).

Ça ne change pas votre IP réelle, hein ! Mais ça peut éventuellement emmêler
les pinceaux d’applications pas super bien conçues, donc c’est toujours bon à
prendre.

### Des recherches¶

Il est même possible d’envoyer de fausses requêtes aux moteurs de recherches
que vous utilisez, afin de noyer vos requêtes dans un flux de requêtes
générées aléatoirement.

Pour cela, utilisez
[TrackMeNot](https://addons.mozilla.org/fr/firefox/addon/trackmenot/).

## Do Not Track¶

Dans l’onglet « vie privée » des préférences, il est possible de dire que vous
ne voulez pas être pisté pendant votre navigation.

Le principe de cette option, c’est que votre navigateur va rajouter un en-tête
« DNT: 1 » à toutes vos requêtes. C’est-à-dire qu’il va dire au serveur «
coucou, mon utilisateur il a dit qu’il voulait pas être surveillé ».

C’est tout. Libre au serveur de faire ce qu’il veut de cette information.

Du coup vous pouvez activer ceci, mais il faudra simplement espérer que les
serveurs derrière traîteront spécifiquement vos requêtes, alors même que c’est
souvent contre leur intérêt.

## La cerise sur le gâteau¶

Vous avez maintenant un navigateur qui sera relativement peu consentant à
divulguer tous ses secrets ou à retenir des choses non sollicitées.

Par contre, votre Firefox fera toujours des requête auprès des régies de pub,
des outils de statistiques, etc… Leur travail s’en trouvera probablement
compliqué, mais ça ne résout pas le problème.

Du coup, vous pouvez installer une de ces extensions, classées par degré de
parano croissant :

### AdBlock¶

[AdBlock Plus](https://addons.mozilla.org/fr/firefox/addon/adblock-plus/), ou
son fork [AdBlock Edge](https://addons.mozilla.org/fr/firefox/addon/adblock-
edge/), sont des extensions ultra-efficaces pour bloquer la publicité.

Il faut savoir qu’AdBlock fonctionne avec un système de _listes_ , qui vont
contenir chacune tout plein de règles de blocages. Or, il y a [des
listes](https://easylist.adblockplus.org/en/) pour bloquer la publicité, mais
[il y en a aussi](https://easylist.adblockplus.org/en/#additionalcontent) qui
vont faire de leur mieux pour bloquer les outils de statistiques, etc…

Il est bon à savoir que vous pouvez vous créer vos filtres personnels : de
temps en temps, vous pouvez ouvrir la liste des éléments bloquables de la page
où vous vous trouvez, et faire de petites règles bloquant les outils de
statistiques qui ne le sont pas déjà.

### Ghostery¶

Si AdBlock ne vous suffit pas, des extensions comme
[Ghostery](https://addons.mozilla.org/fr/firefox/addon/ghostery/), peuvent
venir se rajouter. Ghostery est spécialisé dans le blocage d’outils de
statistiques et autre petits espions.

### RequestPolicy¶

Avec [RequestPolicy](https://www.requestpolicy.com/), on entre dans une autre
catégorie d’extension, qui ne contient pas une liste de choses à bloquer, mais
plutôt une liste de choses à accepter.

Du coup, vous bénéficiez d’une confidentialité vraiment accrue, et vous êtes
par la même occasion protégé de certaines attaques comme les CSRF. Plus besoin
d’extension comme AdBlock ou Ghostery : tout ça est déjà bloqué à la base. Par
contre, certains sites peuvent se mettre à fonctionner mal tant que vous
n’avez pas créé d’exceptions pour eux (typiquement, plus d’images ni de CSS).

Le principe de RequestPolicy est donc d’interdire toutes les requêtes qui ne
sont pas destinées au site sur lequel vous êtes : simple, et efficace. Il peut
aussi autoriser par défaut toutes les requêtes, et ça sera à vous de mettre
les domaines de votre choix en liste noire.

Par contre, après installation, vous vouz rendrez compte que pas mal de sites
vont chercher des ressources sur des
[CDN](https://fr.wikipedia.org/wiki/Content_delivery_network) (gstatic,
cloudfront…), qu’il faudra donc passer en liste blanche. Une fois que ce sera
fait, la plupart des sites fonctionneront parfaîtement, et vous aurez juste à
rajouter des exceptions de temps en temps, pour les sites qui chargent toutes
leurs ressources depuis un domaine différent du leur.

Ah, et je vous conseille d’utiliser au moins RequestPolicy 1.0, qui apporte
pas mal d’améliorations par rapport à la 0.5.

**Mise à jour :** Regardez aussi du côté de Policeman, une alternative que je
trouve personnellement plus aboutie.

### NoScript¶

[NoScript](http://noscript.net/), est tout aussi radical que RequestPolicy,
mais ne fonctionne pas pareil : RequestPolicy fonctionne au niveau « réseau »,
en bloquant certaines requêtes. NoScript, lui, va simplement interdire
l’exécution de tous les scripts Javascript sur la page.

J’ai personellement une préférence pour RequestPolicy, qui « casse » moins les
sites, et bloquera même des petites images qui vont se charger sur un domaine
extérieur.

Par contre, NoScript permet de se prémunir d’exploits utilisant Javascript, et
empêche même le site que vous visitez de faire des choses louches.

## Conclusion¶

Avec toutes ces mesures, on peut arriver à un degré de discrétion plutôt bon.

Pour vous en rendre compte, de l’efficacité de toutes ces techniques, rien de
mieux que de charger une page en regardant toutes les requêtes HTTP qui
passent ;)

Par contre, même si on a vu des moyens pour atténuer largement leur portée,
deux problèmes de fond restent :

### Problème 1 : Avoir un navigateur qui se fond dans la masse¶

Toutefois, des outils comme [Panopticlick](https://panopticlick.eff.org/) nous
montrent qu’il est bien plus dur que ça d’arriver à **vraiment** se camoufler
parmi les autres navigateurs. Votre navigateur a des headers déjà bien à lui,
mais alors si on se met à récupérer des informations par le biais du
Javascript, c’est la fin…

Enlever des headers ? Désactiver Javascript ? Cool, comme ça vous sortez
encore plus de la masse avec votre configuration pas du tout habituelle :/

### Problème 2 : Avoir un navigateur qui ne retient rien¶

Les cookies sont un moyen de stocker des informations sur l’utilisateur,
utiliser l’empreinte de son navigateur (headers, configuration…) peut
permettre de l’idendifier de manière unique et donc de retenir des choses sur
lui.

Mais il existe d’autres moyens de stocker des informations dans le navigateur,
sans passer par les cookies.

Par exemple, le [LocalStorage](http://diveintohtml5.info/storage.html). Celui-
là est également géré par Self-Destructing Cookies.

Par contre, il y a tout un tas d’autres techniques plus ou moins loufoques qui
permettent de stocker des information dans votre navigateur (comme exploiter
son cache, par exemple).

La référence dans le domaine est une petite démo,
[evercookie](http://samy.pl/evercookie/), qui peut vous permettre de découvrir
tout ça.

Bref, il y a moyen de s’amuser…

Previous: [ Web crawler & finding word lists [fr] ](../projets/sets.html)
Next: [ Neo4j tips : starting & optimizing ](neo4j.html)

### [palkeo](../index.html)

  * [Projects](../projets/index.html)
  * [Blog articles](index.html)
  * [Links](http://links.palkeo.com)
  * [Repository](http://repo.palkeo.com/)
  * [About](../about.html)

##  28 May 2015

  * Language: [French](language/french.html)
  * Tag: [firefox](tag/firefox.html)

(C)2020, palkeo.

