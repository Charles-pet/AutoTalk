import pyautogui
import pyperclip
import time

import urllib.request
from io import BytesIO
import win32clipboard
from PIL import Image




width, height = pyautogui.size() # 测量当前电脑屏幕的宽度和高度


def Questions(self, event=None):
    pyautogui.click(TextSendXY)
    str0='◆亲，我养了五只兔子、两只荷兰猪，养了四年了，\n总结了一些喂养宠物的常见问题问答。'
    pyperclip.copy(str0)
    pyautogui.hotkey('ctrl','v')
    pyautogui.press('enter')
    time.sleep (0.3)

    pyautogui.click(TextSendXY)
    str1='1 问:为什么兔子、荷兰猪、龙猫 拉稀、软便。==答案:宠物的肠胃和人不一样，不能吸收食物中的水分，吃多了含水量大的新鲜的蔬菜、水果，就会拉稀。蔬菜水果放在阳台或者窗户边，晒干了再吃，就不会拉稀了。'
    pyperclip.copy(str1)
    pyautogui.hotkey('ctrl','v')
    pyautogui.press('enter')
    time.sleep (0.3)
    def send_to_clipboard(clip_type, data):
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(clip_type, data)
        win32clipboard.CloseClipboard()
        time.sleep (0.5)
    #插入第一张图片
    filepath = r'C:\AutoTalk\PddClient\MiBookAir\Picture\Timothy\Timothyd.jpg'
    image = Image.open(filepath)
    output = BytesIO()
    image.convert("RGB").save(output, "BMP")
    data = output.getvalue()[14:]
    output.close()
    send_to_clipboard(win32clipboard.CF_DIB, data)
    pyautogui.click(TextSendXY)
    pyautogui.hotkey('ctrl','v')
    pyautogui.press('enter')
    time.sleep (1)

    pyautogui.click(TextSendXY)
    str2='2 问:为什么收到的草又干又硬？==答案:宠物的肠胃和人不一样，不能吸收食物中的水分，新鲜的吃多了就会拉稀。必须吃干燥的，草必须是专业彻底烘干的，也才不会发霉，可以长期保存。'
    pyperclip.copy(str2)
    pyautogui.hotkey('ctrl','v')
    pyautogui.press('enter')
    time.sleep (0.3)

    pyautogui.click(TextSendXY)
    str3='3 问:宠物兔粮是什么？==答案:提摩西草、苜蓿草、燕麦草；提摩西草颗粒、苜蓿草颗粒、燕麦草颗粒、混合草颗粒。\n纯草粮宠物吃，健康不得病，可以活到正常寿命，一般8-12岁，个别宠物可以活到20岁。'
    pyperclip.copy(str3)
    pyautogui.hotkey('ctrl','v')
    pyautogui.press('enter')
    time.sleep (0.3)


    pyautogui.click(TextSendXY)
    str4='4 问:饲料兔粮是什么？==答案:成分:玉米、豆粕等。成本低，售价低。是养殖场给肉兔吃的，长期吃消化系统易得病，活不长。\n但是肉兔只需要活到4个月大，就进了屠宰场，所以经济上吃饲料兔粮很划算。\n宠物兔吃饲料兔粮一般活到3-5岁就不行了。'
    pyperclip.copy(str4)
    pyautogui.hotkey('ctrl','v')
    pyautogui.press('enter')
    time.sleep (0.3)

    #插入第二张图片
    filepath = r'C:\AutoTalk\PddClient\MiBookAir\Picture\Timothy\Timothye.jpg'
    image = Image.open(filepath)
    output = BytesIO()
    image.convert("RGB").save(output, "BMP")
    data = output.getvalue()[14:]
    output.close()
    send_to_clipboard(win32clipboard.CF_DIB, data)
    pyautogui.click(TextSendXY)
    time.sleep (0.3)
    pyautogui.hotkey('ctrl','v')
    pyautogui.press('enter')
    time.sleep (0.3)
    pyautogui.press('enter')
    time.sleep (1)

    pyautogui.click(TextSendXY)
    str5='5 问:宠物球虫病是怎么回事？==答案:宠物的死亡原因99%都是球虫病，球虫病大多来自母亲的传染，肠胃会带有球虫病的病原，1-3个月的宠物免疫力最低，也最容易发病。开始时食欲减退，精神沉郁，伏卧不动，生长停滞。眼鼻分泌物增多，体温升高，腹部胀大，肛门沾污，排粪频繁。预防球虫病的药片（地克珠利，网上很多卖的），每个月连吃5天，休息25天不吃药。循环4个月可以停止吃药。'
    pyperclip.copy(str5)
    pyautogui.hotkey('ctrl','v')
    pyautogui.press('enter')
    time.sleep (0.3)

    pyautogui.click(TextSendXY)
    str6='6 问:宠物每天吃多少，吃几顿？==答案:一、宠物每天吃自己体重的百分之五的量，吃饱了就不吃了，所以不限量吃草或者纯草颗粒粮（提摩西草颗粒、苜蓿草颗粒），不限量喝凉白开水。二、如果你给它吃的是玉米、淀粉、豆粉类非纯草比例超过70%的粮不能多吃，喝水也要限量，不然在肠胃遇到水会膨胀，可能会撑死宝宝。'
    pyperclip.copy(str6)
    pyautogui.hotkey('ctrl','v')
    pyautogui.press('enter')
    time.sleep (0.3)

    #插入第三张图片
    filepath = r'C:\AutoTalk\PddClient\MiBookAir\Picture\CaoKeLi\CaoKeLi1.jpg'
    image = Image.open(filepath)
    output = BytesIO()
    image.convert("RGB").save(output, "BMP")
    data = output.getvalue()[14:]
    output.close()
    send_to_clipboard(win32clipboard.CF_DIB, data)
    pyautogui.click(TextSendXY)
    pyautogui.hotkey('ctrl','v')
    pyautogui.press('enter') 
    time.sleep (1)

    #插入第四张图片
    filepath = r'C:\AutoTalk\PddClient\MiBookAir\Picture\CaoKeLi\CaoKeLi2.jpg'
    image = Image.open(filepath)
    output = BytesIO()
    image.convert("RGB").save(output, "BMP")
    data = output.getvalue()[14:]
    output.close()
    send_to_clipboard(win32clipboard.CF_DIB, data)
    pyautogui.click(TextSendXY)
    pyautogui.hotkey('ctrl','v')
    pyautogui.press('enter') 
    time.sleep (1)

    pyautogui.click(TextSendXY)
    str7='7 问:你们家的草、草颗粒安全吗？。==答案:◆这是我养的几名安全质量检查官，每天的工作就是认真的、开心的大吃特吃我家的产品，轮换吃，都很健康、开心，上周下了个小宝宝。'
    pyperclip.copy(str7)
    pyautogui.hotkey('ctrl','v')
    pyautogui.press('enter')
    time.sleep (0.3)
    pyautogui.press('enter')
    time.sleep (0.3)

    pyautogui.click(TextSendXY)
    str8='8 问:你家的草颗粒是兔粮吗？。==答案:◆我家的纯草颗粒是草的升级，就是最好的兔粮，\n只要是兔子、荷兰猪、龙猫天生就是吃草的，草颗粒粮更安全，更容易消化吸收。'
    pyperclip.copy(str8)
    pyautogui.hotkey('ctrl','v')
    pyautogui.press('enter')
    time.sleep (0.3)
    pyautogui.press('enter')
    time.sleep (0.3)

    pyautogui.click(TextSendXY)
    str9='9 问:吃草或者纯草颗粒粮会不会营养不够？。==答案:◆吃草营养全够了。不会营养不良。大草原的兔子一辈子就是吃草，都很健康。'
    pyperclip.copy(str9)
    pyautogui.hotkey('ctrl','v')
    pyautogui.press('enter')
    time.sleep (0.3)

    #插入第五张图片
    filepath = r'C:\AutoTalk\PddClient\MiBookAir\Picture\Timothy\Timothyk.jpg'
    image = Image.open(filepath)
    output = BytesIO()
    image.convert("RGB").save(output, "BMP")
    data = output.getvalue()[14:]
    output.close()
    send_to_clipboard(win32clipboard.CF_DIB, data)
    pyautogui.click(TextSendXY)
    time.sleep (0.3)
    pyautogui.hotkey('ctrl','v')
    pyautogui.press('enter')
    time.sleep (0.3)
    pyautogui.press('enter')
    time.sleep (1)

    pyautogui.click(TextSendXY)
    str10='10 问:宠物需要喝水吗？。==答案:◆需要喝水，兔子、荷兰猪、龙猫都需要喝水，不喝水肯定会渴死。\n部分谣言说兔子不能喝水，是因为饲料兔粮不是草做的，主要成分是玉米、豆粕、淀粉等，遇到水会膨胀，\n宠物吃多了，在肠胃遇到水会膨胀，可能撑死宠物，所以不让喝水。\n我家的纯草兔粮遇到水不会膨胀。\n所以可以无限吃草粮+无限喝水。'
    pyperclip.copy(str10)
    pyautogui.hotkey('ctrl','v')
    pyautogui.press('enter')
    time.sleep (0.3)

    #插入第6张图片
    filepath = r"C:\AutoTalk\PddClient\MiBookAir\Picture\Timothy\Timothyl.png"
    image = Image.open(filepath)
    output = BytesIO()
    image.convert("RGB").save(output, "BMP")
    data = output.getvalue()[14:]
    output.close()
    send_to_clipboard(win32clipboard.CF_DIB, data)
    pyautogui.click(TextSendXY)
    time.sleep (0.3)
    pyautogui.hotkey('ctrl','v')
    pyautogui.press('enter')
    time.sleep (0.3)
    pyautogui.press('enter')
    time.sleep (1)
    pyautogui.click(TextSendXY)
    str11='\n科养:吃草或者纯草颗粒粮（无淀粉，或者淀粉含量不超过20%）；\n渣养:吃一般的兔粮（主要成分:玉米、淀粉、豆粕等）。\n淀粉就是玉米、豆粕等，小宠的小肠只能消化一小部分淀粉，多余的淀粉需要到盲肠去进行消化。而淀粉在盲肠会变成有害菌的能量来源，导致有害菌过度繁殖，造成胀气、积食、肠炎而死。草纤维能够减缓发酵，而淀粉恰恰相反，会使发酵过程加速。。'
    pyperclip.copy(str11)
    pyautogui.hotkey('ctrl','v')
    pyautogui.press('enter')
    time.sleep (0.3)

    Command_sendVideo('E-提')        #-发送视频-提草包装介绍--#
    Command_sendVideo('I-兔')        #-发送视频-宠物吃草颗粒--#
    Command_sendVideo('G-吃')        #-发送视频-宠物吃玉米叶--#

    time.sleep (1)
    pyautogui.click(TextSendXY)
    str12='亲，以上是发一下产品功能介绍和使用说明。'
    pyperclip.copy(str12)
    pyautogui.hotkey('ctrl','v')
    pyautogui.press('enter')
    time.sleep (0.3)

    Command_end()                    #-通用结尾操作----------#



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