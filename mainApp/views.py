from django.shortcuts import render,redirect
from .models import Search
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

# GOOGLE_CHROME_PATH = '/app/.apt/usr/bin/google_chrome'
# CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'

# CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'
# GOOGLE_CHROME_BIN = '/app/.apt/usr/bin/google-chrome'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.binary_location = os.environ.get('GOOGLE_CHROME_BIN')

# driver = webdriver.Chrome(executable_path=os.environ.get('CHROMEDRIVER_PATH'), chrome_options=chrome_options)
# driver.get('https://stackoverflow.com/')


# driver.quit()



def index(request):
    if request.method == 'POST':
        word = request.POST.get('nameword')
        obj = Search()
        obj.word = word
        print(word)
        driver = webdriver.Chrome(executable_path=os.environ.get('CHROMEDRIVER_PATH'), chrome_options=chrome_options)

        # driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get('https://stackoverflow.com')

        search = driver.find_element_by_name('q')
        search.send_keys(word)
        search.send_keys(Keys.RETURN)


        result_links = driver.find_elements_by_css_selector("[class='question-hyperlink']")
        for link in result_links:
            link.send_keys(Keys.CONTROL + 't', Keys.RETURN)
            
    return render(request, template_name='index.html')




