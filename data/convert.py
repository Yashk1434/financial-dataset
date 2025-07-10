import os
from selenium import webdriver
from PIL import Image
import time

# Set up headless Chrome
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--window-size=1200x2000')

driver = webdriver.Chrome(options=options)

# Path to folder containing HTML files
folder_path = "./"

for subfolder in os.listdir(folder_path):
    subfolder_path = os.path.join(folder_path, subfolder)
    if os.path.isdir(subfolder_path):
        for file in os.listdir(subfolder_path):
            if file.endswith(".html"):
                html_path = os.path.abspath(os.path.join(subfolder_path, file))
                image_path = os.path.join(subfolder_path, os.path.splitext(file)[0] + ".png")

                try:
                    # Load HTML file
                    driver.get("file:///" + html_path)
                    time.sleep(2)

                    # Screenshot and save
                    driver.save_screenshot(image_path)
                    print(f"✅ Converted: {file} → {image_path}")

                except Exception as e:
                    print(f"❌ Error converting {file}: {e}")

driver.quit()
print("🎉 All HTML files converted successfully!")
