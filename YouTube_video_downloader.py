#The try block lets you test a block of code for errors. The except block lets you handle the error.
try:
    #import library
    from pytube import YouTube
    from pytube import Playlist
except Exception as e:
    #print Error 
    print("There is a problem")
#take a url of Youtube
user_url=input('please,Enter url :')
url=user_url
#download first stream 
ytd=YouTube(url).streams.first().download()