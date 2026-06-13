class Student:
    def __init__(self, name, chinese,math,english):
        self.name = name
        self.chinese=chinese
        self.math=math
        self.english=english

    def __str__(self):
        return f"姓名：{self.name},语文成绩：{self.chinese},数学成绩：{self.math},英语成绩：{self.english},总分：{self.english+self.math+self.chinese}"

    def update(self,chinese=None,math=None,english=None):
        if chinese is not None:
            self.chinese=chinese
        if math is not None:
            self.math=math
        if english is not None:
            self.english=english


class EduManagement:
    system_version="1.0.0"
    system_name="教务管理系统"

    def __init__(self):
        self.student_list=[]

    def add_student(self):
        name=input("请输入学生姓名：")
        for s in self.student_list:
            if s.name==name:
                print("学生已经存在！")
                return
        chinese = int(input("请输入学生语文成绩："))
        math = int(input("请输入学生数学成绩："))
        english = int(input("请输入学生英语成绩："))
        if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
            stu = Student(name, chinese, math, english)
            self.student_list.append(stu)
            print("添加信息成功！")
        else:
            print("分数不正确！")

    def update_student(self):
        name=input("请输入要修改的学生姓名")
        for s in self.student_list:
            if s.name==name:
                print(f"当前成绩：{s}")
                chinese = int(input("请输入学生新的语文成绩："))
                math = int(input("请输入学生新的数学成绩："))
                english = int(input("请输入学生新的英语成绩："))
                if 0<=chinese<=100 and 0<=math<=100 and 0<=english<=100:
                    s.update(chinese,math,english)
                    print("修改信息成功！")
                    return
                else:
                    print("输入分数不正确！")
                    return
        print("输入学生名字不正确！")

    def delete_student(self):
        name=input("输入删除成绩的学生姓名")
        for s in self.student_list:
            if s.name==name:
                self.student_list.remove(s)
                print("删除成功！")
                return
        print("未找到学生！")

    def query_student(self):
        name=input("请输入查询学生姓名：")

        for s in self.student_list:
            if s.name==name:
                print(s)
                return
        print("未找到学生！")

    def show_student(self):
        for s in self.student_list:
            print(s)

    def run(self):
        print(f"欢迎使用教务管理系统V{EduManagement.system_version}")
        while True:
            print()
            print("#  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  ")
            print("# 1.添加学生  2.修改学生  3.删除学生  4.查询学生  5.展示所有学生  6.退出系统 #")
            print("#  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  ")

            choice=int(input("请输入想要执行的操作，输入1-6"))
            match choice:
                case 1:
                    self.add_student()
                case 2:
                    self.update_student()
                case 3:
                    self.delete_student()
                case 4:
                    self.query_student()
                case 5:
                    self.show_student()
                case 6:
                    break
                case _:
                    print("输入错误")

if __name__ == "__main__":
    edu_management=EduManagement()
    edu_management.run()

