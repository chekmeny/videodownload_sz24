import os
import you_get
import datetime
import time

date = int(input("请输入下载的日期，格式为20221212:"))#输入查询的日期
Ti = int(input("请输入结束下载的时间，仅取时如12:"))#输入查询的结束时间
disk = input("请输入输出文件夹的路径，例如C:/Users/admin/Desktop/videodowl:")#输入要输出视频的文件夹
#mode = int(input('请输入查询方式\n时间段视频下载——1\n单独视频下载——2\n'))
pos = int(input("请输入想要下载的视频地点后方代号：\n石岩梯度塔西南21\n福田2\n罗湖3\n西涌4\n全选5\n请输入你的选择："))

h1=1#定义大于10的时间为h1
h2=1#定义小于10的时间为h2
m=1#初始分钟数
start = datetime.datetime.now()

if Ti >= 10 :
    if pos == 5:
        for h2 in range(0,10,1):

                for m in range(1,7,2):
                    print('正在下载%d的时间为0%d:%d9的视频'%(date,h2,m))
                    os.system('you-get -o %s https://weather.121.com.cn/data_cache/video/rt/files/rt_121_%s0%s%s9.mp4' %(disk,date,h2,m))
                    os.system('you-get -o %s https://weather.121.com.cn/data_cache/video/rt/files/rt_73_%s0%s%s9.mp4' %(disk,date,h2,m))#福田东
                    os.system('you-get -o %s https://weather.121.com.cn/data_cache/video/rt/files/rt_78_%s0%s%s9.mp4' %(disk,date,h2,m))#福田西
                    os.system('you-get -o %s https://weather.121.com.cn/data_cache/video/rt/files/rt_75_%s0%s%s9.mp4' %(disk,date,h2,m))#福田南
                    os.system('you-get -o %s https://weather.121.com.cn/data_cache/video/rt/files/rt_80_%s0%s%s9.mp4' %(disk,date,h2,m))#福田北
                    os.system('you-get -o %s https://weather.121.com.cn/data_cache/video/rt/files/rt_106_%s0%s%s9.mp4' %(disk,date,h2,m))#罗湖东北
                    os.system('you-get -o %s https://weather.121.com.cn/data_cache/video/rt/files/rt_102_%s0%s%s9.mp4' %(disk,date,h2,m))#罗湖西南
                    os.system('you-get -o %s https://weather.121.com.cn/data_cache/video/rt/files/rt_46_%s0%s%s9.mp4' %(disk,date,h2,m))#西涌南
                    time.sleep(10)

        for h1 in range(10,Ti+1,1):

                for m in range(1,7,2):
                    print('正在下载%d的时间为%d:%d9的视频'%(date,h1,m))
                    os.system('you-get -o %s https://weather.121.com.cn/data_cache/video/rt/files/rt_121_%s%s%s9.mp4' %(disk,date,h1,m))
                    os.system('you-get -o %s https://weather.121.com.cn/data_cache/video/rt/files/rt_73_%s%s%s9.mp4' %(disk,date,h1,m))#福田东
                    os.system('you-get -o %s https://weather.121.com.cn/data_cache/video/rt/files/rt_78_%s%s%s9.mp4' %(disk,date,h1,m))#福田西
                    os.system('you-get -o %s https://weather.121.com.cn/data_cache/video/rt/files/rt_75_%s%s%s9.mp4' %(disk,date,h1,m))#福田南
                    os.system('you-get -o %s https://weather.121.com.cn/data_cache/video/rt/files/rt_80_%s%s%s9.mp4' %(disk,date,h1,m))#福田北
                    os.system('you-get -o %s https://weather.121.com.cn/data_cache/video/rt/files/rt_106_%s%s%s9.mp4' %(disk,date,h1,m))#罗湖东北
                    os.system('you-get -o %s https://weather.121.com.cn/data_cache/video/rt/files/rt_102_%s%s%s9.mp4' %(disk,date,h1,m))#罗湖西南
                    os.system('you-get -o %s https://weather.121.com.cn/data_cache/video/rt/files/rt_46_%s%s%s9.mp4' %(disk,date,h1,m))#西涌南
                    time.sleep(10)

    elif pos == 1:#石岩梯度塔西南2
        for h2 in range(0,10,1):

                for m in range(1,7,2):
                    print('正在下载石岩梯度塔西南2%d的时间为0%d:%d9的视频'%(date,h2,m))
                    os.system('you-get -o %s https://weather.121.com.cn/data_cache/video/rt/files/rt_121_%s0%s%s9.mp4' %(disk,date,h2,m))
                    time.sleep(10)

        for h1 in range(10,Ti+1,1):

                for m in range(1,7,2):
                    print('正在下载石岩梯度塔西南2%d的时间为%d:%d9的视频'%(date,h1,m))
                    os.system('you-get -o %s https://weather.121.com.cn/data_cache/video/rt/files/rt_121_%s%s%s9.mp4' %(disk,date,h1,m))
                    time.sleep(10)
    
    elif pos == 2:#福田
        for h2 in range(0,10,1):

                for m in range(1,7,2):
                    print('正在下载福田%d的时间为0%d:%d9的视频'%(date,h2,m))
                    os.system('you-get -o %s https://weather.121.com.cn/data_cache/video/rt/files/rt_73_%s0%s%s9.mp4' %(disk,date,h2,m))#福田东
                    os.system('you-get -o %s https://weather.121.com.cn/data_cache/video/rt/files/rt_78_%s0%s%s9.mp4' %(disk,date,h2,m))#福田西
                    os.system('you-get -o %s https://weather.121.com.cn/data_cache/video/rt/files/rt_75_%s0%s%s9.mp4' %(disk,date,h2,m))#福田南
                    os.system('you-get -o %s https://weather.121.com.cn/data_cache/video/rt/files/rt_80_%s0%s%s9.mp4' %(disk,date,h2,m))#福田北
                    time.sleep(10)

        for h1 in range(10,Ti+1,1):

                for m in range(1,7,2):
                    print('正在下载福田%d的时间为%d:%d9的视频'%(date,h1,m))
                    os.system('you-get -o %s https://weather.121.com.cn/data_cache/video/rt/files/rt_73_%s%s%s9.mp4' %(disk,date,h1,m))#福田东
                    os.system('you-get -o %s https://weather.121.com.cn/data_cache/video/rt/files/rt_78_%s%s%s9.mp4' %(disk,date,h1,m))#福田西
                    os.system('you-get -o %s https://weather.121.com.cn/data_cache/video/rt/files/rt_75_%s%s%s9.mp4' %(disk,date,h1,m))#福田南
                    os.system('you-get -o %s https://weather.121.com.cn/data_cache/video/rt/files/rt_80_%s%s%s9.mp4' %(disk,date,h1,m))#福田北
                    time.sleep(10)

    elif pos == 3:#罗湖
        for h2 in range(0,10,1):

                for m in range(1,7,2):
                    print('正在下载罗湖%d的时间为0%d:%d9的视频'%(date,h2,m))
                    os.system('you-get -o %s https://weather.121.com.cn/data_cache/video/rt/files/rt_106_%s0%s%s9.mp4' %(disk,date,h2,m))#罗湖东北
                    os.system('you-get -o %s https://weather.121.com.cn/data_cache/video/rt/files/rt_102_%s0%s%s9.mp4' %(disk,date,h2,m))#罗湖西南
                    time.sleep(10)

        for h1 in range(10,Ti+1,1):

                for m in range(1,7,2):
                    print('正在下载罗湖%d的时间为%d:%d9的视频'%(date,h1,m))
                    os.system('you-get -o %s https://weather.121.com.cn/data_cache/video/rt/files/rt_106_%s%s%s9.mp4' %(disk,date,h1,m))#罗湖东北
                    os.system('you-get -o %s https://weather.121.com.cn/data_cache/video/rt/files/rt_102_%s%s%s9.mp4' %(disk,date,h1,m))#罗湖西南
                    time.sleep(10)

    elif pos == 4:#西涌
        for h2 in range(0,10,1):

                for m in range(1,7,2):
                    print('正在下载西涌%d的时间为0%d:%d9的视频'%(date,h2,m))
                    os.system('you-get -o %s https://weather.121.com.cn/data_cache/video/rt/files/rt_46_%s0%s%s9.mp4' %(disk,date,h2,m))#西涌南
                    time.sleep(10)

        for h1 in range(10,Ti+1,1):

                for m in range(1,7,2):
                    print('正在下载西涌%d的时间为%d:%d9的视频'%(date,h1,m))
                    os.system('you-get -o %s https://weather.121.com.cn/data_cache/video/rt/files/rt_46_%s%s%s9.mp4' %(disk,date,h1,m))#西涌南
                    time.sleep(10)

