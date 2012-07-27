<!-- David WINCKEL & François Ripp-->

<h1>Authentification</h1>

{if $connexion eq "connexionreussi"}
<p>Connexion en cours...</p>

{literal}
<script language="javascript">

setTimeout ("redirection()", 1000 ); 

function redirection()
{
    document.location.href="?Page=accueil"
}
</script>
{/literal}
{elseif $connexion eq "deconnexionreussi"}
<p>Déconnexion en cours...</p>

{literal}
<script language="javascript">

setTimeout ("redirection()", 1000 ); 

function redirection()
{
    document.location.href="?Page=accueil"
}
</script>
{/literal}
{else}
<p>La combinaison login/mot de passe est incorrecte</p>

<script language="javascript">

setTimeout ("redirection()", 3000 ); 

{literal}
function redirection()
{
    document.location.href="?Page=connexion"
}
</script>
{/literal}
{/if}
