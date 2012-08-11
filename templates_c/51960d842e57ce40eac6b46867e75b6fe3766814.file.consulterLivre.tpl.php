<?php /* Smarty version Smarty-3.1.7, created on 2012-08-11 15:03:31
         compiled from "templates/consulterLivre.tpl" */ ?>
<?php /*%%SmartyHeaderCode:1418278567502658236e3bb5-29571553%%*/if(!defined('SMARTY_DIR')) exit('no direct access allowed');
$_valid = $_smarty_tpl->decodeProperties(array (
  'file_dependency' => 
  array (
    '51960d842e57ce40eac6b46867e75b6fe3766814' => 
    array (
      0 => 'templates/consulterLivre.tpl',
      1 => 1343420742,
      2 => 'file',
    ),
  ),
  'nocache_hash' => '1418278567502658236e3bb5-29571553',
  'function' => 
  array (
  ),
  'variables' => 
  array (
    'Connected' => 0,
  ),
  'has_nocache_code' => false,
  'version' => 'Smarty-3.1.7',
  'unifunc' => 'content_50265823720cd',
),false); /*/%%SmartyHeaderCode%%*/?>
<?php if ($_valid && !is_callable('content_50265823720cd')) {function content_50265823720cd($_smarty_tpl) {?>
<?php if ($_smarty_tpl->tpl_vars['Connected']->value){?>
<h1>Consulter Livre</h1>

<p>Consultation d'un livre que j'ai acheté.</p>
<?php }?><?php }} ?>