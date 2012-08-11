<?php /* Smarty version Smarty-3.1.7, created on 2012-08-11 15:42:01
         compiled from "templates/menu.tpl" */ ?>
<?php /*%%SmartyHeaderCode:3570338744fa149d2ee8bb3-46926445%%*/if(!defined('SMARTY_DIR')) exit('no direct access allowed');
$_valid = $_smarty_tpl->decodeProperties(array (
  'file_dependency' => 
  array (
    'b6da4162c469d98c5e879f8e0b21e18d44108090' => 
    array (
      0 => 'templates/menu.tpl',
      1 => 1344692517,
      2 => 'file',
    ),
  ),
  'nocache_hash' => '3570338744fa149d2ee8bb3-46926445',
  'function' => 
  array (
  ),
  'version' => 'Smarty-3.1.7',
  'unifunc' => 'content_4fa149d2f0c26',
  'has_nocache_code' => false,
),false); /*/%%SmartyHeaderCode%%*/?>
<?php if ($_valid && !is_callable('content_4fa149d2f0c26')) {function content_4fa149d2f0c26($_smarty_tpl) {?>
<p>
<a href="?Page=accueil"><span class="menuElement">Accueil</span></a>

<br />
<span class="menuParent">Les personnages</span>
<a href="?Page=catalogue"><span class="menuElement">Création de personnages</span></a>
<a href="?Page=classesJdr"><span class="menuElement">Classes</span></a>
<a href="?Page=racesJdr"><span class="menuElement">Races</span></a>

<br />
<span class="menuParent">Le système de jeu</span>
<a href="?Page=catalogue"><span class="menuElement">Combat</span></a>
<a href="?Page=catalogue"><span class="menuElement">Monstres</span></a>
</p>

        <?php }} ?>