import numpy as np
import pandas as pd
import pymysql
import json



def MySqlReadData(sqlText,
                  Ip="192.168.1.160",
                  port=3306,
                  db="SLProDB",
                  charset="utf8"):
    mysql_cn = pymysql.connect(
        host=Ip,
        port=port,
        user="root",
        db=db,
        charset=charset,
        password="admin")
    return pd.read_sql(sqlText, con=mysql_cn)


class ProInfoSig(object):
    def __init__(self):
        self.name = ""
        self.des = ""
        self.company = ""
        self.wnd = []



def MakeJilu(recordDt, fileName = ""):
    dicProCnt = {}
    dicDesCnt = {}
    dicCompanyCnt = {}
    for sig in recordDT:
        s = sig["process_info"].replace("\\", "\\\\")
        try:
            tempJsData = json.loads(s)
        except json.decoder.JSONDecodeError:
            print("异常数据注意查看", sig["id"], s)
            continue
        tempPlistData = tempJsData["process"]
        for i in tempPlistData:
            name = i["name"].lower()
            if dicProCnt.get(name) is None:
                dicProCnt[name] = {}
                dicProCnt[name]["cnt"] = 1
                dicProCnt[name]["des"] = i["des"]
                dicProCnt[name]["company"] = i["com"]
            else:
                dicProCnt[name]["cnt"] += 1

            des = i["des"].lower().replace(",", "@")
            if dicDesCnt.get(des) is None:
                dicDesCnt[des] = {}
                dicDesCnt[des]["cnt"] = 1
                dicDesCnt[des]["name"] = i["name"]
                dicDesCnt[des]["company"] = i["com"]
            else:
                dicDesCnt[des]["cnt"] += 1

            com = i["com"].lower().replace(",", "#")
            if dicCompanyCnt.get(com) is None:
                dicCompanyCnt[com] = {}
                dicCompanyCnt[com]["cnt"] = 1
                dicCompanyCnt[com]["name"] = i["name"]
                dicCompanyCnt[com]["des"] = i["des"]
            else:
                dicCompanyCnt[com]["cnt"] += 1
    with open("pro%s.csv" % fileName, "w") as f:
        for k in dicProCnt.keys():
            f.write("%s,%d,%s,%s\n" %
                    (k, dicProCnt[k]["cnt"], dicProCnt[k]["des"],
                     dicProCnt[k]["company"]))

    with open("des%s.csv"%fileName, "w") as f:
        for k in dicDesCnt.keys():
            f.write("%s,%d,%s,%s\n" %
                    (k, dicDesCnt[k]["cnt"], dicDesCnt[k]["name"],
                     dicDesCnt[k]["company"]))

    with open("company%s.csv"%fileName, "w") as f:
        for k in dicCompanyCnt.keys():
            f.write("%s,%d,%s,%s\n" %
                    (k, dicCompanyCnt[k]["cnt"], dicCompanyCnt[k]["des"],
                     dicCompanyCnt[k]["name"]))


def WriteFile(recordDt, fileName = ""):
    # with open(fileName,"w",encoding="utf-8") as f:
    #     json.dump(recordDt, fileName, ensure_ascii=False)
    with open(fileName, "w") as f:
        for i in recordDt:
            f.write(i["process_info"])
            f.write("\r\n")

def GetModuleCheck(data):
    ret = []
    for key in data.keys():
        if data[key] == "" or key == "mo":
            continue;
        else:
            ret.append(key)
    return ret


