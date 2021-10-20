from nested_beta import albums
SONGS_LIST_INDEX = 3
SONG_TITLE_INDEX = 1
while True:
   print("please choose your album(invalid choice exits):")
   for index, (title, artist, year, songs) in enumerate(albums):
       print("{}: {}".format(index + 1, title))
   choice = int(input())
   if 1 <= choice <= len(albums):
       songs_list = albums[choice - 1][SONGS_LIST_INDEX]
       print(songs_list)
   else:
       break
   print("please choose your song: ")
   for index, (track_number, song) in enumerate(songs_list):
       print("{}: {} ".format(index + 1, song))

   song_choice = int(input())
   if 1 <= song_choice <= len(songs_list):
       title = songs_list[song_choice - 1][SONG_TITLE_INDEX]
   else:
       continue
   print("playing {}".format(title))
   print("=" * 40)


print("edit")