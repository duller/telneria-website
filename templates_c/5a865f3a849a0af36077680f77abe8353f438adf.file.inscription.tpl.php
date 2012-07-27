<?php /* Smarty version Smarty-3.1.7, created on 2012-07-27 22:00:23
         compiled from "templates/inscription.tpl" */ ?>
<?php /*%%SmartyHeaderCode:1679984935012f357b5d923-95364533%%*/if(!defined('SMARTY_DIR')) exit('no direct access allowed');
$_valid = $_smarty_tpl->decodeProperties(array (
  'file_dependency' => 
  array (
    '5a865f3a849a0af36077680f77abe8353f438adf' => 
    array (
      0 => 'templates/inscription.tpl',
      1 => 1336417000,
      2 => 'file',
    ),
  ),
  'nocache_hash' => '1679984935012f357b5d923-95364533',
  'function' => 
  array (
  ),
  'has_nocache_code' => false,
  'version' => 'Smarty-3.1.7',
  'unifunc' => 'content_5012f357b9694',
),false); /*/%%SmartyHeaderCode%%*/?>
<?php if ($_valid && !is_callable('content_5012f357b9694')) {function content_5012f357b9694($_smarty_tpl) {?>﻿<!-- David WINCKEL et François Ripp -->


<script type="text/javascript">

        function formVerification()
        {
                var ok = true;

                // Contrôle de surfaces

                // Login
                if (! /^[a-zA-Z0-9_-]{3,16}$/.test(document.getElementById("login").value))
                {
                       document.getElementById("erreurlogin").className = "erreurAffiche";

                        ok = false;
                }
                else
                {
                       document.getElementById("erreurlogin").className = "erreurMasque";
                }

                // Password
                                
                if (! /^[a-zA-Z0-9_-]{6,18}$/.test(document.getElementById("motdepasse").value))
                {
                    document.getElementById("erreurmotdepasse").className = "erreurAffiche";

                    ok = false;
                }
                else
                {
                    document.getElementById("erreurmotdepasse").className = "erreurMasque";
                }  
                    
                if (document.getElementById("motdepasse").value!=document.getElementById("motdepasseverif").value)
                {                     
                    
                    document.getElementById("erreuridentique").className = "erreurAffiche";
                    ok = false;

                }
                else
                {
                    document.getElementById("erreuridentique").className = "erreurMasque";

                }

                // Prénom
                if (! /^[A-Z]+../.test(document.getElementById("prenom").value))
                {
                       document.getElementById("erreurprenom").className = "erreurAffiche";

                        ok = false;
                }
                else
                {
                       document.getElementById("erreurprenom").className = "erreurMasque";
                }
                    

                // Profession
                if (! /^[A-Z]+../.test(document.getElementById("profession").value))
                {
                       document.getElementById("erreurprofession").className = "erreurAffiche";

                        ok = false;
                }
                else
                {
                       document.getElementById("erreurprofession").className = "erreurMasque";
                }

                // Nom
                if (! /^[A-Z]+[A-Z]+[A-Z]+$/.test(document.getElementById("nom").value))
                {
                       document.getElementById("erreurnom").className = "erreurAffiche";

                        ok = false;
                }
                else
                {
                       document.getElementById("erreurnom").className = "erreurMasque";
                }

                // Adresse
                if (! /^.../.test(document.getElementById("adresse").value))
                {
                       document.getElementById("erreuradresse").className = "erreurAffiche";

                        ok = false;
                }
                else
                {
                       document.getElementById("erreuradresse").className = "erreurMasque";
                }

                // Code postal
                if (! /^[0-9]{5}$/.test(document.getElementById("codepostal").value))
                {
                       document.getElementById("erreurcodepostal").className = "erreurAffiche";

                        ok = false;
                }
                else
                {
                       document.getElementById("erreurcodepostal").className = "erreurMasque";
                }

                // Ville
                if (! /^.../.test(document.getElementById("ville").value))
                {
                       document.getElementById("erreurville").className = "erreurAffiche";

                        ok = false;
                }
                else
                {
                       document.getElementById("erreurville").className = "erreurMasque";
                }
                    

                // Pays
                if (! /^.../.test(document.getElementById("pays").value))
                {
                       document.getElementById("erreurpays").className = "erreurAffiche";

                        ok = false;
                }
                else
                {
                       document.getElementById("erreurpays").className = "erreurMasque";
                }

                // Telephone
                if (! /^[0-9]{10}$/.test(document.getElementById("telephone").value))
                {
                       document.getElementById("erreurtelephone").className = "erreurAffiche";

                        ok = false;
                }
                else
                {
                       document.getElementById("erreurtelephone").className = "erreurMasque";
                }

                // Email
                if (! /^([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$/.test(document.getElementById("email").value))
                {
                    document.getElementById("erreuremail").className = "erreurAffiche";
                    ok = false;
                }
                else
                {
                    document.getElementById("erreuremail").className = "erreurMasque";
                }

                return ok;
        }

        </script>


    <h1>Inscription</h1>
    
    <form action="?Page=inscriptionPost" method="POST" onsubmit="return formVerification()">
        <table>
            <tr>
                <td>
                    <label for="login">Login</label>
                </td>

                <td>
                    <input id="login" name="login" type="text">
                </td>
                <td>
                    <span class="erreurMasque" id="erreurlogin"> (3 à 16 caractères alphanumériques)</span>
                </td>
            </tr>
            <tr>
                <td>
                    <label for="motdepasse">Mot de passe</label>
                </td>

                <td>
                    <input id="motdepasse" name="motdepasse" type="password">
                </td>
                <td>
                    <span class="erreurMasque" id="erreurmotdepasse"> (6 à 16 caractères alphanumériques)</span>
                </td>
            </tr>
            <tr>
                <td>
                    <label for="motdepasseverif">Mot de passe (vérification)</label>
                </td>

                <td>
                    <input id="motdepasseverif" name="motdepasseverif" type="password">
                </td>
                <td>
                    <span class="erreurMasque" id="erreuridentique"> (mots de passe non identiques)</span>
                </td>
            </tr>
            <tr>
                <td>
                    <label for="prenom">Prénom</label>
                </td>

                <td>
                    <input id="prenom" name="prenom" type="text">
                </td>

                <td>
                    <span class="erreurMasque" id="erreurprenom"> (1ère lettre en majuscule - 3 caractères minimum)</span>
                </td>
            </tr>
            <tr>
                <td>
                    <label for="nom">Nom</label>
                </td>

                <td>
                    <input id="nom" name="nom" type="text">
                </td>

                <td>
                    <span class="erreurMasque" id="erreurnom"> (En majuscule)</span>
                </td>
            </tr>
            <tr>
                <td>
                    <label for="profession">Profession</label>
                </td>

                <td>
                    <input id="profession" name="profession" type="text">
                </td>

                <td>
                    <span class="erreurMasque" id="erreurprofession"> (1ère lettre en majuscule - 3 caractères minimum)</span>
                </td>
            </tr>
            <tr>
                <td>
                    <label for="sexe">Sexe</label>
                </td>

                <td>
                    <select id="sexe" name="sexe">
                        <option value="M" selected>Homme</option>                     
                        <option value="F">Femme</option> 
                    </select>
                </td>
                <td>
                </td>
            </tr>
            <tr>
                <td>
                    <label for="adresse">Adresse</label>
                </td>

                <td>
                    <input id="adresse" name="adresse" type="text">
                </td>
                <td>
                    <span class="erreurMasque" id="erreuradresse"> (Minimum 3 caractères)</span>
                </td>
            </tr>
            <tr>
                <td>
                    <label for="codepostal">Code postal</label>
                </td>

                <td>
                    <input id="codepostal" name="codepostal" type="text">
                </td>
                <td>
                    <span class="erreurMasque" id="erreurcodepostal"> (5 chiffres)</span>
                </td>
            </tr>
            <tr>
                <td>
                    <label for="ville">Ville</label>
                </td>

                <td>
                    <input id="ville" name="ville" type="text">
                </td>
                <td>
                    <span class="erreurMasque" id="erreurville"> (Minimum 3 caractères)</span>
                </td>
            </tr>
            <tr>
                <td>
                    <label for="pays">Pays</label>
                </td>

                <td>
                    <input id="pays" name="pays" type="text">
                </td>
                <td>
                    <span class="erreurMasque" id="erreurpays"> (Minimum 3 caractères)</span>
                </td>
            </tr>
            <tr>
                <td>
                    <label for="telephone">Téléphone</label>
                </td>

                <td>
                    <input id="telephone" name="telephone" type="text">
                </td>
                <td>
                    <span class="erreurMasque" id="erreurtelephone"> (10 chiffres)</span>
                </td>
            <tr>
                <td>
                    <label for="email">Email</label>
                </td>

                <td>
                    <input id="email" name="email" type="text">
                </td>
                <td>
                    <span class="erreurMasque" id="erreuremail"> (format d'email standard)</span>
                </td>
            </tr>
            <tr>
                <td>
                </td>

                <td>
                    <input id="envoi" value="Enregistrement" type="submit">
                </td>
                <td>
                </td>
            </tr>
        </table>
    </form><?php }} ?>