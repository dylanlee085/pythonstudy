# coding: utf-8


import sys
sys.path.append('D:\\cmder\python\aliyun')


# 阿里云 api key
AccessKeyId = ''
AccessKeySecret = ''
# 服务器所在区
region = 'cn-shenzhen'
# jumpserver 账户密码
username = ''
password = ''

from jumpserver import aliyun_instance, jumpserver

# 获取主机列表
instances = aliyun_instance.instances(AccessKeyId, AccessKeySecret, region)
data = instances.get_instances()
for i in data:
    print(i)

# 创建operation实例
operation = jumpserver.operation_jumpserver()

# 获取token
token = operation.get_token(username, password)

# 获取用户信息
user_info = operation.get_user_info(token)
# print(user_info)

# # 创建节点
node_name = "阿里云"
nodes_list = operation.create_assets_nodes(token, node_name)

# 获取节点信息
nodes_list = operation.get_assets_nodes_list(token)

# 获取节点下的主机
for node_list in nodes_list:
    node_list = node_list['id']
    assets_list = operation.get_assets_assets_list(token, node_list)

# 向指定节点添加主机
for i in instances.get_instances():
    hostname = i[0]
    ip = i[1]
    assets_create = operation.create_assets_assets(token, nodes_list, hostname, ip)
    print(assets_create)


# 更新主机
src_node_list = '1b45617a-6212-4f09-9d36-4a3e6419f540'
des_node_list = '73451f08-6980-11ea-916d-54e1ad4e70e9'
assets_list = operation.get_assets_assets_list(token, src_node_list)
for i in assets_list:
    id = i['id']
    hostname = i["hostname"]
    ip = i["ip"]
    assets = operation.builk_update_assets_assets(token, des_node_list, id, hostname, ip)
    print(assets)



