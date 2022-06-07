from NewSuperWeiboForwardSpider import NewSuperWeiboForward

if __name__ == '__main__':
    # cookie 要换的，参考B站视频 BV1F44y1i7dq
    forwardSpider = NewSuperWeiboForward(mid='Is9M7taaY',
    start_page=1,
    limit=1000000,
    cookie='eat cookie')
    forwardSpider.crawl()