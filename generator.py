from datetime import datetime

print('init: ', datetime.now())
if __name__ == '__main__':
    #return object list
    pars = (value for value in range(10000000) if value % 2 == 0 )
    print(pars)
print('finish: ', datetime.now())
