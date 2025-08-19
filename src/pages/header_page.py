#!/usr/bin/env python
# -*- coding: utf-8 -*-
from src.core.base_page import BasePage
from selenium.webdriver.common.by import By


class HeaderPage(BasePage):
    """顶部导航栏相关功能"""

    LOGO = (By.CSS_SELECTOR, "a.flex-center[href='/zh/'] img[alt='channelwill-logo']")
    PRODUCT_MENU = (By.XPATH, "//header/div/div/div[1]/div/nav[2]/ul/li[1]/button")
    CUSTOMER_CASE = (By.XPATH, "//header/div/div/div[1]/div/nav[1]/a[1]")
    RESOURCE_CENTER = (By.XPATH, "//header/div/div/div[1]/div/nav[2]/ul/li[3]/button")
    PRICING = (By.XPATH, "//header/div/div/div[1]/div/nav[2]/ul/li[4]/a")
    LANGUAGE_SWITCH = (By.XPATH, "//header/div/div/div[3]/div/div/div/span/span[2]/div/span")
    BOOK_DEMO = (By.XPATH, "//header/div/div/div[3]/a/div/span")

    PRODUCT_MENU_TITLE = (By.CSS_SELECTOR, "div.font-semibold.text-md.mb-1")
    RESOURCE_CENTER_TITLE = (By.XPATH, "p.test-sm.font-regular")

    PRODUCT_DROPDOWN_MENU = (By.XPATH, "//header/div/div/div[1]/div/nav[2]/ul/li[1]/div/div/div/main/div")

    ORDER_TRACKING = (By.XPATH, "//header//main/div/div/div[1]/div[1]/div[2]/a[1]")
    ORDER_TRACKING_TITLE = (By.XPATH, "//header//main/div/div/div[1]/div[1]/div[2]/a[1]/div[2]/div")
    ORDER_TRACKING_SUBTITLE = (By.XPATH, "//header//main/div/div/div[1]/div[1]/div[2]/a[1]/div[2]/p")

    @staticmethod
    def product_menu_title(title):
        locator = (
            By.XPATH,
            f"//div[contains(@class, 'font-semibold') and contains(@class, 'text-md') "
            f"and normalize-space(.)='{title}']"
        )
        return locator

    @staticmethod
    def product_menu_subtitle(subtitle):
        locator = (
            By.XPATH,
            f"//p[contains(@class, 'text-sm') and contains(@class, 'font-regular') "
            f"and normalize-space(.)='{subtitle}']"
        )
        return locator

    @staticmethod
    def resource_center_item(item):
        locator = (
            By.XPATH,
            f"//a[contains(@class, 'rounded-sm') and contains(@class, 'px-3') "
            f"and normalize-space(.)='{item}']"
        )
        return locator

#     def check_product_menu(self):
#         self.hover_over_element(self.PRODUCT_MENU)
#         self.wait_for_element_visible(self.PRODUCT_MENU_TITLE)
#
#
# from selenium import webdriver
# from config.conf import Config
#
# driver = webdriver.Chrome()
# driver.get(Config.BASE_URL)
#
# a = HeaderPage(driver)
# print(a.product.text)
# driver.quit()
# a.check_product_menu()
#
#
# a.click_product_menu_content('订单追踪')
# parcelpanel
# print(a.get_product_menu_title_subtitle_dict())
# print(a.get_product_menu_titles())
# print(a.get_product_menu_subtitles())
