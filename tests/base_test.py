from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium import webdriver
from time import sleep
import unittest
from pages.home_page import HomePage


class BaseTest(unittest.TestCase):

    """
    Best Test for each Test Case
    """
    def setUp(self): #przygotowanie do testu
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://localhost:8080")
        self.home_page = HomePage(self.driver)

    def tearDown(self):
        self.driver.quit()

