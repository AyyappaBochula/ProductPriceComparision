# test_amazon.py
from scraper.amazon_scraper import AmazonScraper
import time

def test_amazon():
    print("🧪 Testing Amazon Scraper...")
    
    scraper = AmazonScraper()
    
    try:
        product_name = "iphone 13"
        print(f"🔍 Searching for: {product_name}")
        
        start_time = time.time()
        
        # Test search
        if scraper.search_product(product_name):
            print("✅ Amazon search successful!")
            
            # Test product extraction
            products = scraper.get_product_details(max_products=3)
            
            end_time = time.time()
            print(f"⏱️  Time taken: {end_time - start_time:.2f} seconds")
            
            if products:
                print(f"✅ Amazon found {len(products)} products:")
                for i, product in enumerate(products, 1):
                    print(f"   {i}. {product['name']} - ₹{product['price']}")
                    print(f"      URL: {product['url'][:80]}...")
                    print(f"      Image: {product['image'][:50]}..." if product['image'] else "      Image: None")
            else:
                print("❌ Amazon found 0 products")
                
        else:
            print("❌ Amazon search failed")
            
    except Exception as e:
        print(f"💥 Error during Amazon test: {e}")
        
    finally:
        scraper.close()
        print("🧪 Amazon test completed!")

if __name__ == "__main__":
    test_amazon()