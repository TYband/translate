# -*- coding：utf-8 -*-
# time ：2019/5/2 23:44
# author: 毛利
import requests
from tkinter import *
from tkinter import messagebox
import time
def translation():

    # 接受用户的信息
    content = entry.get()
    if content =='':
        messagebox.showinfo('提示','请输入要翻译的内容')
    else:
        # url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
        data  ={
            'i':content,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            # 时间戳  14位
            # 'salt': '15568459610827',
            # 'sign': '9494fda01d62399b1a3476280a82c990',
            # 时间戳13位
            # 'ts': '1556845961082',
            # 'bv': 'd6c3cd962e29b66abe48fcb8f4dd7f7d',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_REALTlME',
        }

        result = requests.post(url,data)
        tarn = result.json()['translateResult'][0][0]['tgt']
        res.set(tarn)
        print(tarn)



# 创建窗口
root = Tk()

# 窗口标题

root.title('翻译软件')

# 窗口大小 小写的x 不是370*100
root.geometry('370x100')
# 窗口位置
root.geometry('+500+300')
# root.geometry('300x100+500+300')

# 标签控件 font = ('微软雅黑',12)
label = Label(root,text ='输入要翻译的文字')

# 定位  pack 包  place 位置
label.grid(row=0,column =0)
# fg = 'red' 字体颜色
label1 = Label(root,text ='翻译之后的结果:')
label1.grid(row =1,column= 0)
# 输入控件
entry = Entry(root,font =('微软雅黑',15))
entry.grid(row=0,column = 1)
# 翻译之后的结果

res = StringVar()
entry1 = Entry(root,font =('微软雅黑',15),textvariable=res)
entry1.grid(row=1,column = 1)

# 点击按钮

button = Button(root,text="翻译",width=10,command = translation)
# sticky 对齐方式 N S E W
button.grid(row=2,column=0,sticky=W)

button1 = Button(root,text  ='退出',width=10,command = root.quit)
button1.grid(row=2,column = 1,sticky=E )
# 消息循环
root.mainloop()
————————————————
版权声明：本文为CSDN博主「润森」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/weixin_44510615/java/article/details/89785500