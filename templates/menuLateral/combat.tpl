{literal}
    <script type="text/javascript">

    $(function ()
    {
    
        $("h2").prepend("<span> - </span>").click(function()
        {
            var next = $(this).next();
            if(next.css("display") != "none")
            {
                $(next).hide(300);
                $("span", this).html(" + ");
            }
            else
            {
                $(next).show(500);
                $("span", this).html(" - ");
            }
        
        }).css("cursor", "url('ressources/curseurs/GantPointe32.png'), auto");
        
        $("#show").click(function()
        {
            $("h2").next().show(500);
            $("h2 span").html(" - ");
        });
       
        $("#hide").click(function()
        {
            $("h2").next().hide(300);
            $("h2 span").html(" + ");
        });
        
    });

    </script>
{/literal}

<h1 style ="margin-top:70px;">Le combat</h1>

<p style="font-style: italic;">Cliquez sur les titres pour dérouler le contenu. Vous pouvez également tout 
    <a href="#" id="show">dérouler</a> ou tout <a href="#" id="hide">
        <!--<a href="javascript:hideAll();"-->cacher.</a></p>
        <br />
        <p><span class="titreDebutLigne">Points de vie et de mana</span> : 
            Hors combat, les points de vie et de mana sont regagnés par les personnages-joueurs au rythme de [niveau] points par heure.</p>


