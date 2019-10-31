import os
import sys
import random
base_path = os.getcwd()
sys.path.append(base_path)

#定义一些变量的方法
class HandleNumber():
    def get_nsrsbh(self, nsrsbh=None):
        '''随机生成15位纳税人识别号'''
        if nsrsbh == None:
            nsrsbh = "3302019" + str(random.randint(10000000, 99999999))
        else:
            nsrsbh = nsrsbh
        return nsrsbh

    def get_nsrmc(self):
        '''随机生成纳税人名称'''
        nsrmc = "Name_" + str(random.randint(1000, 9999))
        return nsrmc

    def get_blrsj(self):
        '''随机生成11位手机号'''
        blrsjh = "138" + str(random.randint(10000000, 99999999))
        return blrsjh

    def get_blrmc(self):
        '''随机生成办理人名称'''
        blrmc = "ApiTest_" + str(random.randint(1000, 9999))
        return blrmc

    def get_blrzj(self):
        '''随机生成18位办理人证件号码'''
        blrzj = "3302274991" + str(random.randint(10000000, 99999999))
        return blrzj
    def get_blryx(self):
        '''写死办理人邮箱'''
        blryx = "364942727@qq.com"
        return blryx
#实例化类
Get_nsrsbh = HandleNumber()
Get_nsrmc = HandleNumber()
Get_blrsj = HandleNumber()
Get_blrmc = HandleNumber()
Get_blrzj = HandleNumber()
Get_blryx = HandleNumber()

# if __name__ == '__main__':
#     aa = Get_nsrsbh.get_nsrsbh('9133028255795774XU')
#     print(aa)
#     bb = Get_blrsj.get_blrsj()
#     print(bb)
#     cc = Get_blrmc.get_blrmc()
#     print(cc)
#     dd = Get_blrzj.get_blrzj()
#     print(dd)
#     ee = Get_nsrmc.get_nsrmc()
#     print(ee)
#     ff = Get_blryx.get_blryx()
#     print(ff)
