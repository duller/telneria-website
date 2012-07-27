<?php
// David WINCKEL

class HyperController implements IController
{
    public function execute(Smarty $environnement) 
    {
        if (isset($_SESSION["Connected"]) && $_SESSION["Connected"] == true )
        {
            $environnement->assign("Connected", $_SESSION["Connected"]);
            $environnement->assign("Login", $_SESSION["Login"]);
            
            if (isset($_SESSION["Panier"]))
            {
                if (sizeof($_SESSION["Panier"]) > 1)
                    $environnement->assign("panierNombre", sizeof($_SESSION["Panier"]) . " articles");
                else
                    $environnement->assign("panierNombre", sizeof($_SESSION["Panier"]) . " article");
                    
            }
            else
                $environnement->assign("panierNombre", "0 article");
                
        }
        else
        {
            $environnement->assign("Connected", false);
            $environnement->assign("Login", "");
        
        }

    }
}

?>
