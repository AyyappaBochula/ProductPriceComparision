# test_croma.py
from scraper.croma_scraper import CromaScraper
import time

def test_croma():
    print("🧪 Testing Croma Scraper...")
    
    scraper = CromaScraper()
    
    try:
        product_name = "iphone 13" # Croma par iPhone 13 milega
        print(f"🔍 Searching for: {product_name}")
        
        start_time = time.time()
        
        if scraper.search_product(product_name):
            print("✅ Croma search successful!")
            
            products = scraper.get_product_details(max_products=3)
            
            end_time = time.time()
            print(f"⏱️  Time taken: {end_time - start_time:.2f} seconds")
            
            if products:
                print(f"✅ Croma found {len(products)} products:")
                for i, product in enumerate(products, 1):
                    print(f"   {i}. {product['name']} - ₹{product['price']}")
                    print(f"      URL: {product['url'][:80]}...")
                    print(f"      IMAGE: {product['image'][:80]}..." if product.get('image') else "      IMAGE: None")
            else:
                print("❌ Croma found 0 products")
        else:
            print("❌ Croma search failed")

    except Exception as e:
        print(f"💥 Error: {e}")
        
    finally:
        scraper.close()
        print("🧪 Croma test completed!")

if __name__ == "__main__":
    test_croma()