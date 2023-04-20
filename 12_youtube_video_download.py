from pytube import YouTube

link="https://youtu.be/aSZ7IHCk2Jk"
youtube_1= YouTube(link)

print(youtube_1.title)
print(youtube_1.thumbnail_url)
videos = youtube_1.streams.all() # all format 

#videos = youtube_1.streams.filter(only_audio=True) #only audio 

vid= list(enumerate(videos))
for i in vid:
    print(i) 
strm= int(input("enter :  "))
videos[strm].download()    
print("sucessfully download")
