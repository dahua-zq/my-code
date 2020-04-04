student={"stuid":"001","stuname":"zhangsan","score":80}

students=[]

def menu():
    print("学生管理系统")
    print("1.添加学生的信息")
    print("2.删除学生的信息")
    print("3.修改学生的信息")
    print("4.查找学生的信息")
    print("0.退出系统")

def addstu(stu):
    newstu=findstu(stu["stuid"])
    if newstu==None:
        students.append(stu)
        print("添加成功")
    else:
        print("添加失败，学号已存在")

def addstufrominput():
    newstu = student.copy()
    newstu["stuid"] = input("请输入学号:")
    newstu["stuname"] = input("请输入姓名:")
    newstu["score"] = float(input("请输入分数:"))
    addstu(newstu)

def findstu(stu_id):
    for stu in students:
        if stu["stuid"] == stu_id:

            print("查找成功")
            print(stu)
            return stu
        else:
            print("查找失败,查找下一个")


def delstu(stu_id):
    newstu=findstu(stu_id)
    if newstu!=None:
        a = eval(input("是否确定删除此学生信息(0/1):"))
        if a == 1:
            students.remove(newstu)
            print("删除信息成功!")
        if a == 0:
            print("取消删除信息!")

def editstu(stu_id):
    newstu=findstu(stu_id)
    if newstu!=None:
        alternum = eval(input("1.修改姓名\n2.修改学号\n3.修改成绩\n4.退出\n"))
        if alternum == 1:
            newname = input("输入修改后的姓名:")
            newstu["stuname"] = newname
            print("修改成功!")
        elif alternum == 2:
            newid = input("输入修改后的学号:")
            newstu["stuid"] = newid
            print("修改成功!")
        elif alternum == 3:
            newscore = input("输入修改后的成绩:")
            newstu["score"] = newscore
            print("修改成功!")
        elif alternum == 4:
            exit()
        else:
            print("输入错误!")


def quit():
    print("感谢您使用本系统!")
    print("退出系统!")

while True:
    menu()
    a = eval(input("请输入你的选择:"))
    if a == 1:
        n = eval(input("请输入要添加学生n的个数:"))
        for i in range(n):
            addstufrominput()

    if a == 2:
        stu_id = input("请输入要删除的学生的学号:")
        delstu(stu_id)

    if a == 3:
        stu_id = input("请输入要修改的学生的学号:")
        editstu(stu_id)

    if a == 4:
        stu_id = input("请输入要查找学生的学号:")
        findstu(stu_id)

    if a == 0:
        quit()
        break