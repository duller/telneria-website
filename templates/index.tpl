
<!DOCTYPE html>
<html>
   <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        <meta http-equiv="Content-Language" content="fr">

        <meta name="keywords" lang="fr" content="livre,librairie,magasin">
        <meta name="description" content="Librairie de l'Ours - La librairie en ligne !">
        
        <link href="style.css" rel="stylesheet" type="text/css">
        
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
        <div id="hidden">François Ripp : Creative Commons by-nc-sa<br>
    </body>
</html>

