<?php
// David WINCKEL

session_start();

if (isset($_SESSION["Connected"]) && $_SESSION["Connected"] == true && isset($_POST["name"]))
{
    if ($_POST["name"] != "")
    {
        if(!isset($_SESSION["Panier"]))
            $_SESSION["Panier"] = array();

        array_push($_SESSION["Panier"],$_POST["name"]);

        $json = json_encode($_SESSION["Panier"]);
        echo $json;
    }
    else
    {
        unset($_SESSION["Panier"]);
        echo "ok";
    }
}
else
{   
    echo "";
}

?>
