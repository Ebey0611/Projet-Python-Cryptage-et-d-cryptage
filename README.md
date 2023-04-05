# Projet-Python-Cryptage-et-d-cryptage
Le but principal de ce projet est de développer un système de codage et de décodage basé sur le
code de Huffmann.
Le codage d’Huffmann a pour but de coder un texte en binaire préfixé qui consiste à coder chaque
lettre par un mot sur 0, 1 (toujours le même pour une lettre). Etant donné le pourcentage d’occurrence
de chaque lettre dans le texte à coder, l’algorithme de codage des lettres est le suivant :
– Initialement, chaque lettre est un arbre binaire ramené à un sommet étiqueté par la proportion
d’occurences de cette lettre dans le texte. Tant qu’il y a plus d’un arbre, réaliser les opérations
suivantes :
1. Considérer A1 et A2 les deux arbres dont les racines portent les plus petites étiquettes e1
et e2.
2. Construire un nouvel arbre A dont la racine r a pour fils les racines de A1 et A2.
3. La racine r est étiqueté par e1 + e2.
– Pour chaque noeud de l’arbre final, l’arête vers son fils gauche est étiquetée 0 et celle vers son
fils droit 1.
– Le code associé à une lettre est le mot binaire composé des étiquettes sur les arêtes entre la
racine de l’arbre final et la feuille étiquetée avec cette lettre.
Ce projet est composé de trois parties.
