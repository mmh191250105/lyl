def name(count):
    count=str(count)
    while(len(count)<6):
        count='0'+count
    return count+'.txt'
def rough_split():
    file1=open('C:/Users/LYL/Desktop/toutiao/tou8.txt','r',encoding='utf-8')
    count=11819
    addr='C:/Users/LYL/Desktop/toutiao/split/'
    i=0
    '''
    while(i<10):
        b=file1.readline()
        print(b)
        i=i+1
    '''
    while(True):
        judge=file1.readline()
        #print(judge)
        if judge.startswith('  {'):
            #print('yes')
            addr='C:/Users/LYL/Desktop/toutiao/split/'+name(count)
            file=open(addr,'w',encoding='utf-8')
            while(True):
                a=file1.readline();
                if not a.startswith('  }'):
                    file.write(a)
                    continue
                else:
                    break
            count=count+1
            continue
        if judge.startswith(']'):
            break
def detailed_split_news():
    count=1
    while(True):
        if count==14618:
            break
        source_addr='C:/Users/LYL/Desktop/toutiao/split/'+name(count)
        destination_addr='C:/Users/LYL/Desktop/toutiao/news_only/'+name(count)
        souce_file=open(source_addr,'r',encoding='utf-8')
        dest_file=open(destination_addr,'w',encoding='utf-8')
        souce_file.readline()
        souce_file.readline()
        a=souce_file.readline()[14:]
        dest_file.write(a)
        souce_file.close()
        dest_file.close()
        count=count+1
        continue
def detailed_split_comments():
    count = 1
    tag=0
    while (True):
        if count == 11972:
            break
        source_addr = 'C:/Users/LYL/Desktop/txt/split/' + name(count)
        destination_addr = 'C:/Users/LYL/Desktop/txt/comments_only/' + name(count)
        souce_file = open(source_addr, 'r', encoding='utf-8')
        dest_file = open(destination_addr, 'w', encoding='utf-8')
        for i in range(1,8):
            b=souce_file.readline()
            if(b.__contains__('[]')):
                count=count+1
                tag=1
                break
        if tag==1:
            tag=0
            continue
        while(True):
            a=souce_file.readline()
            if not a.startswith("    ]"):
                dest_file.write(a[7:])
                continue
            else:
                break
        souce_file.close()
        dest_file.close()
        count = count + 1
        continue

def split_media():
    file1 = open('C:/Users/LYL/Desktop/chinanews/中国新闻网国内0119以后.txt', 'r', encoding='utf-8')
    addr = 'C:/Users/LYL/Desktop/chinanews/split/'
    i = 0
    '''
    while(i<10):
        b=file1.readline()
        print(b)
        i=i+1
    '''
    count=8866
    while (True):
        judge = file1.readline()
        # print(judge)
        if judge.startswith('  {'):
            # print('yes')
            addr = 'C:/Users/LYL/Desktop/chinanews/split/' + name(count)
            file = open(addr, 'w', encoding='utf-8')
            while (True):
                a = file1.readline();
                if not a.startswith('  }'):
                    file.write(a)
                    continue
                else:
                    break
            count = count + 1
            continue
        if judge.startswith(']'):
            break

def detailed_split_media():
    count = 7998
    while (True):
        if count == 8902:
            break
        source_addr = 'C:/Users/LYL/Desktop/chinanews/split/' + name(count)
        destination_addr = 'C:/Users/LYL/Desktop/chinanews/others/' + name(count)
        souce_file = open(source_addr, 'r', encoding='utf-8')
        dest_file = open(destination_addr, 'w', encoding='utf-8')
        a=souce_file.readline()
        a=a[11:len(a)-3]
        dest_file.write(a)
        souce_file.readline()
        souce_file.readline()
        while(True):
            a = souce_file.readline()
            #print(a)
            if(a.startswith("      \"\"")):
                continue
            if not(a.startswith("    ]")):
                a=a[9:len(a)-3]
                dest_file.write(a)
                continue
            else:
                break
        souce_file.close()
        dest_file.close()
        count = count + 1
        continue

