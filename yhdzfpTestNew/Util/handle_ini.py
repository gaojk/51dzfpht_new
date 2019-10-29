import os
import sys
import configparser
base_path = os.getcwd()
sys.path.append(base_path)

#定义获取ini配置文件方法的类
class HandleINI():
    def load_ini(self):
        '''加载配置文件ini'''
        config = configparser.ConfigParser()
        file_path = 'C:/Users/Charseki\Desktop\yhdzfpTestNew\yhdzfpTestNew\Config/server.ini'
        config.read(file_path, encoding='utf-8-sig')
        return config

    def get_ini_value(self, option, sections=None):
        '''获取配置文件ini内容'''
        if sections == None:
            sections = 'server'
        config = self.load_ini()
        try:
            data = config.get(sections, option)
        except Exception:
            print('没有获取到值')
            data = None
        return data

get_ini = HandleINI()

# if __name__ == '__main__':
#     aa = get_ini.get_ini_value('host_yhdzfp')
#     print(aa)
#     bb = get_ini.get_ini_value('host_51dzfpht_new')
#     print(bb)




