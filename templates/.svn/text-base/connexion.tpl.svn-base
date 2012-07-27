<!-- David Winckel et François Ripp -->

{literal}
<script type="text/javascript">

        function formVerification()
        {
                var ok = true;

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

                // Mot de passe
                if (! /^[a-zA-Z0-9_-]{6,18}$/.test(document.getElementById("motdepasse").value))
                {
                    document.getElementById("erreurmotdepasse").className = "erreurAffiche";
                    ok = false;
                }
                else
                {
                    document.getElementById("erreurmotdepasse").className = "erreurMasque";
                }
                    
                return ok;
        }

</script>
{/literal}

<h1>Connexion</h1>

<form action="?Page=authentification" method="POST" onsubmit="return formVerification()">
    <table>
        <tr>
            <td>
                <label for="login">Login</label>
            </td>

            <td>
                <input name="login" id="login" type="text">
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
                <input name="motdepasse" id="motdepasse" type="password">
            </td>
            <td>
                <span class="erreurMasque" id="erreurmotdepasse"> (6 à 16 caractères alphanumériques)</span>
            </td>
        </tr>
        <tr>
            <td>
            </td>

            <td>
                <input id="envoi" value="Authentification" type="submit">
            </td>
            <td>
            </td>
        </tr>
        <tr>
            <td>
                Pas de compte
            </td>

            <td>
                <a href="?Page=inscription">Inscription</a>
            </td>
            <td>
            </td>
        </tr>
        <tr>
            <td>
                Mot de passe perdu
            </td>

            <td>
                <a href="?Page=perdu">Récupérer mon mot de passe</a>
            </td>
            <td>
            </td>
        </tr>
    </table>
</form>