from pytube import YouTube
import os
from subprocess import run


arr = []
arr1=[]
output_path=input("Enter the output path: ")
ur = input("Enter youtube video link: ")
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
    '-i', os.path.join(output_path, out_file),'-b:a',(str(max(arr1))+"k"),
    os.path.join(output_path, out_file_name+".mp3"),
    
])
os.remove(out_file)
print(yt.title+" has been downloaded to " + output_path)