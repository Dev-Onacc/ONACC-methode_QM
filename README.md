
# Correction des Biais Climatiques par Quantile Mapping

## Description du Projet
Ce projet fournit une application interactive développée avec **Streamlit** pour la correction des biais dans les données climatiques simulées à l'aide de la méthode de **Quantile Mapping** (QM). L'application permet aux utilisateurs de télécharger des jeux de données simulées et observées, de sélectionner une période spécifique pour l'application de la correction, et de visualiser les résultats sous forme de graphiques interactifs. Les utilisateurs peuvent aussi obtenir des métriques de performance tell...

### Fonctionnalités
- **Chargement des données** : Les utilisateurs peuvent télécharger des fichiers `.xlsx` contenant les données simulées et observées.
- **Sélection de la période** : Filtrer les données pour une période spécifique en sélectionnant des dates dans une interface interactive.
- **Correction des biais** : Correction des données simulées en utilisant la méthode de Quantile Mapping.
- **Visualisation des résultats** : Affichage de graphiques pour comparer les données observées, simulées et corrigées.
- **Métriques de performance** : Calcul du RMSE et du biais pour évaluer la précision de la correction.
- **Carte de chaleur des écarts** : Affichage de cartes de chaleur pour visualiser les écarts de température.
- **Téléchargement des résultats** : Possibilité de télécharger les données corrigées en format `.xlsx`.

## Prérequis
Avant de lancer l'application, vous devez installer les dépendances suivantes :

- **Python 3.x**
- **Streamlit**
- **Pandas**
- **NumPy**
- **SciPy**
- **Plotly**
- **Seaborn**
- **Matplotlib**
- **scikit-learn**
- **Openpyxl**

Vous pouvez installer les dépendances nécessaires en exécutant la commande suivante dans votre terminal :

```bash
pip install streamlit pandas numpy scipy plotly seaborn matplotlib scikit-learn openpyxl
```

## Utilisation de l'Application

1. **Lancer l'application Streamlit** :
    Une fois les dépendances installées, vous pouvez lancer l'application Streamlit en exécutant la commande suivante :

    ```bash
    streamlit run main.py
    ```

    Assurez-vous que le fichier `app.py` correspond au nom de votre fichier Python contenant l'application Streamlit.

2. **Télécharger les données** :
    - Téléchargez les fichiers `.xlsx` contenant les données simulées et observées dans les sections dédiées de l'interface Streamlit.
    - Les fichiers doivent contenir les colonnes suivantes : `date`, `temperature_min`, `temperature_max`, `precipitation`.

3. **Sélectionner la période** :
    Utilisez l'outil de sélection de dates pour choisir la période sur laquelle appliquer la correction des biais.

4. **Visualiser les résultats** :
    - Les graphiques interactifs affichent les températures minimales, maximales et les précipitations avant et après correction.
    - Les métriques de performance (RMSE et biais) sont calculées et affichées pour chaque variable.
    - Les cartes de chaleur montrent les écarts de température corrigée par rapport aux données observées.

5. **Télécharger les données corrigées** :
    Après avoir appliqué la correction, vous pouvez télécharger les données corrigées au format `.xlsx` à l'aide du bouton de téléchargement.

## Méthode de Correction

La méthode utilisée pour la correction des biais est le **Quantile Mapping** (QM). Cette technique ajuste les données simulées de manière à ce que leurs quantiles correspondent à ceux des données observées. En d'autres termes, elle permet d’ajuster les données simulées de manière non linéaire pour refléter les distributions observées.

Les étapes principales sont :
1. Calculer les quantiles des données simulées.
2. Utiliser les quantiles pour intercepter et ajuster les données simulées afin qu'elles correspondent à la distribution observée.

## Métriques de Performance

Les performances de la correction sont évaluées à l’aide des métriques suivantes :
- **RMSE (Root Mean Square Error)** : Mesure la différence quadratique moyenne entre les données observées et les données simulées ou corrigées.
- **Biais** : Mesure la différence moyenne entre les données simulées ou corrigées et les données observées.

## Exemple de Résultats

Après avoir appliqué la correction, les utilisateurs peuvent voir les graphiques suivants :
- Évolution des températures minimales, maximales et des précipitations avant et après correction.
- Carte de chaleur des écarts de température.
- Table des métriques de performance pour chaque variable.

## Conclusion

Ce projet fournit une solution interactive pour la correction des biais climatiques à l'aide de la méthode Quantile Mapping. L'application offre des outils visuels pour évaluer l'impact de la correction et les performances des modèles simulés. Elle est utile pour les chercheurs, les climatologues et les professionnels de la gestion des ressources naturelles souhaitant améliorer la précision des modèles climatiques et prendre des décisions éclairées.

## Auteur
- **Nom** : POUM BIMBAE Paul Ghislain
- **Entreprise/Organisation** : ONACC
- **Contact** : poum.bimbar@onacc.cm

---

Merci d'utiliser ce projet ! N'hésitez pas à contribuer ou à poser des questions via les issues.
