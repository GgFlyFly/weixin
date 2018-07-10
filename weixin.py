#!/usr/bin/env python3
#_*_ coding:utf-8 _*_
import itchat
itchat.auto_login()#自动登录，扫描二维码
for friend in itchat.get_friends(update=True)[0:]:
    #用print查看好友微信名、备注、性别、省份
    print(friend['NickName'],friend['RemarkName'],friend['Sex'],friend['Province'],friend['Signature'])
    img = itchat.get_head_img(userName=friend["UserName"])
    path = "/Users/QYX/HeadImages/" + friend['NickName'] + "(" + friend['RemarkName']+").jpg"
    try:
        with open(path,"wb") as f:
            f.write(img)
    except Exception as e:
        print(repr(e))

itchat.run()
