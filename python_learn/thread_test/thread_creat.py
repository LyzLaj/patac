import threading
import time


# 方式一：通过threading。Thread创建多线程

def target(n1, n2):
    for i in range(n1, n2):
        print("线程 %s 的数值 %d" % (threading.currentThread().name, i))
        time.sleep(1)


print("线程 %s 的数值 %d" % (threading.currentThread().name, 1))


thread1 = threading.Thread(target=target, args=(1, 10))
thread2 = threading.Thread(target=target, args=(11, 20))
thread1.start()
thread2.start()


# 方式二：通过继承threading。Thread类

#
# class MyThread(threading.Thread):
#     def run(self):
#         for i in range(1, 10):
#             print("线程 %s 的数值 %d" % (threading.currentThread().name, i))
#             time.sleep(1)
#
#
# print("线程 %s 的数值 %d" % (threading.currentThread().name, 1))
#
# thread1 = MyThread()
# thread2 = MyThread()
# thread1.start()
# thread2.start()
