#!/usr/bin/env python
# -*- coding: utf-8 -*-
from src.core.base_page import BasePage
from selenium.webdriver.common.by import By


class ContactSalesPage(BasePage):
    # 预约演示页面

    NAME = (By.XPATH, "//*[@id='book-demo_firstname']")
    EMAIL = (By.XPATH, "//*[@id='book-demo_email']")
    WEB_URL = (By.XPATH, "//*[@id='book-demo_website']")
    PRODUCT = (By.XPATH, "//*[@id='book-demo']/div[3]/div[1]/div[2]/div[1]/div/div/div/span/div")
    NOTES = (By.XPATH, "//*[@id='book-demo_anything_else_you_think_we_should_know_about_you']")
    AGREEMENT = (By.XPATH, "//*[@id='book-demo_agreement']")
    BOOK_DEMO = (By.XPATH, "//body/div[1]/div[2]/div/div/div[2]/div/button")


    def submit_book_demo(self, name, email, web_url, product_name, notes=None):
        self.input_text(self.NAME, name)
        self.input_text(self.EMAIL, email)
        self.input_text(self.WEB_URL, web_url)
        # self.click(self.PRODUCT)
        # self.click(product_option)

        self.input_text(self.NOTES, notes)
        # element_to_be_clickable无效，直接点击
        elem = self.find_element(self.AGREEMENT)
        elem.click()
        self.click(self.BOOK_DEMO)



from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.channelwill.com/zh/contact-sales/")

a = ContactSalesPage(driver)
a.submit_book_demo("zk123", "123@gmail.com", "www.baidu123.com", "订单追踪", "备注123")
# driver.quit()