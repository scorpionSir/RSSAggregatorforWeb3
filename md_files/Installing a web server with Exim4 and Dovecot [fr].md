Quelques notes sur l’installation d’un serveur mail, avec gestion en IMAPS et
configuration d’un « catch-all » pour pouvoir reçevoir tous les mails envoyés
(indiféremment de la partie de l’adresse mail avant l’arobaze).

## Configuration de Dovecot

Installer les paquets :

    
    
    dovecot-common dovecot-core dovecot-imapd dovecot-managesieved dovecot-sieve
    

L’installer, puis dans `/etc/dovecot/dovecot.conf` décommenter :

    
    
    #ssl_cert_file = /etc/ssl/certs/dovecot.pem
    #ssl_key_file = /etc/ssl/private/dovecot.pem
    

Décommenter la section `protocol lda` pour pouvoir mettre `postmaster_address`
à la valeur souhaitée. Également décommenter `disable_plaintext_auth`, pour
activer la directive.

## Intégration de Dovecot avec Exim

Dans `/etc/exim4/conf.d/transports` créer un fichier `20_dovecot` contenant :

    
    
    dovecot:
        driver = pipe
        command = /usr/lib/dovecot/deliver
        message_prefix =
        message_suffix =
        log_output
        delivery_date_add
        envelope_to_add
        return_path_add
        temp_errors = 64 : 69 : 70: 71 : 72 : 73 : 74 : 75 : 78
    

Puis modifier `/etc/exim4/conf.d/router/900_exim4-config_local_user` pour
mettre la valeur de `transport` au transport nouvellement créé :

    
    
    transport = dovecot
    

## Configuration d’Exim

Pour celà, utilisez la commande suivante :

    
    
    dpkg-reconfigure exim4-config
    

Le premier dialogue vous demande le type de configuration général, vous devez
donc indiquer la première option (les mails sont reçus et envoyés avec SMTP),
ou la seconde si vous utilisez un smarthost.

Lors de l’étape vous demandant les adresses IP où écouter pour des connexions
SMTP, entrez `0.0.0.0 ; ::1` pour écouter sur toutes les interfaces.

Quand on vous demandera les autres destinations où les mails sont acceptés,
vous pouvez rentrer une liste de domaines séparés par un point-virgule.
L’étoile semble acceptée : Il est possible de rentrer `*.palkeo.com` par
exemple.

Pour stocker les mails, utilisez donc le format « Maildir » dans les
répertoires utilisateurs.

Enfin, découpez la configuration en petits fichiers.

## Mise en place du catch-all

Pour celà, modifiez votre `/etc/aliases` et rajoutez une entrée du type :

    
    
    *: utilisateur
    

Où utilisateur est le nom de l’utilisateur vers lequel vont être redirigés les
mails.

Il suffit alors de créer un fichier `/etc/exim4/conf.d/router/999_catchall`
contenant :

    
    
    catchall:
        driver = redirect
        data = ${lookup{*}lsearch{/etc/aliases}}
        #local_parts = !/etc/exim4/catchall_blacklist
        domains = +local_domains
        retry_use_local_part
    

Si vous le souhaitez, vous pouvez décommenter la ligne `local_parts` et créer
le fichier `catchall_blacklist` qui contiendra une liste d’utilisateurs qui ne
seront pas redirigés (utile si vous recevez du spam sur une adresse en
particulier).

N’oubliez pas de rafraîchir votre configuration (je suppose qu’un `update-
exim4.conf` devrait suffire).

## Utilisation de fail2ban

Pour utiliser fail2ban avec Dovecot, créez un fichier
`/etc/fail2ban/filter.d/dovecot.conf` contenant :

    
    
    [Definition]
    #failregex = (?: pop3-login|imap-login): (?:Authentication failure|Aborted login \(auth failed|Aborted login \(tried to use disabled|Disconnected \(auth failed).*rip=(?P<host>\S*),.*
    failregex = .*auth-worker.*pam\(.*,(?P<host>\S*)\): pam_authenticate\(\) failed: Authentication failure.*
    ignoreregex =</code>
    

Éditez aussi `/etc/fail2ban/jail.conf`, pour ajouter :

    
    
    [dovecot]
    enabled  = true
    port     = smtp,ssmtp,imap2,imap3,imaps,pop3,pop3s
    filter   = dovecot
    logpath  = /var/log/mail.log</code>
    

Enfin, pensez à modifier le fichier `/etc/dovecot/dovecot.conf` pour
décommenter la ligne :

    
    
    #auth_verbose = yes
    

Puis rechargez la configuration, et voilà :)

