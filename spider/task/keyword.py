# coding:utf-8
import time

from spider.db.redis_db import Cookies
from spider.task.workers import app
from spider.service import keyword
from spider.loggers.log import crawler

logger = crawler
from WeChatModel.admin import KeywordDao


@app.task(ignore_result=True)
def keyword_task(kw):
    logger.info('使用:' + kw + '爬取公众号信息')
    keyword.search_keyword(kw)


@app.task(ignore_result=True)
def excute_keyword_task():
    infos = KeywordDao.get_enable()
    logger.info('本次搜索关键词个数:' + str(len(infos)))
    for info in infos:
        kw = info.name
        logger.info('分发账号爬取任务:' + kw)
        app.send_task('spider.task.keyword.keyword_task', args=[kw], queue='search_keyword_queue')
