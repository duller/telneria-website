<?php
// David Winckel
require_once('pear/MDB2.php');

class DatabaseConnexion {
  
   private static $_instance = null;
   private $db = null;
   
   private function __construct() 
   {
        $this->db = MDB2::connect('mysql://root:root@localhost/librairieOurs');

        if (MDB2::isError($this->db)) 
        {
            die("Connexion error: " . $this->db->getDebugInfo());
        }
   }
   
   public function requete($sql)
   {
       return $this->db->query($sql);
   }

   public static function getInstance() 
   {
     if(is_null(self::$_instance)) 
     {
        self::$_instance = new DatabaseConnexion();  
     }
 
     return self::$_instance;
   }
}
 

?>
