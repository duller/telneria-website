<?php
// David WINCKEL & François Ripp

require_once 'modeles/metier/Livre.php';

class GestionLivre 
{
    private $liste;
    
    public function __construct() 
    {
        $this->liste[0] = new Livre("livrerouge","Le livre rouge","ressources/RedBook.png",19.80,"12/03/2011");
        $this->liste[1] = new Livre("livremonstre","Le livre des monstres","ressources/MonsterBook.png",36.20,"23/02/2009");
    }

    public function getLivres()
    {
        return $this->liste;
    }
    
    public function getLivre($nomLivre)
    {
        foreach ($this->liste as $value) 
        {
            if ($value->m_key == $nomLivre)
            {
                return $value;
            }
        }
        return null;
    }
}

?>
