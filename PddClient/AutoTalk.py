#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os, sys
from tkinter import *
from tkinter.font import Font
from tkinter.ttk import *
# from tkinter.messagebox import *

import pyautogui
import time
import pyperclip

import urllib.request
from io import BytesIO
import win32clipboard
from PIL import Image
##参数设置：
##华为Mate Book 14:屏幕分辨率:2160,1440 放大150%
##华为Mate Station X：屏幕分辨率:3840,2560 放大400% HDR：开
##华为Mate Station B520：屏幕分辨率:3600,2400 放大200% HDR：开
##华为Mate Station B520：屏幕分辨率:3600,2400 放大200% HDR：开
##华为Mate Book X Pro：屏幕分辨率:3120,2080 放大200% HDR：开

width, height = pyautogui.size() # 测量当前电脑屏幕的宽度和高度
print('Welcome Boss, 当前电脑的屏幕分辨率:', width, height)
time.sleep (0.3)


class Application_ui(Frame):
    #这个类仅实现界面生成功能，具体事件处理代码在子类Application中。
    def __init__(self, master=None): #菜单属性设置
        Frame.__init__(self, master)
        self.master.title('JingJing_AutoTalk 3.0       BestFood Co., LTD.      版本号：2023-05-08')
        self.master.geometry(PingMu)
        self.createWidgets()
        self.master.wm_attributes('-topmost',1)     #置顶窗口显示
        self.master.iconbitmap(r'C:\autotalk\PddClient\MiBookAir\Picture\miniJJ2.ico')
        self.master.attributes("-alpha",0.9)        #窗体透明度
        

    def createWidgets(self): #菜单显示
        self.top = self.winfo_toplevel()
        self.style = Style()

        self.Command30Var = StringVar(value='微\n笑\n\n30')
        self.style.configure('TCommand30.TButton', font=('HarmonyOS Sans SC Black',FontSize))
        self.Command30 = Button(self.top, text='微笑', textvariable=self.Command30Var, command=self.Command30_Cmd, style='TCommand30.TButton')
        self.Command30.setText = lambda x: self.Command30Var.set(x)
        self.Command30.text = lambda : self.Command30Var.get()
        self.Command30.place(relx=0.932, rely=0.5, relwidth=0.068, relheight=0.51)

        self.Command29Var = StringVar(value='今天\n发货\n\n 29')
        self.style.configure('TCommand29.TButton', font=('HarmonyOS Sans SC Black',FontSize))
        self.Command29 = Button(self.top, text='今天发货', textvariable=self.Command29Var, command=self.Command29_Cmd, style='TCommand29.TButton')
        self.Command29.setText = lambda x: self.Command29Var.set(x)
        self.Command29.text = lambda : self.Command29Var.get()
        self.Command29.place(relx=0.865, rely=0.5, relwidth=0.068, relheight=0.51)

        self.Command28Var = StringVar(value=' 羊 驼\n苜蓿草\n\n   28')
        self.style.configure('TCommand28.TButton', font=('HarmonyOS Sans SC Black',FontSize))
        self.Command28 = Button(self.top, text='羊驼苜蓿草', textvariable=self.Command28Var, command=self.Command28_Cmd, style='TCommand28.TButton')
        self.Command28.setText = lambda x: self.Command28Var.set(x)
        self.Command28.text = lambda : self.Command28Var.get()
        self.Command28.place(relx=0.799, rely=0.5, relwidth=0.068, relheight=0.51)

        self.Command27Var = StringVar(value='感谢\n好评\n\n27')
        self.style.configure('TCommand27.TButton', font=('HarmonyOS Sans SC Black',FontSize))
        self.Command27 = Button(self.top, text='空白27', textvariable=self.Command27Var, command=self.Command27_Cmd, style='TCommand27.TButton')
        self.Command27.setText = lambda x: self.Command27Var.set(x)
        self.Command27.text = lambda : self.Command27Var.get()
        self.Command27.place(relx=0.732, rely=0.5, relwidth=0.068, relheight=0.51)

        self.Command26Var = StringVar(value='邀下单\n 提+苜\n\n 26')
        self.style.configure('TCommand26.TButton', font=('HarmonyOS Sans SC Black',FontSize))
        self.Command26 = Button(self.top, text='邀请下单', textvariable=self.Command26Var, command=self.Command26_Cmd, style='TCommand26.TButton')
        self.Command26.setText = lambda x: self.Command26Var.set(x)
        self.Command26.text = lambda : self.Command26Var.get()
        self.Command26.place(relx=0.666, rely=0.5, relwidth=0.068, relheight=0.51)

        self.Command25Var = StringVar(value='啥不\n能吃\n\n 25')
        self.style.configure('TCommand25.TButton', font=('HarmonyOS Sans SC Black',FontSize))
        self.Command25 = Button(self.top, text='啥不能吃', textvariable=self.Command25Var, command=self.Command25_Cmd, style='TCommand25.TButton')
        self.Command25.setText = lambda x: self.Command25Var.set(x)
        self.Command25.text = lambda : self.Command25Var.get()
        self.Command25.place(relx=0.599, rely=0.5, relwidth=0.068, relheight=0.51)

        self.Command24Var = StringVar(value=' 专 家\n养兔子\n\n   24')
        self.style.configure('TCommand24.TButton', font=('HarmonyOS Sans SC Black',FontSize))
        self.Command24 = Button(self.top, text='专家养兔子', textvariable=self.Command24Var, command=self.Command24_Cmd, style='TCommand24.TButton')
        self.Command24.setText = lambda x: self.Command24Var.set(x)
        self.Command24.text = lambda : self.Command24Var.get()
        self.Command24.place(relx=0.533, rely=0.5, relwidth=0.068, relheight=0.51)

        self.Command23Var = StringVar(value='制作\n草饼\n\n 23')
        self.style.configure('TCommand23.TButton', font=('HarmonyOS Sans SC Black',FontSize))
        self.Command23 = Button(self.top, text='制作草饼', textvariable=self.Command23Var, command=self.Command23_Cmd, style='TCommand23.TButton')
        self.Command23.setText = lambda x: self.Command23Var.set(x)
        self.Command23.text = lambda : self.Command23Var.get()
        self.Command23.place(relx=0.466, rely=0.5, relwidth=0.068, relheight=0.51)

        self.Command22Var = StringVar(value='草颗粒\n纯草粮\n\n   22')
        self.style.configure('TCommand22.TButton', font=('HarmonyOS Sans SC Black',FontSize))
        self.Command22 = Button(self.top, text='草颗粒纯草粮', textvariable=self.Command22Var, command=self.Command22_Cmd, style='TCommand22.TButton')
        self.Command22.setText = lambda x: self.Command22Var.set(x)
        self.Command22.text = lambda : self.Command22Var.get()
        self.Command22.place(relx=0.399, rely=0.5, relwidth=0.068, relheight=0.51)

        self.Command21Var = StringVar(value='综合\n兔粮\n\n 21')
        self.style.configure('TCommand21.TButton', font=('HarmonyOS Sans SC Black',FontSize))
        self.Command21 = Button(self.top, text='综合兔粮', textvariable=self.Command21Var, command=self.Command21_Cmd, style='TCommand21.TButton')
        self.Command21.setText = lambda x: self.Command21Var.set(x)
        self.Command21.text = lambda : self.Command21Var.get()
        self.Command21.place(relx=0.333, rely=0.5, relwidth=0.068, relheight=0.51)

        self.Command20Var = StringVar(value='无限\n吃草\n\n 20')
        self.style.configure('TCommand20.TButton', font=('HarmonyOS Sans SC Black',FontSize))
        self.Command20 = Button(self.top, text='无限吃草', textvariable=self.Command20Var, command=self.Command20_Cmd, style='TCommand20.TButton')
        self.Command20.setText = lambda x: self.Command20Var.set(x)
        self.Command20.text = lambda : self.Command20Var.get()
        self.Command20.place(relx=0.266, rely=0.5, relwidth=0.068, relheight=0.51)

        self.Command19Var = StringVar(value='不吃\n提草\n\n 19')
        self.style.configure('TCommand19.TButton', font=('HarmonyOS Sans SC Black',FontSize))
        self.Command19 = Button(self.top, text='不吃提草', textvariable=self.Command19Var, command=self.Command19_Cmd, style='TCommand19.TButton')
        self.Command19.setText = lambda x: self.Command19Var.set(x)
        self.Command19.text = lambda : self.Command19Var.get()
        self.Command19.place(relx=0.2, rely=0.5, relwidth=0.068, relheight=0.51)

        self.Command18Var = StringVar(value='20年\n提 草\n\n  18')
        self.style.configure('TCommand18.TButton', font=('HarmonyOS Sans SC Black',FontSize))
        self.Command18 = Button(self.top, text='20年提草', textvariable=self.Command18Var, command=self.Command18_Cmd, style='TCommand18.TButton')
        self.Command18.setText = lambda x: self.Command18Var.set(x)
        self.Command18.text = lambda : self.Command18Var.get()
        self.Command18.place(relx=0.133, rely=0.5, relwidth=0.068, relheight=0.51)

        self.Command17Var = StringVar(value='  两种\n一起吃\n\n 17')
        self.style.configure('TCommand17.TButton', font=('HarmonyOS Sans SC Black',FontSize))
        self.Command17 = Button(self.top, text='两种一起吃', textvariable=self.Command17Var, command=self.Command17_Cmd, style='TCommand17.TButton')
        self.Command17.setText = lambda x: self.Command17Var.set(x)
        self.Command17.text = lambda : self.Command17Var.get()
        self.Command17.place(relx=0.067, rely=0.5, relwidth=0.068, relheight=0.51)

        self.Command16Var = StringVar(value=' 宠 物\n常见题\n\n   16')
        self.style.configure('TCommand16.TButton', font=('HarmonyOS Sans SC Black',FontSize))
        self.Command16 = Button(self.top, text='宠物常见题', textvariable=self.Command16Var, command=self.Command16_Cmd, style='TCommand16.TButton')
        self.Command16.setText = lambda x: self.Command16Var.set(x)
        self.Command16.text = lambda : self.Command16Var.get()
        self.Command16.place(relx=0., rely=0.5, relwidth=0.068, relheight=0.51)

        self.Command15Var = StringVar(value=' 满18\n送1元\n\n   15')
        self.style.configure('TCommand15.TButton', font=('HarmonyOS Sans SC Black',FontSize))
        self.Command15 = Button(self.top, text='满11送2元', textvariable=self.Command15Var, command=self.Command15_Cmd, style='TCommand15.TButton')
        self.Command15.setText = lambda x: self.Command15Var.set(x)
        self.Command15.text = lambda : self.Command15Var.get()
        self.Command15.place(relx=0.932, rely=0., relwidth=0.068, relheight=0.51)

        self.Command14Var = StringVar(value='明天\n发货\n\n 14')
        self.style.configure('TCommand14.TButton', font=('HarmonyOS Sans SC Black',FontSize))
        self.Command14 = Button(self.top, text='明天发货', textvariable=self.Command14Var, command=self.Command14_Cmd, style='TCommand14.TButton')
        self.Command14.setText = lambda x: self.Command14Var.set(x)
        self.Command14.text = lambda : self.Command14Var.get()
        self.Command14.place(relx=0.865, rely=0., relwidth=0.068, relheight=0.51)

        self.Command13Var = StringVar(value=' 每 天\n吃多少\n\n   13')
        self.style.configure('TCommand13.TButton', font=('HarmonyOS Sans SC Black',FontSize))
        self.Command13 = Button(self.top, text='每天吃多少', textvariable=self.Command13Var, command=self.Command13_Cmd, style='TCommand13.TButton')
        self.Command13.setText = lambda x: self.Command13Var.set(x)
        self.Command13.text = lambda : self.Command13Var.get()
        self.Command13.place(relx=0.799, rely=0., relwidth=0.068, relheight=0.51)

        self.Command12Var = StringVar(value='病\n兔\n\n12')
        self.style.configure('TCommand12.TButton', font=('HarmonyOS Sans SC Black',FontSize))
        self.Command12 = Button(self.top, text='空白12', textvariable=self.Command12Var, command=self.Command12_Cmd, style='TCommand12.TButton')
        self.Command12.setText = lambda x: self.Command12Var.set(x)
        self.Command12.text = lambda : self.Command12Var.get()
        self.Command12.place(relx=0.732, rely=0., relwidth=0.068, relheight=0.51)

        self.Command11Var = StringVar(value='_饲养_\n荷兰猪\n\n11')
        self.style.configure('TCommand11.TButton', font=('HarmonyOS Sans SC Black',FontSize))
        self.Command11 = Button(self.top, text='视频坐标', textvariable=self.Command11Var, command=self.Command11_Cmd, style='TCommand11.TButton')
        self.Command11.setText = lambda x: self.Command11Var.set(x)
        self.Command11.text = lambda : self.Command11Var.get()
        self.Command11.place(relx=0.666, rely=0., relwidth=0.068, relheight=0.51)

        self.Command10Var = StringVar(value='草屑\n说明\n\n10')
        self.style.configure('TCommand10.TButton', font=('HarmonyOS Sans SC Black',FontSize))
        self.Command10 = Button(self.top, text='草屑说明', textvariable=self.Command10Var, command=self.Command10_Cmd, style='TCommand10.TButton')
        self.Command10.setText = lambda x: self.Command10Var.set(x)
        self.Command10.text = lambda : self.Command10Var.get()
        self.Command10.place(relx=0.599, rely=0., relwidth=0.068, relheight=0.51)

        self.Command9Var = StringVar(value='苜蓿草\n吨报价\n\n   09')
        self.style.configure('TCommand9.TButton', font=('HarmonyOS Sans SC Black',FontSize))
        self.Command9 = Button(self.top, text='获取像素颜色', textvariable=self.Command9Var, command=self.Command9_Cmd, style='TCommand9.TButton')
        self.Command9.setText = lambda x: self.Command9Var.set(x)
        self.Command9.text = lambda : self.Command9Var.get()
        self.Command9.place(relx=0.533, rely=0., relwidth=0.068, relheight=0.51)

        self.Command8Var = StringVar(value='润肠\n_草_\n\n_08')
        self.style.configure('TCommand8.TButton', font=('HarmonyOS Sans SC Black',FontSize))
        self.Command8 = Button(self.top, text='润肠草', textvariable=self.Command8Var, command=self.Command8_Cmd, style='TCommand8.TButton')
        self.Command8.setText = lambda x: self.Command8Var.set(x)
        self.Command8.text = lambda : self.Command8Var.get()
        self.Command8.place(relx=0.466, rely=0., relwidth=0.068, relheight=0.51)

        self.Command7Var = StringVar(value='磨牙\n_棒_\n\n_07')
        self.style.configure('TCommand7.TButton', font=('HarmonyOS Sans SC Black',FontSize))
        self.Command7 = Button(self.top, text='磨牙棒', textvariable=self.Command7Var, command=self.Command7_Cmd, style='TCommand7.TButton')
        self.Command7.setText = lambda x: self.Command7Var.set(x)
        self.Command7.text = lambda : self.Command7Var.get()
        self.Command7.place(relx=0.399, rely=0., relwidth=0.068, relheight=0.51)

        self.Command6Var = StringVar(value='_木_\n颗粒\n\n_06')
        self.style.configure('TCommand6.TButton', font=('HarmonyOS Sans SC Black',FontSize))
        self.Command6 = Button(self.top, text='木颗粒', textvariable=self.Command6Var, command=self.Command6_Cmd, style='TCommand6.TButton')
        self.Command6.setText = lambda x: self.Command6Var.set(x)
        self.Command6.text = lambda : self.Command6Var.get()
        self.Command6.place(relx=0.333, rely=0., relwidth=0.068, relheight=0.51)

        self.Command5Var = StringVar(value='_牵_\n引绳\n\n_05')
        self.style.configure('TCommand5.TButton', font=('HarmonyOS Sans SC Black',FontSize))
        self.Command5 = Button(self.top, text='牵引绳', textvariable=self.Command5Var, command=self.Command5_Cmd, style='TCommand5.TButton')
        self.Command5.setText = lambda x: self.Command5Var.set(x)
        self.Command5.text = lambda : self.Command5Var.get()
        self.Command5.place(relx=0.266, rely=0., relwidth=0.068, relheight=0.51)

        self.Command4Var = StringVar(value='木\n屑\n\n04')
        self.style.configure('TCommand4.TButton', font=('HarmonyOS Sans SC Black',FontSize))
        self.Command4 = Button(self.top, text='木屑', textvariable=self.Command4Var, command=self.Command4_Cmd, style='TCommand4.TButton')
        self.Command4.setText = lambda x: self.Command4Var.set(x)
        self.Command4.text = lambda : self.Command4Var.get()
        self.Command4.place(relx=0.2, rely=0., relwidth=0.068, relheight=0.51)

        self.Command3Var = StringVar(value=' 宠 物\n好关系\n\n   03')
        self.style.configure('TCommand3.TButton', font=('HarmonyOS Sans SC Black',FontSize))
        self.Command3 = Button(self.top, text='宠物好关系', textvariable=self.Command3Var, command=self.Command3_Cmd, style='TCommand3.TButton')
        self.Command3.setText = lambda x: self.Command3Var.set(x)
        self.Command3.text = lambda : self.Command3Var.get()
        self.Command3.place(relx=0.133, rely=0., relwidth=0.068, relheight=0.51)

        self.Command2Var = StringVar(value='养仓鼠\n 禁 忌\n\n   02')
        self.style.configure('TCommand2.TButton', font=('HarmonyOS Sans SC Black',FontSize))
        self.Command2 = Button(self.top, text='养仓鼠禁忌', textvariable=self.Command2Var, command=self.Command2_Cmd, style='TCommand2.TButton')
        self.Command2.setText = lambda x: self.Command2Var.set(x)
        self.Command2.text = lambda : self.Command2Var.get()
        self.Command2.place(relx=0.067, rely=0., relwidth=0.068, relheight=0.51)

        self.Command1Var = StringVar(value='浴\n沙\n\n01')
        self.style.configure('TCommand1.TButton', font=('HarmonyOS Sans SC Black',FontSize))
        self.Command1 = Button(self.top, text='浴沙', textvariable=self.Command1Var, command=self.Command1_Cmd, style='TCommand1.TButton')
        self.Command1.setText = lambda x: self.Command1Var.set(x)
        self.Command1.text = lambda : self.Command1Var.get()
        self.Command1.place(relx=0., rely=0., relwidth=0.068, relheight=0.51)
        #self.Command20.place(relx=0.899, rely=0., relwidth=0.101, relheight=0.509)

