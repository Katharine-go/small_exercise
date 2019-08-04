import user
import videotape
import bro_videotape
class shop(object):
    def __init__(self):

        self.video =[]
        self.report =[]
        self.overdue=[]
        self.user=[]
        self.day=30

    def addVideo(self,videotape):
        """
        添加库存：
          如果为新的录像带，直接添加到原有库存
          如果不是新的录像带，直接增加数量

        """
        if len(self.video) >0:
            flag =0
            for i in range(len(self.video)):
                if(self.video[i].index == videotape.index and self.video[i].name == videotape.name):
                    self.video[i].number += videotape.number
                    flag =1
                if(flag != 1):
                    self.video.append(videotape)
        else:
            self.video.append(videotape)

    def delVideo(self, videotape):

            """
            进行下货：
                库存中有录像带：
                    录像带数量小于所需数量：
                        输出提示--库存不够，只有多少数量
                    录像带数大于或等于所需数量：
                        减少库存，并输出提示--剩余库存数量
                        若数量减为0，则清除该录像带的记录
                库存中没有录像带：
                    输出提示--没有该录像带
            """
            flag = 0
            for i in range(len(self.video)):
                if (self.video[i].index == videotape.index and self.video[i].name == videotape.name):
                    flag = 1
                    if (self.video[i].number >= videotape.number):
                        self.video[i].number -= videotape.number
                        print('录像带ID：%s | 录像带名称：%s | 录像带剩余数量：%s | 录像带价格：%s' % (
                        self.video[i].index, self.video[i].name, self.video[i].number, self.video[i].price))
                        if (self.video[i].number == 0):
                            self.video.remove(self.video[i])
                    else:
                        print('录像带ID：%s | 录像带名称：%s | 录像带数量：%s | 录像带价格：%s' % (
                        self.video[i].index, self.video[i].name, self.video[i].number, self.video[i].price))
                        print("录像带库存数量不足！！请核对记录！！")
                    break
            if (flag == 0):
                print("库存中没有该录像带！！请核对记录！！")

    def findvideo(self, l):

            """
            查找录像带：
                库存中有录像带：
                    输出录像带详情以及借阅的相关信息
                库存中没有录像带：
                    输出提示--没有录像带
            """
            flag = 0
            if (isinstance(l, int)):
                """
                以录像带序列号为查找
                """
                for i in range(len(self.video)):
                    if (self.video[i].index == l):
                        flag = 1
                        print('录像带ID：%s | 录像带名称：%s | 录像带数量：%s | 录像带价格：%s' % (
                        self.video[i].index, self.video[i].name, self.video[i].number, self.video[i].price))
                        for i in range(len(self.report)):
                            if (self.report[i].video_id == l):
                                print('录像带名称：%s|录像带ID:%s|借录像带的人：%s|借阅时间：%s|应还时间:%s' % (
                                self.report[i].video_name, self.report[i].video_id, self.report[i].user_name,
                                self.report[i].user_id, self.report[i].time_bor, self.report[i].time_re))
                if (flag == 0):
                    print("库存中没有该录像带！！")
            else:
                for i in range(len(self.video)):
                    if (self.video[i].name == l):
                        flag = 1
                        print('录像带ID：%s | 录像带名称：%s | 录像带数量：%s | 录像带价格：%s' % (
                        self.video[i].index, self.video[i].name, self.video[i].number, self.video[i].price))
                        for i in range(len(self.report)):
                            if (self.report[i].video_name == l):
                                print('录像带名称：%s|录像带id:%s|借录像带的人：%s|借阅时间：%s|应还时间:%s' % (
                                self.report[i].video_name, self.report[i].video_id, self.report[i].user_name,
                                self.report[i].user_id, self.report[i].time_bor, self.report[i].time_re))

            if (flag == 0):
                print("库存中没有该产品！！")

    def adduser(self,user_name):
        u = user(user_name,len(self.user)+1)
        self.user.append(u)

    def finduser(self,l):
        flag =0
        if(isinstance(l,int)):
            """
                        以ID号为查找
                        """
            for i in range(len(self.user)):
                if (self.user[i].ind == l):
                    flag = 1
                    print(
                        '用户名称：%s | 用户ID：%s | 已借录像带数：%s' % (self.user[i].name, self.user[i].ind, self.user[i].n_video()))
            if (flag == 0):
                print("用户中没有该用户！！")
        else:
            for i in range(len(self.user)):
                if (self.user[i].name == l):
                    flag = 1
                    print(
                        '用户名称：%s | 用户ID：%s | 已借录像带数：%s' % (self.user[i].name, self.user[i].ind, self.user[i].n_video()))

            if (flag == 0):
                print("用户中没有该用户！！")

    def List_video(self):
        for i in range(len(self.video)):
            print('录像带ID：%s | 录像带名称：%s | 录像带数量：%s | 录像带价格：%s' % (
            self.video[i].index, self.video[i].name, self.video[i].number, self.video[i].price))

    def List_user(self):
        for i in range(len(self.user)):
            print('用户名称：%s | 用户ID：%s | 已借录像带数：%s' % (self.user[i].name, self.user[i].index, self.user[i].n_video()))

    def borrowVideo(self,video_l,user_ID,day):
        flag =0
        if (isinstance(video_l,int)):
            for i in range(len(self.video)):
                if(self.video[i].index == video_l):
                    flag = 1
                    if(self.video[i].number ==0):
                        print('该录像带已全部借出！')
                        for i in range(len(self.report)):
                            print(i)
                            if (self.report[i].video_id == video_l):
                                print('录像带名称：%s|录像带id:%s|借阅人ID：%s|借阅时间：%s|应还时间:%s' % (
                                self.report[i].video_name, self.report[i].video_id, self.report[i].user_id,
                                self.report[i].time_bor, self.report[i].time_re))
                        else:
                            re = bro_videotape(self.video[i].name, self.video[i].index, user_ID, day, self.day + day, day,
                                               0)
                            self.report.append(re)
                            flag1 = self.user[user_ID - 1].video_bor(re)
                            if (flag1 == 1):
                                self.video[i].number -= 1
                            print('用户名称：%s | 用户ID：%s | 已借录像带数：%s' % (
                            self.user[user_ID - 1].name, self.user[user_ID - 1].index, self.user[user_ID - 1].n_video()))

            if(flag == 0):
                print("库存中没有该录像带！")

        else:
            for i in range(len(self.video)):
                if (self.video[i].name == video_l):
                    flag = 1
                    if (self.video[i].number == 0):
                        print('该录像带已全部借出！')
                        for i in range(len(self.report)):
                            if (self.report[i].video_name == video_l):
                                print('录像带名称：%s|录像带id:%s|借阅人ID：%s|借阅时间：%s|应还时间:%s' % (
                                self.report[i].video_name, self.report[i].video_id, self.report[i].user_id,
                                self.report[i].time_bor, self.report[i].time_re))
                    else:
                        re = bro_videotape(self.video[i].name, self.video[i].index, user_ID, day, self.day + day, day, 0)
                        self.report.append(re)
                        flag1 = self.user[user_ID - 1].video_bor(re)
                        if (flag1 == 1):
                            self.video[i].number -= 1
                        print('用户名称：%s | 用户ID：%s | 已借录像带数：%s' % (
                        self.user[user_ID - 1].name, self.user[user_ID - 1].index, self.user[user_ID - 1].n_video()))

            if (flag == 0):
                print("库存中没有该录像带！")

        self.overduereport_update(day)
        self.user[user_ID - 1].list_video()

    def returnVideo(self, video_l, user_l, day):
        self.overduereport_update(day)
        if (isinstance(video_l, int)):
            for i in range(len(self.report)):
                if (self.report[i].video_id == video_l and self.report[i].user_id == user_l):
                    self.report.remove(self.report[i])
                    re = self.report[i]
                    self.user[user_l - 1].video_bor(re)
            for i in range(len(self.overdue)):
                if (self.overdue[i].video_id == video_l and self.overdue[i].user_id == user_l):
                    print('录像带名称：%s|录像带id:%s|借阅人ID：%s|借阅时间：%s|应还时间:%s|逾期时间：%s' % (
                    self.overdue[i].video_name, self.overdue[i].video_id, self.overdue[i].user_id,
                    self.overdue[i].time_bor, self.overdue[i].time_re, self.overdue[i].day))
                    self.overdue.remove(self.overdue[i])
            self.video[i].number += 1
        else:
            for i in range(len(self.report)):
                if (self.report[i].video_name == video_l and self.report[i].user_id == user_l):
                    self.report.remove(self.report[i])
            for i in range(len(self.overdue)):
                if (self.overdue[i].video_name == video_l and self.overdue[i].user_id == user_l):
                    self.overdue.remove(self.overdue[i])
            self.video[i].number += 1

    def list_report(self):
        for i in range(len(self.report)):
            print('录像带名称：%s|录像带id:%s|借阅人ID：%s|借阅时间：%s|应还时间:%s' % (
            self.report[i].video_name, self.report[i].video_id, self.report[i].user_id, self.report[i].time_bor,
            self.report[i].time_re))

    def overduereport_update(self, day):
        self.overdue = []
        for i in range(len(self.report)):
            if ((day - self.report[i].time_bor) > self.day):  # 逾期
                self.overdue.append(self.report[i])

    def overduereport(self, day):
        self.overduereport_update(day)
        for i in range(len(self.overdue)):
            print('录像带名称：%s|录像带id:%s|借阅人ID：%s|借阅时间：%s|应还时间:%s|逾期时间：%s' % (
            self.overdue[i].video_name, self.overdue[i].video_id, self.overdue[i].user_id, self.overdue[i].time_bor,
            self.overdue[i].time_re, self.overdue[i].day))




















