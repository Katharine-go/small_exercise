class user:
    def __init__(self,name,index =0,bor_report =[]):
        """

        :param name: 租借录像带的用户姓名
        :param index: 用户的id
        :param bor_report: 租借的电影列表
        """
        self.name = name
        self.index = index
        self.bor_report =[]

    def video_bor(self,bor_videotape,flag =1):
        if(len(self.bor_report) <5 or flag ==0):
            if flag ==1:
                self.bor_report.append(bor_videotape)
                return 1
            else:
                self.bor_report.remove(bor_videotape)
                return 2
        else:
            print("超出可借电影带数目")
            return 0

    def n_video(self):
        return len(self.bor_report)

    def list_video(self):
        for i in range(len(self.bor_report)):
            print(self.bor_report[i])