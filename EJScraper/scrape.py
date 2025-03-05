import datetime
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://eurojackpot.de")
assert "EUROJACKPOT" in driver.title


def save_jackpot(pick_numbers, euro_numbers, date):
    with open("eurojackpot.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([pick_numbers + [euro_numbers]] + [date])


first_ever_pick = datetime.date(2012, 3, 23)
recent_pick = datetime.date.today()


numbers = driver.find_elements(By.CLASS_NAME, "winning-number")
all_numbers = [num.text for num in numbers]
first_five = all_numbers[:5]
last_two = all_numbers[5:]

# while first_ever_pick <= recent_pick:
