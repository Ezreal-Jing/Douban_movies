import scrapy
from ..items import MovieItem

class MoviescrapeSpider(scrapy.Spider):
    name = 'moviescrape'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/subject/27203644/comments']

    def parse(self, response):#使用parse方法进行解析
        #提取数据
        for sel in response.css('div.comment-item '):
            #ID = sel.css('div.comment-item::attr(data-cid)').extract_first()#extract_first()直接返回字符串而不是列表，适用于只有一个字符串的列表
            comments = sel.css('div.comment-item div.comment p.comment-content span.short::text').extract_first()
            rating = sel.css('div.comment-item div.comment h3 span.comment-info span::attr(title)').extract_first()#注意不同星级所属的类不同
            #votes = sel.css('div.comment-item div.comment h3 span.comment-vote span.votes.vote-count::text').extract_first()


            movie = MovieItem()#创建item封装数据
            #movie['ID'] = ID#用户ID
            movie['comments'] = comments#评论正文
            movie['rating'] = rating#评价星级
            #movie['votes'] = votes#评价有用数量

            yield movie#通过生成器将items返回engine
        #提取链接，产生新的请求
        next_url = response.css('div#paginator.center a.next::attr(href)').extract_first()
        if next_url:#判断下一页链接是否存在
            next_url = response.urljoin(next_url)#通过urljoin函数生成绝对url地址
            yield scrapy.Request(next_url,callback=self.parse,meta={'cookiejar':'firefox'})#使用浏览器cookie登录
