import os
import logging
def Search(pathname,text):
    try:
        for x in os.listdir(pathname):
            if os.path.isdir(x):
                Search(os.path.join(pathname,x),text)
            elif os.path.isfile(x) and os.path.splitext(x)[1]==text:
                print(os.path.join(pathname,x))
    except Exception as e:
        logging.exception(e)

if __name__ == '__main__':
    
    Search('C:\\Users\\Grq','.py')
    