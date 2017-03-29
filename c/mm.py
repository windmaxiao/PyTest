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
    #������ʽ����ҳ��
    page_find = r'<span class="current-comment-page">[[^[](\d\d\d\d)]</span>'
    page = re.findall(page_find,html)
    
    return page[0]
    
def find_imgs(url):
    html = url_open(url).decode('utf-8')
    img_addrs = []
    #������ʽ���ҵ�ַ
    jpg_add = r'<img src="([^"]+\.jpg)"'
    gif_add = r'<img src="([^"]+\.gif)"'
    jpg_addrs = re.findall(jpg_add,html)
    gif_addrs = re.findall(gif_add,html)
    img_addrs = jpg_addrs+gif_addrs
    
    return img_addrs

def save_imgs(folder,img_addrs):

    for each in img_addrs:
        filename = each.split('/')[-1]   #ȡ��ַ���һ��Ϊ�ļ���
        with open(filename,'wb') as f:
            img = url_open(each)
            f.write(img)
            
def download_mm(folder, pages):
    if os.path.exists(folder):      #�ж��ļ���123�Ƿ����
        pass
    else:
        os.mkdir(folder)        #�粻���ڴ����ļ���

    os.chdir(folder)            #���ļ���

    url = 'http://jandan.net/ooxx/'
    page_num = int(get_page(url))

    for i in range(pages):
        page_num -= 1
        page_url = url + 'page-' + str(page_num) + '#comments'
        img_addrs = find_imgs(page_url)
        save_imgs(folder,img_addrs)

def main():
    while True:
        flag = input('�������棿��y or n��:')
        if flag == 'y':
            name = input('������Ҫ�������ļ������ƣ�')
            page = int(input('������Ҫ��ȡ��ҳ����'))
            print('��ȡ��.....')
            download_mm(name,page)
            print('��ȡ��ɣ���')
        elif flag == 'n':
            break
        
if __name__ == '__main__':
    main()
