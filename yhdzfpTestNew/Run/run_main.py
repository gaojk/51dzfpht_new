import os
import sys
import json
import requests
from yhdzfpTestNew.Util.handle_excel import get_excel
from yhdzfpTestNew.Util.handle_ini import get_ini
from yhdzfpTestNew.Util.handle_nsrsbh import Get_blrzj, Get_blrmc, Get_nsrsbh, Get_blrsj, Get_blryx, Get_nsrmc
base_path = os.getcwd()
sys.path.append(base_path)
url = get_ini.get_ini_value('host_51dzfpht_new') + get_excel.get_cell_value(2, 4)
headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
data = json.loads(get_excel.get_cell_value(2, 8))
data['nsrsbh'] = Get_nsrsbh.get_nsrsbh()
data['nsrmc'] = Get_nsrmc.get_nsrmc()
data['blrmc'] = Get_blrmc.get_blrmc()
data['blrsj'] = Get_blrsj.get_blrsj()
data['blryx'] = Get_blryx.get_blryx()
data['blrzj'] = Get_blrzj.get_blrzj()
print("新增的纳税人识别号为：", data['nsrsbh'])
r = requests.post(url=url, data=data, headers=headers).text
print(r)