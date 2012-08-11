
{if $Connected}
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
    {section name=produit loop=$livresUtilisateur}
    <tr>
        <td>
            <a href="?Page=fiches/consulterLivre&Produit={$livresUtilisateur[produit].key}" title="{$livresUtilisateur[produit].titre}">
            {$livresUtilisateur[produit].titre}
            <a/>
        </td>
        <td>
            
            {$livresUtilisateur[produit].dateAchat}
        </td>

    </tr>
    {/section}

</table>
{/if}