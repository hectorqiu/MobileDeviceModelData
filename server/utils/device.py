# -*- coding:utf-8 -*-
# @Author: hectorqiu (hectorqiuiscool@gmail.com)
# @Date: 2019-11-15 17:47:00
# @Last Modified By: hectorqiu (hectorqiuiscool@gmail.com>)
# @Last Modified: 2019-11-15 17:47:04

import os
from typing import Tuple


class DeviceModelHelper:
    """设备型号助手类，用于把设备型号转换成功品牌、名称"""

    _cache = {}

    def __init__(self):
        self.reload()

    def reload(self):
        mobile_txt_path = 'data/mobile.txt'
        self._cache = self.load_mobile_model_dict(mobile_txt_path)

    def get_brand_and_name(self, model: str) -> Tuple[str, str]:
        """获取型号对应的品牌和设备名称

        Returns:
            (brand, name) or (None, None) if not exists
        """
        arr = self._cache.get(model)

        if arr:
            model, name, brand = arr
            return (brand, name)
        return (None, None)

    @staticmethod
    def load_mobile_model_dict(mobile_txt_path):

        d = {}
        with open(mobile_txt_path, 'r') as f:
            for line in f:
                if line.startswith('#'):
                    continue
                arr = line.strip().split(":")

                if len(arr) == 3:
                    model, name, brand = arr
                    d[model] = arr
        return d


device_model_helper = DeviceModelHelper()
