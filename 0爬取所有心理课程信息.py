from course_XL import *
from savefile import save1,load1
filename="new所有的心理课.csv"
f=open(filename,'w')
f.close()
v=[['课程id','课程名','学校id','学校名称','教师id','教师姓名','参与人数','评价人数']]
CourseInfo(v)
save_to_csv(v,filename)
save1(v,filename="AllCourse.model")
print('保存数组结束！')
# v=pd.DataFrame({"用户ID": x,"参与的课程": v1}) #第一列为数字序号
# v.to_csv(filename)
print("写入文件：{}结束！".format(filename))

# canyu,pingjia=[],[]
# with codecs.open('tmp所有的心理课.csv', encoding='utf-8') as f: #打开文件
#   items=csv.reader(f) #读取文件，这里不能直接输出
#   for row in items:
#     canyu.append(row[6]) #保存文件中第6列的信息
#     pingjia.append(row[7])
# canyu.pop(0) #第一个元素是列名称，所以要删掉
# pingjia.pop(0)
# s1,s2=0,0 #参与总人数，评价总人数
# for i in range(len(canyu)):
#     s1+=int(canyu[i])
#     s2+=int(pingjia[i])
# print("心理学参与总人数为{},评价总数为{}".format(s1,s2))

