class AfficherUnMessageALEcranEnMajuscule:
    def afficher_un_message_en_majuscule(self, message_a_afficher: str) -> None:
        if self._le_message_est_en_majuscule(message_a_afficher):
            print(message_a_afficher)
        else:
            print(self._mettre_le_message_en_majuscule(message_a_afficher))

    @staticmethod
    def _mettre_le_message_en_majuscule(message_a_mettre_en_majuscule: str) -> str:
        return message_a_mettre_en_majuscule.upper()

    @staticmethod
    def _le_message_est_en_majuscule(message_a_afficher: str) -> bool:
        return message_a_afficher.isupper()
