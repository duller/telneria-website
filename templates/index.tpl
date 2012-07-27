<!-- David Winckel -->

<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
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
        <div id="hidden">©David WINCKEL et François RIPP<br><a href="http://validator.w3.org/check?uri=referer"><img
      src="http://www.w3.org/Icons/valid-html401" alt="Valid HTML 4.01 Transitional" height="31" width="88"></a></div>
    </body>
</html>

