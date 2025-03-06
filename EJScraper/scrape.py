import datetime
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


driver = webdriver.Chrome()
driver.get("https://eurojackpot.de")
assert "EUROJACKPOT" in driver.title


def save_jackpot(pick_numbers, euro_numbers, date):
    with open("eurojackpot.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([pick_numbers + [euro_numbers]] + [date])


dropdown_year = Select(driver.find_element(By.CSS_SELECTOR, "body > app-root > div.container > div > div >"
                                                     " app-winning-numbers > div > div > div > div >"
                                                     " section:nth-child(2) > form > div >"
                                                     " div.flex-grow-1.flex-md-grow-0.me-3 > select"))

start_year = 2012
current_year = start_year
first_ever_pick = datetime.date(2012, 3, 23)
recent_pick = datetime.date.today()

# dropdown_year.select_by_visible_text(str(start_year))


# all_dates = [date.text for date in dropdown_date.options]
# print(all_dates)

# numbers = driver.find_elements(By.CLASS_NAME, "winning-number")
# all_numbers = [num.text for num in numbers]
# first_five = all_numbers[:5]
# last_two = all_numbers[5:]

for year in range(2025, 2011, -1):
    dropdown_year.select_by_visible_text(str(year))

    dropdown_date = Select(driver.find_element(By.CSS_SELECTOR, "body > app-root > div.container > div > div > "
                                                                "app-winning-numbers > div > div > div > div > "
                                                                "section:nth-child(2) > form > div > "
                                                                "div:nth-child(2) > select"))

    for date in dropdown_date.options:
        date.(date.text)


print("durchgelaufen")
time.sleep(10)