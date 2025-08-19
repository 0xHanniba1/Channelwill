#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from src.pages.header_page import HeaderPage
from loguru import logger
import pytest
from config.conf import Config


class TestHeaderMenu:
    """顶部菜单栏测试"""

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        driver.get(Config.BASE_URL)
        self.header = HeaderPage(driver)
        self.driver = driver

    def test_product_menu_hover(self):
        # 悬停在产品菜单
        self.header.hover_over_element(self.header.PRODUCT_MENU)
        dropdown = self.header.wait_for_element_visible(self.header.PRODUCT_DROPDOWN_MENU, timeout=10)
        # 验证弹出菜单
        assert dropdown.is_displayed()

        # 移开鼠标
        self.header.move_to_element(self.header.RESOURCE_CENTER)
        time.sleep(1)
        assert not dropdown.is_displayed()

    def test_product_dropdown_menu_content(self):
        logger.info("测试产品弹出菜单的内容")
        self.header.hover_over_element(self.header.PRODUCT_MENU)

        # 验证菜单内容
        expected = ['订单追踪', '自动退换货', '运输保障', '评论&UGC', '会员积分', '多语言翻译', 'SEO&速度优化']
        # self.header.wait_for_element_visible(self.header.PRODUCT_MENU_TITLE)
        content = self.header.find_elements(self.header.PRODUCT_MENU_TITLE)
        actual_content = [title.text for title in content]

        assert expected == actual_content
        logger.info(f"actual_content: {actual_content}")

    def test_product_order_tracking(self):
        logger.info("测试订单追踪")
        self.header.hover_over_element(self.header.PRODUCT_MENU)

        # 验证title 和 subtitle
        title = self.header.find_element(self.header.ORDER_TRACKING_TITLE)
        subtitle = self.header.find_element(self.header.ORDER_TRACKING_SUBTITLE)
        assert title.text == "订单追踪"
        assert subtitle.text == "提供优质的的售后物流追踪体验"

        # 验证点击跳转
        self.header.click(self.header.ORDER_TRACKING)
        assert self.header.wait_for_url("/parcelpanel", timeout=10)
