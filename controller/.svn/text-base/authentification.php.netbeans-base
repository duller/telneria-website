<?php
// David WINCKEL
require_once('modeles/manipulation/DatabaseConnexion.php');

class Controller implements IController
{
    
    public function execute(Smarty $environnement) 
    {    
        
        // Phase de connexion
        if (isset($_POST["login"]) && isset($_POST["motdepasse"]) )
        {
            $probleme = 0;
            
            if (! preg_match("/^[a-zA-Z0-9_-]{3,16}$/", $_POST["login"]) )
            {
                $probleme = 1;
            }

            if (! preg_match("/^[a-zA-Z0-9_-]{6,18}$/", $_POST["motdepasse"]) )
            {
                $probleme = 1;
            }
            
            if ($probleme == 0)
            {
                $result = DatabaseConnexion::getInstance()->requete("select * from client where LOGIN='" .$_POST["login"]. "' AND PASSWD='".md5($_POST["motdepasse"])."'");

                if ($result->numRows()) // Si il y a une ligne de résultat (donc si un utilisateur existe)
                {
                    $_SESSION["Connected"] = true;
                    $_SESSION["Login"] = $_POST["login"];
                    setcookie("Login", $_SESSION["Login"],time()+3600*24*7); // Validité de session 7 jours

                    $environnement->assign("connexion","connexionreussi");
                }
                else
                {
                    $environnement->assign("connexion","");
                }
            }
                else
                {
                    $environnement->assign("","");
                }
                         
        }
        else // Phase de deconnexion
        {
            $_SESSION["Connected"] = false;
            unset($_SESSION["Login"]);
            setcookie("Login", "",0); // Destruction du cookie
            
            $environnement->assign("connexion","deconnexionreussi");


        }
        
    }
}

?>
