# down pdf from ece and save
#  -*- coding:utf-8 -*-
# 完成功能，下载完整法规条款，到r120-R140
# 只下载英文版。待完成语言功能，选择下载英文，法文或俄文版
# 待完成显示功能，下载进度条显示
# 找不到网址的忽略，进行下一个
# 下载完成后 放入‘regulation 文件夹。及各法规文件件

import htmllib, formatter, urllib, re

def download_website(webbase_site, filename):
    f = urllib.urlopen(webbase_site+filename)
    print webbase_site+filename
    pdf_file = f.read()
    doc = open(filename[1:], 'wb')
    doc.write(pdf_file)
    doc.close()

    return

def download_webpage(pages):
    f = urllib.urlopen(pages)
    html = f.read()  # 将上述网页读入html
    # print html
    out_file = open(pages[-13:], 'w')
    out_file.write(html)
    k = 0
    while (k < len(html)):

        print len(html)
        i = html.lower().find('e.pdf', k)  # 下载pdf文件，找到".pdf" 字段位置, only English
        j = html.lower().find('/r', i - 14)  # 找到之前法规开始位置以eg. /r001xx.
        print j, i + 5, k  #
        if j < i:
            reg_name = html[j:i + 5]  # 截取法规号字段
            down_site = "http://www.unece.org/fileadmin/DAM/trans/main/wp29/wp29regs"
           # website = down_site + reg_name  # 固定的开始网页
            websiteupdate = "/updates" + reg_name
            # 异常前缀处理
            website2013 = "/2013" + reg_name  # check we can find there are some /2013/rxxx.pdf
            website2015 = "/2015" + reg_name  # check we can find there are some /2015/rxxx.pdf
            websiteold = "/old" + reg_name  # check we can find there are some /2015/rxxx.pdf

            # print website
        k = j + 50  ## check the html file ,we can find the next one ,at lest after

        if websiteupdate in html:
            webbase_site = down_site + '/updates'
        elif website2013 in html:
            webbase_site = down_site + '/2013'
        elif website2015 in html:
            webbase_site = down_site + '/2015'
        elif websiteold in html:
            webbase_site = down_site +'/old'
        else:
            webbase_site = down_site

        download_website(webbase_site, reg_name)

        if reg_name[2:5]=='020' or reg_name[2:5]=='040' or reg_name[2:5]=='060' or \
                        reg_name[2:5] == '080' or reg_name[2:5]=='100'or\
                        reg_name[2:5]=='120' or reg_name[2:5]=='140':
         # if r020,r040,r080,r100
            break


#if __name__ == '__main__':
#   main()
couter = 0

webbase_page = 'http://www.unece.org/trans/main/wp29/'
for couter in range(7):
    pagerange=str(20*couter+1)+'-'+str(20*(couter+1))
    download_page = webbase_page+"wp29regs"+pagerange+'.html'
    print download_page
    download_webpage(download_page)



print u'下载结束'
