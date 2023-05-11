import pyautogui


width, height = pyautogui.size() # 测量当前电脑屏幕的宽度和高度

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
#╚═══════════════════════