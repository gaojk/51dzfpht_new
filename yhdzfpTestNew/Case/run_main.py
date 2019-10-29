


import json
import requests

headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}
data = {
    "nsrsbh": nsrsbh,
    "nsrmc": "接口测试" + nsrsbh,
    "blrmc": "办理人名称",
    "blrsj": mobile,
    "blryx": "办理人邮箱",
    "blrzj": "办理人证件号码"
    }