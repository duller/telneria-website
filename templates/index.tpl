
<!DOCTYPE html>
<html>
   <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        <meta http-equiv="Content-Language" content="fr">

        <meta name="keywords" lang="fr" content="jeu de rôle, medieval, fantasy">
        <meta name="description" content="Les légendes de Telnaria - le site internet">
                
        <link rel="stylesheet" href="style/layout.css">
        <link rel="stylesheet" href="style/style.css">
        <link rel="stylesheet" href="style/formulaire.css">
        <script type="text/javascript" src="js/Jquery.js"></script>
        <title>{$nom}</title>
    </head>

    <body>
        <div id="header">{include file="header.tpl"}</div>
        <div id="topmenu">{include file="topmenu.tpl"}</div>
        <div id="menu">{include file="menu.tpl"}</div>
        <div id="content">{include file=$page}</div>
    	<div id="footer">{include file="footer.tpl"}</div>
        <div id="hidden">François Ripp, Jérôme Rotfarb : Creative Commons by-nc-sa & GPL V3</div>
    </body>
</html>

