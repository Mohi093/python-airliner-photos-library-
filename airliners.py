import json
import requests
from bs4 import BeautifulSoup
import os

class AirlinersNetScraper:
    def __init__(self, save_path="imgs"):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Referer': 'https://www.airliners.net',
            'Upgrade-Insecure-Requests': '1'
        }
        self.session = requests.Session()
        self.save_path = save_path
        
        # Create save directory if it doesn't exist
        if not os.path.exists(self.save_path):
            os.makedirs(self.save_path)

    def get_images(self, aircraft_name):
        search_query = aircraft_name.replace(" ", "+")
        safe_filename = aircraft_name.replace("/", "-").replace("\\", "-")
        
        url = f"https://www.airliners.net/search?keywords={search_query}&sortBy=dateAccepted&sortOrder=desc&perPage=36&display=detail"
        
        response = self.session.get(url, headers=self.headers)
        print("HTML Response Status:", response.status_code)
        
        if response.status_code != 200:
            return []
            
        soup = BeautifulSoup(response.text, "html.parser")
        images = soup.find_all("img", class_="lazy-load")
        count = 0
        downloaded_files = []

        for image in images:
            img_url = image.get('data-src') or image.get('src')
            if img_url and img_url.lower().endswith('.jpg'):
                count += 1
                filepath = os.path.join(self.save_path, f"{safe_filename} {count}.jpg")
                
                try:
                    with open(filepath, "wb") as file:
                        img_response = requests.get(img_url)
                        file.write(img_response.content)
                    downloaded_files.append(filepath)
                except Exception as e:
                    print(f"Error downloading {img_url}: {e}")

        return downloaded_files

# Example usage:
if __name__ == "__main__":
    scraper = AirlinersNetScraper(save_path="aircraft_images")
    files = scraper.get_images("Bf-109")
    print(f"Downloaded images: {len(files)}")


