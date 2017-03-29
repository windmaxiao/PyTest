import urllib.request
import os
import re


def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36')
    response = urllib.request.urlopen(url)
    html = response.read()

    return html

def get_page(url):

    html = url_open(url).decode('utf-8')
    #正则表达式查找页码
    page_find = r'<span class="current-comment-page">[[^[](\d\d\d\d)]</span>'
    page = re.findall(page_find,html)
    
    return page[0]
    
def find_imgs(url):
    html = url_open(url).decode('utf-8')
    img_addrs = []
    #正则表达式查找地址
    jpg_add = r'<img src="([^"]+\.jpg)"'
    gif_add = r'<img src="([^"]+\.gif)"'
    jpg_addrs = re.findall(jpg_add,html)
    gif_addrs = re.findall(gif_add,html)
    img_addrs = jpg_addrs+gif_addrs
    
    return img_addrs

def save_imgs(folder,img_addrs):

    for each in img_addrs:
        filename = each.split('/')[-1]   #取网址最后一段为文件名
        with open(filename,'wb') as f:
            img = url_open(each)
            f.write(img)
            
def download_mm(folder, pages):
    if os.path.exists(folder):      #判断文件夹123是否存在
        pass
    else:
        os.mkdir(folder)        #如不存在创建文件夹

    os.chdir(folder)            #打开文件夹

    url = 'http://jandan.net/ooxx/'
    page_num = int(get_page(url))

    for i in range(pages):
        page_num -= 1
        page_url = url + 'page-' + str(page_num) + '#comments'
        img_addrs = find_imgs(page_url)
        save_imgs(folder,img_addrs)

def main():
    while True:
        flag = input('开启爬虫？（y or n）:')
        if flag == 'y':
            name = input('请输入要创建的文件夹名称：')
            page = int(input('请输入要爬取的页数：'))
            print('爬取中.....')
            download_mm(name,page)
            print('爬取完成！！')
        elif flag == 'n':
            break
        
if __name__ == '__main__':
    main()
