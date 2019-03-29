#-*-coding:utf-8-*-
import os,sys
os.getcwd()
sys.path.append(os.getcwd())
import threading
import time


def a(file,times):
    for i in range(times):
        print('a %s---%s'%(file,time.ctime()))
        time.sleep(2)

def b(file ,times):
    for i in range(times):
        print('b %s---%s'%(file,time.ctime()))
        time.sleep(2)
#创建线程组，用于装载线程
threads=[]
#创建线程a1,并添加到线程组
a1=threading.Thread(target=a,args=(u'大连必胜',2))
threads.append(a1)

a2=threading.Thread(target=b,args=(u'北京龟安',2))
threads.append(a2)

if __name__ == '__main__':

#启动线程
    for i in threads:
        i.start()
#守护线程
#如果不用join对诶个线程做等待终止，那么在线程运行过程中会直接执行最后终止end
    for i in threads:
        i.join()
    print ('threads end in %s'%time.ctime())



