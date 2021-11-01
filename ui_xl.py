import json
import pandas as pd
import xlsxwriter



file ='hornpipe_record_label.json'
data = None
with open(file, 'r') as f:
	data = json.load(f)

	
channel_id, stats = data.popitem()
print(channel_id)
channel_stats = stats["channel_statistics"]
video_stats = stats["video_data"]


print('views', channel_stats["viewCount"])
print('subscriber', channel_stats["subscriberCount"])
print('videos', channel_stats["videoCount"])



sorted_vids = sorted(video_stats.items(), key=lambda item: int(item[1]["viewCount"]), reverse=True)
stats = []



for vid in sorted_vids:
	video_id = vid[0]
	title = vid[1]["title"]

	print(title)

	views = int(vid[1]["viewCount"])
	likes = int(vid[1]["likeCount"])
	dislikes = int(vid[1]["dislikeCount"])
	#comments = int(vid[1]["commentCount"])
	stats.append([title, views,likes,dislikes])

	
#df = pd.DataFrame(stats, columns=["title", "viewCount"])
#df["title"]=title[0::2]
#df["viewCount"]=views[1::2]
#df["likeCount"]=likes[2::2]
#df["dislikeCount"]=dislikes[3::2]
#df = pd.read_excel('/home/ubuntu/Documents/hornpipe/filename.xlsm', sheetname=1) # can also index sheet by name or fetch all sheets
#mylist = df['column name'].tolist()
#df.to_csv(r'result', header=None, index=None, sep=' ', mode='a')




workbook = xlsxwriter.Workbook('result.xlsx')
worksheet = workbook.add_worksheet("My sheet")


row = 0
col = 0

# Iterate over the data and write it out row by row.
for title, views,likes,dislikes in (stats):
	worksheet.write(row, col, title)
	worksheet.write(row, col + 1, views)
	worksheet.write(row, col + 2, likes)
	worksheet.write(row, col + 3, dislikes)
	row += 1

workbook.close()



