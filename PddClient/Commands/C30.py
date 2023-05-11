import pyautogui
import pyperclip
import time

import urllib.request
from io import BytesIO
import win32clipboard
from PIL import Image




width, height = pyautogui.size() # 测量当前电脑屏幕的宽度和高度



def WeiXiao():

    pyautogui.click(TextSendXY)
    str1=' ☺ '           #"/:^_^🙂"
    pyperclip.copy(str1)
    pyautogui.hotkey('ctrl','v')
    pyautogui.press('enter') 
    time.sleep (0.3)

    Command_end()                           #------通用结尾操作----------#








# 自定义坐标:
#╔════════════════════════════════════════════════╗
if width == 2160: 
#判断为:  MateBook14
    #║发送图文对话，点击点。         
    TextSendXY = 1324,1200
    PingMu = '1213x110+613+35'
    print('判断为MateBook14，发送对话坐标为',TextSendXY)
    #║主界面，（视频按钮）。           
    sendVideoX,sendVideoY = 761,1022
    print('主界面，视频按钮，坐标为',sendVideoX,sendVideoY) 
    #║定位坐标:视频搜索框。             
    ShiPinSouSuoKuang = 1218,592
    print('视频搜索框，输入点:',ShiPinSouSuoKuang)
    #║定位坐标:视频发送按钮           
    videoFaSong = 760,783
    #║定位坐标:打包，邀请下单                           ║    
    YaoQingXiaDan = 1338,1020
    #║定位坐标:打包，邀请下单：“选择商品” 搜索框
    XuanZeShangPinSouSuoKuang = 969,352
    #║定位坐标:打包，邀请下单：加入清单
    JiaRuQingDan = 1000,540
    #║定位坐标:打包，邀请下单：加入清单,选择：第一个规格的商品
    XuanZeGuiGe = 800,668
    #║定位坐标:打包，邀请下单：加入清单,选择：第一个规格的商品,“确定”按钮
    XuanZeGuiGeQueding = 1368,1025
    #║定位坐标:打包，邀请下单：“发送”按钮
    DaBaoFaSong = 1600,1100
    #║设定客服软件字体大小:
    FontSize = 8                     
elif width == 1920:
#判断为:  MiBook Pro                   
    #║发送图文对话，点击点。        
        TextSendXY = 1270,960                      
        PingMu = '992x95+500+10'
        print('判断为MiBook Pro，发送对话坐标为',TextSendXY)       
    #║主界面，（视频按钮）。      
        sendVideoX,sendVideoY = 634,736
        print('主界面，视频按钮，坐标为',TextSendXY) 
    #║定位坐标:打包，邀请下单                           ║    
        YaoQingXiaDan = 1238,727
    #║定位坐标:打包，邀请下单：“选择商品” 搜索框
        XuanZeShangPinSouSuoKuang = 868,232
    #║定位坐标:打包，邀请下单：加入清单
        JiaRuQingDan = 870,390
    #║定位坐标:打包，邀请下单：加入清单,选择：第一个规格的商品
        XuanZeGuiGe = 720,500
    #║定位坐标:打包，邀请下单：加入清单,选择：第一个规格的商品,“确定”按钮
        XuanZeGuiGeQueding = 1200,800
    #║定位坐标:打包，邀请下单：“发送”按钮
        DaBaoFaSong = 1400,860
    #║设定客服软件字体大小:
        FontSize = 8    
