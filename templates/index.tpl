
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        <meta http-equiv="Content-Language" content="fr">

        <meta name="keywords" lang="fr" content="jeu de rôle, medieval, fantasy">
        <meta name="description" content="Les contrées de Telneria - le site internet">

        <link rel="stylesheet" href="style/layout.css">
        <link rel="stylesheet" href="style/style.css">
        <link rel="stylesheet" href="style/formulaire.css">
        <link rel="stylesheet" href="style/images.css">
        <link rel="stylesheet" href="style/pagesAttributs.css">
        <link rel="stylesheet" href="style/pagesJeu.css">
        <link rel="stylesheet" href="style/pagesMonde.css">
        <link rel="stylesheet" href="style/pagesPersonnages.css">
        <link rel="stylesheet" media="screen" href="style/fonts.css" rel="stylesheet" type="text/css"/> 

        <style media="screen" type="text/css">
            /*Permet de cacher la barre de défilement horizontal tout en gardant le défilement*/
            html, body {
                padding: 0;
                margin: 0;
                overflow: hidden;
            }
            #container {
                position: absolute;
                left: 0;
                top: 0;
                right: -30px;
                bottom: 0;	
                padding-right: 15px;
                overflow-y: scroll;
            }
        </style>

        <script type="text/javascript" src="js/Jquery.js"></script>
        <title>{$nom}</title>
    </head>

    <body>
        <div id="container">
            <!--<div id="header">{ include file="header.tpl"}</div>-->
            <div id="topmenu">{include file="topmenu.tpl"}</div>

            <div id="menu">{include file="menu.tpl"}</div>
            <div id="content">{include file=$page}</div>
            <div id="footer">{include file="footer.tpl"}</div>
            <div style="font-family:'Orthoventional'; font-size:16px; padding-bottom:10px;color:white;" id="hidden">
                François Ripp : Creative Commons by-nc-sa & GPL</div>
        </div>
    </body>
</html>

