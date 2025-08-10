#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    """全局的 driver fixture"""
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
