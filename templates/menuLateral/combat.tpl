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

<h1>Le combat</h1>

<p>Cliquez sur les titres pour dérouler le contenu. Vous pouvez également tout 
    <a href="#" id="show">dérouler</a> ou tout <a href="#" id="hide">
        <!--<a href="javascript:hideAll();"-->cacher.</a></p>


<div style="max-width:1600px;">

    <div class="divZoneCombatTitre">
        <h2 class="titreCombat">Initiative et actions</h2>
        <div id="divInitiative" class="divPageCombat">

            <div class="div30">
                <h3>Initiative</h3>
                <p>Au début de chaque combat, tous les protagonistes font un jet d'initiative pour déterminer l'ordre de jeu. Ce jet est modifié par la dextérité.</p>
                <p>L'initiative peut être modifié négativement si un protagoniste est pris par surprise ou est affairé à autre chose, c'est au MJ de le décider.</p>


                <h3>Actions</h3>
                <p>Les joueurs, ainsi que les monstres et pnj joués par le MJ, ont le choix entre plusieurs actions, qui sont complètes ou non.</p>
                <br />
                <p>Sont considérées comme des actions complètes :</p>
                <ul>
                    <li>Se déplacer de 10m</li>
                    <li>Fouiller, inspecter ou se concentrer</li>
                    <li>Attaquer</li>
                    <li>Lancer un sort</li>
                </ul>
            </div>
            <div class="div30">
                <h3>Demi-actions</h3>
                <p>Le joueur peut également effectuer plusieurs actions si elles ne sont pas complètes. 
                    Il peut en l'occurrence charger et attaquer à la suite dans un maximum de 10 mètres, 
                    la réussite est déterminée par un jet d'équilibre pour la charge et par un jet d'attaque classique pour l'attaque portée.</p><br />
                <p>Sont considérés comme des demi-actions :</p>
                <ul>
                    <li>Utiliser un don</li>
                    <li>Changer d'arme</li>
                    <li>Se déplacer de 5m</li>
                    <li>Se mettre en position de défense, ce qui donne +1 à la CA.</li>
                    <li>Se mettre en position d'attaque, ce qui donne +1 au prochain jet de toucher.</li>
                </ul>
            </div>
            <div class="div40">
                <img class="communImages imageCombatJetToucher" src="ressources/14-Combat/Combat.Asthenot.DA.jpg">
            </div>

        </div>
    </div>



    <div class="divZoneCombatTitre">
        <h2 class="titreCombat">Les attaques et les jets de toucher</h2>
        <div id="divAttaque" class="divPageCombat">

            <div class="div30">
                <h3>Jet de toucher</h3>
                <p>Lorsqu'un protagoniste attaque un ennemi, il jette un dé de toucher pour savoir si son attaque est un succès ou un échec. 
                    Les attaques au corps à corps sont modifiés par la force, 
                    les attaques à distance sont modifiés par la dexterité, les sorts sont offensifs sont modifiés par l'intelligence, 
                    tandis que les sorts de soins sont modifiés par la sagesse.</p>
                <p>Une réussite critique peut être obtenue lorsque le score au d20 est de 20, ce qui se traduit en un doublement des dégâts infligés.</p>
                <p>Un échec critique est obtenu lorsque le score au d20 est de 1, c'est nécessairement un échec et qui a des conséquences néfastes, et de préférence drôles, sur le personnage.</p>
                <p>Le jet obtenu est comparé à la classe d'armure ou magique de la cible pour déterminer la réussite de l'action.</p>

            </div>

            <div class="div40">
                <img class="communImages imageCombatJetToucher" src="ressources/14-Combat/Combat.SilverlightDream.DA.jpg">
            </div>

            <div class="div30">
                <h3>Sorts et techniques</h3>

                <p>Les sorts et techniques sont déterminées en fonction des classes, la description de chaque classe indique leur nom et leur description.</p>
                <p>Chaque sort a un coût en mana fixe, les points de mana peuvent être récupérés hors combat en buvant ou en se reposant. 
                    Le coût réel du sort est le coût indiqué plus le niveau du personnage.</p>
                <p>Les sorts de soins touchent si le jet atteint la valeur 10, si le jet atteint 20, le soin est critique et est doublé. 
                    Le jet est modifié par la sagesse. Si le jet atteint de 6 à 9, le soin atteint tout de même sa cible, mais le soin est diminué de moitié. 
                    Si le jet donne 1, le soigneur subit 1 point de dégât.</p>
                <p>Les sorts offensifs touchent avec le modificateur d'intelligence et en fonction de la classe magique des ennemis.</p>
            </div>

        </div>
    </div>



    <div class="divZoneCombatTitre">
        <h2 class="titreCombat">Modificateurs de toucher : classe d'armure et classe magique</h2>
        <div id="divModificateurs" class="divPageCombat">
            <div class="divMoitieGauche">
                <h3>Attaques physiques</h3>
                <img class="communImages imageCombatModificateurs" src="ressources/14-Combat/hammer-drop.png">
                <p>Pour déterminer le succès d'une attaque physique, il faut comparer le jet de toucher avec la classe d'armure de la cible. 
                    Si le résultat est supérieur ou égal, l'attaque touche et les dégâts infligés sont déterminés en fonction de l'arme utilisée.</p>
                <p>La classe d'armure est déterminée à partir de la classe d'armure de base, qui est de 10, des éventuelles pièces d'armure, de la dextérité et du modificateur de taille.</p>
            </div>
            <div class="divMoitieDroite">
                <h3>Attaques magiques</h3>
                <img class="communImages imageCombatModificateurs" src="ressources/14-Combat/unfriendly-fire.png">
                <p>Pour déterminer le sucès d'une attaque magique, il faut comparer le jet de toucher avec la classe magique de la cible. 
                    Si le résultat est supérieur ou égal, l'attaque touche et les dégâts infligés sont déterminés par le sort utilisé.</p>
                <p>La classe magique est déterminée à partir de la classe magique de base, qui est de 10, des éventuelles pièces d'armures magiques, du charisme et du modificateur de taille.</p>
                <p>Les classes magiques les plus puissantes, à savoir clerc, sorcier, magicien et druide, ont un bonus de +1 à la classe magique.</p>
            </div>
            <div style="float:left;margin-left:1%;">
                <h4>Tableau du modificateur de taille :</h4>
                <table>
                    <tr>
                        <td style="height: 30px">
                            <p class="ptabstrong">Taille</p>
                        </td>
                        <td>
                            <p class="ptab">Minuscule</p>
                        </td>
                        <td>
                            <p class="ptab">Très petit</p>
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
                            <p class="ptab">Très grand</p>
                        </td>
                        <td>
                            <p class="ptab">Énorme</p>
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

                </table>
            </div>

        </div>
    </div>



    <div class="divZoneCombatTitre">
        <h2 class="titreCombat">Incapacités et mort</h2>
        <div id="divIncapacite" class="divPageCombat">
            <div class="divEtroite">
            <img class="communImages imageCrane" src="ressources/14-Combat/Crane.jpg">
            <h3>Mise hors de combat</h3>
            <p>Lorsqu'un joueur ou un monstre voit ses points de vie atteindre 0, il devient inconscient et ne peut plus mener d'actions. 
                Si les points de vie d'un joueur atteignent -10, l'intéressé est mort et ni la fin du combat ni des soins d'un autre joueur ne peuvent rétablir la victime.</p>
            <p>Pour ramener un personnage à la vie, il faut utiliser un sort de résurrection ou utiliser les premiers secours.</p>
