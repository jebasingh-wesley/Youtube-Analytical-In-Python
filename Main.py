from youtube_statistics import YTstats


API_KEY = "AIzaSyACqQvFC2ICnlKSb0Kx5s-0Jbnk7WiOeFE"
channel_id = "UC2v2_RW4vfFLTUxqa_c2WnQ"


yt = YTstats(API_KEY, channel_id)


yt.get_channel_statistics()
yt.get_channel_video_data()



yt.dump()