if __name__ == "__main__":


    #统计进程终端出现次数
    dicProCnt = {}
    dicDesCnt = {}
    dicCompanyCnt = {}

    #计费模型
    Module = [
        {
            "name": "",
            "des": "计费安全组件",
            "com": "成都吉胜科技有限责任公司",
            "sign": "",
            "tle": "",
            "mo": "计费"
        },
        {
            "name": "",
            "des": "佳星计费",
            "com": "西安英奇计算机工程有限公司",
            "sign": "",
            "tle": "",
            "mo": "计费"
        },
        {
            "name": "",
            "des": "8圈网吧经营管理平台",
            "com": "跃动网络",
            "sign": "",
            "tle": "",
            "mo": "计费"
        },
        {
            "name": "",
            "des": "嘟嘟牛计费系统客户端",
            "com": "深圳市嘟嘟牛科技有限公司",
            "sign": "",
            "tle": "",
            "mo": "计费"
        },
        {
            "name": "",
            "des": "网吧远程管理服务",
            "com": "杭州顺网科技股份有限公司",
            "sign": "",
            "tle": "",
            "mo": "无盘"
        },
        {
            "name": "",
            "des": "启动器",
            "com": "杭州顺网科技股份有限公司",
            "sign": "",
            "tle": "",
            "mo": "无盘"
        },
        {
            "name": "",
            "des": "EyooMenu",
            "com": "湖北盛天网络技术股份有限公司",
            "sign": "",
            "tle": "",
            "mo": "无盘"
        },
        {
            "name": "",
            "des": "易乐游客户端主程序",
            "com": "湖北盛天网络技术股份有限公司",
            "sign": "",
            "tle": "",
            "mo": "无盘"
        },
        {
            "name": "",
            "des": "万象客户端网盾实名插件",
            "com": "成都吉胜科技有限责任公司",
            "sign": "",
            "tle": "",
            "mo": "实名"
        },
        {
            "name": "culclientview.exe",
            "des": "翔天净网-网络文化监管系统客户端",
            "com": "",
            "sign": "",
            "tle": "",
            "mo": "实名"
        },
        {
            "name": "amn.exe",
            "des": "翔天净网-网络文化监管系统客户端 setup",
            "com": "",
            "sign": "",
            "tle": "",
            "mo": "实名"
        },
        {
            "name": "",
            "des": "PubWin客户端实名插件",
            "com": "上海新浩艺软件有限公司",
            "sign": "",
            "tle": "",
            "mo": "实名"
        },
        {
            "name": "",
            "des": "网盾实名模块",
            "com": "优码创达软件技术有限公司",
            "sign": "",
            "tle": "",
            "mo": "实名"
        },
        {
            "name": "",
            "des": "网盾实名审计保护程序",
            "com": "深圳市希之光科技有限公司",
            "sign": "",
            "tle": "",
            "mo": "实名"
        },
        {
            "name": "",
            "des": "万象网吧管理软件客户端",
            "com": "成都吉胜科技",
            "sign": "",
            "tle": "",
            "mo": "计费"
        },
        {
            "name": "",
            "des": "8圈智能场所管理平台",
            "com": "跃动网络",
            "sign": "",
            "tle": "",
            "mo": "计费"
        },
        {
            "name": "",
            "des": "上网场所安全服务系统终端配置程序",
            "com": "重庆智多信息发展有限公司",
            "sign": "",
            "tle": "",
            "mo": "实名"
        },
        {
            "name": "",
            "des": "clsmn",
            "com": "成都吉胜科技有限责任公司",
            "sign": "",
            "tle": "",
            "mo": "计费"
        },
        {
            "name": "",
            "des": "迅闪网吧远程管理服务",
            "com": "上海新浩艺软件有限公司",
            "sign": "",
            "tle": "",
            "mo": "无盘"
        },
        {
            "name": "",
            "des": "BarClientSafeCenter.exe",
            "com": "上海新浩艺软件有限公司",
            "sign": "",
            "tle": "",
            "mo": "实名"
        },
        {
            "name": "",
            "des": "净网先锋(2013)-客户端",
            "com": "北京万辰博海文化传播有限公司",
            "sign": "",
            "tle": "",
            "mo": "实名"
        },
        {
            "name": "CulClientView.exe",
            "des": "翔天净网-网络文化监管系统客户端",
            "com": "",
            "sign": "",
            "tle": "",
            "mo": "实名"
        },
        {
            "name": "NSdominatsd.exe",
            "des": "",
            "com": "",
            "sign": "Chongqing Intelligent Information Tech Co.,Ltd",
            "tle": "",
            "mo": "计费"
        },
        {
            "name": "",
            "des": "",
            "com": "成都吉胜科技有限责任公司",
            "sign": "成都吉胜科技有限责任公司",
            "tle": "",
            "mo": "计费"
        },
        {
            "name": "",
            "des": "",
            "com": "吉胜科技",
            "sign": "成都吉胜科技有限责任公司",
            "tle": "",
            "mo": "计费"
        },
        {
            "name": "knbclient.exe",
            "des": "",
            "com": "",
            "sign": "成都边锋领沃网络技术有限公司",
            "tle": "",
            "mo": "无盘"
        },
        {
            "name": "",
            "des": "wxcltaidex",
            "com": "新浩艺软件技术有限公司",
            "sign": "shanghai xin hao yi software Co., Ltd",
            "tle": "",
            "mo": "计费"
        },
        {
            "name": "",
            "des": "",
            "com": "杭州召唤科技有限公司",
            "sign": "杭州召唤科技有限公司",
            "tle": "",
            "mo": "无盘"
        },
        # 1、类型:计费, 进程名称:wxcltaidex.exe,标题:万象网管
        # 2、无盘， 进程名称:BarClientView.exe, 公司：顺网网维大师
        #{"name":"","des":"","com":"","sign":"","tle":"","mo":""},
        {
            "name": "",
            "des": "",
            "com": "",
            "sign": "",
            "tle": "万象网管",
            "mo": "计费"
        },
        {
            "name": "BarClientView.exe",
            "des": "",
            "com": "顺网网维大师",
            "sign": "",
            "tle": "",
            "mo": "无盘"
        },
        {"name":"pwcli.exe","des":"丕微科技企业有限公司--网吧客户端","com":"","sign":"","tle":"","mo":"计费"},
        {"name":"pwcli.exe","des":"","com":"丕微科技企业有限公司","sign":"","tle":"","mo":"计费"},
        {"name":"","des":"丕微科技企业有限公司--网吧客户端","com":"丕微科技企业有限公司","sign":"","tle":"","mo":"计费"},
        {"name":"","des":"OBT计费系统","com":"OBTZA","sign":"","tle":"","mo":"计费"},
        {"name":"","des":"OBT计费系统","com":"","sign":"西安正奥实业有限公司","tle":"","mo":"计费"},
        {"name":"msgwin.exe","des":"","com":"OBTZA","sign":"","tle":"","mo":"计费"},
        {"name":"msgwin.exe","des":"","com":"","sign":"西安正奥实业有限公司","tle":"","mo":"计费"},
        {"name":"","des":"镜像P2P服务","com":"杭州顺网科技股份有限公司","sign":"","tle":"","mo":"无盘"},
        {"name":"","des":"镜像P2P服务","com":"","sign":"Hangzhou Shunwang Technology Co.,Ltd","tle":"","mo":"无盘"},
        {"name":"knbmenu.exe","des":"","com":"","sign":"成都边锋领沃网络技术有限公司","tle":"","mo":"无盘"},
        {"name":"UDO.exe","des":"嘟嘟牛计费系统客户端","com":"","sign":"","tle":"","mo":"计费"},
        {"name":"UDO.exe","des":"","com":"深圳市嘟嘟牛科技有限公司","sign":"","tle":"","mo":"计费"},
        {"name":"UDO.exe","des":"","com":"","sign":"深圳市嘟嘟牛科技有限公司","tle":"","mo":"计费"},
        {"name":"","des":"嘟嘟牛计费系统客户端","com":"深圳市嘟嘟牛科技有限公司","sign":"","tle":"","mo":"计费"},
        {"name":"","des":"嘟嘟牛计费系统客户端","com":"","sign":"深圳市嘟嘟牛科技有限公司","tle":"","mo":"计费"},
        {"name":"wxcltaidex.exe","des":"wxcltaidex","com":"","sign":"","tle":"","mo":"计费"},
        {"name":"wxcltaidex.exe","des":"","com":"新浩艺软件技术有限公司","sign":"","tle":"","mo":"计费"},
        {"name":"","des":"wxcltaidex","com":"新浩艺软件技术有限公司","sign":"","tle":"","mo":"计费"},
        {"name":"wxcltaidex.exe","des":"","com":"成都吉胜科技有限责任公司","sign":"","tle":"","mo":"计费"},
        {"name":"wxcltaidex.exe","des":"","com":"","sign":"shanghai xin hao yi software Co., Ltd","tle":"","mo":"计费"},
        {"name":"","des":"wxcltaidex","com":"成都吉胜科技有限责任公司","sign":"","tle":"","mo":"计费"},
        {"name":"","des":"wxcltaidex","com":"","sign":"shanghai xin hao yi software Co., Ltd","tle":"","mo":"计费"},
        {"name":"LOCALSER.EXE","des":"嘟嘟牛计费","com":"","sign":"","tle":"","mo":"计费"},
        {"name":"LOCALSER.EXE","des":"","com":"嘟嘟牛计费","sign":"","tle":"","mo":"计费"},
        {"name":"LOCALSER.EXE","des":"","com":"","sign":"深圳市嘟嘟牛科技股份有限公司","tle":"","mo":"计费"},
        {"name":"","des":"嘟嘟牛计费","com":"嘟嘟牛计费","sign":"","tle":"","mo":"计费"},
        {"name":"","des":"嘟嘟牛计费","com":"","sign":"深圳市嘟嘟牛科技股份有限公司","tle":"","mo":"计费"},
        {"name":"八哥计费.exe","des":"八哥计费","com":"","sign":"","tle":"","mo":"计费"},
        {"name":"wxCashier.exe","des":"PUBWIN OL收银端","com":"","sign":"","tle":"","mo":"计费"},
        {"name":"wxCashier.exe","des":"","com":"新浩艺科技有限责任公司","sign":"","tle":"","mo":"计费"},
        {"name":"wxCashier.exe","des":"","com":"","sign":"shanghai xin hao yi software Co., Ltd","tle":"","mo":"计费"},
        {"name":"","des":"PUBWIN OL收银端","com":"新浩艺科技有限责任公司","sign":"","tle":"","mo":"计费"},
        {"name":"","des":"PUBWIN OL收银端","com":"","sign":"shanghai xin hao yi software Co., Ltd","tle":"","mo":"计费"},
        {"name":"JFCLI.exe","des":"计费大师客户端","com":"","sign":"","tle":"","mo":"计费"},
        {"name":"JFCLI.exe","des":"","com":"www.jifeidashi.com","sign":"","tle":"","mo":"计费"},
        {"name":"","des":"计费大师客户端","com":"www.jifeidashi.com","sign":"","tle":"","mo":"计费"},
        {"name":"pwClient6.0.exe","des":"","com":"","sign":"","tle":"piway计费系统6.0","mo":"计费"},
        {"name":"ZHLHBarClient.exe","des":"召唤绿化大师客户端","com":"","sign":"","tle":"","mo":"无盘"},
        {"name":"ZHLHBarClient.exe","des":"","com":"杭州召唤科技有限公司","sign":"","tle":"","mo":"无盘"},
        {"name":"","des":"召唤绿化大师客户端","com":"杭州召唤科技有限公司","sign":"","tle":"","mo":"无盘"},
        {"name":"kvnserver64.exe","des":"","com":"","sign":"成都边锋领沃网络技术有限公司","tle":"","mo":"无盘"},
        {"name":"lwclient64.exe","des":"","com":"","sign":"成都边锋领沃网络技术有限公司","tle":"","mo":"无盘"},
        {"name":"lwhardware64.exe","des":"","com":"","sign":"成都边锋领沃网络技术有限公司","tle":"","mo":"无盘"},
        {"name":"BarClientView.exe","des":"网吧游戏管理客户端","com":"","sign":"","tle":"","mo":"无盘"},
        {"name":"BarClientView.exe","des":"","com":"杭州顺网科技股份有限公司","sign":"","tle":"","mo":"无盘"},
        {"name":"BarClientView.exe","des":"","com":"","sign":"Hangzhou Shunwang Technology Co.,Ltd","tle":"","mo":"无盘"},
        {"name":"","des":"网吧游戏管理客户端","com":"杭州顺网科技股份有限公司","sign":"","tle":"","mo":"无盘"},
        {"name":"","des":"网吧游戏管理客户端","com":"","sign":"Hangzhou Shunwang Technology Co.,Ltd","tle":"","mo":"无盘"},
        {"name":"","des":"网吧游戏管理客户端","com":"","sign":"","tle":"","mo":"无盘"},
        {"name":"ZHLHBarClientTask.exe","des":"召唤绿化大师客户端启动程序","com":"","sign":"","tle":"","mo":"无盘"},
        {"name":"ZHLHBarClientTask.exe","des":"","com":"杭州召唤科技有限公司","sign":"","tle":"","mo":"无盘"},
        {"name":"yqsclient.exe","des":"摇钱树网管客户端主程序","com":"","sign":"","tle":"","mo":"计费"},
        {"name":"yqsclient.exe","des":"","com":"郑州易灵信软件有限公司","sign":"","tle":"","mo":"计费"},
        {"name":"yqsclient.exe","des":"","com":"","sign":"郑州易灵信软件有限公司","tle":"","mo":"计费"},
        {"name":"","des":"摇钱树网管客户端主程序","com":"郑州易灵信软件有限公司","sign":"","tle":"","mo":"计费"},
        {"name":"","des":"摇钱树网管客户端主程序","com":"","sign":"郑州易灵信软件有限公司","tle":"","mo":"计费"},
        {"name":"rwyNCMc.exe","des":"","com":"深圳任网游科技发展有限公司","sign":"","tle":"","mo":"计费"},
        {"name":"rwyNCMc.exe","des":"","com":"","sign":"深圳任网游科技发展有限公司","tle":"","mo":"计费"}, 


        {"name":"knbclient.exe","des":"","com":"","sign":"杭州边锋网络技术有限公司","tle":"","mo":"无盘"},
        {"name":"knbmenu.exe","des":"","com":"","sign":"杭州边锋网络技术有限公司","tle":"","mo":"无盘"},
        {"name":"eyoorun.exe","des":"易乐游客户端主程序","com":"","sign":"","tle":"","mo":"无盘"},
        {"name":"eyoorun.exe","des":"","com":"Hubei Century Network Technology Co., Ltd.","sign":"","tle":"","mo":"无盘"},
        {"name":"","des":"易乐游客户端主程序","com":"Hubei Century Network Technology Co., Ltd.","sign":"","tle":"","mo":"无盘"},
        {"name":"BarClientView.exe","des":"APlus Module","com":"","sign":"","tle":"","mo":"无盘"},
        {"name":"BarClientView.exe","des":"","com":"上海新浩艺软件有限公司","sign":"","tle":"","mo":"无盘"},
        {"name":"BarClientView.exe","des":"","com":"","sign":"Shanghai Hintsoft Co., Ltd.","tle":"","mo":"无盘"},
        {"name":"","des":"APlus Module","com":"","sign":"Shanghai Hintsoft Co., Ltd.","tle":"","mo":"无盘"},
        {"name":"","des":"","com":"上海新浩艺软件有限公司","sign":"Shanghai Hintsoft Co., Ltd.","tle":"","mo":"无盘"},
        {"name":"P2PSyncService.exe","des":"镜像P2P服务","com":"","sign":"","tle":"","mo":"无盘"},
        {"name":"P2PSyncService.exe","des":"","com":"上海新浩艺软件有限公司","sign":"","tle":"","mo":"无盘"},
        {"name":"P2PSyncService.exe","des":"","com":"","sign":"Shanghai Hintsoft Co.,Ltd.","tle":"","mo":"无盘"},
        {"name":"","des":"镜像P2P服务","com":"上海新浩艺软件有限公司","sign":"","tle":"","mo":"无盘"},
        {"name":"","des":"镜像P2P服务","com":"","sign":"Shanghai Hintsoft Co.,Ltd.","tle":"","mo":"无盘"},
        {"name":"RichtechGameMenu.exe","des":"锐起八爪鱼游戏菜单","com":"","sign":"","tle":"","mo":"无盘"},
        {"name":"RichtechGameMenu.exe","des":"","com":"","sign":"上海锐起信息科技有限公司","tle":"","mo":"无盘"},
        {"name":"","des":"","com":"锐起八爪鱼游戏菜单","sign":"上海锐起信息科技有限公司","tle":"","mo":"无盘"},
        {"name":"eyoocore.exe","des":"E-yoo Client Core Service","com":"","sign":"","tle":"","mo":"无盘"},
        {"name":"eyoocore.exe","des":"","com":"湖北盛天网络技术股份有限公司","sign":"","tle":"","mo":"无盘"},
        {"name":"","des":"E-yoo Client Core Service","com":"湖北盛天网络技术股份有限公司","sign":"","tle":"","mo":"无盘"},

        {"name":"yqs.exe","des":"摇钱树游戏客户端","com":"","sign":"","tle":"","mo":"计费"},
        {"name":"yqs.exe","des":"","com":"金华市盘古信息技术有限公司","sign":"","tle":"","mo":"计费"},
        {"name":"yqs.exe","des":"","com":"","sign":"金华市盘古信息技术有限公司","tle":"","mo":"计费"},
        {"name":"","des":"摇钱树游戏客户端","com":"金华市盘古信息技术有限公司","sign":"","tle":"","mo":"计费"},
        {"name":"","des":"摇钱树游戏客户端","com":"","sign":"金华市盘古信息技术有限公司","tle":"","mo":"计费"},
        {"name":"PubwinClient.exe","des":"","com":"","sign":"shanghai xin hao yi software Co., Ltd","tle":"","mo":"计费"},
        {"name":"cltupdate.exe","des":"CltUpdate Module","com":"","sign":"","tle":"","mo":"计费"},
        {"name":"cltupdate.exe","des":"","com":"新浩艺软件技术有限公司","sign":"","tle":"","mo":"计费"},
        {"name":"cltupdate.exe","des":"","com":"","sign":"shanghai xin hao yi software Co., Ltd","tle":"","mo":"计费"},
        {"name":"","des":"CltUpdate Module","com":"新浩艺软件技术有限公司","sign":"","tle":"","mo":"计费"},
        {"name":"","des":"CltUpdate Module","com":"","sign":"shanghai xin hao yi software Co., Ltd","tle":"","mo":"计费"},
        {"name":"wxplgctl64.exe","des":"wxplgctl64","com":"","sign":"","tle":"","mo":"计费"},
        {"name":"wxplgctl64.exe","des":"","com":"HintSoft","sign":"","tle":"","mo":"计费"},
        {"name":"wxplgctl64.exe","des":"","com":"","sign":"shanghai xin hao yi software Co., Ltd","tle":"","mo":"计费"},
        {"name":"","des":"wxplgctl64","com":"HintSoft","sign":"","tle":"","mo":"计费"},
        {"name":"","des":"wxplgctl64","com":"","sign":"shanghai xin hao yi software Co., Ltd","tle":"","mo":"计费"},


        {"name":"BarClientView.exe","des":"","com":"","sign":"","tle":"游戏菜单","mo":"无盘"},
        {"name":"menu.exe","des":"方格子网娱平台V6","com":"","sign":"","tle":"","mo":"无盘"},
        {"name":"menu.exe","des":"","com":"上海网恒文化传播有限公司","sign":"","tle":"","mo":"无盘"},
        {"name":"menu.exe","des":"","com":"","sign":"Shanghai wangheng Co., LTD","tle":"","mo":"无盘"},
        {"name":"","des":"方格子网娱平台V6","com":"上海网恒文化传播有限公司","sign":"","tle":"","mo":"无盘"},
        {"name":"","des":"方格子网娱平台V6","com":"","sign":"Shanghai wangheng Co., LTD","tle":"","mo":"无盘"},
        # {"name":"","des":"","com":"","sign":"","tle":"","mo":""},
        # {"name":"","des":"","com":"","sign":"","tle":"","mo":""},
        # {"name":"","des":"","com":"","sign":"","tle":"","mo":""},
        # {"name":"","des":"","com":"","sign":"","tle":"","mo":""},
        # {"name":"","des":"","com":"","sign":"","tle":"","mo":""},
        # {"name":"","des":"","com":"","sign":"","tle":"","mo":""},
        # {"name":"","des":"","com":"","sign":"","tle":"","mo":""},
        # {"name":"","des":"","com":"","sign":"","tle":"","mo":""},
        # {"name":"","des":"","com":"","sign":"","tle":"","mo":""},
        # {"name":"","des":"","com":"","sign":"","tle":"","mo":""},
        # {"name":"","des":"","com":"","sign":"","tle":"","mo":""},
        # {"name":"","des":"","com":"","sign":"","tle":"","mo":""},
        # {"name":"","des":"","com":"","sign":"","tle":"","mo":""},
        # {"name":"","des":"","com":"","sign":"","tle":"","mo":""},
        #         {"name":"","des":"","com":"","sign":"","tle":"","mo":""},
        # {"name":"","des":"","com":"","sign":"","tle":"","mo":""},
        # {"name":"","des":"","com":"","sign":"","tle":"","mo":""},
        # {"name":"","des":"","com":"","sign":"","tle":"","mo":""},
        # {"name":"","des":"","com":"","sign":"","tle":"","mo":""},
        # {"name":"","des":"","com":"","sign":"","tle":"","mo":""},
        # {"name":"","des":"","com":"","sign":"","tle":"","mo":""},
        # {"name":"","des":"","com":"","sign":"","tle":"","mo":""},
        # {"name":"","des":"","com":"","sign":"","tle":"","mo":""},
        # {"name":"","des":"","com":"","sign":"","tle":"","mo":""},
        # {"name":"","des":"","com":"","sign":"","tle":"","mo":""},
        # {"name":"","des":"","com":"","sign":"","tle":"","mo":""},////


        {"name":"","des":"召唤绿化大师客户端启动程序","com":"杭州召唤科技有限公司","sign":"","tle":"","mo":"无盘"}
        # {"name":"","des":"","com":"","sign":"","tle":"","mo":""},////
#         100000 30917 398 0 1879
# 不满足的个数 33194
# 占总记录的0.33
#         计费：	名称					描述												公司										签名
# 		pwcli.exe				丕微科技企业有限公司--网吧客户端					
# 		pwcli.exe																	丕微科技企业有限公司
# 								丕微科技企业有限公司--网吧客户端					丕微科技企业有限公司
# 								OBT计费系统											OBTZA										
# 								OBT计费系统																						西安正奥实业有限公司
								
								
# 		msgwin.exe																												西安正奥实业有限公司
# 		msgwin.exe																	OBTZA											

 
#  无盘：	名称					描述												公司										签名
# 								镜像P2P服务											杭州顺网科技股份有限公司		
# 								镜像P2P服务																						Hangzhou Shunwang Technology Co.,Ltd
# 		knbmenu.exe																												成都边锋领沃网络技术有限公司
    ]

    moduleNoShiPing = []
    for data in Module:
        if data["mo"] == "实名":
            continue
        else:
            moduleNoShiPing.append(data)
    print(moduleNoShiPing)

    print("现在模型的个数",len(moduleNoShiPing))
    RecordWuPan=[]
    RecordJiFei=[]
    RecordShiMing=[]
    RecordFullNo = []

    dt = MySqlReadData("select id,process_info from qt_new_proc181031 limit 0,100000")
    #print(dt["process_info"])
    proDataList = []
    recordDT = dt.to_dict(orient="record")
    recordNoModule = []
    recordModule = []

    for sig in recordDT:
        s = sig["process_info"].replace("\\", "\\\\")
        try:
            tempJsData = json.loads(s)
        except json.decoder.JSONDecodeError:
            # print("异常数据注意查看",sig["id"],s)
            continue
        tempPlistData = tempJsData["process"]
        moduleName = []
        for i in tempPlistData:
            for m in moduleNoShiPing:
                li = GetModuleCheck(m)
                b = True
                for ckey in li:
                    if ckey == "tle":
                        if len(i["wnd"]) == 0:
                            # print("需要检测标题的类型", m);
                            b = False
                            break
                        bTiteIs = False
                        for wndInfo in i["wnd"]:
                            if wndInfo["tite"].lower() == m[ckey].lower():
                                bTiteIs = True
                                break
                        if bTiteIs == False:
                            b = False
                            break
                        else:
                            print("标题满足",sig["id"])
                            continue
                    if m[ckey].lower() != i[ckey].lower():
                        b = False
                        break
                if b:
                    if m["mo"] not in moduleName:
                        moduleName.append(m["mo"])

                # if m["name"] == "" and m["sign"]=="":
                #     if i["des"].lower() == m["des"].lower() and i["com"].lower() == m["com"].lower():
                #         if m["mo"] in moduleName:
                #             continue
                #         else:
                #             moduleName.append(m["mo"])
                # if m["des"] == "" and m["sign"] == "":
                #     if i["name"].lower() == m["name"].lower() and i["com"].lower() == m["com"].lower():
                #         if m["mo"] in moduleName:
                #             continue
                #         else:
                #             moduleName.append(m["mo"])
                # if m["com"] == "" and m["sign"] == "":
                #     if i["name"].lower() == m["name"].lower() and i["des"].lower() == m["des"].lower():
                #         if m["mo"] in moduleName:
                #             continue
                #         else:
                #             moduleName.append(m["mo"])
                # if m["com"] == "" and m["des"] == "":
                #     if i["name"].lower() == m["name"].lower(
                #     ) and i["sign"].lower() == m["sign"].lower():
                #         if m["mo"] in moduleName:
                #             continue
                #         else:
                #             moduleName.append(m["mo"])
                # if m["com"] == "" and m["name"] == "":
                #     if i["sign"].lower() == m["sign"].lower(
                #     ) and i["des"].lower() == m["des"].lower():
                #         if m["mo"] in moduleName:
                #             continue
                #         else:
                #             moduleName.append(m["mo"])
                # if m["name"] == "" and m["des"] == "":
                #     if i["com"].lower() == m["com"].lower() and i["sign"].lower(
                #     ) == m["sign"].lower():
                #         if m["mo"] in moduleName:
                #             continue
                #         else:
                #             moduleName.append(m["mo"])






        print(sig["id"], moduleName)
        if(len(moduleName) == 2):
            recordModule.append(sig)
        else:
            recordNoModule.append(sig)
        if len(moduleName) == 1 and moduleName[0] == "无盘":
            RecordWuPan.append(sig)
        if len(moduleName) == 1 and moduleName[0] == "计费":
            RecordJiFei.append(sig)
        # if len(moduleName) == 1 and moduleName[0] == "实名":
        #     RecordShiMing.append(sig)
        if len(moduleName) == 0:
            RecordFullNo.append(sig)

    print(len(recordDT),len(RecordWuPan),len(RecordJiFei),len(RecordShiMing),len(RecordFullNo))
    dayNew = "31_"
    cnt = 0
    WriteFile(RecordWuPan, "%s_无盘%d.txt"%(dayNew,cnt))
    WriteFile(RecordJiFei, "%s_计费%d.txt" % (dayNew, cnt))
    WriteFile(RecordShiMing, "%s_实名%d.txt" % (dayNew, cnt))
    WriteFile(RecordFullNo, "%s_完全不匹配%d.txt" % (dayNew, cnt))
    print("不满足的个数",len(recordNoModule))
    print("占总记录的%.2f"%(len(recordNoModule)/len(recordDT)))
    # MakeJilu(recordNoModule,"2")
    print("ok")
