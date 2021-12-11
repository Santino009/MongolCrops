import os  #与操作系统的交互
import requests
from docx import Document
from lxml import etree
from docx.shared import Inches, Pt
from docx.oxml.ns import qn
class MySpider():
    def __init__(self):
        self.headers = {
            'Cookie': 'PHPSESSID=nvughit10fb2upo2ptbh6sebj4; user_joqin=%7B%22U218265542%22%3A%2220201007%22%7D; qinggis_johiyal_id=%7B%22132515%22%3A1601995355%2C%22127323%22%3A1601995458%2C%22134681%22%3A1602030310%7D; hailta_ip=218.26.55.42; __tins__7950903=%7B%22sid%22%3A%201602030328310%2C%20%22vd%22%3A%201%2C%20%22expires%22%3A%201602032128310%7D; __51cke__=; __51laig__=1; u218265542=%7B%22ip%22%3A%22218.26.55.42%22%2C%22time_in%22%3A1602030330%2C%22count_rec%22%3A1%2C%22time_stop%22%3A0%7D; check_access=1; yunsuo_session_verify=32d9156c719f4fe0fc4135ed8f4d2bac',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'
        }


    def request(self, url):
        #获取标题
        all_title_href = requests.get(url, headers=self.headers)  #传递URL参数
        tree = etree.HTML(all_title_href.text)
        urls = tree.xpath('//div[@class="box_ga"]//a/@href')
        self.detail_info(urls)

        '''详情页'''
    def detail_info(self, urls):

        #http://www.qinggis.net/134357.html
        # urls = urls[0]
        # urls = [urls]
        for url in urls:
            new_url = 'http://www.qinggis.net/' + url
            print('正在获取:' + new_url)
            html_ = requests.get(new_url, headers=self.headers)
            html_.encoding = 'utf8'
            tree = etree.HTML(html_.text)    #调用HTML类进行初始化，构造XPath解析对象  ##lxml第一步是初始化。
            #content = tree.xpath('//div[@id="content"]//text()')
            string = ''   #清洗空白数据
            #for i in content:
               # string = string + i.strip()

            #隐藏之后的《续读》
            #id="content_all"
            content = tree.xpath('//div[@id="content_all"]//text()')
            for i in content:
                string = string + i.strip()
            self.save_to_doc(string, url)

    def save_to_doc(self, string, name):
        doc = Document()  # doc对象
      #  doc.styles["Normal"].font.size = Pt(9)   #字体大小设置
     #   doc.styles['Normal'].font.name = 'Menksoft2012'    #字体
    #    doc.styles['Normal']._element.rPr.rFonts.set(qn('w:eastAsia'), u'Menksoft2012')
        doc.add_paragraph(string)  # 添加文字
        doc.save('./data/{}.doc'.format(name))


if __name__ == '__main__':
    try:
        os.makedirs('data')
    except:
        pass
    spidef = MySpider()
    spidef.request("http://www.qinggis.net/index.php?act=contentlist&did=199&page=48")