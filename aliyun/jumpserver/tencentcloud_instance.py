0# -*- coding: utf-8 -*-
from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
# 导入对应产品模块的client models。
from tencentcloud.cvm.v20170312 import cvm_client, models


class instances():
    def __init__(self, AccessKeyId, AccessKeySecret, region):
        self.AccessKeyId = AccessKeyId
        self.AccessKeySecret0 = AccessKeySecret
        self.region = region

    def get_instances(self):
        try:
            # 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey
            cred = credential.Credential(AccessKeyId, AccessKeySecret)
            # 实例化要请求产品(以cvm为例)的client对象
            client = cvm_client.CvmClient(cred, region)
            # 实例化一个请求对象
            # req = models.DescribeZonesRequest()
            # # 通过client对象调用想要访问的接口，需要传入请求对象
            # resp = client.DescribeZones(req)

            req = models.DescribeInstancesRequest()
            resp = client.DescribeInstances(req)
            # 输出json格式的字符串回包
            print(resp.to_json_string())
            info = resp.to_json_string()
            return info
        except TencentCloudSDKException as err:
            print(err)

AccessKeyId = ''
AccessKeySecret = ''
region = 'ap-guangzhou'
instances = instances(AccessKeyId, AccessKeySecret, region)
instances.get_instances()