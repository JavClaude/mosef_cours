import pandas as pd


class RecuperationDesDonnéesDuTitanic:
    @staticmethod
    def get_données_du_titanic() -> pd.DataFrame:
        print("Récupération des données du titanic ⌛")
        dataframe_avec_les_données_du_titanic = pd.read_csv("https://osf.io/download/aupb4/")
        print("Données du titanic correctement récupérées ✅")
        return dataframe_avec_les_données_du_titanic
