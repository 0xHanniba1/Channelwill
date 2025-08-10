#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.pages.header_page import HeaderPage
from loguru import logger
import pytest
from config.conf import Config


class TestHeaderMenu:
    """顶部菜单栏测试"""

    # 测试数据配置
    EXPECTED_MENU_DATA = {
        '订单追踪': {
            'subtitle': '提供优质的的售后物流追踪体验',
            'url_fragment': 'parcelpanel'
        },
        '自动退换货': {
            'subtitle': '简化流程管理并将退货转化为换货',
            'url_fragment': 'parcelpanel-returns'
        },
        '运输保障': {
            'subtitle': '无忧配送，让消费者更放心',
            'url_fragment': 'shopping-protection'
        },
        '评论&UGC': {
            'subtitle': '将首次购买客户转变为品牌的忠实粉丝',
            'url_fragment': 'trustoo-io'
        },
        '会员积分': {
            'subtitle': '提供一体化忠诚度解决方案，让用户从“喜欢”到“热爱”',
            'url_fragment': 'loloyal'
        },
        '多语言翻译': {
            'subtitle': '打破语言界限，轻松打开全球市场',
            'url_fragment': 'langwill'
        },
        'SEO&速度优化': {
            'subtitle': '改善网站SEO，提高网站排名，在竞争中脱颖而出',
            'url_fragment': 'seoant'
        }
    }

    def test_product_menu_content(self, driver):
        """测试产品菜单的内容是否正确显示"""
        logger.info("测试产品菜单内容显示")

        driver.get(Config.BASE_URL)
        header = HeaderPage(driver)
        header.check_product_menu()

        actual_data = header.get_product_menu_title_subtitle_dict()
        expected_data = {title: data['subtitle'] for title, data in self.EXPECTED_MENU_DATA.items()}

        logger.debug(f"实际菜单数据: {actual_data}")
        logger.debug(f"期望菜单数据: {expected_data}")

        assert actual_data == expected_data, f"菜单内容不匹配\n实际: {actual_data}\n期望: {expected_data}"

    @pytest.mark.parametrize("title,data",
                             [(title, data) for title, data in EXPECTED_MENU_DATA.items()],
                             ids=[title for title in EXPECTED_MENU_DATA.keys()])
    def test_product_menu_navigation(self, driver, title, data):
        """测试产品菜单各项的导航功能"""
        logger.info(f"测试产品菜单项导航: {title}")

        driver.get(Config.BASE_URL)
        header = HeaderPage(driver)

        # 显示产品菜单
        header.check_product_menu()

        # 点击菜单项
        header.click_product_menu_content(title)

        # 验证页面跳转
        url_fragment = data['url_fragment']
        success = header.wait_for_url(url_fragment, timeout=10)

        if not success:
            current_url = driver.current_url
            logger.error(f"导航失败 - 菜单项: {title}, 期望URL包含: {url_fragment}, 当前URL: {current_url}")

        assert success, f"点击'{title}'后，页面未跳转到包含'{url_fragment}'的URL"

    def test_product_menu_hover_behavior(self, driver):
        """测试产品菜单的悬停行为"""
        logger.info("测试产品菜单悬停行为")

        driver.get(Config.BASE_URL)
        header = HeaderPage(driver)

        # 验证菜单默认不可见
        assert not header.is_element_visible(header.PRODUCT_MENU_TITLE), "菜单应该默认隐藏"

        # 悬停后菜单应该可见
        header.check_product_menu()
        assert header.is_element_visible(header.PRODUCT_MENU_TITLE), "悬停后菜单应该显示"

        logger.info("产品菜单悬停行为测试通过")

    @pytest.mark.smoke
    def test_product_menu_basic_functionality(self, driver):
        """冒烟测试：验证产品菜单基本功能"""
        logger.info("执行产品菜单冒烟测试")

        driver.get(Config.BASE_URL)
        header = HeaderPage(driver)

        # 基本功能验证
        header.check_product_menu()
        titles = header.get_product_menu_titles()

        assert len(titles) > 0, "产品菜单应该包含至少一个选项"
        assert len(titles) == len(
            self.EXPECTED_MENU_DATA), f"菜单项数量不匹配，期望{len(self.EXPECTED_MENU_DATA)}个，实际{len(titles)}个"

        logger.info(f"产品菜单包含 {len(titles)} 个选项，冒烟测试通过")
