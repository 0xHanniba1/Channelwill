#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Config:
    """测试配置类"""

    BASE_URL = "https://www.channelwill.com/zh/"
    # USERNAME = "standard_user"
    # PASSWORD = "secret_sauce"

    # 根据环境扩展
    ENVIRONMENTS = {
        'dev': "https://www.channelwill.com/zh/",
        'staging': "https://www.channelwill.com/zh/",
        'prod': "https://www.channelwill.com/zh/"
    }

    @classmethod
    def get_url(cls, env=None):
        """获取对应环境的 URL"""
        if env and env in cls.ENVIRONMENTS:
            return cls.ENVIRONMENTS[env]
        return cls.BASE_URL