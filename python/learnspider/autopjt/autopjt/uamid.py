# uamid下载中间件
import urllib.request
import random
from autopjt.settings import UAPOOL
from scrapy.contrib.downloadermiddleware.useragent import UserAgentMiddleware

class Uamid(UserAgentMiddleware):
    def __init__(self, ua=''):
        self.ua = ua

    def process_request(self, request, spider):
        thisua = random.choice(UAPOOL)
        #print("当前使用的user-agent是：" + thisua)
        request.headers.setdefault('User-Agent', thisua)