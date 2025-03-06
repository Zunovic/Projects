import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome()
driver.get("https://eurojackpot.de")
track_time = time.time()

def save_jackpot(pick_numbers, euro_numbers, pick_date):
    with open("eurojackpot.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([[pick_date] + [pick_numbers] + [euro_numbers]])


# Alle Jahre werden iteriert anhand des CSS selectors
for year in range(2025, 2011, -1):
    dropdown_year = Select(WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.CSS_SELECTOR, "select.form-select"))))

    dropdown_year.select_by_visible_text(str(year))
    time.sleep(2)
    dropdown_date = Select(WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.CSS_SELECTOR, "div:nth-child(2) > select"))))

    for i in range(len(dropdown_date.options)):
        # Für jedes Jahr gibt es eine Liste mit verfügbaren Ziehungen die aus der options Methode genommen wird.
        # Wenn der Timer entfernt wird kann nicht mehr iteriert werden, da die Seite nicht so schnell nachlädt
        dropdown_date.select_by_index(i)
        time.sleep(0.1)

        # Alle Ziehungstage werden abgerufen und die Zahlen werden entnommen
        picked_numbers = driver.find_elements(By.CLASS_NAME, "winning-number")
        all_picks = [n.text for n in picked_numbers]
        first_five = all_picks[:5]
        last_two = all_picks[5:]
        date = dropdown_date.options[i].text

        # Function call um die gezogenen Nummern zu speichern
        save_jackpot(first_five, last_two, date)

        # Nur für Debugzwecke: Kann auskommentiert werden wenn nicht benötigt
        print(f"Zahlen vom {date} = {first_five} + {last_two} gespeichert!")

count_time = time.time()
print(f"Alle Zahlen von der Seite wurden in {int((count_time-track_time) / 60)} Minuten und {int((count_time-track_time) % 60)} Sekunden gespeichert.")
driver.quit()