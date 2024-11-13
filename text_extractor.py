from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from ranking_functions import get_embedding
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

def text_extraction(link, holistic_query):

    query_embedding = get_embedding(holistic_query)

    options = Options()
    options.add_argument("--headless=new")
    # Initialize Selenium WebDriver in headless mode
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    url = link
    driver.get(url)

    # Allow some time for the page to load completely
    time.sleep(1)

    # Find elements by XPath
    elements = driver.find_elements(By.XPATH, '//*[contains(@class, "style-scope patent-text")]')
    cosine_sims = [{"Cosine Similarity": 0,
            "Text": ""}]
    # Extract and print the text from each element
    for element in elements:
        element = element.text
        embedding = get_embedding(element)
        cosine_sim = cosine_similarity(query_embedding, embedding)
        cosine_sims.append({
            "Cosine Similarity": cosine_sim[0],
            "Text": element
        })
    # Convert list to DataFrame
    cosines = pd.DataFrame(cosine_sims)

    # Find the row with maximum Cosine Similarity
    max_similarity_row = cosines.loc[cosines['Cosine Similarity'].idxmax()]

    # Get the values
    max_cosine = max_similarity_row['Cosine Similarity']
    corresponding_text = max_similarity_row['Text']

    # print(f"Maximum Number: {max_cosine}, Associated Text: {corresponding_text}")

    return max_cosine, corresponding_text
