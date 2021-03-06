# -*- coding:utf-8 -*-
# @Author: hectorqiu (hectorqiuiscool@gmail.com)
# @Date: 2019-11-15 17:43:55
# @Last Modified By: hectorqiu (hectorqiuiscool@gmail.com>)
# @Last Modified: 2019-11-15 17:43:57

from flask import Flask, jsonify
from utils.device import device_model_helper

app = Flask(__name__)


@app.route('/api/device/<model>')
def get_device_info(model: str):
    """根据型号代号获取设备信息"""
    if model:
        brand, name = device_model_helper.get_brand_and_name(model)

    resp_dict = {
        'model': model,
        'brand': brand,
        'name': name
    }

    return jsonify(resp_dict)

