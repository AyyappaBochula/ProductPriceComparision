# debug_amazon.py
from scraper.amazon_scraper import AmazonScraper

def debug_amazon():
    print("🔍 Debugging Amazon...")
    
    scraper = AmazonScraper()
    
    try:
        # Just open Amazon and see what happens
        scraper.driver.get("https://www.amazon.in")
        scraper.random_delay(5, 7)
        
        print(f"Page Title: {scraper.driver.title}")
        print(f"Current URL: {scraper.driver.current_url}")
        
        # Check if we got redirected to captcha
        if "captcha" in scraper.driver.current_url.lower() or "robot" in scraper.driver.current_url.lower():
            print("❌ CAPTCHA detected!")
        else:
            print("✅ No CAPTCHA detected")
            
        # Save screenshot
        scraper.driver.save_screenshot("debug_amazon.png")
        print("📸 Screenshot saved as debug_amazon.png")
        
        # Try to find search box
        search_box = scraper.wait_for_element("#twotabsearchtextbox", timeout=10)
        if search_box:
            print("✅ Search box found")
        else:
            print("❌ Search box NOT found")
            
    except Exception as e:
        print(f"Error: {e}")
    
    finally:
        scraper.close()

if __name__ == "__main__":
    debug_amazon()