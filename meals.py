from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time


class Meals:

    chrome_driver_path = Service("chromedriver")  # Define Chrome Driver path

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=options, service=chrome_driver_path)

    breakfast_recipe_webpage = "https://www.eatingwell.com/recipes/17916/mealtimes/breakfast-brunch/"
    lunch_recipe_webpage = "https://www.eatingwell.com/recipes/17963/mealtimes/lunch/"
    dinner_recipe_webpage = "https://www.eatingwell.com/recipes/17947/mealtimes/dinner/"

    def __init__(self):
        self.breakfast_dict = {}
        self.lunch_dict = {}
        self.dinner_dict = {}

    def get_breakfast(self):
        self.driver.get(self.breakfast_recipe_webpage)
        time.sleep(5)
        self.load_more()
        get_title_and_link = self.driver.find_elements(by=By.CLASS_NAME, value="elementFont__titleLink")

        for i in range(len(get_title_and_link)):
            try:
                self.breakfast_dict[i] = {
                    "name": get_title_and_link[i].get_attribute("title"),
                    "direction_link": get_title_and_link[i].get_attribute("href")
                }
            except RuntimeError:
                print("Error getting breakfast from the webpage.")
                self.breakfast_dict[i] = {
                    "name": "Breakfast Salad with Egg & Salsa Verde Vinaigrette",
                    "direction_link": "https://www.eatingwell.com/recipe/281188/breakfast-salad-with-egg-salsa-verde-vinaigrette/"
            }

    def get_lunch(self):
        self.driver.get(self.lunch_recipe_webpage)
        time.sleep(5)
        self.load_more()
        get_title_and_link = self.driver.find_elements(by=By.CLASS_NAME, value="elementFont__titleLink")

        for i in range(len(get_title_and_link)):
            try:
                self.lunch_dict[i] = {
                    "name": get_title_and_link[i].get_attribute("title"),
                    "direction_link": get_title_and_link[i].get_attribute("href")
                }
            except RuntimeError:
                print("Error getting lunch from the webpage.")
                self.lunch_dict[i] = {
                    "name": "Chickpea & Quinoa Bowl with Roasted Red Pepper Sauce",
                    "direction_link": "https://www.eatingwell.com/recipe/258195/chickpea-quinoa-bowl-with-roasted-red-pepper-sauce/"
                }

    def get_dinner(self):
        self.driver.get(self.dinner_recipe_webpage)
        time.sleep(5)
        self.load_more()
        get_title_and_link = self.driver.find_elements(by=By.CLASS_NAME, value="elementFont__titleLink")

        for i in range(len(get_title_and_link)):
            try:
                self.dinner_dict[i] = {
                    "name": get_title_and_link[i].get_attribute("title"),
                    "direction_link": get_title_and_link[i].get_attribute("href")
                }
            except RuntimeError:
                print("Error getting dinner from the webpage.")
                self.dinner_dict[i] = {
                    "name": "One-Pot Garlicky Shrimp & Broccoli",
                    "direction_link": "https://www.eatingwell.com/recipe/7919492/one-pot-garlicky-shrimp-broccoli/"
                }

    def load_more(self):
        for click in range(4):
            time.sleep(2)
            self.driver.find_element(by=By.ID, value="category-page-list-related-load-more-button").click()
