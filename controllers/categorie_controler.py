from models.categorie import Categorie

class CategorieControler():
    def __init__(self, url, nom):
        self.url = url
        self.nom = nom
    
    def categorie_scrappers(self):
        categorie = Categorie(self.nom, self.url)

        categorie.create_folder()

        items = categorie.get_all_sub_categorie()

        for item in items:

            print(f"\033[94mNom\033[0m : {item["name"]}\n\033[94mUrl\033[0m : {item["url"]}")

        return items
