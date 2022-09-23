try:
      for i in range(5):
            print(10/i,end='')
except ZeroDivisionError:
      print('除数为零，产生了除零错误！')
except:
      print('某种原因，出错了！')

