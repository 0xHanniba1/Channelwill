#!/usr/bin/env python
# -*- coding: utf-8 -*-
from src.core.base_page import BasePage
from selenium.webdriver.common.by import By


class HeaderPage(BasePage):
    """顶部导航栏相关功能"""

    # 定位器
    LOGO = (By.XPATH, "//header/div/div/div[1]/a/img")
    PRODUCT_MENU = (By.XPATH, "//button[normalize-space(text())='产品']")
    CUSTOMER_CASE = (By.XPATH, "//header/div/div/div[1]/div/nav[1]/a[1]")
    RESOURCE_CENTER = (By.XPATH, "//button[normalize-space(text())='资源中心']")
    PRICING = (By.XPATH, "//header/div/div/div[1]/div/nav[2]/ul/li[4]/a")
    LANGUAGE_SWITCH = (By.XPATH, "//header/div/div/div[3]/div/div/div/span/span[2]/div/span")
    BOOK_DEMO = (By.XPATH, "//header/div/div/div[3]/a/div/span")

    # 弹出菜单标题
    PRODUCT_MENU_TITLE = (By.XPATH, "//div[contains(@class,'mb-1') and contains(@class,'text-md')]")
    PRODUCT_MENU_SUBTITLE = (By.XPATH, "//p[contains(@class, 'text-sm') and contains(@class, 'font-regular')]")


    def check_product_menu(self):
        self.hover_over_element(self.PRODUCT_MENU)
        self.wait_for_element_visible(self.PRODUCT_MENU_TITLE)

    def get_product_menu_titles(self):
        """获取'产品'菜单下的选项主题"""
        elements = self.find_elements(self.PRODUCT_MENU_TITLE)
        return [elem.text for elem in elements]

    def get_product_menu_subtitles(self):
        elements = self.find_elements(self.PRODUCT_MENU_SUBTITLE)
        return [elem.text for elem in elements]

    def get_product_menu_title_subtitle_dict(self):
        titles = self.get_product_menu_titles()
        subtitles = self.get_product_menu_subtitles()

        return {title: subtitle for title, subtitle in zip(titles, subtitles)}

    @staticmethod
    def get_product_menu_item_locator(title):
        """生成特定标题的定位器"""
        locator = (By.XPATH, f'//div[contains(@class,"mb-1") and normalize-space(text())="{title}"]')
        return locator

    def click_product_menu_content(self, title):
        """点击产品菜单中的具体项目"""
        locator = self.get_product_menu_item_locator(title)
        self.find_element(locator).click()


# from selenium import webdriver
# from config.conf import Config
#
# driver = webdriver.Chrome()
# driver.get(Config.BASE_URL)
# a = HeaderPage(driver)
# a.check_product_menu()
#
#
# a.click_product_menu_content('订单追踪')
# parcelpanel
# print(a.get_product_menu_title_subtitle_dict())
# print(a.get_product_menu_titles())
# print(a.get_product_menu_subtitles())
