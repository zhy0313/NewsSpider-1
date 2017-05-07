from urllib import request
from bs4 import BeautifulSoup
from http import cookiejar


class PageSpider(object):
    def __init__(self, page_url):
        self.page_url = page_url

    def getContent(self):
        try:
            response = request.urlopen(self.page_url)
            if response.getcode() != 200:
                print("fail to get to first page")
                return None

            html_cont = response.read()
            soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')

            main_content = soup.find('div', id = 'main_content')
            titleDiv = soup.find('div', id="titL")

            if main_content is not None:
                #获取文章标题
                title = soup.find('h1').text.strip()
                #获取发行时间
                datetime = soup.find('span', itemprop = 'datePublished').text.strip()

                #获取正文
                contents = []
                soup_contents = main_content.find_all('p')
                for con in soup_contents:
                    img = con.find('img')
                    #图片
                    if(img != None):
                        contents.append(['img', img['src']])
                    #正文
                    else:
                        contents.append(['p', con.text.strip()])

                print('title: ' + title)
                print('datetime: ' + datetime)
                for c in contents:
                    print("%s %s" % (c[0], c[1]))

                return {'title': title, 'datetime': datetime, 'content': contents}
            elif titleDiv is not None:
                #标题
                title = titleDiv.find('h1').text
                #日期及时间
                datetime = titleDiv.find('p').text

                head = soup.find('head')
                #获取解说文字
                p = head.find('meta',itemprop = 'description')['content']
                #获取图片
                img = head.find('meta',itemprop = 'image')['content']

                print('title: ' + title)
                print('datetime: ' + datetime)
                contents = [['img',img],['p',p]]
                for c in contents:
                    print("%s %s" % (c[0], c[1]))

                return {'title': title, 'datetime': datetime, 'content': contents}
            else :
                return None
        except:
            print("Something wrong!")
            return None






