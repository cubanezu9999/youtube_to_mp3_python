from asyncio.windows_events import NULL
from pytube import Playlist
from pytube import YouTube
import os


arr = []
arr1=[]
url = input("Enter playlist url: ")
yt1 = Playlist(url)
output_path="D:\muzica\pytube download"
print('Number of videos in playlist: %s' % len(yt1.video_urls))
for ur in yt1:
   #print(ur)
   yt= YouTube(ur)
   t=yt.streams.filter(only_audio=True)
   for s in t:
   #print(s.abr)
      arr.append(s.abr)
      for i in arr:
     
        bitrate = int ( ''.join(filter(str.isdigit, i) ) )
        #print(bitrate)
        arr1.append(bitrate)
   steam = yt.streams.filter(only_audio = True,abr = str(max(arr1))+"kbps")
   #https://www.youtube.com/playlist?list=PLCD2cdBTyJroUbao24kvr1QIJQOYmh66_&jct=H2AegSLKn1cwztjOfYk3K2A6_J9HRgprint(steam)
   #steam.first().download()
   out_file = steam.first().download(output_path)
   base, ext = os.path.splitext(out_file)
   new_file = base + '.mp3'
   os.rename(out_file, new_file)
   print(yt.title+" has been downloaded to " + output_path)
