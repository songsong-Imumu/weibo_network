# -*- coding: utf-8 -*-
# author:           inspurer(月小水长)
# create_time:      2021/10/26 21:45
# 运行环境           Python3.6+
# github            https://github.com/inspurer
# 微信公众号         月小水长

from NewSuperWeiboForwardSpider import NewSuperWeiboForward

# cookie 是 filter 搜 repost
forwardSpider = NewSuperWeiboForward(mid='4467107636950632',
                                     cookie='')
forwardSpider.crawl()
