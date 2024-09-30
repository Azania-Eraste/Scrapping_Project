from controllers.categorie_controler import CategorieControler
from controllers.sous_categorie_controler import SousCategorieControler
from controllers.product_controler import ProductControler
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from controllers.scrape_default_categorie import ScrapeDefaultCategorie
from controllers.scrape_categorie import ScrapeCategorie
import os


class MainNav:

    def show_nav(self):
        while True:
            try :
                print("=------------==============================----------------=")
                print("¦------------¦----------------------------¦----------------¦")
                print("¦------------¦-\033[1;94mAZA programme : Bienvenue\033[0m--¦----------------¦")
                print("¦------------¦----------------------------¦----------------¦")
                print("=------------==============================----------------=")
                print('\n')
                print("=---/\----/\----/\----/\----/\----/\----/\----/\----/\----/-=")
                print("¦--/--\--/--\033[94mProjet python : web scrapping\033[0m-\--/--\--/--\--/--¦")
                print("=-/----\/----\/----\/----\/----\/----\/----\/----\/----\/---=\n")
                print('\n')
                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                print("<=---------------------------------------------------------=>")
                print("<¦-------------------------\033[94mMENU\033[0m----------------------------¦>")
                print("<=---------------------------------------------------------=>\n")
                print("\033[94m 1 \033[0m => Scraper une catégorie \n\033[94m 2 \033[0m => Scraper 5 categories \n\033[94m 0 \033[0m => Quitter \n")
                choix = input("Votre choix : ")
                
                if choix == '0':
                    print("\033[32mAu revoir !\033[0m")
                    break
                elif choix == '1':
                    
                    url = input("Entrez l'url de la categorie : ")
                    
                    scrape = ScrapeCategorie(url)

                    scrape.scrappe_categorie()

                elif choix == '2':

                    default =  ScrapeDefaultCategorie()

                    default.default_scrapper()
                
                else:
                    print("\033[91mVeuillez choisir un choix valide .\033[0m")
            except Exception as e:
                print(f"Erreur {e}")