def sort_sign_news():
    search_count=1
    new_count=1
    likes_addr = 'C:/Users/LYL/Desktop/txt/likes&comments/likes.txt'
    comm_addr = 'C:/Users/LYL/Desktop/txt/likes&comments/comments.txt'
    likes = open(likes_addr, 'r', encoding='utf-8')
    comments = open(comm_addr, 'r', encoding='utf-8')
    print("人民日报：")
    while (True):
        if(search_count==4200):
            print("4.8-6.30: ")
            print(new_count)
        if (search_count == 6212):
            print("3.10-4.7: ")
            print(new_count)
        if (search_count == 8246):
            print("2.10-3.9: ")
            print(new_count)
        if (search_count == 10083):
            print("1.23-2.9 ")
            print(new_count)
        if (search_count == 11972):
            break
        key_addr = 'C:/Users/LYL/Desktop/txt/keywords_of_comments_only/' + name(search_count)
        destination_addr = 'C:/Users/LYL/Desktop/txt/imp_news/' + name(new_count)
        key_file = open(key_addr, 'r', encoding='utf-8')
        dest_file = open(destination_addr, 'w', encoding='utf-8')
        l = likes.readline()
        l = l[:len(l) - 1]
        c = comments.readline()
        c = c[:len(c) - 1]
        if (int(l) >= 100000 or int(c) >= 10000):
            a = key_file.readline()
            dest_file.write(a)
            new_count = new_count + 1
        key_file.close()
        dest_file.close()
        search_count = search_count + 1
    likes.close()
    comments.close()
    print("12.8-1.22: ")
    print(new_count)




    search_count=1
    new_count=1259
    likes_addr = 'C:/Users/LYL/Desktop/toutiao/likes&comments/likes.txt'
    comm_addr = 'C:/Users/LYL/Desktop/toutiao/likes&comments/comments.txt'
    likes = open(likes_addr, 'r', encoding='utf-8')
    comments = open(comm_addr, 'r', encoding='utf-8')
    print("今日头条：")
    while (True):

        if (search_count == 5598):
            print("4.8-6.30: ")
            print(new_count)
        if (search_count == 7747):
            print("3.10-4.7: ")
            print(new_count)
        if (search_count == 10026):
            print("2.10-3.9: ")
            print(new_count)
        if (search_count == 11839):
            print("1.23-2.9 ")
            print(new_count)
        if (search_count == 14618):
            break
        key_addr = 'C:/Users/LYL/Desktop/toutiao/keywords_of_comments_only/' + name(search_count)
        destination_addr = 'C:/Users/LYL/Desktop/toutiao/imp_news/' + name(new_count)
        key_file = open(key_addr, 'r', encoding='utf-8')
        dest_file = open(destination_addr, 'w', encoding='utf-8')
        l=likes.readline()
        l=l[:len(l)-1]
        c=comments.readline()
        c=c[:len(c)-1]
        if(int(l)>=20000 or int(c)>=2000):
            a=key_file.readline()
            dest_file.write(a)
            new_count=new_count+1
        key_file.close()
        dest_file.close()
        search_count=search_count+1
    print("12.8-1.22: " + new_count)
sort_sign_news()

def test():
    likes_addr = 'C:/Users/LYL/Desktop/txt/likes&comments/likes.txt'
    likes = open(likes_addr, 'r', encoding='utf-8')
    l = likes.readline()
    l=l[:len(l)-1]
    print(l)








# 直方图
import numpy
import pandas
import matplotlib.pyplot as plt
import seaborn
seaborn.set(context='notebook',font='simhei',style='whitegrid')
import warnings
#不发出警告
warnings.filterwarnings('ignore')
from scipy.stats import norm  # 使用直方图和最大似然高斯分布拟合绘制分布
def draw():
    '''
    rs = numpy.random.RandomState(50)  # 设置随机数种子
    s = pandas.Series(rs.randn(100) * 100)
    '''

    addr = 'C:/Users/LYL/Desktop/toutiao/likes&comments/likes.txt'
    list=[]
    file = open(addr, 'r', encoding='utf-8')
    count=1
    while(True):
        if(count<14618):
            a=file.readline()
            list.append(int(a[:len(a)-1]))
            count=count+1
            continue
        else:
            break
    list.sort()

    '''
    for i in range (1,10):
        list.pop()
        '''

    s=pandas.Series(list)


    #print(list)
    #C:\Users\LYL\Desktop\txt\likes&comments

    plt.figure(figsize=(16, 8))
    seaborn.distplot(s, bins=200, hist=True, kde=True, norm_hist=False,
                 rug=True, vertical=False, label='likes',
                 axlabel='点赞数(百万)', hist_kws={'color': 'y', 'edgecolor': 'k'},
                 fit=norm)
    # 用标准正态分布拟合
    plt.legend()
    plt.grid(linestyle='--')
    plt.show()