<div style="max-width:1600px;">

    <div class="divZoneCombatTitre"  style="max-width: 100%;">
        <h2 class="titreCombat">Initiative et actions</h2>
        <div id="divInitiative" class="divPageCombat" style="max-width: 100%;">
            
            <div class="div40" style="float:right;">
                <img class="communImages imageCombatJetToucher" src="ressources/14-Combat/fuite.png" title="Illustration : François Ripp">
            </div>
            
            <div class="div60">
                <div class="divMoitieGauche">
                    <h3 class="h3region">Initiative</h3>
                    <img class="communImages imageCombatInitiative" src="ressources/14-Combat/fleche-droite.png" title="Illustration : Lorc, Open Game Art" style="border-radius: 0;">
                    <p>Au début de chaque combat, le maître du jeu décide qui des joueurs ou des monstres a l'initiative.</p>
                    <p>Lorsqu'aucun des camps n'a clairement l'avantage de la surprise, un jet de dé permet de prendre la décision de manière impartiale.</p>
                </div>
                <div class="divMoitieGauche">
                    <h3 class="h3region">Tour de jeu</h3>
                    <img class="communImages imageCombatInitiative" src="ressources/14-Combat/cycle.png" title="Illustration : Lorc, Open Game Art">
                    <p>Un tour de jeu est écoulé lorsque tous les protagonistes ont accompli leur action, s'ils ne sont pas évanouis ou décédés.</p>
                    <p>Le maître du jeu peut modifier le tour de jeu en faisant intervenir un protagoniste, il peut faire un jet d'initiative pour le nouvel arrivant.</p>
                </div>
                    
            </div>
                
            <div class="div60">
                <div class="divMoitieGauche">
                    <h3 class="h3region">Actions</h3>
                    <p>Les joueurs, ainsi que les monstres et pnj joués par le MJ, peuvent faire une action complète par tour.</p>
                    <br />
                    <p>Sont considérées comme des actions complètes :</p>
                    <ul>
                        <li>Se déplacer de 10m</li>
                        <li>Utiliser une compétence</li>
                        <li>Attaque simple</li>
                        <li>Lancer un sort / Utiliser une technique</li>
                        <li>Charger : jet d'équilibre, suivi d'un jet de toucher avec un malus de 2.</li>
                        <li>Faire un jet de premiers secours.</li>
                    </ul>
                </div>
                <div class="divMoitieGauche">
                    <h3 class="h3region">Demi-actions</h3>
                    <p>Le joueur peut également effectuer plusieurs actions pendant un tour si elles ne sont pas complètes.</p><br />
                    <p>Sont considérés comme des demi-actions :</p>
                    <ul>
                        <li>Utiliser un don</li>
                        <li>Sortir son arme ou en changer</li>
                        <li>Se déplacer de 5m</li>
                        <li>Se mettre en position de défense, ce qui donne +1 à l'EP (esquive physique).</li>
                        <li>Se concentrer spirituellement, ce qui donne +1 à l'EM (esquive magique).</li>
                        <li>Se mettre en position d'attaque, ce qui donne +1 au prochain jet de toucher.</li>
                    </ul>
                </div>
            </div>
            
            
                
        </div>
    </div>



    <div class="divZoneCombatTitre">
        <h2 class="titreCombat">Les attaques et les jets de toucher</h2>
        <div id="divAttaque" class="divPageCombat">

            <div class="div30">
                <h3 class="h3region">Jet de toucher</h3>
                <img class="communImages imageCombatInitiative" src="ressources/14-Combat/diving-dagger.png" title="Illustration : Lorc, Open Game Art" style="border-radius: 20px 0 0 0 ;">
                <p>Lorsqu'un protagoniste attaque un ennemi, il jette un dé 20 de toucher pour savoir si son attaque est un succès ou un échec. 
                    Selon le type d'attaque, une caractéristique différente est utilisée pour pondérer le jet.</p>
                <ul>
                    <li>Corps-à-corps (attaque simple & technique) : Force</li>
                    <li>Distance (attaque simple & technique) : Habileté</li>
                    <li>Sort offensif : Intelligence</li>
                    <li>Sort de soin & défensif : Volonté</li>
                </ul>
                <p>Une réussite critique peut être obtenue lorsque le score au dé est de 20, ce qui se traduit par une réussite assurée et un doublement de l'effet.</p>
                <p>Un échec critique est obtenu lorsque le score au dé est de 1, c'est nécessairement un échec ayant des conséquences néfastes.</p>

            </div>

            <div class="div40">
                <img class="communImages imageCombatJetToucher" src="ressources/14-Combat/combat.png" title="Illustration : François Ripp">
            </div>

            <div class="div30">
                <h3 class="h3region">Sorts et techniques</h3>
                <img class="communImages imageCombatInitiative" style="float:right;margin:0 0 0 10px;" src="ressources/14-Combat/dripping-goo.png" title="Illustration : Lorc, Open Game Art">
                <p>Les sorts et techniques sont détaillés pour chacune des classes de personnages. Ils ont un coût en mana défini auquel s'ajoute le niveau du personnage.</p>
                <p>Les sorts de soins et défensifs ne peuvent pas être esquivés, leur réussite est déterminée par le score du jet au dé 20, pondéré par le modificateur de volonté :</p>
                <ul>
                    <li>Score de 20 (au dé) : réussite critique, effet du soin doublé</li>
                    <li>Score entre 10 et 19 : réussite, effet normal</li>
                    <li>Score entre 5 et 9 : réussite partielle, effet diminué de moitié (arrondi au supérieur)</li>
                    <li>Score entre 1 et 4 : échec, effet nul</li>
                    <li>Score de 1 (au dé) : échec critique, le soigneur subit 1+niveau points de dégâts</li>
                </ul>
            </div>


        </div>
    </div>



    <div class="divZoneCombatTitre">
        <h2 class="titreCombat">Modificateurs de toucher : esquive physique (EP) et esquive magique (EM)</h2>
        <div id="divModificateurs" class="divPageCombat">
            <div class="divMoitieGauche">
                <h3 class="h3region">Attaques physiques (mêlée et distance)</h3>
                <img class="communImages imageCombatModificateurs" src="ressources/14-Combat/hammer-drop.png" title="Illustration : Lorc, Open Game Art">
                <p>Pour déterminer le succès d'une attaque physique, il faut comparer le jet de toucher avec l'esquive physique de la cible. 
                    Si le résultat est supérieur ou égal, l'attaque touche et les dégâts infligés sont déterminés en fonction de l'arme utilisée.</p>
                <p>L'esquive physique est déterminée à partir de l'esquive physique de base, qui est de 10, des éventuelles pièces d'armure, de l'habileté et du modificateur de taille.</p>
            </div>
            <div class="divMoitieDroite">
                <h3 class="h3region">Attaques magiques (30 mètres de portée)</h3>
                <img class="communImages imageCombatModificateurs" src="ressources/14-Combat/unfriendly-fire.png" title="Illustration : Lorc, Open Game Art">
                <p>Pour déterminer le succès d'une attaque magique, il faut comparer le jet de toucher avec l'esquive magique de la cible. 
                    Si le résultat est supérieur ou égal, l'attaque touche et les dégâts infligés sont déterminés par le sort utilisé.</p>
                <p>L'esquive magique est déterminée à partir de l'esquive magique de base, qui est de 10, des éventuelles pièces d'armures magiques, de la prestance et du modificateur de taille.</p>
                <p>Les classes magiques les plus puissantes, à savoir clerc, sorcier, magicien et druide, ont un bonus de +1 à l'esquive magique.</p>
            </div>
            <div style="text-align:center;">
                <div style="display:inline-block;">
                    <h4 style="box-shadow: none;">Tableau du modificateur de taille :</h4>
                    <table>
                        <tr>
                            <td style="height: 30px">
                                <p class="ptabstrong">Taille</p>
                            </td>
                            <td>
                                <p class="ptab">Infime</p>
                            </td>
                            <td>
                                <p class="ptab">Minuscule</p>
                            </td>
                            <td>
                                <p class="ptab">Petit</p>
                            </td>
                            <td>
                                <p class="ptab">Moyen</p>
                            </td>
                            <td>
                                <p class="ptab">Grand</p>
                            </td>
                            <td>
                                <p class="ptab">Énorme</p>
                            </td>
                            <td>
                                <p class="ptab">Gigantesque</p>
                            </td>
                            <td>
                                <p class="ptab">Colossal</p>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <p class="ptabstrong">Modificateur</p>
                            </td>
                            <td>
                                <p class="ptab">+3</p>
                            </td>
                            <td>
                                <p class="ptab">+2</p>
                            </td>
                            <td>
                                <p class="ptab">+1</p>
                            </td>
                            <td>
                                <p class="ptab">0</p>
                            </td>
                            <td>
                                <p class="ptab">-1</p>
                            </td>
                            <td>
                                <p class="ptab">-2</p>
                            </td>
                            <td>
                                <p class="ptab">-3</p>
                            </td>
                            <td>
                                <p class="ptab">-4</p>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <p class="ptabstrong">Échelle</p>
                            </td>
                            <td>
                                <p class="ptab">< 10 cm</p>
                            </td>
                            <td>
                                <p class="ptab">10 cm - 50 cm</p>
                            </td>
                            <td>
                                <p class="ptab">50 cm - 1 m</p>
                            </td>
                            <td>
                                <p class="ptab">1 m - 2 m</p>
                            </td>
                            <td>
                                <p class="ptab">2 m - 3 m</p>
                            </td>
                            <td>
                                <p class="ptab">3 m - 5 m</p>
                            </td>
                            <td>
                                <p class="ptab">5 m - 10 m</p>
                            </td>
                            <td>
                                <p class="ptab">> 10 m</p>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <p class="ptabstrong">Exemple</p>
                            </td>
                            <td>
                                <p class="ptab">Rat</p>
                            </td>
                            <td>
                                <p class="ptab">Faucon</p>
                            </td>
                            <td>
                                <p class="ptab">Gobelin</p>
                            </td>
                            <td>
                                <p class="ptab">Elfe</p>
                            </td>
                            <td>
                                <p class="ptab">Varelias</p>
                            </td>
                            <td>
                                <p class="ptab">Ogre </p>
                            </td>
                            <td>
                                <p class="ptab">Ancien Troll des collines</p>
                            </td>
                            <td>
                                <p class="ptab">Dragon vénérable</p>
                            </td>
                        </tr>
                        
                    </table>
                </div>
            </div>
            
            <div class="divMoitieGauche">
                <h3 class="h3region">Attaques et sorts de zone</h3>
                <img class="communImages imageCombatModificateurs" src="ressources/14-Combat/arrow-flights.png" title="Illustration : Lorc, Open Game Art">
                <p>Pour déterminer le succès d'une attaque ou d'un sort de zone, le fonctionnement est le même que pour les attaques simples et seul un jet de dé est effectué.</p>
                <p>Pour chaque monstre ou joueur visé, si le jet est supérieur à leur EP ou EM, ce protagoniste est affecté par l'effet.</p>
            </div>
            
            <div class="divMoitieDroite">
                <h3 class="h3region">Dégâts infligés</h3>
                <img class="communImages imageCombatModificateurs" src="ressources/14-Combat/broken-bone.png" title="Illustration : Lorc, Open Game Art">
                <p>Lorsqu'une attaque est un succès, les dégâts infligés sont ceux du sort lancé ou de l'arme utilisée. 
                    À ces dégâts, il convient d'ajouter le niveau du joueur pour les attaques simples. 
                    Pour les sorts et les attaques spéciales, les dégâts sont spécifiés sur la fiche de classe du personnage.</p>
                <p>Dans le cas d'une attaque simple, il est également possible de frapper à mains nues, les dégâts infligés sont alors de 1d1 plus le niveau.</p>
            </div>

        </div>
    </div>


    <div class="divZoneCombatTitre">
        <h2 class="titreCombat">Incapacités et mort</h2>
        <div id="divIncapacite" class="divPageCombat">
            <div class="divEtroite">
                <img class="communImages imageCrane" style="box-shadow:none;" src="ressources/14-Combat/crane.png" title="Illustration : François Ripp">
                <h3 class="h3region" style="margin-right:180px;">Mise hors de combat</h3>
                <p>Lorsqu'un joueur ou un monstre voit ses points de vie atteindre 0, il devient inconscient et ne peut plus mener d'actions. Il perd ensuite 1 point de vie par tour.
                    Si les points de vie d'un joueur atteignent -10, l'intéressé est mort et ni la fin du combat ni des soins d'un autre joueur ne peuvent rétablir la victime.</p>
                <p>Pour ramener un personnage à la vie, il faut utiliser un sort de résurrection ou trouver un PNJ capable de le faire.</p>
            </div>
            <div class="divMoitieGauche">
                <h3 class="h3region">Regagner conscience : jet de Dernier espoir</h3>
                <img class="communImages imageCombatModificateurs" src="ressources/14-Combat/back-pain.png" title="Illustration : Lorc, Open Game Art">
                <p>Lorsqu'un joueur voit ses points de vie descendre sous la barre des 1 points de vie, il perd conscience et ne peut plus effectuer d'action. 
                    Cependant, à chaque tour, il peut tenter de regagner conscience avec un jet de Dernier espoir.</p>
                <p>Un jet de Dernier espoir nécessite de faire 10 avec 1d20, si tel est le cas, le joueur peut alors effectuer une action pour ce tour. 
                    Regagner conscience ne soigne pas des dégâts subis, ce qui résulte en une perte de conscience une fois l'action effectuée.</p>
                <p>Ce regain de conscience peut être tenté à chaque début de tour pour le personnage en question.</p>
            </div>
            <div class="divMoitieDroite">
                <h3 class="h3region">Récupération des blessures : jet de Premiers secours</h3>
                <img class="communImages imageCombatModificateurs" src="ressources/14-Combat/cut-palm.png" title="Illustration : Lorc, Open Game Art">
                <p>Les points de vie peuvent être regagnés par les sorts de soins, les potions de vie ou les premiers secours. 
                    Les premiers secours permettent à un joueur de porter assitance à un coéquipier évanoui afin qu'il reprenne le combat.
                <p>Un dé à 20 faces est lancé, si le jet atteint moins de 5, les premiers secours échouent. 
                    Si le jet atteint entre 5 et 9, la victime se relève mais s'écroule à nouveau une fois son action effectuée. 
                    Si le jet est au moins de 10, la victime regagne 5pv et peut effectuer une action. 
                    Si les 5pv ne ramènent pas à au moins 1pv, le joueur s'écroule également une fois l'action effectuée.</p>
                <p>Un échec critique achève le joueur, tandis qu'une réussite critique soigne le joueur pour 10pv.</p>
            </div>
        </div>
    </div>


    <div class="divZoneCombatTitre">
        <h2 class="titreCombat">Le Telnas</h2>
        <div id="divTelnas" class="divPageCombat divEtroite">
            <img class="communImages imageCombatTelnas" src="ressources/14-Combat/telnas.jpg" title="Illustration : François Ripp" style="margin-top:-30px;">
            <p>Le Telnas est la matérialisation physique d'une forme très pure de magie des arcanes.</p>
            <p>Elle permet au joueur d'invoquer une épaisse fumée bleue qu'il peut contrôler à sa guise.</p>
            <p>Voici quelques exemples de l'utilisation du Telnas par ordre de difficulté :</p>
            <ul>
                <li>Matérialisation d'une clé pour ouvrir une serrure que le crochetage n'a pas permis de forcer.</li>
                <li>Matérialisation d'une épée infligeant des dégâts magiques aux spectres ou aux élémentaires.</li>
                <li>Matérialisation d'une sphère de protection autour du groupe de joueur.</li>
            </ul>

            <br />

            <p>Lors de l'utilisation du Telnas, le joueur décrit en détails ce qu'il essaye de faire. Le MJ estime ensuite le score
                nécessaire au dé 20 pour réussir l'action, ce score est ensuite pondéré par le niveau de maîtrise du Telnas du joueur.</p>

        </div>

    </div>

</div>