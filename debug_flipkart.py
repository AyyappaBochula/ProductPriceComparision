# debug_flipkart.py
import os
import sys

# Debug the flipkart_scraper file
file_path = os.path.join('scraper', 'flipkart_scraper.py')
print(f"Checking file: {file_path}")

# Read the file content
with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    print("First 10 lines of file:")
    for i, line in enumerate(lines[:10], 1):
        print(f"{i}: {line.strip()}")

# Try to import
try:
    from scraper.flipkart_scraper import FlipkartScraper
    print("✅ SUCCESS: FlipkartScraper imported successfully!")
    
    # Test the scraper
    scraper = FlipkartScraper()
    print("✅ Scraper created successfully!")
    scraper.close()
    
except Exception as e:
    print(f"❌ Import failed: {e}")