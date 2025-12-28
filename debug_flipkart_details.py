# debug_flipkart_details.py
from scraper.flipkart_scraper import FlipkartScraper
from selenium.webdriver.common.by import By
import time

def debug_details():
    print("🔍 Debugging Flipkart Product Details...")
    
    scraper = FlipkartScraper()
    
    try:
        product_name = "iphone 13"
        print(f"Searching for: {product_name}")
        
        if scraper.search_product(product_name):
            print("✅ Search successful!")
            
            # Wait for results
            scraper.random_delay(5, 7)
            
            # Save screenshot
            scraper.driver.save_screenshot("flipkart_debug.png")
            print("📸 Screenshot saved: flipkart_debug.png")
            
            # Get first product and debug it
            all_divs = scraper.driver.find_elements(By.TAG_NAME, "div")
            product_divs = [div for div in all_divs if div.get_attribute("data-id")]
            
            if product_divs:
                first_product = product_divs[0]
                print(f"\n🔍 Debugging first product:")
                print(f"Data-id: {first_product.get_attribute('data-id')}")
                print(f"Text content: {first_product.text[:200]}...")
                
                # Try to find name
                print("\n🔍 Looking for product name:")
                name_selectors = ["a.IRpwTa", "a._1fQZEK", "a.s1Q9rs", "div._4rR01T"]
                for selector in name_selectors:
                    try:
                        elem = first_product.find_element(By.CSS_SELECTOR, selector)
                        print(f"✅ Found with '{selector}': {elem.text}")
                    except:
                        print(f"❌ Not found with '{selector}'")
                
                # Try to find price
                print("\n🔍 Looking for product price:")
                price_selectors = ["div._30jeq3", "div._25b18c", "div._1_WHN1"]
                for selector in price_selectors:
                    try:
                        elem = first_product.find_element(By.CSS_SELECTOR, selector)
                        print(f"✅ Found with '{selector}': {elem.text}")
                    except:
                        print(f"❌ Not found with '{selector}'")
            
        else:
            print("❌ Search failed")
            
    except Exception as e:
        print(f"❌ Error: {e}")
    
    finally:
        scraper.close()
        print("Debug complete!")

if __name__ == "__main__":
    debug_details()