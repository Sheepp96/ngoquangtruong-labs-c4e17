from youtube_dl import YoutubeDL

# dl  = YoutubeDL()
# dl.download(['https://www.youtube.com/watch?v=2dMOgvytko4'])

# dl = YoutubeDL()
# dl.download(['https://www.youtube.com/watch?v=hY33HnVKFGo','https://www.youtube.com/watch?v=UCXao7aTDQM'])

# options = {
#     'format': 'bestaudio/audio'
# }
# dl = YoutubeDL(options)
# dl.download(['https://www.youtube.com/watch?v=KWS4lkthUts'])

# options = {
#     'default_search': 'ytsearch', # tell downloader to search instead of directly downloading
#     'max_downloads' : 1 # tell downloader to download only the first entry
#
# }
# dl = YoutubeDL(options)
# dl.download(['Tái ngộ - Blacka'])

options = {
    'default_search' : 'ytsearch',
    'max_downloads'  : 1,
    'format'         : 'bestaudio/audio'
}
dl = YoutubeDL(options)
dl.download(['Sử kí tư mã thiên audio'])
