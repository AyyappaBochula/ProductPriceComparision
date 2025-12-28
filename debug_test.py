# debug_test.py
import os
import sys

# Debug: Check what's in the amazon_scraper file
file_path = os.path.join('scraper', 'amazon_scraper.py')
print(f"Reading file: {file_path}")

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()
    print("File content:")
    print("=" * 50)
    print(content)
    print("=" * 50)

# Try to import
try:
    from scraper.amazon_scraper import AmazonScraper
    print("✅ SUCCESS: Import worked!")
    
    # Test the scraper
    scraper = AmazonScraper()
    print("✅ Scraper created successfully!")
    scraper.close()
    
except Exception as e:
    print(f"❌ Import failed: {e}")