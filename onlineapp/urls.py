from django.conf.urls import url
from django.urls import path
#need to remove this
from onlineapp.SerializerViews.CollegeRestViews import *
from onlineapp.SerializerViews.StudentRestViews import *
from onlineapp.views.college import *
from rest_framework_jwt.views import *
urlpatterns = [

    # path('test/',test),
    # path('populate_db/',upload_data),
    # auth
    # url(r'^api-token-refresh/', refresh_jwt_token),
    # url(r'^api-token-auth/', obtain_jwt_token),
    # url(r'^api-token-verify/', verify_jwt_token),
    path("colleges/", CollegeListView.as_view(),name="collegesList"),
    # id is pk
    path('colleges/<int:pk>/', CollegeDetailsView.as_view(),name="marks"),
    path('colleges/<int:pk>/addstudent/',CreateStudentView.as_view(),name="addstudent"),
    path('colleges/createcollege/', CreateCollegeView.as_view(),name="createcollege"),
    path('colleges/<int:pk>/deletecollege/', DeleteCollegeView.as_view(),name="deletecollege"),
    path('colleges/<int:pk>/editcollege/', EditCollegeView.as_view(),name="editcollege"),
    path('colleges/<int:pk>/deletestudent/', DeleteStudentView.as_view(), name="deletestudent"),
    path('colleges/<int:pk>/editstudent/', EditStudentView.as_view(), name="editstudent"),
    path('signup/',singnUpView.as_view(),name='signup'),
    path('',LoginView.as_view(),name='login'),
    path('logout/',logout_user,name="logout"),
    path('api/colleges/<int:pk>/',CollegeDetailsRestView),
    path('api/colleges/', CollegeListRestView),

    path('api/students/', StudentList.as_view()),
    path('api/students/<int:sid>/', StudentList.as_view()),
    #get all students in  a college.
    #post a student in a college.
    path('api/colleges/<int:pk>/students/', StudentList.as_view()),
    #get a particular student,all students in that college..
    # put,delete a student in a college.(update)
    path('api/colleges/<int:pk>/students/<int:sid>/', StudentList.as_view()),

]


#  path('testview2/', views.testview2)
# path("colleges/",CollegeView.as_view())
# path('hk/',views.first_hello),
# path('email/',views.emailname),
# path('std/<int:id>/',views.iddetails),
# path('collegelist/',views.CollegeList),
# path('collegedetails/<str:acr>/',views.CollegeDetails),
# path('testview/',views.testview),





"""
http://127.0.0.1:8000/api/students/

    {
        "id": 121,
        "name": "madhu",
        "dob": null,
        "email": "dg@gmail.com",
        "db_folder": "sdfsf",
        "dropped_out": false,
        "college": 11
    }

PUT  request to url with the json data as the above 

"""
