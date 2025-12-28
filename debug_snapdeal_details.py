from scraper.snapdeal_scraper import SnapdealScraper
from selenium.webdriver.common.by import By
import time

def debug_snapdeal_html():
    print("🕵️ Debugging Snapdeal Product HTML...")
    scraper = SnapdealScraper()
    
    try:
        # 1. Search
        if scraper.search_product("watch for men"):
            print("✅ Search OK. Waiting for results...")
            time.sleep(5)
            
            # 2. Get Product Containers
            products = scraper.driver.find_elements(By.CSS_SELECTOR, "div.product-tuple-listing")
            
            if products:
                print(f"📦 Found {len(products)} products.")
                first_prod = products[0]
                
                # 3. Print Inner HTML of the first product
                print("\n" + "="*50)
                print("📜 HTML OF FIRST PRODUCT:")
                print("="*50)
                print(first_prod.get_attribute('innerHTML'))
                print("="*50 + "\n")
                
                # 4. Try Extracting Text
                print(f"📄 Full Text Content: {first_prod.text}")
                
            else:
                print("❌ No product containers found to debug.")
        else:
            print("❌ Search failed.")
            
    except Exception as e:
        print(f"💥 Error: {e}")
    finally:
        scraper.close()

if __name__ == "__main__":
    debug_snapdeal_html()