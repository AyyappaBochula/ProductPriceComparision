# test_snapdeal.py
from scraper.snapdeal_scraper import SnapdealScraper
import time

def test_snapdeal():
    print("🧪 Testing Snapdeal Scraper (FIXED)...")
    
    scraper = SnapdealScraper()
    
    try:
        # Hum "watch for men" search karenge
        product_name = "watch for men" 
        
        print(f"🔍 Searching for: {product_name}")
        
        start_time = time.time()
        
        if scraper.search_product(product_name):
            print("✅ Snapdeal search successful!")
            
            products = scraper.get_product_details(max_products=3)
            
            end_time = time.time()
            print(f"⏱️  Time taken: {end_time - start_time:.2f} seconds")
            
            if products:
                print(f"✅ Snapdeal found {len(products)} products:")
                for i, product in enumerate(products, 1):
                    print(f"   {i}. {product['name'][:50]}... - ₹{product['price']}")
                    print(f"      URL: {product['url'][:80]}..." if product['url'] else "      URL: None")
                    print(f"      IMAGE: {product['image'][:80]}..." if product.get('image') else "      IMAGE: None")
            else:
                print("❌ Snapdeal found 0 products (Check scraper logic)")
        else:
            print("❌ Snapdeal search failed")

    except Exception as e:
        print(f"💥 Error: {e}")
        
    finally:
        scraper.close()
        print("🧪 Snapdeal test completed!")

if __name__ == "__main__":
    test_snapdeal()