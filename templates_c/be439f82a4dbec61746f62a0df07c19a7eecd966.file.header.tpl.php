<?php /* Smarty version Smarty-3.1.7, created on 2012-07-27 20:47:29
         compiled from "templates/header.tpl" */ ?>
<?php /*%%SmartyHeaderCode:13519637594fa149d2e98354-58600264%%*/if(!defined('SMARTY_DIR')) exit('no direct access allowed');
$_valid = $_smarty_tpl->decodeProperties(array (
  'file_dependency' => 
  array (
    'be439f82a4dbec61746f62a0df07c19a7eecd966' => 
    array (
      0 => 'templates/header.tpl',
      1 => 1336417000,
      2 => 'file',
    ),
  ),
  'nocache_hash' => '13519637594fa149d2e98354-58600264',
  'function' => 
  array (
  ),
  'version' => 'Smarty-3.1.7',
  'unifunc' => 'content_4fa149d2ec774',
  'variables' => 
  array (
    'Connected' => 0,
    'panierNombre' => 0,
    'Login' => 0,
  ),
  'has_nocache_code' => false,
),false); /*/%%SmartyHeaderCode%%*/?>
<?php if ($_valid && !is_callable('content_4fa149d2ec774')) {function content_4fa149d2ec774($_smarty_tpl) {?><!-- David Winckel & François Ripp-->
<p>
<a class="lienBlanc" href="?Page=accueil">Accueil</a><br>

<?php if ($_smarty_tpl->tpl_vars['Connected']->value){?>
    <a class="lienBlanc" href="?Page=panier">Mon panier (<span id="nombreArticle"><?php echo $_smarty_tpl->tpl_vars['panierNombre']->value;?>
</span>)</a><br>
<a class="lienBlanc" href="?Page=compte">Mon compte (<?php echo $_smarty_tpl->tpl_vars['Login']->value;?>
)</a><br>
<a class="lienBlanc" href="?Page=authentification">Déconnexion</a><br>
</p>
<?php }else{ ?>
<p>
<a class="lienBlanc" href="?Page=connexion">Connexion</a><br>
<a class="lienBlanc" href="?Page=inscription">Inscription</a>
<?php }?>
</p><?php }} ?>