elif width == 3840:
#判断为:  Mate Station X
    #║发送图文对话，点击点。                        ║
        TextSendXY = 2420,2280                   #║
        #智能显示AutoTalk，判断当前窗口是否是 客服客户端
        pix2 = pyautogui.pixel(68,30)       #定位屏幕左上角，判断当前界面客户端是: 拼多多 or 千牛
        #设定显示窗口大小和位置
        PingMu = '1992x194+1200+30'
        print('判断为Mate Station X，发送对话坐标为',TextSendXY)
    #║主界面，（视频按钮）。                        ║
        sendVideoX,sendVideoY = 1396,1787
        print('主界面，视频按钮，坐标为',sendVideoX,sendVideoY) 
    #║定位坐标:视频搜索框。                         ║
        ShiPinSouSuoKuang = 2258,1026
        print('视频搜索框，输入点:',ShiPinSouSuoKuang)
    #║定位坐标:视频发送按钮                         ║
        videoFaSong = 1398,1360
    #║定位坐标:打包，邀请下单                           ║    
        YaoQingXiaDan = 2338,1798
    #║定位坐标:打包，邀请下单：“选择商品” 搜索框
        XuanZeShangPinSouSuoKuang = 1700,600
    #║定位坐标:打包，邀请下单：加入清单
        JiaRuQingDan = 1735,951
    #║定位坐标:打包，邀请下单：加入清单,选择：第一个规格的商品
        XuanZeGuiGe = 1396,1186
    #║定位坐标:打包，邀请下单：加入清单,选择：第一个规格的商品,“确定”按钮
        XuanZeGuiGeQueding = 2446,1846
    #║定位坐标:打包，邀请下单：“发送”按钮
        DaBaoFaSong = 2885,1975
    #║设定客服软件字体大小:
        FontSize = 8    
elif width == 3600:
#判断为:  Mate Station B520
    #║发送图文对话，点击点。                        ║
        TextSendXY = 2275,2088                   #║
        #智能显示AutoTalk，判断当前窗口是否是 客服客户端
        pix2 = pyautogui.pixel(68,30)       #定位屏幕左上角，判断当前界面客户端是: 拼多多 or 千牛
        #设定显示窗口大小和位置
        PingMu = '1700x160+1100+75'
        print('判断为Mate Station B520，发送对话坐标为',TextSendXY)
    #║主界面，（视频按钮）。                        ║
        sendVideoX,sendVideoY = 1268,1705
        print('主界面，视频按钮，坐标为',sendVideoX,sendVideoY) 
    #║定位坐标:视频搜索框。                         ║
        ShiPinSouSuoKuang = 2038,977
        print('视频搜索框，输入点:',ShiPinSouSuoKuang)
    #║定位坐标:视频发送按钮                         ║
        videoFaSong = 1274,1291
    #║定位坐标:打包，邀请下单                           ║    
        YaoQingXiaDan = 2233,1704
    #║定位坐标:打包，邀请下单：“选择商品” 搜索框
        XuanZeShangPinSouSuoKuang = 1609,587
    #║定位坐标:打包，邀请下单：加入清单
        JiaRuQingDan = 1621,905
    #║定位坐标:打包，邀请下单：加入清单,选择：第一个规格的商品
        XuanZeGuiGe = 1323,1119
    #║定位坐标:打包，邀请下单：加入清单,选择：第一个规格的商品,“确定”按钮
        XuanZeGuiGeQueding = 2277,1713
    #║定位坐标:打包，邀请下单：“发送”按钮
        DaBaoFaSong = 2677,1839
    #║设定客服软件字体大小:
        FontSize = 8
elif width == 3120:
#判断为:  Mate Book14X Pro
    #║发送图文对话，点击点。                        ║
        TextSendXY = 2275,2088                   #║
        #智能显示AutoTalk，判断当前窗口是否是 客服客户端
        pix2 = pyautogui.pixel(68,30)       #定位屏幕左上角，判断当前界面客户端是: 拼多多 or 千牛
        #设定显示窗口大小和位置
        PingMu = '1700x160+1100+75'
        print('判断为Mate BookX Pro，发送对话坐标为',TextSendXY)
    #║主界面，（视频按钮）。                        ║
        sendVideoX,sendVideoY = 1268,1705
        print('主界面，视频按钮，坐标为',sendVideoX,sendVideoY) 
    #║定位坐标:视频搜索框。                         ║
        ShiPinSouSuoKuang = 2038,977
        print('视频搜索框，输入点:',ShiPinSouSuoKuang)
    #║定位坐标:视频发送按钮                         ║
        videoFaSong = 1274,1291
    #║定位坐标:打包，邀请下单                           ║    
        YaoQingXiaDan = 2233,1704
    #║定位坐标:打包，邀请下单：“选择商品” 搜索框
        XuanZeShangPinSouSuoKuang = 1609,587
    #║定位坐标:打包，邀请下单：加入清单
        JiaRuQingDan = 1621,905
    #║定位坐标:打包，邀请下单：加入清单,选择：第一个规格的商品
        XuanZeGuiGe = 1323,1119
    #║定位坐标:打包，邀请下单：加入清单,选择：第一个规格的商品,“确定”按钮
        XuanZeGuiGeQueding = 2277,1713
    #║定位坐标:打包，邀请下单：“发送”按钮
        DaBaoFaSong = 2677,1839
    #║设定客服软件字体大小:
        FontSize = 8   
