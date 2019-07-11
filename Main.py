import sys
import random

import os
import time

import re

import test
import requests
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget

from PyQt5 import QtWidgets
from test import Ui_Dialog


class main(QtWidgets.QWidget, Ui_Dialog):
    def __init__(self):
        super(main, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.BeginVerfity)  ##槽函数不用加括号
        self.txtVerfityCd.textChanged.connect(self.txtVerfityCdChange);
        self.txtConsole.setText("程序启动。")

    # 开始验证
    def BeginVerfity(self):  # 定义槽


        self.init();

    baseCode = "";
    baseCdPositionList = [];
    hiddenLength = 0;  # 替换问号位数
    seedText = ""
    seedLength = 0;  # 随机种子长度
    offset = 0;  # 偏移量
    msg_invcode = [
        "恭喜您，您可以使用這個邀請碼註冊！",
        "邀請碼不存在或已被使用，您無法注冊！",
        "驗證碼不正確，請重新填寫"
    ];

    session ='';
    url="http://www.t66y.com";
    timeOut=10;
    cookies ={};
    def init(self):
        self.txtConsole.append("初始化中..." + str(time.time()))
        self.baseCode = self.txtBaseCode.text();  # 拼接码

        for index in range(len(self.baseCode)):
            if (self.baseCode[index] == '?'):
                self.baseCdPositionList.append(index);
        self.txtConsole.append("问号位置：" + str(self.baseCdPositionList))
        self.seedText = self.txtSeed.text();
        self.txtConsole.append("随机数种子：" + str(self.seedText))

        self.hiddenLength = len(self.baseCdPositionList);
        self.seedLength = len(self.seedText);
        try:
            self.initHttp();
            os.makedirs("./data/unVerifityImg/", exist_ok=1)
            os.makedirs("./data/VerifityImg/", exist_ok=1)
            self.nextVerfityCd();
            self.nextVerfityImg();
            self.txtConsole.append("初始化完成" + str(time.time()))
        except OSError as err:
            self.txtConsole.append("初始化错误。" + str(time.time()))
            print(str(err))

    def initHttp(self):
        proxies = {"http": "socks5://127.0.0.1:1090", "https": "socks5://127.0.0.1:1090"}  # 代理
        '''
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            # "Cookie": "__cfduid=d43804812c8d3a340b8f024e7088bca681558284563; UM_distinctid=16ad1031ec60-0ef1a2ff994f2c-3c720356-1fa400-16ad1031ec725a; CNZZDATA950900=cnzz_eid%3D1518989184-1558281391-http%253A%252F%252Fwww.t66y.com%252F%26ntime%3D1560412506; PHPSESSID=go0rne1hhn6rvkgnakurke5eh6; 227c9_lastvisit=0%091560415446%09%2Fregister.php%3F",
            # "Cookie":"__cfduid=d43804812c8d3a340b8f024e7088bca681558284563; UM_distinctid=16ad1031ec60-0ef1a2ff994f2c-3c720356-1fa400-16ad1031ec725a; CNZZDATA950900=cnzz_eid%3D1518989184-1558281391-http%253A%252F%252Fwww.t66y.com%252F%26ntime%3D1560674707; PHPSESSID=69q9i46a0n7av91hcbcd93pg85; 227c9_lastvisit=0%091560679496%09%2Fregister.php%3F",
            "Host": "www.t66y.com",
            "Pragma": "no-cache",
            "Referer": "http://www.t66y.com/index.php",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
        }
        '''
        # https: // www.t66y.com / register.php
        session = requests.session();
        self.session = session;
        resp = session.get(self.url+"/register.php", proxies=proxies,timeout=self.timeOut)# headers=headers
        cookies = resp.headers.get("set-cookie");
        cfduid = re.findall("__cfduid=(.*?);",cookies)[0];
        phpSessId = re.findall("PHPSESSID=(.*?;)", cookies)[0];
        #phpSessId = phpSessId[:phpSessId.__len__()-2];
        self.cookies={"__cfduid":cfduid,"PHPSESSID":phpSessId}
        print(self.cookies)
        self.txtConsole.append("httpCookie初始化完成。")

    # 获取下个生成的邀请吗
    def nextVerfityCd(self):
        # 随机数种子长度×所需种子位数 作为底数好取值。
        numEvery = self.seedLength ** self.hiddenLength
        if self.offset >= (numEvery):  # 已经超出循环一圈
            return -1
        for index in range(0, self.hiddenLength):
            seedOne = self.seedText[(numEvery + self.offset) // (self.seedLength ** index) % self.seedLength];
            self.baseCode = self.baseCode[:self.baseCdPositionList[-(1 + index)]] + seedOne + self.baseCode[
                                                                                              self.baseCdPositionList[
                                                                                                  -(1 + index)] + 1:]
        self.txtCdNow.setText(self.baseCode)
        self.txtOffset.setText(str(self.offset))

        self.offset += 1;
        return self.baseCode;

    # 获取下个验证码
    def nextVerfityImg(self):
        randLeft = random.randint(1, 10 ** 8) * (10 ** 8);
        randRight = random.randint(1, 10 ** 8);
        randNum = (randLeft + randRight) / (10 ** 16);
        print(time.time())
        resp = self.session.get("https://www.t66y.com/require/codeimg.php?" + str(randNum),timeout=self.timeOut,cookies=self.cookies)
        print(time.time())
        imgFile = open("./data/unVerifityImg/" + str(randNum) + str(resp.headers.get("content-type")).replace("/", "."),
                       "wb");
        imgFile.write(resp.content)
        imgFile.close()
        self.label_2.setPixmap(QtGui.QPixmap(imgFile.name))

    def txtVerfityCdChange(self):  # 输入验证码后开始校验
        verfityCd = self.txtVerfityCd.text();
        if verfityCd.__len__() != 4:
            return;
        postData = {"reginvcode": self.baseCode,
                    "validate": verfityCd,
                    "action": "reginvcodeck"}
        print(time.time())
        resp = self.session.post("https://www.t66y.com/register.php?", data=postData,cookies=self.cookies)
        print(time.time())
        result = resp.text[resp.text.index("'") + 1:resp.text.index("'") + 2];
        resultInt = int(result)
        if resultInt == 2:
            self.nextVerfityImg();
        elif resultInt == 1:
            self.nextVerfityCd();
            self.nextVerfityImg();
        elif resultInt == 0:
            #验证码正确
            pass
        else:
            self.txtConsole.append("出现意外。")
        self.txtConsole.append(self.msg_invcode[resultInt])
        self.txtVerfityCd.setText("");


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    myshow = main()
    myshow.show()
    sys.exit(app.exec_())
