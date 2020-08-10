#!/usr/bin/env python3
#coding=utf-8

import requests
import json

#api地址：https://www.dnspod.cn/docs/index.html
#获取api token：https://support.dnspod.cn/Kb/showarticle/tsid/227
dnspod_id = "xxxxx"  #获取到token对应的id
dnspod_token = "xxxxx" #获取到的token
domain = "example.com"  #域名
sub_domain = "xxxx" #记录
api_url = 'https://dnsapi.cn'
Type = "A"  #ipv6记录类型是"AAAA"，ipv4记录类型是"A"

if Type == "AAAA":
    try:
        real_value = requests.get("http://v6.ip.zxinc.org/getip",timeout=5).text
    except:
        real_value = json.loads(requests.get("http://ip.renfei.net",timeout=5).text).get("clientIP")
else:
    try:
        real_value = requests.get("http://members.3322.org/dyndns/getip",timeout=5).text.replace("\n", "")
    except:
        real_value = requests.get("http://ifconfig.me/ip",timeout=5).text
        #real_value = requests.get("http://ipinfo.io/ip",timeout=5).text.replace("\n", "")

def getRecordList():
    payload = {
        'login_token' : (dnspod_id+","+dnspod_token),
        'format' : "json",
        'domain' : domain,
        'sub_domain' : sub_domain
    }
    r = requests.post((api_url+"/Record.List"),data=payload)
    return r.json()['records'][0]

def addRecord():
    payload = {
        'login_token' : (dnspod_id+","+dnspod_token),
        'format' : "json",
        'domain' : domain,
        'sub_domain' : sub_domain,
        'record_type' : Type,
        'record_line' : "默认",
        'value' : real_value
    }
    r = requests.post((api_url+"/Record.Create"),data=payload)

def updateRecord(x):
    payload = {
        'login_token' : (dnspod_id+","+dnspod_token),
        'format' : "json",
        'domain' : domain,
        'record_id' : x,
        'sub_domain' : sub_domain,
        'record_line' : "默认",
        'record_type' : Type,
        'value' : real_value
    }
    r = requests.post((api_url+"/Record.Modify"),data=payload)

try:
    if getRecordList()['value'] != real_value:
        updateRecord(getRecordList()['id'])
        print("Update_record:",(sub_domain+"."+domain),real_value)
    else:
        print("Records don't need to be updated")
except:
    addRecord()
    print("Add_record:",(sub_domain+"."+domain),real_value)
