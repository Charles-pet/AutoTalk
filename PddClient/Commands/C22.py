import pyautogui
import pyperclip
import time

import urllib.request
from io import BytesIO
import win32clipboard
from PIL import Image



width, height = pyautogui.size() # 测量当前电脑屏幕的宽度和高度


def Grass_pellets(self, event=None):

    pyautogui.click(TextSendXY)
    str1='◆亲，我家的纯草颗粒，就是传说中的加拿大洛基山雪提纯草兔粮、纯草荷兰猪粮、纯草龙猫粮，是食草类宠物的健康主粮。'
    pyperclip.copy(str1)
    pyautogui.hotkey('ctrl','v')
    pyautogui.press('enter')
    time.sleep (0.3)

    pyautogui.click(TextSendXY)
    str2='◆营养成分:\n粗蛋白7.5%，\n粗脂肪1.9%，\n粗纤维32%，\n无氮浸出物52.3%，\n钙0.5%，磷0.24%，\n草质细嫩，适口性好，适合:兔子、龙猫、荷兰猪做主食、主粮。营养成分均衡全面。'
    pyperclip.copy(str2)
    pyautogui.hotkey('ctrl','v')
    pyautogui.press('enter')
    time.sleep (0.3)

    pyautogui.click(TextSendXY)
    str3='◆出生25天以上的幼兔、小荷兰猪、小龙猫都能吃，纯草粮含有丰富的粗纤维，这些纤维在体内有效改善肠胃功能。'
    pyperclip.copy(str3)
    pyautogui.hotkey('ctrl','v')
    pyautogui.press('enter')
    time.sleep (0.3)

    pyautogui.click(TextSendXY)
    str4='◆磨牙效果好，能让兔兔、荷兰猪很好的磨牙，预防牙齿问题，无限吃草粮不会胀肚子，吃饱了就不吃了。'
    pyperclip.copy(str4)
    pyautogui.hotkey('ctrl','v')
    pyautogui.press('enter')
    time.sleep (0.3)

    pyautogui.click(TextSendXY)
    str5='◆我养的兔兔、荷兰猪还不到一个月，一直喂的是纯草粮，吃的很香、很健康。'
    pyperclip.copy(str5)
    pyautogui.hotkey('ctrl','v')
    pyautogui.press('enter')
    time.sleep (0.3)

    pyautogui.click(TextSendXY)
    str6='◆相反实在不肯吃草粮的兔兔、荷兰猪只给它草粮和水，别的都不给，饥饿疗法，三天见效，就像小孩进了肯德基，绝对不会吃馒头。先把它挑食的习惯纠正过来，以后就会轻松很多。'
    pyperclip.copy(str6)
    pyautogui.hotkey('ctrl','v')
    pyautogui.press('enter')
    time.sleep (0.3)

    pyautogui.click(TextSendXY)
    str7='◆饲喂方法就是无限纯草粮，无限喝水。每周吃一次新鲜蔬菜补充维生素，蔬菜晒干再吃，放在阳台或者窗户边至少一天。营养已经足够了。'
    pyperclip.copy(str7)
    pyautogui.hotkey('ctrl','v')
    pyautogui.press('enter')
    time.sleep (0.3)

    pyautogui.click(TextSendXY)
    str8='◆纯草颗粒加工温度七十度，草里面的寄生虫和虫卵都杀死，所以更安全更健康，草纤维也熟化了，更有利于消化吸收。'
    pyperclip.copy(str8)
    pyautogui.hotkey('ctrl','v')
    pyautogui.press('enter')
    time.sleep (0.3)

    pyautogui.click(TextSendXY)
    str9='◆纯草粮可以替代吃草。耐吃、省事，不浪费，你也不用再为了宠物只吃叶子，不吃草杆子的事操心了。'
    pyperclip.copy(str9)
    pyautogui.hotkey('ctrl','v')
    pyautogui.press('enter')
    time.sleep (0.3)

    pyautogui.click(TextSendXY)
    str10='◆纯草颗粒粮适合宠物:（垂耳兔、毛毛兔、侏儒兔、小白兔、荷兰猪、龙猫），一定要记住，这些宠物天生就是吃草的。我家的草颗粒是纯草粮。'
    pyperclip.copy(str10)
    pyautogui.hotkey('ctrl','v')
    pyautogui.press('enter')
    time.sleep (0.3)

    pyautogui.click(TextSendXY)
    str11='◆亲，因为我们是纯草颗粒粮，坚持不添加任何化学粘合剂，运输途中受到颠簸，会产生一些草屑，都是草粉，可以收集一下，制作成磨牙草饼。如有需要，我可以给你发制作磨牙草饼的教程。'
    pyperclip.copy(str11)
    pyautogui.hotkey('ctrl','v')
    pyautogui.press('enter')
    time.sleep (0.3)

    pyautogui.click(TextSendXY)
    str12='◆100%加拿大进口优质提摩西草压制的，什么都不加.\n草颗粒是草的升级可以代替吃草。'
    pyperclip.copy(str12)
    pyautogui.hotkey('ctrl','v')
    pyautogui.press('enter')
    time.sleep (0.3)


    def send_to_clipboard(clip_type, data):
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(clip_type, data)
        win32clipboard.CloseClipboard()
        time.sleep (0.5)
    filepath = r'C:\autotalk\PddClient\MiBookAir\Picture\FeedProblem\FeedProblem1.jpg'
    image = Image.open(filepath)
    output = BytesIO()
    image.convert("RGB").save(output, "BMP")
    data = output.getvalue()[14:]
    output.close()
    send_to_clipboard(win32clipboard.CF_DIB, data)
    pyautogui.click(TextSendXY)
    pyautogui.hotkey('ctrl','v')
    time.sleep (0.3)
    pyautogui.press('enter') 
    time.sleep (1)

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