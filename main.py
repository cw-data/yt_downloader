from pytube import YouTube

# youtube video downloader based on https://www.youtube.com/watch?v=EMlM6QTzJo0&ab_channel=TiffInTech

def Download(link):
    try:
        youtubeObject = YouTube(link)
        youtubeObject = youtubeObject.streams.get_highest_resolution()
        youtubeObject.download(output_path="yt_downloader/20221226/")
    except:
        print("There has been an error in downloading your youtube video")
    print("This download has completed!")

link = input("Please put your youtube link here! URL: ")
Download(link)