from pytube import YouTube
import os


arr = []
arr1=[]
output_path="D:\muzica\pytube download"
ur = input("Enter youtube video link:")
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
#print(steam)
#steam.first().download()
out_file = steam.first().download(output_path)
base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)
print(yt.title+" has been downloaded to " + output_path)