<?php
// François Ripp

require_once 'modeles/manipulation/GestionLivre.php';

class Controller implements IController
{
    
    public function execute(Smarty $environnement) 
    {
        $gl = new GestionLivre();
        $livres = $gl->getLivres();
        
        for ($i = 0;$i < sizeof($livres);$i++)
        {
            $array[$i] = array(
                    "key" => $livres[$i]->m_key,
                    "titre" => $livres[$i]->m_titre,
                    "prix" => $livres[$i]->m_prix,
                    "image" => $livres[$i]->m_image,
                    "dateAchat" => $livres[$i]->m_dateAchat
                    ); 
        }
                
        $environnement->assign("livresUtilisateur",$array);
        
    }
}

?>
