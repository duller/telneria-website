
<!DOCTYPE html>
<html>
   <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        <meta http-equiv="Content-Language" content="fr">

        <meta name="keywords" lang="fr" content="jeu de rôle, medieval, fantasy">
        <meta name="description" content="Les légendes de Telneria - le site internet">
                
        <link rel="stylesheet" href="style/layout.css">
        <link rel="stylesheet" href="style/style.css">
        <link rel="stylesheet" href="style/formulaire.css">
        <script type="text/javascript" src="js/Jquery.js"></script>
        <title>{$nom}</title>
        <link rel="stylesheet" media="screen" href="style/fonts.css" rel="stylesheet" type="text/css"/> 
    </head>

    <body>
        <!--<div id="header">{ include file="header.tpl"}</div>-->
        <div id="topmenu">{include file="topmenu.tpl"}</div>
        <div id="menu">{include file="menu.tpl"}</div>
        <div id="content">{include file=$page}</div>
    	<div id="footer">{include file="footer.tpl"}</div>
        <div style="font-family: 'Orthoventional'; font-size:16px;padding-bottom: 10px;"id="hidden">
            François Ripp : Creative Commons by-nc-sa & GPL</div>
    </body>
</html>

