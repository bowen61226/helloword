
import win32com.client

dm=win32com.client.Dispatch('dm.dmsoft')#调用大漠插件，获取大漠对象

print(dm.ver())#输出大漠版本号