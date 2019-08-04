class bro_videotape:
    def __init__(self,video_name,video_id,user_id,time_bor,time_re,time_now,day):
        self.video_name = video_name
        self.video_id = video_id
        self.user_id = user_id
        self.time_bor = time_bor
        self.time_re = time_re
        self.time_now = time_now
        self.day = day

    def __str__(self):
        return '录像带名称: %s|录像带id: %s|租赁者: %s|借阅时间：%s|到期时间：%s'%(self.video_name,
                                                              self.video_id,self.user_id,self.time_bor,self.time_re)
    