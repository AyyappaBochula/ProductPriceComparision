from scraper.flipkart_scraper import FlipkartScraper
from selenium.webdriver.common.by import By
import time

def debug_iphone():
    print("🕵️ Debugging Flipkart iPhone HTML...")
    scraper = FlipkartScraper()
    
    try:
        # Search for iPhone specifically
        if scraper.search_product("iphone 15"):
            print("✅ Search OK. Waiting for results...")
            time.sleep(5)
            
            # Find ANY product container (using generic selector)
            products = scraper.driver.find_elements(By.CSS_SELECTOR, "div[data-id]")
            
            if products:
                print(f"📦 Found {len(products)} items.")
                first_prod = products[0]
                
                print("\n" + "="*50)
                print("📜 HTML OF FIRST IPHONE RESULT:")
                print("="*50)
                # Print HTML to identify classes
                print(first_prod.get_attribute('outerHTML')[:2000]) # First 2000 chars is enough
                print("="*50 + "\n")
                
                print(f"📄 Text: {first_prod.text[:100]}...")
            else:
                print("❌ No products found.")
        else:
            print("❌ Search failed.")
            
    except Exception as e:
        print(f"💥 Error: {e}")
    finally:
        scraper.close()

if __name__ == "__main__":
    debug_iphone()