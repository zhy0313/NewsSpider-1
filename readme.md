## 新闻网站爬虫

### PhoenixNews: 凤凰新闻网站

网站链接：http://news.ifeng.com/

__theme_spider__ 用于爬取分类的新闻网页的链接,将一个网页中的所有新闻的链接<br>
爬取到一个list中返回

__page_spider__  用于爬取该网页的内容，得到该新闻网页中该新闻的标题，发布时间<br>
以及正文，正文爬取时分为三种格式：p、strong和img，p为正文段落，strong为加粗字体，<br>
img为图片，并得到其链接，其储存顺序按照网页显示顺序

__mongodb_driver.py__  用于连接mongodb数据库，将爬取的数据储存在数据库中


