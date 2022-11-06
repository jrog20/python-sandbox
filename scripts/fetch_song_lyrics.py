# Fetch Song lyrics
# pip install lyricsgenius
import lyricsgenius as Lyrics

lyrics = Lyrics.Genius("TOKEN")

# Search for a song (title, artist)
song = lyrics.search_song("I Like That", "Janelle Monáe")
print(song.lyrics)

# # search album (album, artist)
album = lyrics.search_album("Funhouse", "P!nk")
print(album)

artist = lyrics.search_artist("P!nk", max_songs=3, sort="title")
print(artist.songs)

# save lyrics to file
song.save_lyrics()