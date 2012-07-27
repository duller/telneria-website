<?php
/* David Winckel */
session_start();

require('libs/Smarty.class.php');

$smarty = new Smarty;
$smarty->template_dir = 'templates/';
$smarty->compile_dir = 'templates_c/';
$smarty->config_dir = 'configs/';
$smarty->cache_dir = 'cache/';

$smarty->assign("nom","Librairie de l'Ours");

if(isset($_GET["Page"]) && is_file("templates/".$_GET["Page"].".tpl"))
{
	$page = $_GET["Page"];
}
else
{
	$page = "accueil";
}

include "global/interfaces/IController.php";
include "global/hypercontroller.php";

$hc = new HyperController();
$hc->execute($smarty);


if(is_file("controller/" . $page . ".php"))
{
    include "controller/" . $page . ".php";

    $c = new Controller();
    $c->execute($smarty);
}
    
$smarty->assign("page",$page . ".tpl");

$smarty->display('index.tpl');



?>
