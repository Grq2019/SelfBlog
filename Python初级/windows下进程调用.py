from multiprocessing import Process
import os
def run_process(name,num):
    if num==10:
        return
    print('Child process %s(%s) parent process is (%s)' %(name,os.getpid(),os.getppid()))
    num+=1
    p=Process(target=run_process,args=('test',num))
    p.start()
if __name__ == '__main__':
    print()
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_process, args=('test',1))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')
    