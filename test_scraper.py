# test_scraper.py
from scraper.base_scraper import BaseScraper

def test_base_scraper():
    print("🚀 Testing Base Scraper...")
    
    # Scraper create karein
    scraper = BaseScraper()
    
    try:
        # Ek test website open karein
        print("Opening website...")
        scraper.driver.get("https://httpbin.org/user-agent")
        
        # Page ka title print karein
        print(f"Page Title: {scraper.driver.title}")
        
        # Random delay (anti-blocking)
        scraper.random_delay(2, 3)
        
        # Page content dekhein
        page_content = scraper.driver.page_source
        if "user-agent" in page_content.lower():
            print("✅ SUCCESS: Scraper working perfectly!")
        else:
            print("❌ Something went wrong")
            
    except Exception as e:
        print(f"❌ Error: {e}")
    
    finally:
        # Browser band karein
        scraper.close()
        print("Test complete!")

if __name__ == "__main__":
    test_base_scraper()