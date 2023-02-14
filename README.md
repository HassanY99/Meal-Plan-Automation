# Meal-Plan-Automation

Since, I am a Fitness Fanatic and I always trying to find healthy diet plans. I decided to create a program that does that all for me as scrolling through hundreds of recipes everyday and trying to figure out what to make for the day consumes a lot of time this programs saves a lot of that effort and can be used by many others who are consistently looking for a healthy meal plan.

- I made this app using python OOP and automation that uses Selenium web driver which collects healthy breakfast, lunch and dinner recipes from [Eating Well](https://www.eatingwell.com/). A google form is then filled through automation with all the data gathered and a google spreadsheet is then sent to the user where he can keep track and find all the recipes.
- I used requests, smtplib, time, selenium, BeautifulSoup and random module in this program.

## CLASSES
* Main: Contains all the computation, runs the program and once all data gathered sends out an email.
* Meals: Creates Breakfast, Lunch and Dinner dictionary from the data that it is getting from [Eating Well](https://www.eatingwell.com/).
* PrepTime: Defines the attributes to get the time from the randomly chosen meal link using random module and the data is web scrapped using Beautiful Soup.
* Form: Creates a submit function that fills out the entire form and records user response.

## LOGIC
* The Meals class has functions that each gets its own category of data and each creating a dictionary of over 100 recipes.
* The PrepTime function gets active preperation time from the directions link that is randomely chosen.
* The form is automatically filled in the end when all the data has been gathered in each dictionary and time is also recorded.
* In the end, smtplib is used to send user an email out with spreadsheet that was created with his meal plan for the day.

## INSTRUCTIONS
* Open up the project in your preferred IDE, fill in some of the data in the code where mentioned e.g. your email, password e.t.c. 
* Replicate the google form that is present in this code and link your google spreadhsheet. (add that link in the code where mentioned)
* Run the program in your IDE, a seperate chrome window will open where the program automatically runs and all window will close after program is executed.
* Once completed, you will recieve an email that has a link to your spreadsheet and will contain your plan for the day.
