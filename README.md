# Ordo

Ordo est une application Kivy permettant de gérer plusiuers applications en une seule et est adapté particulièrement pour des supports tactiles.

![Présentation](img/presentation.jpg)

## Architecture du projet

Dans le dossier ordo, deux dossiers sont parmi les plus importants : 

- parameters : contient le fichier de paramètres ordo.json pour configurer la taille de l'écran approprié ainsi que les plugins à installer dans l'ordre prédéfini.

Exemple : 

```
{
    "show_cursor":true,
    "resizable":false,
    "fullscreen":false,
    "width":1024,
    "height":600,
    "plugins" : ["plugin_1", "plugin_2", "plugin_3"]
}
```

- plugins : Contient l'ensemble des plugins à ajouter. Un formalisme doit être respecté pour chacun des plug-ins (des exemples sont à venir)

## Commandes

### Lancer l'application.

```
poetry run python main.py
```

### Désinstaller un plugin

```
poetry run uninstall nom_de_mon_plugin
```

Il est recommandé de ne pas supprimer le dossier du plugin manuellement afin de nettoyer également les librairies nécessaires uniquement au plugin à supprimer.