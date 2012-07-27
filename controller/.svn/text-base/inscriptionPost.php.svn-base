<?php
// David WINCKEL
require_once('modeles/manipulation/DatabaseConnexion.php');

class Controller implements IController
{
    
    public function execute(Smarty $environnement) 
    {
        $probleme = 0;
            
        if (! preg_match("/^[A-Z]+[A-Z]+[A-Z]+$/", $_POST["nom"]) )
        {
            $probleme = 1;
        }

        if (! preg_match("/^[A-Z]+../", $_POST["prenom"]) )
        {
            $probleme = 1;
        }

        if (! preg_match("/^[a-zA-Z0-9_-]{3,16}$/", $_POST["login"]) )
        {
            $probleme = 1;
        }

        if (! preg_match("/^[a-zA-Z0-9_-]{6,18}$/", $_POST["motdepasse"]) )
        {
            $probleme = 1;
        }

        if ($_POST["motdepasse"] != $_POST["motdepasseverif"])
        {
            $probleme = 1;
        }
        
        if (! preg_match("/^.../", $_POST["adresse"]) )
        {
            $probleme = 1;
        }

        if (! preg_match("/^[0-9]{10}$/", $_POST["telephone"]) )
        {
            $probleme = 1;
        }

        if (! preg_match("/^([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$/", $_POST["email"]) )
        {
            $probleme = 1;
        }

        if (! preg_match("/^[A-Z]+../", $_POST["profession"]) )
        {
            $probleme = 1;
        }

        if ( $_POST["sexe"] != "M" && $_POST["sexe"] != "F")
        {
            $probleme = 1;
        }

        if (! preg_match("/^[0-9]{5}$/", $_POST["codepostal"]) )
        {
            $probleme = 1;
        }

        if (! preg_match("/^.../", $_POST["pays"]) )
        {
            $probleme = 1;
        }

        if (! preg_match("/^.../", $_POST["ville"]) )
        {
            $probleme = 1;
        }

        if ($probleme == 0)
        {
            $retour = DatabaseConnexion::getInstance()->requete(
                "INSERT into client VALUES(
                    null
                    ,'".$_POST["nom"]."'
                    ,'".$_POST["prenom"]."'
                    ,'".$_POST["login"]."'
                    ,'".md5($_POST["motdepasse"])."'
                    ,'".$_POST["adresse"]."'
                    ,'".$_POST["telephone"]."'
                    ,'".$_POST["email"]."'
                    ,'".$_POST["profession"]."'
                    ,'".$_POST["sexe"]."'
                    ,'".$_POST["codepostal"]."'
                    ,'".$_POST["pays"]."'
                    ,'".$_POST["ville"]."'
                        )");
            
            $environnement->assign("inscription","reussi");

        }
        else
        {
            $environnement->assign("inscription","");

        }
       
         
    }
}

?>
