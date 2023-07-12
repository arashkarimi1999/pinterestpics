import sqlite3
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pymongo


# Connects to the SQLite database and retrieves all the rows from the "jobs" table
conn = sqlite3.connect('jobs/db.sqlite3')
cursor = conn.cursor()
cursor.execute('SELECT * FROM jobs')
results = cursor.fetchall()
conn.close()


# Initializes a Chrome webdriver
driver = webdriver.Chrome()
driver.maximize_window()


photoes = []

for result in results:
    # Navigates to the Pinterest search page
    driver.get(f'https://www.pinterest.com/search/pins/?q={result[1]}')
    sleep(5)

    for i in range(1, result[2]+1):
        # Extracts the image links
        f = driver.find_element(
            By.XPATH, f'/html/body/div[1]/div/div[1]/div/div[3]/div/div[2]/div[2]/div/div/div/div[1]/div[{(i-1)%15+1}]/div/div/div/div/div[1]/a/div/div/div/div/div[1]/img')
        link = f.get_attribute('src')

        photoes.append({'tag': result[1], 'link': link})

        # scrolls the page to load more images for every 15 image
        if i % 15 == 0:
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            sleep(1)

driver.quit()

# Connects to the MongoDB database
# Inserts the extracted image links into the "items" collection in the "pinterest" database
client = pymongo.MongoClient()
db = client['pinterest']
collection = db['items']
collection.insert_many(photoes)
