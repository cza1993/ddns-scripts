#!/usr/bin/env python3
#coding=utf-8

# 需要安装两个aliyun的库
# aliyun-python-sdk-core和aliyun-python-sdk-alidns
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkalidns.request.v20150109.DescribeSubDomainRecordsRequest import DescribeSubDomainRecordsRequest
from aliyunsdkalidns.request.v20150109.AddDomainRecordRequest import AddDomainRecordRequest
from aliyunsdkalidns.request.v20150109.UpdateDomainRecordRequest import UpdateDomainRecordRequest
import json
import requests

RR = "test"  #记录
DomainName = "example.com"  #域名
Type = "AAAA"  #ipv6记录类型是"AAAA"，ipv4记录类型是"A"
AccessKeyId = "***********" #换成自己的AccessKeyId
AccessKeySecret = "*************" #换成自己的AccessKeySecret
client = AcsClient(AccessKeyId,AccessKeySecret,'cn-hangzhou')
SubDomain = RR+"."+DomainName

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

def DescribeSDR(X):
    request = DescribeSubDomainRecordsRequest()
    request.set_accept_format('json')
    request.set_SubDomain(X)
    response = client.do_action_with_exception(request)
    return (json.loads(str(response, encoding='utf-8')).get('DomainRecords').get('Record'))[0]

def add_record(x):
    request = AddDomainRecordRequest()
    request.set_accept_format('json')
    request.set_DomainName(DomainName)
    request.set_RR(RR)
    request.set_Type(Type)
    request.set_Value(x)
    response = client.do_action_with_exception(request)
    return str(response, encoding='utf-8')

def update_record(x,y):
    request = UpdateDomainRecordRequest()
    request.set_accept_format('json')
    request.set_RecordId(x)
    request.set_RR(RR)
    request.set_Type(Type)
    request.set_Value(y)
    response = client.do_action_with_exception(request)
    return str(response, encoding='utf-8')

try:
    if DescribeSDR(SubDomain).get('Value') != real_value:
        update_record(DescribeSDR(SubDomain).get('RecordId'),real_value)
        print("Update_record:",SubDomain,real_value)
    else:
        print("Records don't need to be updated")
except:
    add_record(real_value)
    print("Add_record:",SubDomain,real_value)