else: 
    print("自定义坐标：这台电脑的型号没有检测到。")
#╚════════════════════════════════════════════════╝


# 自定义函数:
#╔════════════════════════════════════════════════╗
def Command_end():
    #判断为:  MateBook14
        if width == 2160:
            pix2 = pyautogui.pixel(30,15)
        #判断当前界面为:拼多多客户端
            if pix2 == (94,182,40):                       
                #点击拼多多左上角:今日需接待
                pyautogui.click(113,269)                  
                time.sleep (0.1)
                #屏幕中找到 “拼多多已回复” 图标，输出图标中心位置坐标
                sendVideoXYHF,sendVideoYYHF = pyautogui.locateCenterOnScreen(r"C:\autotalk\PddClient\HuaWeiBook\Picture\PddReplied-MB14.png",region=(78,312,365,1365))
                #点击拼多多已回复:第一人对话
                time.sleep (0.3) 
                pyautogui.click(sendVideoXYHF,sendVideoYYHF+50) 
                time.sleep (0.1) 
    #判断为:  MiBook Pro
        elif width == 1920:
            pix2 = pyautogui.pixel(30,15)
        #判断当前界面为:拼多多客户端
            if pix2 == (94,182,40):                       
                #点击拼多多左上角:今日需接待                
                pyautogui.click(168,220)    
                #屏幕中找到 “拼多多已回复” 图标，输出图标中心位置坐标
                sendVideoXYHF,sendVideoYYHF = pyautogui.locateCenterOnScreen(r"C:\AutoTalk\PddClient\MiBookAir\Picture\PddReplied.png",region=(63,240,260,982))
                #点击拼多多已回复:第一人对话
                time.sleep (0.3) 
                pyautogui.click(sendVideoXYHF,sendVideoYYHF+50) 
                time.sleep (1)
    #判断为:  Mate Station X
        elif width == 3840:        
            pix2 = pyautogui.pixel(68,30)
        #判断当前界面为:拼多多客户端
            if pix2 == (94,182,40):                        
                #点击拼多多左上角:今日接待
                pyautogui.click(361,493)                  
                time.sleep (0.1)
                #屏幕中找到 “拼多多已回复” 图标，输出图标中心位置坐标
                sendVideoXYHF,sendVideoYYHF = pyautogui.locateCenterOnScreen(r"C:\autotalk\PddClient\HuaWeiBook\Picture\PddReplied-MS-X.png",region=(78,312,365,1365))
                time.sleep (0.3) 
                pyautogui.click(sendVideoXYHF,sendVideoYYHF+50) #点击拼多多已回复:第一人对话
                time.sleep (0.1)
    #判断为:  Mate Station B520
        elif width == 3600:        
            pix2 = pyautogui.pixel(68,30)
        #判断当前界面为:拼多多客户端
            if pix2 == (94,182,40):                        
                #点击拼多多左上角:今日接待
                pyautogui.click(340,451)                  
                time.sleep (0.1)
                #屏幕中找到 “拼多多已回复” 图标，输出图标中心位置坐标
                sendVideoXYHF,sendVideoYYHF = pyautogui.locateCenterOnScreen(r"C:\autotalk\PddClient\HuaWeiBook\Picture\PddReplied-MS-B520.png",region=(135,523,600,2255))
                time.sleep (0.3) 
                pyautogui.click(sendVideoXYHF,sendVideoYYHF+60) #点击拼多多已回复:第一人对话
                time.sleep (0.1)
        else:
            print("end操作：这台电脑的型号没有检测到。")
