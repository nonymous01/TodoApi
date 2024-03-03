'all/ : affiche tout les ajous

'create/ : cree un nouveau todo
    {"title":<le titre>,
    "description":<la description>
    }

'update/<int:pk>/': fais la mise a jour des données
    {"title":<nouveau titre>,
    "description":<nouveau description>
    }

'delete/<int:pk>' : supprimé les donner
    {"title":<le titre>,
    "description":<la description>
    }

'sing/' : inscripntion
    {"username":<le nom>,
    "email":<email>,
    "password":<password>
    }

'loging/ : se connecter
     {
    "email":<email>,
    "password":<password>
    }
    
'all_to' : afficher tout les user inscrit