else:

    if pos == 5:
        for h2 in range(0,Ti+1,1):

                for m in range(1,7,2):
                    print('正在下载%d的时间为0%d:%d9的视频'%(date,h2,m))
                    os.system('you-get -o %s https://weather.121.com.cn/data_cache/video/rt/files/rt_121_%s0%s%s9.mp4' %(disk,date,h2,m))
                    os.system('you-get -o %s https://weather.121.com.cn/data_cache/video/rt/files/rt_73_%s0%s%s9.mp4' %(disk,date,h2,m))#福田东
                    os.system('you-get -o %s https://weather.121.com.cn/data_cache/video/rt/files/rt_78_%s0%s%s9.mp4' %(disk,date,h2,m))#福田西
                    os.system('you-get -o %s https://weather.121.com.cn/data_cache/video/rt/files/rt_75_%s0%s%s9.mp4' %(disk,date,h2,m))#福田南
                    os.system('you-get -o %s https://weather.121.com.cn/data_cache/video/rt/files/rt_80_%s0%s%s9.mp4' %(disk,date,h2,m))#福田北
                    os.system('you-get -o %s https://weather.121.com.cn/data_cache/video/rt/files/rt_106_%s0%s%s9.mp4' %(disk,date,h2,m))#罗湖东北
                    os.system('you-get -o %s https://weather.121.com.cn/data_cache/video/rt/files/rt_102_%s0%s%s9.mp4' %(disk,date,h2,m))#罗湖西南
                    os.system('you-get -o %s https://weather.121.com.cn/data_cache/video/rt/files/rt_46_%s0%s%s9.mp4' %(disk,date,h2,m))#西涌南
                    time.sleep(10)

    

    elif pos == 1:#石岩梯度塔西南2
        for h2 in range(0,Ti+1,1):

                for m in range(1,7,2):
                    print('正在下载石岩梯度塔西南2%d的时间为0%d:%d9的视频'%(date,h2,m))
                    os.system('you-get -o %s https://weather.121.com.cn/data_cache/video/rt/files/rt_121_%s0%s%s9.mp4' %(disk,date,h2,m))
                    time.sleep(10)

    
    elif pos == 2:#福田
        for h2 in range(0,Ti+1,1):

                for m in range(1,7,2):
                    print('正在下载福田%d的时间为0%d:%d9的视频'%(date,h2,m))
                    os.system('you-get -o %s https://weather.121.com.cn/data_cache/video/rt/files/rt_73_%s0%s%s9.mp4' %(disk,date,h2,m))#福田东
                    os.system('you-get -o %s https://weather.121.com.cn/data_cache/video/rt/files/rt_78_%s0%s%s9.mp4' %(disk,date,h2,m))#福田西
                    os.system('you-get -o %s https://weather.121.com.cn/data_cache/video/rt/files/rt_75_%s0%s%s9.mp4' %(disk,date,h2,m))#福田南
                    os.system('you-get -o %s https://weather.121.com.cn/data_cache/video/rt/files/rt_80_%s0%s%s9.mp4' %(disk,date,h2,m))#福田北
                    time.sleep(10)

    
    elif pos == 3:#罗湖
        for h2 in range(0,Ti+1,1):

                for m in range(1,7,2):
                    print('正在下载罗湖%d的时间为0%d:%d9的视频'%(date,h2,m))
                    os.system('you-get -o %s https://weather.121.com.cn/data_cache/video/rt/files/rt_106_%s0%s%s9.mp4' %(disk,date,h2,m))#罗湖东北
                    os.system('you-get -o %s https://weather.121.com.cn/data_cache/video/rt/files/rt_102_%s0%s%s9.mp4' %(disk,date,h2,m))#罗湖西南
                    time.sleep(10)

        

    elif pos == 4:#西涌
        for h2 in range(0,Ti+1,1):

                for m in range(1,7,2):
                    print('正在下载西涌%d的时间为0%d:%d9的视频'%(date,h2,m))
                    os.system('you-get -o %s https://weather.121.com.cn/data_cache/video/rt/files/rt_46_%s0%s%s9.mp4' %(disk,date,h2,m))#西涌南
                    time.sleep(10)

        
end = datetime.datetime.now()
dur = end-start
print('下载已完成')
print('用时:', dur)
