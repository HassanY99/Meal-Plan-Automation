from bs4 import BeautifulSoup
import requests
import time


class PrepTime:

    headers = {  # add header
        "Accept-Language": "Add your accept-language",
        "User-Agent": "Add your user-agent info"
    }

    def __init__(self):
        self.b_time = ""
        self.l_time = ""
        self.d_time = ""

    def get_time(self, b_link, l_link, d_link):
        breakfast_response = requests.get(url=b_link, headers=self.headers).text
        lunch_response = requests.get(url=l_link, headers=self.headers).text
        dinner_response = requests.get(url=d_link, headers=self.headers).text

        breakfast_soup = BeautifulSoup(breakfast_response, "html.parser")
        time.sleep(2)
        try:
            self.b_time = breakfast_soup.find(name="div", class_="elementFont__subtitle").getText()
        except AttributeError:
            print("Breakfast_Time Error ---")
            self.b_time = "Please see prep time in the given link"

        lunch_soup = BeautifulSoup(lunch_response, "html.parser")
        time.sleep(2)
        try:
            self.l_time = lunch_soup.find(name="div", class_="elementFont__subtitle").get_text()
        except AttributeError:
            print("Lunch time Error --")
            self.b_time = "Please see prep time in the given link"

        dinner_soup = BeautifulSoup(dinner_response, "html.parser")
        time.sleep(2)
        try:
            self.d_time = dinner_soup.find(name="div", class_="elementFont__subtitle").get_text()
        except AttributeError:
            print("Dinner time error --")
            self.b_time = "Please see prep time in the given link"
