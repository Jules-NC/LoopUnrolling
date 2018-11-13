import re


def deroulage(ligne_, variable, nombre, sens_=True):
    """
    Déroule une ligne de code un certain nombre de fois suivant une unique variable
    Vous DEVEZ remplacer k par k+0 pour différencier les variables
    Vous DEVEZ ajuster vous-même les k+=2 dans les boucles
    Vous EVITEZ d'y passer 10,000 ans
    :param ligne_: La ligne de code à dérouler
    :type ligne_: string
    :param variable: Le nom de la variable à dérouler
    :type variable: string
    :param nombre: Nombre de déroulages
    :type nombre: int
    :param sens_: True pour croissant (default), False pour décroissant
    :type sens_: boolean
    :return: La string correspondant au déroulage demandé
    :rtype: string => Vous pouvez utiliser derouler DANS derouler DANS derouler !
    :Example:
    >>> print(deroulage("lh.at<float>(i-1, k+0);", "i", 3))
    lh.at<float>(i-1, k+0);
    lh.at<float>(i+0, k+0);
    lh.at<float>(i+1, k+0);
    <BLANKLINE>
    >>> print(deroulage(deroulage("lh.at<float>(i+0, k-2);", "k", 4), "i", 3, False))
    lh.at<float>(i+0, k-2);
    lh.at<float>(i+0, k-1);
    lh.at<float>(i+0, k+0);
    lh.at<float>(i+0, k+1);
    <BLANKLINE>
    lh.at<float>(i-1, k-2);
    lh.at<float>(i-1, k-1);
    lh.at<float>(i-1, k+0);
    lh.at<float>(i-1, k+1);
    <BLANKLINE>
    lh.at<float>(i-2, k-2);
    lh.at<float>(i-2, k-1);
    lh.at<float>(i-2, k+0);
    lh.at<float>(i-2, k+1);
    <BLANKLINE>
    <BLANKLINE>
    """
    ligne = ligne_  # On évite de toucher à la string d'origine

    # On différencie les + et les - pour bien additionner
    indexs_plus = [m.end() for m in re.finditer(variable + '\+', ligne)]
    indexs_moins = [m.end() for m in re.finditer(variable + '-', ligne)]

    # On transforme en liste pour pouvoir modifier le machin
    ligne = list(ligne)
    lignes = [ligne[:] for _ in range(nombre)]

    resultat = []
    for i, ligne in enumerate(lignes):
        # Sens (+ ou -)
        sens = 1
        if sens_ is False:
            sens = -1

        for index in indexs_plus:
            res_t = int(ligne[index]) + i * sens
            ligne[index] = res_t
            if res_t < 0:
                ligne[index - 1] = ""

        for index in indexs_moins:
            res_t = -int(ligne[index]) + i * sens
            ligne[index] = res_t
            if res_t >= 0:
                ligne[index - 1] = "+"
            else:
                ligne[index - 1] = ""
        # Retour à une string
        resultat.append("".join(str(e) for e in ligne) + "\n")

    # Renvoie une string => Utilisation imbriquée TMTC
    return "".join(str(e) for e in resultat)
