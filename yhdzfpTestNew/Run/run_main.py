import os
import sys
import json
from yhdzfpTestNew.Util.handle_excel import get_excel
from yhdzfpTestNew.Util.handle_nsrsbh import Get_blrzj, Get_blrmc, Get_nsrsbh, Get_blrsj, Get_blryx, Get_nsrmc
from yhdzfpTestNew.Base.base_request import send_request

base_path = os.getcwd()
sys.path.append(base_path)

class RunMain:

    def run_case(self):
        rows = get_excel.get_rows_count()
        for i in range(rows):
            excel_data = get_excel.get_rows_value(i+2)
            is_run = excel_data[2]
            if is_run == 'yes':
                data = json.loads(excel_data[7], encoding=False)
                data['nsrsbh'] = Get_nsrsbh.get_nsrsbh()
                print("办理人纳税识别号为：", data['nsrsbh'])
                data['nsrmc'] = Get_nsrmc.get_nsrmc()
                data['blrmc'] = Get_blrmc.get_blrmc()
                data['blrsj'] = Get_blrsj.get_blrsj()
                data['blryx'] = Get_blryx.get_blryx()
                data['blrzj'] = Get_blrzj.get_blrzj()
                data['blrzjhm'] = Get_blrzj.get_blrzj()
                method = excel_data[4]
                url = excel_data[3]
                res = send_request.run_main(method, url, data,)
                print(res)

if __name__ == '__main__':
    run = RunMain()
    run.run_case()