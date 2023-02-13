import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from meals import Meals
from submit_form import Form
from prep_time import PrepTime
import smtplib

chrome_driver_path = Service("chromedriver")  # Define Chrome Driver path

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=chrome_driver_path)

USER_EMAIL = "to_address_UserEmail"  # Add email to which user you want to send recipes
MY_EMAIL = "from_addr@gmail.com"  # Add email that you are going use to send out the email
MY_PASSWORD = "from_addr_password"  # Add that email's password

# Get all meals
meals = Meals()
meals.get_breakfast()
meals.get_lunch()
meals.get_dinner()

# Randomly pick one meal from the dictionary
b_dict = random.choice(meals.breakfast_dict)
l_dict = random.choice(meals.lunch_dict)
d_dict = random.choice(meals.dinner_dict)
print(f"{b_dict} \n{l_dict} \n{d_dict}")

# Beautiful Soup - Get time from the meal link chosen
time = PrepTime()
time.get_time(b_dict["direction_link"], l_dict["direction_link"], d_dict["direction_link"])
print(time.b_time, time.l_time, time.b_time)


# Submit Form
form = Form()
form.submit(b_dict["name"], b_dict["direction_link"], time.b_time, l_dict["name"], l_dict["direction_link"], time.l_time,
            d_dict["name"], d_dict["direction_link"], time.d_time)

driver.quit()
# Send email to user
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=MY_PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=USER_EMAIL,
        msg=f"Subject:Today's Meal Plan \n\n Here is your custom meal plan for today: "
            f"Add your google spreadsheet link here"  # From replicated google docs link you would have access to
                                                      # your own spreadsheet
    )
