# coding: utf-8


import requests
import json
import uuid

class operation_jumpserver():
    def __init__(self):
        pass

    # 获取token
    def get_token(self, username, password):
        url = 'http://192.168.22.250/api/v1/authentication/auth/'
        query_args = {
            "username": username,
            "password": password
        }
        response = requests.post(url, data=query_args)
        token = json.loads(response.text)['token']
        return token

    # 获取用户信息
    def get_user_info(self, token):
        url = 'http://192.168.22.250/api/v1/users/users/'
        header_info = {"Authorization": 'Bearer ' + token}
        response = requests.get(url, headers=header_info)
        info = json.loads(response.text)
        return info

    # 获取节点信息
    def get_assets_nodes_list(self, token):
        url = 'http://192.168.22.250/api/v1/assets/nodes/'
        header_info = {"Authorization": 'Bearer ' + token}
        response = requests.get(url, headers=header_info)
        node_list = json.loads(response.text)
        return node_list


    # 创建节点信息
    def create_assets_nodes(self, token, node_name):
        uid = str(uuid.uuid1())
        url = 'http://192.168.22.250/api/v1/assets/nodes/'
        payload = {
                    "id": uid,
                    "value": node_name
                  }
        # headers 中content-Type必须配置为application/json， 否则payload中内容无法被识别
        headers_info = {
            'Authorization': 'Bearer ' + token,
            'Content-Type': 'application/json'
        }
        payload = json.dumps(payload)
        response = requests.post(url, data=payload, headers=headers_info)
        nodes_list = json.loads(response.text)
        return nodes_list

    # 获取节点下的主机资产
    def get_assets_assets_list(self, token, nodes_list):
        url = 'http://192.168.22.250/api/v1/assets/assets/?node=' + nodes_list
        header_info = {"Authorization": 'Bearer ' + token, 'content-type': "application/json"}
        response = requests.get(url, headers=header_info)
        assets = json.loads(response.text)
        return assets


    # 添加主机资产
    def create_assets_assets(self, token, nodes_list, hostname, ip):
        url = 'http://192.168.22.250/api/v1/assets/assets/'
        payload = {
                    "ip": ip,
                    "hostname": hostname,
                    "platform": "Linux",
                    "nodes": [
                        nodes_list
                    ]
                  }
    # headers 中content-Type必须配置为application/json， 否则payload中内容无法被识别
        headers_info = {
            'Authorization': 'Bearer ' + token,
            'Content-Type': 'application/json'
        }
        payload = json.dumps(payload)
        response = requests.post(url, data=payload, headers=headers_info)
        assets = json.loads(response.text)
        return assets


    # 更新主机资产
    def builk_update_assets_assets(self, token, nodes_list, id, hostname, ip):
        url = 'http://192.168.22.250/api/v1/assets/assets/%s/' % id
        payload = {
                        "id": id,
                        "ip": ip,
                        "hostname": hostname,
                        "platform": "Linux",
                        "nodes": [
                            nodes_list
                        ]
                  }
    # headers 中content-Type必须配置为application/json， 否则payload中内容无法被识别
        headers_info = {
            'Authorization': 'Bearer ' + token,
            'Content-Type': 'application/json'
        }
        payload = json.dumps(payload)
        response = requests.put(url, data=payload, headers=headers_info)
        assets = json.loads(response.text)
        return assets