</div>
            <div class="divMoitieGauche">
            <h3>Regagner conscience</h3>
            <p>Lorsqu'un joueur voit ses points de vie descendre sous la barre des 1 points de vie, il perd conscience et ne peut plus effectuer d'action. 
                Cependant, à chaque tour, il peut tenter de regagner conscience avec un jet de sauvegarde.</p>
            <p>Un jet de sauvegarde nécessite de faire 10 avec 1d20, si tel est le cas, le joueur peut alors effectuer une action pour ce tour. 
                Regagner conscience ne soigne pas des dégâts subis, ce qui résulte en une perte de conscience une fois l'action effectuée.</p>
            <p>Ce regain de conscience peut être tenté à chaque début de tour pour le personnage en question.</p>
</div>
            <div class="divMoitieDroite">
            <h3>Récupération des blessures</h3>
            <p>Les points de vie peuvent être regagnés par les sorts de soins, les potions de vie ou les premiers secours. 
                Les premiers secours permettent à un joueur de porter assitance à un coéquipier afin qu'il reprenne le combat.
            <p>Un dé de récupération est lancé, si le jet atteint moins de 5 avec 1d20, la récupération échoue. 
                Si le jet atteint entre 5 et 9, la victime se relève mais s'écroule à nouveau une fois son action effectuée. 
                Si le jet est au moins de 10 , la victime se relève avec 3pv.</p>
            <p>Un échec critique achève le joueur, tandis qu'une réussite critique soigne le joueur pour 10pv.</p>
            </div>
        </div>
    </div>


    <div class="divZoneCombatTitre">
        <h2 class="titreCombat">Le Telnas</h2>
        <div id="divTelnas" class="divPageCombat divEtroite">
            <img class="communImages imageCombatTelnas" src="ressources/14-Combat/TelnasBleu.Demiruigi.DA.jpg">
            <p>Le Telnas est une matérialisation physique d'une forme très pure de magie des arcanes.</p>
            <p>Elle permet au joueur d'invoquer une épaisse fumée bleue qu'il peut contrôler à sa guise.</p>
            <p>Voici quelques exemples de l'utilisation du Telnas par ordre de difficulté :</p>
            <ul>
                <li>Matérialisation d'une clé pour ouvrir une serrure que le crochetage n'a pas permis de forcer.</li>
                <li>Matérialisation d'une épée infligeant des dégâts magiques aux spectres ou aux élémentaires.</li>
                <li>Matérialisation d'une sphère de protection autour du groupe de joueur.</li>
            </ul>

            <br />

            <p>Lors de l'utilisation du Telnas, le joueur décrit en détails ce qu'il essaye de faire. Le MJ estime ensuite le score
                nécessaire au dé 20 pour réussir l'action, ce score est pondéré par le niveau de maîtrise du Telnas du joueur.</p>

        </div>

    </div>

</div>