from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class SeleniumService():
    @staticmethod
    def get_raw_response(url: str):
        options = Options()
        options.add_argument("--headless")  # Run in headless mode (no UI)
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.get(url)

        # Get page source (fully rendered HTML)
        html_content = driver.page_source

        if not html_content:
            raise ValueError(f"Empty HTML content. URL: {url}")
        
        return html_content
    
    @staticmethod
    def filter_content(html_content: str, keywords: list[str], year: int):
        soup = BeautifulSoup(html_content, "html.parser")
        
        for panel in soup.find_all("div", class_="lsow-panel-title"):
            if panel.text.strip() == str(2025):
                content_div = panel.find_next_sibling("div", class_="lsow-panel-content")
                if content_div:
                    text = content_div.get_text().lower() 
                    if all(keyword.lower() in text for keyword in keywords):
                        print("Both 'concurs' and 'specialist IT' are present in the HTML.")
                    else:
                        print("One or both keywords are missing.")
        return text