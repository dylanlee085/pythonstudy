# coding=utf-8


import json
from aliyunsdkcore.client import AcsClient
# from aliyunsdkcore.acs_exception.exceptions import ClientException
# from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkecs.request.v20140526.DescribeInstancesRequest import DescribeInstancesRequest



class instances():
    def __init__(self, AccessKeyId, AccessKeySecret, region):
        self.AccessKeyId = AccessKeyId
        self.AccessKeySecret = AccessKeySecret
        self.region = region

    def get_instances(self):
        client = AcsClient(self.AccessKeyId, self.AccessKeySecret, self.region)
        request = DescribeInstancesRequest()
        request.set_accept_format('json')
        request.set_PageNumber(1)
        response = client.do_action_with_exception(request)
        TotalCount = json.loads(response)["TotalCount"]
        if TotalCount % 10 == 0:
            PageNums = TotalCount / 10
        else:
            PageNums = int(TotalCount / 10) + 1
        print("*****总共主机列表页面为%d每页为10条记录*****" % PageNums)
        for PageNum in range(1, PageNums+1):
            request = DescribeInstancesRequest()
            request.set_accept_format('json')
            request.set_PageNumber(PageNum)
            response = client.do_action_with_exception(request)
            for host in json.loads(response)["Instances"]["Instance"]:
                # info = [host["InstanceName"], host["NetworkInterfaces"]["NetworkInterface"][0]["PrimaryIpAddress"]]
                # yield info
                yield host

