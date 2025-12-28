# test_flipkart.py
from scraper.flipkart_scraper import FlipkartScraper

def test_flipkart():
    print("🧪 Testing Flipkart Scraper (Universal)...")
    
    scraper = FlipkartScraper()
    
    try:
        # Ab hum 'Watch' search karke dekhenge ki naya logic chal raha hai ya nahi
        product_name = "analog watch for men" 
        print(f"🔍 Searching for: {product_name}")
        
        if scraper.search_product(product_name):
            print("✅ Search successful!")
            
            # Products extract karein
            products = scraper.get_product_details(max_products=5)
            
            print(f"\n📦 Found {len(products)} products:")
            for i, product in enumerate(products, 1):
                print(f"{i}. {product['name'][:40]}... | ₹{product['price']}")
                print(f"   Image: {product['image'][:60]}..." if product['image'] else "   Image: None")
        else:
            print("❌ Search failed")
            
    except Exception as e:
        print(f"💥 Error: {e}")
    
    finally:
        scraper.close()
        print("Test complete!")

if __name__ == "__main__":
    test_flipkart()