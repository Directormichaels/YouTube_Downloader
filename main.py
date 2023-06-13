from pytube import YouTube
from sys import argv


if len(argv) > 1:
    link = argv[1]
else:
    link = input("Enter your YouTube link ")


link_obj = YouTube(link)

print("Title: ", link_obj.title)
print("Views: ", link_obj.views)


y_download = link_obj.streams.filter(res="360p").first()

location = input("Add your download folder...")
location = location.replace("\\", "/")

y_download.download(location)
#C:\Users\Trust\Desktop\Segun\VSCodess\dd