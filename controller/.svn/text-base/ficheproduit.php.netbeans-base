<?php
// David WINCKEL

require_once 'modeles/manipulation/GestionLivre.php';

class Controller implements IController
{
    
    public function execute(Smarty $environnement) 
    {
        
        $gl = new GestionLivre();
        
        $produit = $gl->getLivre($_GET["Produit"]);
                
        $environnement->assign("nomProduit",$produit->m_titre);
        
        $environnement->assign("imageProduit",$produit->m_image);
        
        $environnement->assign("prixProduit",$produit->m_prix);
        
    }
}

?>
