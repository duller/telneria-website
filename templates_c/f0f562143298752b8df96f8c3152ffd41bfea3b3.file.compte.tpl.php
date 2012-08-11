<?php /* Smarty version Smarty-3.1.7, created on 2012-08-11 15:03:21
         compiled from "templates/compte.tpl" */ ?>
<?php /*%%SmartyHeaderCode:182817631950265819c715e7-27847386%%*/if(!defined('SMARTY_DIR')) exit('no direct access allowed');
$_valid = $_smarty_tpl->decodeProperties(array (
  'file_dependency' => 
  array (
    'f0f562143298752b8df96f8c3152ffd41bfea3b3' => 
    array (
      0 => 'templates/compte.tpl',
      1 => 1343420742,
      2 => 'file',
    ),
  ),
  'nocache_hash' => '182817631950265819c715e7-27847386',
  'function' => 
  array (
  ),
  'variables' => 
  array (
    'Connected' => 0,
  ),
  'has_nocache_code' => false,
  'version' => 'Smarty-3.1.7',
  'unifunc' => 'content_50265819cafc4',
),false); /*/%%SmartyHeaderCode%%*/?>
<?php if ($_valid && !is_callable('content_50265819cafc4')) {function content_50265819cafc4($_smarty_tpl) {?>
<?php if ($_smarty_tpl->tpl_vars['Connected']->value){?>
<h1>Compte</h1>

<p> Mon compte : les informations personnelles de l'utilisateur connecté</p>

<p><a href="?Page=livresachetes&sansPrix">Mes livres achetés</a></p>
<?php }?><?php }} ?>