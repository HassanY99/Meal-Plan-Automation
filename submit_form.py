from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class Form:
    chrome_driver_path = Service("chromedriver")  # Define Chrome Driver path

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=options, service=chrome_driver_path)

    forms_link = "https://docs.google.com/forms/d/e/1FAIpQLSfJwYiLRgD-OxrjFzi4ZoWV1ooUsWdG2A3ba5_NDxtkRL1zOg/viewform?usp=sf_link"  # Replicate this forms link

    driver.get(forms_link)
    breakfast_name_input = driver.find_element(by=By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
    breakfast_link_input = driver.find_element(by=By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
    breakfast_time_input = driver.find_element(by=By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
    lunch_name_input = driver.find_element(by=By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input")
    lunch_link_input = driver.find_element(by=By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input")
    lunch_time_input = driver.find_element(by=By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input")
    dinner_name_input = driver.find_element(by=By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input")
    dinner_link_input = driver.find_element(by=By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input")
    dinner_time_input = driver.find_element(by=By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div[1]/div/div[1]/input")
    submit_form = driver.find_element(by=By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span")

    def submit(self, b_name, b_direction, b_time, l_name, l_direction, l_time, d_name, d_direction, d_time):

        self.breakfast_name_input.send_keys(b_name)
        self.breakfast_link_input.send_keys(b_direction)
        self.breakfast_time_input.send_keys(b_time)

        self.lunch_name_input.send_keys(l_name)
        self.lunch_link_input.send_keys(l_direction)
        self.lunch_time_input.send_keys(l_time)

        self.dinner_name_input.send_keys(d_name)
        self.dinner_link_input.send_keys(d_direction)
        self.dinner_time_input.send_keys(d_time)

        self.submit_form.click()
