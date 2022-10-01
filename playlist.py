from asyncio.windows_events import NULL
from pytube import Playlist
from pytube import YouTube
import os
from subprocess import run


arr = []
arr1=[]
url = input("Enter playlist url: ")
yt1 = Playlist(url)
output_path=input("Enter the output path: ")
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
   
   out_file = steam.first().download(output_path)
   
   out_file_name = out_file[:-5]
   run([
     'ffmpeg',
     '-i','-b:a {}'.format(bitrate), os.path.join(output_path, out_file),'-b:a',(str(max(arr1))+"k"),
     os.path.join(output_path, out_file_name+".mp3")
    
       ])
   os.remove(out_file)
   print(yt.title+" has been downloaded to " + output_path)
