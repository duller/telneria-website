
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

        <script type="text/javascript" src="js/Jquery.js"></script>
        <title>{$nom}</title>
    </head>

    <body>

        {literal}
            <script type="text/javascript">

            $(function ()
            {
                setHauteurClasses();
                    
                $( window ).resize(function() {
                    setHauteurClasses();
                });
        
                function setHauteurClasses()
                {
                    setHauteurDiv($("#idVoieMagie"), $("#idVoieFoi"), false);
                    setHauteurDiv($("#idVoieNature"), $("#idVoieDiscretion"), $("#idVoieGuerre"));
                    setHauteurDiv($("#idPrestige1"), $("#idPrestige2"), false);
                    setHauteurDiv($("#idAlignementLoyal"), $("#idAlignementBon"), false);
                    setHauteurDiv($("#idAlignementNeutreEthique"), $("#idAlignementChaotique"), false);
                    setHauteurDiv($("#idAlignementChaotique"), $("#idAlignementMauvais"), false);
                    setHauteurDiv($("#idDon01"), $("#idDon02"), $("#idDon03"));
                    setHauteurDiv($("#idDon11"), $("#idDon21"), $("#idDon31"));
                    setHauteurDiv($("#idDon12"), $("#idDon22"), $("#idDon32"));
                    setHauteurDiv($("#idDon13"), $("#idDon23"), $("#idDon33"));
                    setHauteurDiv($("#idForce"), $("#idIntel"), false);
                    setHauteurDiv($("#idHabil"), $("#idVolonte"), false);
                    setHauteurDiv($("#idVigueur"), $("#idPrestance"), false);
                    //setHauteurDiv($("#idPrepGauche"), $("#idPrepDroite"), false);
                    //setHauteurDiv($("#idExpGauche"), $("#idExpDroite"), false);
                }
                    
                function setHauteurDiv(gauche, milieu, droite)
                {
                    if (!gauche.length)
                    {
                        return;
                    }

                    gauche.css('height','auto');
                    milieu.css('height','auto');
                    if (droite)
                    {
                        droite.css('height','auto');
                    }                
                    var maxH = 0;
                    if (gauche.height() > maxH)
                    {
                        maxH = gauche.height();
                    }
                    if (milieu.height() > maxH)
                    {
                        maxH = milieu.height();
                    }
                    if (droite && droite.height() > maxH)
                    {
                        maxH = droite.height();
                    }
                        
                    gauche.height(maxH);
                    milieu.height(maxH);
                    if (droite)
                    {
                        droite.height(maxH);
                    }
                }
            });

            </script>
        {/literal}

        <div id="container">
            <!--<div id="header">{ include file="header.tpl"}</div>-->
            <div id="topmenu">{include file="topmenu.tpl"}</div>

            <div id="menu">{include file="menu.tpl"}</div>
            <div id="content">{include file=$page}</div>
            <div id="footer">{include file="footer.tpl"}</div>
            <div style="font-family:'Orthoventional'; font-size:16px; padding-bottom:10px;color:white;" id="hidden" class="lienBlanc">
                François Ripp : Creative Commons by-nc-sa & GPL</div>
        </div>
    </body>
</html>

