<?php /* Smarty version Smarty-3.1.7, created on 2012-07-27 22:00:15
         compiled from "templates/catalogue.tpl" */ ?>
<?php /*%%SmartyHeaderCode:19509529955012f34f8bfcd5-12933748%%*/if(!defined('SMARTY_DIR')) exit('no direct access allowed');
$_valid = $_smarty_tpl->decodeProperties(array (
  'file_dependency' => 
  array (
    '7a9a7377a24016027656bbab53448d4d51d832e3' => 
    array (
      0 => 'templates/catalogue.tpl',
      1 => 1335967010,
      2 => 'file',
    ),
  ),
  'nocache_hash' => '19509529955012f34f8bfcd5-12933748',
  'function' => 
  array (
  ),
  'variables' => 
  array (
    'catalogueProduit' => 0,
  ),
  'has_nocache_code' => false,
  'version' => 'Smarty-3.1.7',
  'unifunc' => 'content_5012f34f95acc',
),false); /*/%%SmartyHeaderCode%%*/?>
<?php if ($_valid && !is_callable('content_5012f34f95acc')) {function content_5012f34f95acc($_smarty_tpl) {?>﻿<!-- David Winckel et François Ripp -->
<h1>Catalogue</h1>

<table>
    <tr>
        <td>
            Titre du livre
        </td>
        <td>
            Prix
        </td>

    </tr>
    <?php if (isset($_smarty_tpl->tpl_vars['smarty']->value['section']['produit'])) unset($_smarty_tpl->tpl_vars['smarty']->value['section']['produit']);
$_smarty_tpl->tpl_vars['smarty']->value['section']['produit']['name'] = 'produit';
$_smarty_tpl->tpl_vars['smarty']->value['section']['produit']['loop'] = is_array($_loop=$_smarty_tpl->tpl_vars['catalogueProduit']->value) ? count($_loop) : max(0, (int)$_loop); unset($_loop);
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
            <a href="?Page=ficheproduit&amp;Produit=<?php echo $_smarty_tpl->tpl_vars['catalogueProduit']->value[$_smarty_tpl->getVariable('smarty')->value['section']['produit']['index']]['key'];?>
" title="<?php echo $_smarty_tpl->tpl_vars['catalogueProduit']->value[$_smarty_tpl->getVariable('smarty')->value['section']['produit']['index']]['titre'];?>
">
            <?php echo $_smarty_tpl->tpl_vars['catalogueProduit']->value[$_smarty_tpl->getVariable('smarty')->value['section']['produit']['index']]['titre'];?>

            </a>
        </td>
        <td>
            
            <?php echo $_smarty_tpl->tpl_vars['catalogueProduit']->value[$_smarty_tpl->getVariable('smarty')->value['section']['produit']['index']]['prix'];?>
 €
        </td>

    </tr>
    <?php endfor; endif; ?>

</table><?php }} ?>