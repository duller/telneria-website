<?php
// François Ripp

class Controller implements IController
{
    
    public function execute(Smarty $environnement) 
    {
        if (isset($_SESSION["Panier"]))
        {
            for ($i = 0;$i < sizeof($_SESSION["Panier"]);$i++)
            {
                $array[$i] = array(
                        "nom" => $_SESSION["Panier"][$i]
                        ); 
            }

            $environnement->assign("panier",$array);
        }
        else
        {
            $environnement->assign("panier",array());
            
        }
        
    }
}

?>