def Command_sendVideo(bianhao):
    #判断为:  MateBook14                          ║
        if width == 2160:
            #判断当前界面为:拼多多客户端
            pix2 = pyautogui.pixel(30,15)
            if pix2 == (94,182,40):                       
                pyautogui.click(sendVideoX,sendVideoY)
                time.sleep (1)
                #获取指定像素颜色值
                pix = pyautogui.pixel(sendVideoX,sendVideoY-22)
                print('MateBook14取色:',pix)
                #无限循环，直到指定像素颜色匹配（弹出视频搜索框正常）
                while pix != (176, 175, 175):
                    pyautogui.click(sendVideoX,sendVideoY)
                    print('不匹配，重新点击主界面视频按钮')
                    time.sleep(1)
                    pix  = pyautogui.pixel(sendVideoX,sendVideoY-22)
                #找到视频搜索框
                pyautogui.click(sendVideoX+395,sendVideoY-428)
                time.sleep (1)
                #输入视频编号
                str99=bianhao
                pyperclip.copy(str99)
                pyautogui.hotkey('ctrl','v')
                time.sleep (0.5)
                #发送介绍视频
                pyautogui.click(sendVideoX,sendVideoY-244) #视频发送 坐标
                time.sleep (1)
    #判断为:  MiBook Pro                          ║
        elif width == 1920:
            #判断当前界面为:拼多多客户端
            pix2 = pyautogui.pixel(30,15)
            if pix2 == (94,182,40):                       
                pyautogui.click(sendVideoX,sendVideoY)
                time.sleep (1)
                #获取指定像素颜色值
                pix = pyautogui.pixel(sendVideoX,sendVideoY-24)
                print('MiBook Pro取色:',pix)

                #无限循环，直到指定像素颜色匹配（弹出视频搜索框正常）
                while pix != (176, 175, 175):
                    pyautogui.click(sendVideoX,sendVideoY)
                    print('不匹配，重新点击主界面视频按钮')
                    time.sleep(1)
                    pix = pyautogui.pixel(sendVideoX,sendVideoY-24)
                else:
                    pass
                #找到视频搜索框
                pyautogui.click(sendVideoX+395,sendVideoY-357)
                time.sleep (1)
                #输入视频编号
                str99=bianhao
                pyperclip.copy(str99)
                pyautogui.hotkey('ctrl','v')
                time.sleep (0.5)
                #发送介绍视频
                pyautogui.click(sendVideoX,sendVideoY-202) #视频发送 坐标
                time.sleep (1)
    #判断为:  Mate Station X                      ║
        elif width == 3840:
            #判断当前界面为:拼多多客户端
            pix2 = pyautogui.pixel(68,30)
            if pix2 == (94,182,40):                       
                pyautogui.click(sendVideoX,sendVideoY)
                time.sleep (1)
                #获取指定像素颜色值
                pix = pyautogui.pixel(sendVideoX,sendVideoY-35)
                print('Mate Station X取色:',pix)
                #无限循环，直到指定像素颜色匹配（弹出视频搜索框正常）
                while pix != (176, 175, 175):
                    pyautogui.click(sendVideoX,sendVideoY)
                    print('不匹配，重新点击主界面视频按钮')
                    time.sleep(1)
                    pix  = pyautogui.pixel(sendVideoX,sendVideoY-22)
                else:
                    pass
                #找到视频搜索框
                pyautogui.click(ShiPinSouSuoKuang)
                time.sleep (1)
                #输入视频编号
                str99=bianhao
                pyperclip.copy(str99)
                pyautogui.hotkey('ctrl','v')
                time.sleep (0.5)
                #发送介绍视频
                pyautogui.click(videoFaSong) #视频发送 坐标
                time.sleep (1)
    #判断为:  Mate Station B520                   ║
        elif width == 3600:
            #判断当前界面为:拼多多客户端
            pix2 = pyautogui.pixel(68,30)
            if pix2 == (92,178,39):                       
                pyautogui.click(sendVideoX,sendVideoY)
                time.sleep (1)
                #获取指定像素颜色值
                pix = pyautogui.pixel(sendVideoX,sendVideoY-39)
                print('Mate Station X取色:',pix)
                #无限循环，直到指定像素颜色匹配（弹出视频搜索框正常）
                while pix != (176, 175, 175):
                    pyautogui.click(sendVideoX,sendVideoY)
                    print('不匹配，重新点击主界面视频按钮')
                    time.sleep(1)
                    pix  = pyautogui.pixel(sendVideoX,sendVideoY-22)
                else:
                    pass
                #找到视频搜索框
                pyautogui.click(ShiPinSouSuoKuang)
                time.sleep (1)
                #输入视频编号
                str99=bianhao
                pyperclip.copy(str99)
                pyautogui.hotkey('ctrl','v')
                time.sleep (0.5)
                #发送介绍视频
                pyautogui.click(videoFaSong) #视频发送 坐标
                time.sleep (1)
        else:
            print("发送视频操作：这台电脑的型号没有检测到。")
