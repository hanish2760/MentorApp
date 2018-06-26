import threading
import time
import requests


home='http://127.0.0.1:8000/api/'

def GetStudentByid(id):

    req=requests.get(home+'students/'+str(id))
    print (req.json())
    pass

def GetStudentsByColleges(pk):
    req=requests.get(home+'colleges/'+str(pk)+'/students')
    print(req.json())
    pass



GetStudentByid(21)
print('\n')
GetStudentsByColleges(2)

t1=threading.Thread(name='f1',targer=GetStudentsByColleges,kwargs={'pk':2})
t1.start()
t2 = threading.Thread(name='f2', target=GetStudentByid,kwargs={'id':21})
t2.start()
def f1(q):
    pass

q=[1,2,3]

def create(self):
    t1 = threading.Thread(name='f1', targer=f1)
    t1.start()

