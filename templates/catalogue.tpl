
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
    {section name=produit loop=$catalogueProduit}
    <tr>
        <td>
            <a href="?Page=ficheproduit&amp;Produit={$catalogueProduit[produit].key}" title="{$catalogueProduit[produit].titre}">
            {$catalogueProduit[produit].titre}
            </a>
        </td>
        <td>
            
            {$catalogueProduit[produit].prix} €
        </td>

    </tr>
    {/section}

</table>