def Command_daBao():#-邀请下单命令-#
    #判断为:  MateBook14
        if width == 2160:
            #点击 “邀请下单” 按钮
            pyautogui.click(YaoQingXiaDan)
            time.sleep (1)
            #点击 “选择商品” 搜索框(第一个商品)
            pyautogui.click(XuanZeShangPinSouSuoKuang)
            time.sleep (0.5)
            #输入商品名称
            str1='静静二番加拿大'
            pyperclip.copy(str1)
            pyautogui.hotkey('ctrl','v')
            time.sleep (1)
            pyautogui.click(JiaRuQingDan)         #加入清单
            time.sleep (1)
            pyautogui.click(XuanZeGuiGe)          #选择：加拿大提摩西草250克装1袋
            time.sleep (0.5)
            pyautogui.click(XuanZeGuiGeQueding)   #点击：确定                 
            time.sleep (0.5)
            #点击 “选择商品” 搜索框(第二个商品)
            pyautogui.click(XuanZeShangPinSouSuoKuang)
            time.sleep (0.5)
            #输入商品名称
            str2='静静2022苜蓿草'
            pyperclip.copy(str2)
            pyautogui.hotkey('ctrl','a')
            time.sleep (0.5)
            pyautogui.hotkey('ctrl','v')
            time.sleep (1)
            pyautogui.click(JiaRuQingDan)    #加入清单
            time.sleep (1)
            pyautogui.click(XuanZeGuiGe)   #选择：苜蓿草半斤装2袋
            time.sleep (0.5)
            pyautogui.click(XuanZeGuiGeQueding)   #点击：确定          
            time.sleep (1)

            pyautogui.click(DaBaoFaSong)   #点击：发送              
            time.sleep (0.5)
    #判断为:  MiBook Pro
        elif width == 1920:
            #点击 “邀请下单” 按钮
            pyautogui.click(YaoQingXiaDan)
            time.sleep (1)
            #点击 “选择商品” 搜索框(第一个商品)
            pyautogui.click(XuanZeShangPinSouSuoKuang)
            time.sleep (0.5)
            #输入商品名称
            str1='静静二番加拿大'
            pyperclip.copy(str1)
            pyautogui.hotkey('ctrl','v')
            time.sleep (1)
            pyautogui.click(JiaRuQingDan)         #加入清单
            time.sleep (1)
            pyautogui.click(XuanZeGuiGe)          #选择：加拿大提摩西草250克装1袋
            time.sleep (0.5)
            pyautogui.click(XuanZeGuiGeQueding)   #点击：确定                 
            time.sleep (0.5)
            #点击 “选择商品” 搜索框(第二个商品)
            pyautogui.click(XuanZeShangPinSouSuoKuang)
            time.sleep (0.5)
            #输入商品名称
            str2='静静2022苜蓿草'
            pyperclip.copy(str2)
            pyautogui.hotkey('ctrl','a')
            time.sleep (0.5)
            pyautogui.hotkey('ctrl','v')
            time.sleep (1)
            pyautogui.click(JiaRuQingDan)    #加入清单
            time.sleep (1)
            pyautogui.click(XuanZeGuiGe)   #选择：苜蓿草半斤装2袋
            time.sleep (0.5)
            pyautogui.click(XuanZeGuiGeQueding)   #点击：确定          
            time.sleep (1)

            pyautogui.click(DaBaoFaSong)   #点击：发送              
            time.sleep (0.5)
    #判断为:  Mate Station X
        elif width == 3840:        
            #点击 “邀请下单” 按钮
            pyautogui.click(YaoQingXiaDan)
            time.sleep (1)
            #点击 “选择商品” 搜索框(第一个商品)
            pyautogui.click(XuanZeShangPinSouSuoKuang)
            time.sleep (0.5)
            #输入商品名称
            str1='静静二番加拿大'
            pyperclip.copy(str1)
            pyautogui.hotkey('ctrl','v')
            time.sleep (1)
            pyautogui.click(JiaRuQingDan)         #加入清单
            time.sleep (1)
            pyautogui.click(XuanZeGuiGe)          #选择：加拿大提摩西草250克装1袋
            time.sleep (0.5)
            pyautogui.click(XuanZeGuiGeQueding)   #点击：确定                 
            time.sleep (0.5)
            #点击 “选择商品” 搜索框(第二个商品)
            pyautogui.click(XuanZeShangPinSouSuoKuang)
            time.sleep (0.5)
            #输入商品名称
            str2='静静2022苜蓿草'
            pyautogui.hotkey('ctrl','a')
            time.sleep (0.5)
            pyperclip.copy(str2)
            pyautogui.hotkey('ctrl','v')
            time.sleep (1)
            pyautogui.click(JiaRuQingDan)    #加入清单
            time.sleep (1)
            pyautogui.click(XuanZeGuiGe)   #选择：苜蓿草半斤装2袋
            time.sleep (0.5)
            pyautogui.click(XuanZeGuiGeQueding)   #点击：确定          
            time.sleep (1)

            pyautogui.click(DaBaoFaSong)   #点击：发送              
            time.sleep (0.5)
    #判断为:  Mate Station X
        elif width == 3600:        
            #点击 “邀请下单” 按钮
            pyautogui.click(YaoQingXiaDan)
            time.sleep (1)
            #点击 “选择商品” 搜索框(第一个商品)
            pyautogui.click(XuanZeShangPinSouSuoKuang)
            time.sleep (0.5)
            #输入商品名称
            str1='静静二番加拿大'
            pyperclip.copy(str1)
            pyautogui.hotkey('ctrl','v')
            time.sleep (1)
            pyautogui.click(JiaRuQingDan)         #加入清单
            time.sleep (1)
            pyautogui.click(XuanZeGuiGe)          #选择：加拿大提摩西草250克装1袋
            time.sleep (0.5)
            pyautogui.click(XuanZeGuiGeQueding)   #点击：确定                 
            time.sleep (0.5)
            #点击 “选择商品” 搜索框(第二个商品)
            pyautogui.click(XuanZeShangPinSouSuoKuang)
            time.sleep (0.5)
            #输入商品名称
            str2='静静2022苜蓿草'
            pyautogui.hotkey('ctrl','a')
            time.sleep (0.5)
            pyperclip.copy(str2)
            pyautogui.hotkey('ctrl','v')
            time.sleep (1)
            pyautogui.click(JiaRuQingDan)    #加入清单
            time.sleep (1)
            pyautogui.click(XuanZeGuiGe)   #选择：苜蓿草半斤装2袋
            time.sleep (0.5)
            pyautogui.click(XuanZeGuiGeQueding)   #点击：确定          
            time.sleep (1)

            pyautogui.click(DaBaoFaSong)   #点击：发送              
            time.sleep (0.5)
        else:
            print("打包选择商品操作：这台电脑的型号没有检测到。")
#╚═══════════════════════════════════════════════╝