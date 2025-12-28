# debug_flipkart_watch.py
from scraper.flipkart_scraper import FlipkartScraper
from selenium.webdriver.common.by import By
import time

def debug_flipkart_html():
    print("🕵️ Debugging Flipkart Watch HTML...")
    scraper = FlipkartScraper()
    
    try:
        # 1. Search for Watch
        if scraper.search_product("analog watch for men"):
            print("✅ Search OK. Waiting for results...")
            time.sleep(5)
            
            # 2. Get Product Containers (using the selector that worked)
            products = scraper.driver.find_elements(By.CSS_SELECTOR, "div[data-id]")
            
            if products:
                print(f"📦 Found {len(products)} products.")
                first_prod = products[0]
                
                # 3. Print Inner HTML
                print("\n" + "="*50)
                print("📜 HTML OF FIRST PRODUCT:")
                print("="*50)
                # OuterHTML gives us the container class too
                print(first_prod.get_attribute('outerHTML'))
                print("="*50 + "\n")
                
                # 4. Try Extracting Text
                print(f"📄 Text Content: {first_prod.text}")
                
            else:
                print("❌ No product containers found.")
        else:
            print("❌ Search failed.")
            
    except Exception as e:
        print(f"💥 Error: {e}")
    finally:
        scraper.close()

if __name__ == "__main__":
    debug_flipkart_html()