from user_imp import Users
from categories_imp import Categories
from course_imp import Courses
import json

user = Users(1,"Kevin","kevilezama@gmail.com",False)
print(user)

course1 = Courses("A001BAF","Docker and Kubernets",100.00,"5 stars",[user.user_name])
print(course1)

