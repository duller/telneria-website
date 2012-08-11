<?php /* Smarty version Smarty-3.1.7, created on 2012-08-11 15:03:11
         compiled from "templates/authentification.tpl" */ ?>
<?php /*%%SmartyHeaderCode:11427686675026580f9ff707-99196406%%*/if(!defined('SMARTY_DIR')) exit('no direct access allowed');
$_valid = $_smarty_tpl->decodeProperties(array (
  'file_dependency' => 
  array (
    'c7494ec7fc490b2ceb55c9f347e9381f7490fb44' => 
    array (
      0 => 'templates/authentification.tpl',
      1 => 1344689879,
      2 => 'file',
    ),
  ),
  'nocache_hash' => '11427686675026580f9ff707-99196406',
  'function' => 
  array (
  ),
  'variables' => 
  array (
    'connexion' => 0,
  ),
  'has_nocache_code' => false,
  'version' => 'Smarty-3.1.7',
  'unifunc' => 'content_5026580fa4fe8',
),false); /*/%%SmartyHeaderCode%%*/?>
<?php if ($_valid && !is_callable('content_5026580fa4fe8')) {function content_5026580fa4fe8($_smarty_tpl) {?>

<h1>Authentification</h1>

<?php if ($_smarty_tpl->tpl_vars['connexion']->value=="connexionreussie"){?>
<p>Connexion en cours...</p>


<script language="javascript">

setTimeout ("redirection()", 1000 ); 

function redirection()
{
    document.location.href="?Page=accueil"
}
</script>

<?php }elseif($_smarty_tpl->tpl_vars['connexion']->value=="deconnexionreussie"){?>
<p>Déconnexion en cours...</p>


<script language="javascript">

setTimeout ("redirection()", 1000 ); 

function redirection()
{
    document.location.href="?Page=accueil"
}
</script>

<?php }else{ ?>
<p>La combinaison login/mot de passe est incorrecte</p>

<script language="javascript">

setTimeout ("redirection()", 3000 ); 


function redirection()
{
    document.location.href="?Page=connexion"
}
</script>

<?php }?>
<?php }} ?>