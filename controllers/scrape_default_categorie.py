from .categorie_controler import CategorieControler
from .sous_categorie_controler import SousCategorieControler
from .product_controler import ProductControler
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import os


class ScrapeDefaultCategorie():
    
    def __init__(self) -> None:

        options = Options()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--start-maximized")
        options.binary_location = "C:/Program Files/Mozilla Firefox/firefox.exe"

        script_dir = os.path.dirname(__file__)
        geckodriver_path = os.path.join(script_dir, 'geckodriver.exe')
        service = Service(executable_path=geckodriver_path)
        self.driver = webdriver.Firefox(service=service, options=options)

    def default_scrapper(self):
        
        url = "https://www.alibaba.com/"

        categorie = []

        self.driver.get(url)
        categories_elements = self.driver.find_elements(By.CSS_SELECTOR, 'div.panel-content.secondary-cate-content div')

        for categorie in categories_elements[:5]:

            bouton = self.driver.find_element(By.CSS_SELECTOR, 'div.tab-title')

            bouton.click()

            url_elt = categorie.find_element(By.CSS_SELECTOR, 'a')

            url = url_elt.get_attribute('href')

            name_element = url_elt.find_element(By.CSS_SELECTOR, ' span.item-name')
            name = name_element.text

            controler_categorie = CategorieControler(url,name)

            sous_categories = controler_categorie.categorie_scrappers()

            product_categorie_list = {}

            for sous_categorie in sous_categories:

                print(f'\n\nDebut du scrapping de la sous categorie {sous_categorie["name"]}\n')

                controler_sous_categorie = SousCategorieControler(sous_categorie, controler_categorie)

                products = controler_sous_categorie.sous_categorie_scrapper()

                if controler_categorie.nom not in product_categorie_list:
                    product_categorie_list[controler_categorie.nom] = {}

                if sous_categorie["name"] not in product_categorie_list[controler_categorie.nom]:
                    product_categorie_list[controler_categorie.nom][sous_categorie["name"]] = []

                for product in products:
                    product_categorie_list[controler_categorie.nom][sous_categorie["name"]].append(product)

                    save_product = ProductControler(product, controler_sous_categorie)
                    save_product.produit_scrapper()


                print(f'\n\nLe scrapping de la sous categorie {sous_categorie["name"]} est terminé\n')
