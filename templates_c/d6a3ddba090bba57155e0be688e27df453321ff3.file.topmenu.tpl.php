<?php /* Smarty version Smarty-3.1.7, created on 2012-07-27 22:49:59
         compiled from "templates/topmenu.tpl" */ ?>
<?php /*%%SmartyHeaderCode:16990045024fa149d2ec43f0-92519548%%*/if(!defined('SMARTY_DIR')) exit('no direct access allowed');
$_valid = $_smarty_tpl->decodeProperties(array (
  'file_dependency' => 
  array (
    'd6a3ddba090bba57155e0be688e27df453321ff3' => 
    array (
      0 => 'templates/topmenu.tpl',
      1 => 1343420742,
      2 => 'file',
    ),
  ),
  'nocache_hash' => '16990045024fa149d2ec43f0-92519548',
  'function' => 
  array (
  ),
  'version' => 'Smarty-3.1.7',
  'unifunc' => 'content_4fa149d2ec79b',
  'has_nocache_code' => false,
),false); /*/%%SmartyHeaderCode%%*/?>
<?php if ($_valid && !is_callable('content_4fa149d2ec79b')) {function content_4fa149d2ec79b($_smarty_tpl) {?>

<form action="?Page=recherche" method="POST">
    <label for="tb_recherche">Recherche</label>
    <select>
        <option value="tous">Tous les livres</option>
        <option value="poche">Livres de poche</option>
        <option value="broche">Livres brochés</option>
        <option value="relie">Livres reliés</option>
    </select>
    <input id="tb_recherche" type="text">
    <input onclick="alert('Non implementé')" type="submit">
</form><?php }} ?>