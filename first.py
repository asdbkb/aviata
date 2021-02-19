import unittest
from selenium import webdriver
import time
PATH = "C:\Program Files (x86)\chromedriver.exe"

class testAviata(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(PATH)

    def test_aviata(self):
        driver = self.driver
        driver.get("https://aviata.kz/")

        driver.find_element_by_xpath("/html/body/div[5]/form/div/div[2]/div[1]/div[1]/span[2]")
        # Популярные города "Откуда"

        driver.find_element_by_xpath("/html/body/div[5]/form/div/div[2]/div[1]/div[2]/span[2]")
        # Популярные города "Куда"

        driver.find_element_by_xpath("/html/body/div[5]/form/div/div[2]/div[1]/div[1]/span[2]/a[1]").click()
        # Нажимаем на первый город из популярных городов "Откуда"

        driver.find_element_by_xpath("/html/body/div[5]/form/div/div[2]/div[1]/div[2]/span[2]/a[1]").click()
        # Нажимаем на первый город из популярных городов "Куда"

        driver.find_element_by_xpath("/html/body/div[5]/form/div/div[4]/div/button").click()
        # Нажимаем на кнопку "Найти билеты"

        time.sleep(60)
        # Ждём пока идёт поиск

        driver.find_element_by_xpath('//*[@id="app"]/div/main/div[1]/div[3]/div[2]/div/div[2]')
        driver.find_element_by_xpath('//*[@id="app"]/div/main/div[1]/div[3]/div[2]/div/div[3]')
        # Проверяем наличие первых двух рейсов в списке найденных рейсов

        # 1
        # 2



    def tearDown(self):
        self.driver.close()
