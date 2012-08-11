<?php /* Smarty version Smarty-3.1.7, created on 2012-08-11 15:03:29
         compiled from "templates/livresachetes.tpl" */ ?>
<?php /*%%SmartyHeaderCode:713050804502658218efe41-22392014%%*/if(!defined('SMARTY_DIR')) exit('no direct access allowed');
$_valid = $_smarty_tpl->decodeProperties(array (
  'file_dependency' => 
  array (
    'dacb90e8d5be458e165879f8778229e6a6724ff6' => 
    array (
      0 => 'templates/livresachetes.tpl',
      1 => 1343420742,
      2 => 'file',
    ),
  ),
  'nocache_hash' => '713050804502658218efe41-22392014',
  'function' => 
  array (
  ),
  'variables' => 
  array (
    'Connected' => 0,
    'livresUtilisateur' => 0,
  ),
  'has_nocache_code' => false,
  'version' => 'Smarty-3.1.7',
  'unifunc' => 'content_50265821962bd',
),false); /*/%%SmartyHeaderCode%%*/?>
<?php if ($_valid && !is_callable('content_50265821962bd')) {function content_50265821962bd($_smarty_tpl) {?>
<?php if ($_smarty_tpl->tpl_vars['Connected']->value){?>
<h1>Mes livres</h1>

<table>
    <tr>
        <td>
            Titre du livre
        </td>
        <td>
            Acheté le
        </td>

    </tr>
    <?php if (isset($_smarty_tpl->tpl_vars['smarty']->value['section']['produit'])) unset($_smarty_tpl->tpl_vars['smarty']->value['section']['produit']);
$_smarty_tpl->tpl_vars['smarty']->value['section']['produit']['name'] = 'produit';
$_smarty_tpl->tpl_vars['smarty']->value['section']['produit']['loop'] = is_array($_loop=$_smarty_tpl->tpl_vars['livresUtilisateur']->value) ? count($_loop) : max(0, (int)$_loop); unset($_loop);
$_smarty_tpl->tpl_vars['smarty']->value['section']['produit']['show'] = true;
$_smarty_tpl->tpl_vars['smarty']->value['section']['produit']['max'] = $_smarty_tpl->tpl_vars['smarty']->value['section']['produit']['loop'];
$_smarty_tpl->tpl_vars['smarty']->value['section']['produit']['step'] = 1;
$_smarty_tpl->tpl_vars['smarty']->value['section']['produit']['start'] = $_smarty_tpl->tpl_vars['smarty']->value['section']['produit']['step'] > 0 ? 0 : $_smarty_tpl->tpl_vars['smarty']->value['section']['produit']['loop']-1;
if ($_smarty_tpl->tpl_vars['smarty']->value['section']['produit']['show']) {
    $_smarty_tpl->tpl_vars['smarty']->value['section']['produit']['total'] = $_smarty_tpl->tpl_vars['smarty']->value['section']['produit']['loop'];
    if ($_smarty_tpl->tpl_vars['smarty']->value['section']['produit']['total'] == 0)
        $_smarty_tpl->tpl_vars['smarty']->value['section']['produit']['show'] = false;
} else
    $_smarty_tpl->tpl_vars['smarty']->value['section']['produit']['total'] = 0;
if ($_smarty_tpl->tpl_vars['smarty']->value['section']['produit']['show']):

            for ($_smarty_tpl->tpl_vars['smarty']->value['section']['produit']['index'] = $_smarty_tpl->tpl_vars['smarty']->value['section']['produit']['start'], $_smarty_tpl->tpl_vars['smarty']->value['section']['produit']['iteration'] = 1;
                 $_smarty_tpl->tpl_vars['smarty']->value['section']['produit']['iteration'] <= $_smarty_tpl->tpl_vars['smarty']->value['section']['produit']['total'];
                 $_smarty_tpl->tpl_vars['smarty']->value['section']['produit']['index'] += $_smarty_tpl->tpl_vars['smarty']->value['section']['produit']['step'], $_smarty_tpl->tpl_vars['smarty']->value['section']['produit']['iteration']++):
$_smarty_tpl->tpl_vars['smarty']->value['section']['produit']['rownum'] = $_smarty_tpl->tpl_vars['smarty']->value['section']['produit']['iteration'];
$_smarty_tpl->tpl_vars['smarty']->value['section']['produit']['index_prev'] = $_smarty_tpl->tpl_vars['smarty']->value['section']['produit']['index'] - $_smarty_tpl->tpl_vars['smarty']->value['section']['produit']['step'];
$_smarty_tpl->tpl_vars['smarty']->value['section']['produit']['index_next'] = $_smarty_tpl->tpl_vars['smarty']->value['section']['produit']['index'] + $_smarty_tpl->tpl_vars['smarty']->value['section']['produit']['step'];
$_smarty_tpl->tpl_vars['smarty']->value['section']['produit']['first']      = ($_smarty_tpl->tpl_vars['smarty']->value['section']['produit']['iteration'] == 1);
$_smarty_tpl->tpl_vars['smarty']->value['section']['produit']['last']       = ($_smarty_tpl->tpl_vars['smarty']->value['section']['produit']['iteration'] == $_smarty_tpl->tpl_vars['smarty']->value['section']['produit']['total']);
?>
    <tr>
        <td>
            <a href="?Page=consulterLivre&Produit=<?php echo $_smarty_tpl->tpl_vars['livresUtilisateur']->value[$_smarty_tpl->getVariable('smarty')->value['section']['produit']['index']]['key'];?>
" title="<?php echo $_smarty_tpl->tpl_vars['livresUtilisateur']->value[$_smarty_tpl->getVariable('smarty')->value['section']['produit']['index']]['titre'];?>
">
            <?php echo $_smarty_tpl->tpl_vars['livresUtilisateur']->value[$_smarty_tpl->getVariable('smarty')->value['section']['produit']['index']]['titre'];?>

            <a/>
        </td>
        <td>
            
            <?php echo $_smarty_tpl->tpl_vars['livresUtilisateur']->value[$_smarty_tpl->getVariable('smarty')->value['section']['produit']['index']]['dateAchat'];?>

        </td>

    </tr>
    <?php endfor; endif; ?>

</table>
<?php }?><?php }} ?>