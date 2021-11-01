import json
import pandas as pd
import xlsxwriter



file ='madan_gowri.json'
data = None
with open(file, 'r') as f:
	data = json.load(f)

	
channel_id, stats = data.popitem()

channel_stats = stats["channel_statistics"]
video_stats = stats["video_data"]






sorted_vids = sorted(video_stats.items(), key=lambda item: int(item[1]["viewCount"]), reverse=True)
stats = []




print(channel_id)
print('views', channel_stats["viewCount"])
print('subscriber', channel_stats["subscriberCount"])
print('videos', channel_stats["videoCount"])


for vid in sorted_vids:
	#video_id = vid[1]
	#print(video_id)
	title = vid[1]["title"]
	#print(title)
	views = int(vid[1]["viewCount"])
	likes = int(vid[1]["likeCount"])
	dislikes = int(vid[1]["dislikeCount"])
	comments = int(vid[1]["commentCount"])
	stats.append([title, views,likes,dislikes,comments])

#video_id,

import pandas as pd   
df = pd.DataFrame(stats)
df.to_csv('filename.csv', index=False)