class Application(Application_ui):
    #这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        Application_ui.__init__(self, master)

    def Command30_Cmd(self, event=None):    #30
        from Commands import C30
        C30.WeiXiao()
    def Command29_Cmd(self, event=None):    #29
        from Commands import C29
        C29.Today()
    def Command28_Cmd(self, event=None):    #28
        from Commands import C28
        C28.Alpaca()
    def Command27_Cmd(self, event=None):    #27
        from Commands import C27
        C27.Acclaim()
    def Command26_Cmd(self, event=None):    #26
        from Commands import C26
        C26.Invite()
    def Command25_Cmd(self, event=None):    #25
        from Commands import C25
        C25.NoEat()
    def Command24_Cmd(self, event=None):    #24
        from Commands import C24
        C24.Experience()
    def Command23_Cmd(self, event=None):    #23
        from Commands import C23
        C23.Grass_cakes()
    def Command22_Cmd(self, event=None):    #22
        from Commands import C22
        C22.Grass_pellets()
    def Command21_Cmd(self, event=None):    #21
        from Commands import C21
        C21.Mix_grass_pellets()
    def Command20_Cmd(self, event=None):    #20
        from Commands import C20
        C20.Unlimited_grazing()
    def Command19_Cmd(self, event=None):    #19
        from Commands import C19
        C19.Not_eat_grass()
    def Command18_Cmd(self, event=None):    #18
        from Commands import C18
        C18.Old_grass()
    def Command17_Cmd(self, event=None):    #17
        from Commands import C17
        C17.How_much_to_eat()
    def Command16_Cmd(self, event=None):    #16
        from Commands import C16
        C16.Questions()
    def Command15_Cmd(self, event=None):    #15
        from Commands import C15
        C15.Coupons()
    def Command14_Cmd(self, event=None):    #14
        from Commands import C14
        C14.Tomorrow()
    def Command13_Cmd(self, event=None):    #13
        from Commands import C13
        C13.Recipe()
    def Command12_Cmd(self, event=None):    #12
        from Commands import C12
        C12.Sick_rabbits()
    def Command11_Cmd(self, event=None):    #11
        from Commands import C11
        C11.Dutch_pig()
    def Command10_Cmd(self, event=None):    #10
        from Commands import C10
        C10.Introduction_pellets()
    def Command9_Cmd(self, event=None):     #09
        from Commands import C09
        C09.Ton_grass_price()
    def Command8_Cmd(self, event=None):     #08
        from Commands import C08
        C08.Moisturizer()
    def Command7_Cmd(self, event=None):     #07
        from Commands import C07
        C07.Teething_sticks()
    def Command6_Cmd(self, event=None):     #06
        from Commands import C06
        C06.Wood_pellets()
    def Command5_Cmd(self, event=None):     #05
        from Commands import C05
        C05.Rabbit_rope()
    def Command4_Cmd(self, event=None):     #04
        from Commands import C04
        C04.Sawdust()
    def Command3_Cmd(self, event=None):     #03
        from Commands import C03
        C03.Socializing()
    def Command2_Cmd(self, event=None):     #02
        from Commands import C02
        C02.Taboo()
    def Command1_Cmd(self, event=None):     #01
        from Commands import C01
        C01.Bath_sand


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
    #判断为:  Mate Station B520                      ║
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
#╚════════════════════════════════════════════════╝

if __name__ == "__main__":
    top = Tk()
    Application(top).mainloop()



