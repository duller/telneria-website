<?php /* Smarty version Smarty-3.1.7, created on 2012-07-27 22:00:17
         compiled from "templates/ficheproduit.tpl" */ ?>
<?php /*%%SmartyHeaderCode:10616099545012f351346c70-68666418%%*/if(!defined('SMARTY_DIR')) exit('no direct access allowed');
$_valid = $_smarty_tpl->decodeProperties(array (
  'file_dependency' => 
  array (
    'b6b1e98dadaaeda8761a581d497fc282d1106a41' => 
    array (
      0 => 'templates/ficheproduit.tpl',
      1 => 1335968946,
      2 => 'file',
    ),
  ),
  'nocache_hash' => '10616099545012f351346c70-68666418',
  'function' => 
  array (
  ),
  'variables' => 
  array (
    'nomProduit' => 0,
    'imageProduit' => 0,
    'prixProduit' => 0,
    'Connected' => 0,
  ),
  'has_nocache_code' => false,
  'version' => 'Smarty-3.1.7',
  'unifunc' => 'content_5012f3513adc1',
),false); /*/%%SmartyHeaderCode%%*/?>
<?php if ($_valid && !is_callable('content_5012f3513adc1')) {function content_5012f3513adc1($_smarty_tpl) {?>﻿<!-- David Winckel et François Ripp -->


<script type="text/javascript">

function ajoutPanier(panier)
{
    $.ajax(
        {
            type: "POST",
            url: "ajax.php",
            data: { name: panier}
        }
        ).done(function( json ) 
        {
            if (json != "")
            {
                var panier = eval('(' + json + ')');

                var objCount=0;
                for(_obj in panier) objCount++;
                
                if (objCount > 1)
                    $("#nombreArticle").text(objCount + " articles");
                else
                    $("#nombreArticle").text(objCount +" article");
                    
                    
                alert("Nouveau produit ajouté au panier");
            }
            else
            {
                alert("Ajout au panier impossible");

            }
        });
}

</script>


<h1>Fiche produit</h1>

<p><?php echo $_smarty_tpl->tpl_vars['nomProduit']->value;?>
</p>

<p><img src="<?php echo $_smarty_tpl->tpl_vars['imageProduit']->value;?>
"></p>

<p>Prix : <?php echo $_smarty_tpl->tpl_vars['prixProduit']->value;?>
 €</p>

<?php if ($_smarty_tpl->tpl_vars['Connected']->value){?>
<p><a href="#" onclick="ajoutPanier('<?php echo $_smarty_tpl->tpl_vars['nomProduit']->value;?>
')">Ajout au panier</a></p>
<?php }?><?php }} ?>