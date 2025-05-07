# import yaml
# import os

# # 获取当前工作目录
# config_path = os.path.join(os.getcwd(), 'config.yaml')

# # 读取配置文件
# with open(config_path, 'r') as f:
#     config = yaml.safe_load(f)

# # 读取配置
# username = config['General']['username']
# password = config['General']['password']
# theme = config['Settings']['theme']
# font_size = config['Settings']['font_size']

# print(f"Username: {username}, Password: {password}, Theme: {theme}, Font Size: {font_size}")


import configparser

# 创建配置解析器
config = configparser.ConfigParser()

# 读取配置文件
config.read('config.ini')

# 获取某个 section 下的键值
username = config.get('General', 'username')
password = config.get('General', 'password')
theme = config.get('Settings', 'theme')
font_size = config.getint('Settings', 'font_size')

# 输出读取的配置
print(f"Username: {username}, Password: {password}, Theme: {theme}, Font Size: {font_size}")

# 修改某个配置项
config.set('Settings', 'theme', 'light')

# 写回到配置文件
with open('config.ini', 'w') as configfile:
    config.write(configfile)
