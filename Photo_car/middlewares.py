# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import random


class PhotoCarSpiderMiddleware(object):
    # user-agents随机请求头中间件
    USER_AGENTS = [
        'Mozilla/5.0 (Macintosh; U; Intel Mac os x 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3299.84 Safari/537.36',
        'Mozilla/5.0 (compatible; MISE 9.0; Windows NT 6.1;Trident/5.0)',
        'Mozilla/4.0 (compatible; MISE 8.0; Windows NT 6.0;Trident/4.0)',
        'Mozilla/5.0 (Macintosh; Intel Mac os x 10.6; rv,2.0.1) Gecko/20100101 Firefox/4.0.1',
        'Mozilla/5.0 (Windows NT 6.1; rv,2.0.1) Gecko/20100101 Firefox/4.0.1',
    ]
    def process_request(self, request,spider):
        user_agent = random.choice(self.USER_AGENTS)
        request.headers['User-Agent'] = user_agent