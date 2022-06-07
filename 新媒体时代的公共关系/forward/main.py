from NewSuperWeiboForwardSpider import NewSuperWeiboForward

if __name__ == '__main__':
    # mid = 'LgMCuoK06'
    # 张文宏
    # mid = 'Ll8dE7wfL'
    # 李文亮
    # mid = 'Is9M7taaY'
    # 老坛酸菜牛肉面 中国新闻网
    # mid = 'LjT7nDMqE'
    # 杭州碎尸案二审
    # mid = 'LnuvM6F9C'
    # 教授
    # mid = 'Lnk5XocPS'
    # 新浪公益
    # mid = 'Lnnr5axnx'
    # 昆明专升本 地瓜熊老六
    # mid = 'LnLW3acor'
    # 人教版教材
    # mid = 'LuLajkggA'
    # 人教版教材，地瓜熊老六
    # mid = 'LuKqJvDXf'
    # 河南120
    mid = 'Lw1KObNuX'
    forwardSpider = NewSuperWeiboForward(mid=mid,
    start_page=1,
    limit=3000000,
    cookie='eat cookie')
    forwardSpider.crawl()