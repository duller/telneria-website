<!-- David WINCKEL -->
{if $Connected}
<h1>Panier</h1>

{literal}
<script type="text/javascript">

function viderPanier()
{
    $.ajax(
        {
            type: "POST",
            url: "ajax.php",
            data: { name: ""}
        }
        ).done(function( json ) 
        {
            if (json != "")
            {
                $("#listePanier").text("");
                alert("Panier vide");
            }
            else
            {
                alert("Impossible de vider le panier");
                
            }           
        });
}

</script>
{/literal}

<p><a href="#" onclick="viderPanier()">Vider le panier</a></p>

<table>
    <tr>
        <td>
            Titre du livre
        </td>

    </tr>
    {section name=id loop=$panier}
    <tr>
        <td id="listePanier">
            {$panier[id].nom}
        </td>

    </tr>
    {/section}

</table>
{/if}