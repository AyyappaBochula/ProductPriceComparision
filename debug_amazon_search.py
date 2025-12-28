# debug_amazon_search.py
from scraper.amazon_scraper import AmazonScraper
import time

def debug_amazon_search():
    print("🔍 Debugging Amazon Search...")
    
    scraper = AmazonScraper()
    
    try:
        product_name = "iphone 13"
        print(f"Searching for: {product_name}")
        
        if scraper.search_product(product_name):
            print("✅ Search successful!")
            
            # Wait a bit more
            scraper.random_delay(3, 5)
            
            # Get current URL and title
            print(f"Current URL: {scraper.driver.current_url}")
            print(f"Page Title: {scraper.driver.title}")
            
            # Check if we're on search results page
            if "field-keywords" in scraper.driver.current_url or "search" in scraper.driver.current_url:
                print("✅ On search results page")
            else:
                print("❌ Not on search results page")
            
            # Save multiple screenshots
            scraper.driver.save_screenshot("debug_search_results.png")
            print("📸 Screenshot saved: debug_search_results.png")
            
            # Try to find any products with simple selectors
            print("\n🔍 Looking for products with different selectors:")
            
            selectors_to_try = [
                "div.s-result-item",
                "div[data-component-type='s-search-result']",
                ".s-main-slot div",
                ".sg-col-inner",
                "div[data-asin]",
                ".s-card-container"
            ]
            
            for selector in selectors_to_try:
                try:
                    elements = scraper.driver.find_elements(By.CSS_SELECTOR, selector)
                    print(f"Selector '{selector}': Found {len(elements)} elements")
                    
                    # If we found elements, try to get text from first few
                    if elements and len(elements) > 0:
                        for i, elem in enumerate(elements[:2]):
                            try:
                                text = elem.text.replace('\n', ' ')[:100]
                                print(f"  Element {i}: {text}...")
                            except:
                                print(f"  Element {i}: [Could not get text]")
                            
                except Exception as e:
                    print(f"Selector '{selector}': Error - {e}")
            
            # Now try to get products with the main method
            print("\n🎯 Trying main product extraction...")
            products = scraper.get_product_details(max_products=3)
            
            print(f"\n📦 Final result: Found {len(products)} products")
            for product in products:
                print(f"   - {product['name']} | ₹{product['price']}")
                
        else:
            print("❌ Search failed")
            
    except Exception as e:
        print(f"❌ Error: {e}")
    
    finally:
        scraper.close()
        print("Debug complete!")

if __name__ == "__main__":
    debug_amazon_search()