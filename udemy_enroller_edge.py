# Install all the requirements by running requirements.py in IDLE or follow the alternate instructions at
# https://github.com/aapatre/Automatic-Udemy-Course-Enroller-GET-PAID-UDEMY-COURSES-for-FREE/ Make sure you have
# cleared all saved payment details on your Udemy account & the browser!
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from core import Settings
from core.utils import redeem_courses

settings = Settings()

driver = webdriver.Edge(EdgeChromiumDriverManager().install())

# Maximizes the browser window since Udemy has a responsive design and the code only works
# in the maximized layout
driver.maximize_window()

redeem_courses(driver, settings)
