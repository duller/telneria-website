<?php
// David WINCKEL

class Livre 
{
    public $m_key;
    public $m_titre;
    public $m_image;
    public $m_prix;
    public $m_dateAchat;//valide uniquement quand le livre 
    //est dans la liste des livres achetés d'un utilisateur
    
    public function __construct($key,$titre,$image,$prix,$dateAchat = null) 
    {
        $this->m_key = $key;
        $this->m_titre = $titre;
        $this->m_image = $image;
        $this->m_prix = $prix;
        $this->m_dateAchat = $dateAchat;
    }
}

?>
