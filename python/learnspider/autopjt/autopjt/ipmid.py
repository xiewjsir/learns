# 导入随机数模块，目的是随机挑选一个IP池中的ip
import random
# 从settings文件（myfirstpjt.settings为settings文件的地址）中导入设置好的IPPOOL
from autopjt.settings import IPPOOL
# 导入官方文档中HttpProxyMiddleware对应的模块
from scrapy.contrib.downloadermiddleware.httpproxy import HttpProxyMiddleware

class IPPOOLS(HttpProxyMiddleware):
    # 初始化方法
    def __init__(self, ip=''):
        self.ip = ip

    # process_request()方法，主要进行请求处理
    def process_request(self, request, spider):
        # 先随机选择一个IP
        thisip = random.choice(IPPOOL)
        # 输出当前选择的IP，便于调试观察
        #print("当前使用的IP是：" + thisip["ipaddr"])
        # 将对应的IP实际添加为具体的代理，用该IP进行爬取
        request.meta["proxy"] = "http://" + thisip["ipaddr"]