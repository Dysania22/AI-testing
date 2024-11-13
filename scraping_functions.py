from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import re
import pandas as pd
from text_extractor import text_extraction
from styler import color_background

def scraper(query, holistic_query):
    options = Options()
    options.add_argument("--headless=new")
    # Initialize Selenium WebDriver in headless mode
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    # Open the Google Patents search page
    concatenating = str(query).replace(" ", "+")
    url = f"https://patents.google.com/?q=({concatenating})"
    driver.get(url)

    # Allow some time for the page to load completely
    time.sleep(1)

    # Find the search result items
    patent_results = []
    results = driver.find_elements(By.CSS_SELECTOR, 'search-result-item')
    index = 1
    for el in results:

        # Extract the title (inside <h3> -> <span>)
        title = el.find_element(By.CSS_SELECTOR, 'h3 span#htmlContent').text.strip()

        metadata = ' '.join(el.find_element(By.CSS_SELECTOR, 'h4.metadata').text.split())
        number = find_string_with_numerals(metadata)

        # Extract Priority Date
        date = el.find_element(By.CSS_SELECTOR, 'h4.dates').text.split('•')[0].strip()

        # Build URL because those links are IMPOSSIBLE to extract
        link = "https://patents.google.com/patent/" + number + "/en"

        similarities, text = text_extraction(link, holistic_query)

        patent_results.append({
            "Original Ranking": index,
            "Name": title,
            "Link": link,
            "Number": number,
            "Cosine Similarity": similarities,
            "Best Snippet": text,
            "Date": date
        })
        index = index + 1

    df = pd.DataFrame(patent_results, columns = ["Original Ranking",
                                                 "Name",
                                                 "Link",
                                                 "Number",
                                                 "Cosine Similarity",
                                                 "Best Snippet",
                                                 "Date"])

    df_ordered = df.sort_values(by='Cosine Similarity', ascending=False)
    return df_ordered

def find_string_with_numerals(input_string):
    words = input_string.split(' ')
    for word in words:
        if re.search(r'\d{5,}', word):
            return word
    return None

def make_clickable(val):
    # target _blank to open new window
    return '<a target="_blank" href="{}">{}</a>'.format(val, val)
