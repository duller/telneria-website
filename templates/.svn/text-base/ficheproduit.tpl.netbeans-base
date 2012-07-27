<!-- David Winckel et François Ripp -->

{literal}
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
{/literal}

<h1>Fiche produit</h1>

<p>{$nomProduit}</p>

<p><img src="{$imageProduit}"></p>

<p>Prix : {$prixProduit} €</p>

{if $Connected}
<p><a href="#" onclick="ajoutPanier('{$nomProduit}')">Ajout au panier</a></p>
{/if}