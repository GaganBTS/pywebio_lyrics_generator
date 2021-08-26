import argparse


import pywebio
from pywebio.input import input, FLOAT,TEXT
from pywebio.output import put_text,put_error,put_warning,put_loading,put_html
from scrape import Lyrics_Scraping
def lyrics():
    pywebio.session.set_env(title='LYRICS GENERATOR',output_animation=True)
    song = input('Enter the name of the song',type=TEXT)
    artist = input('Enter the artist name',type=TEXT)
    with put_loading('border','dark'):

     if song != '' or artist != '':
      song_lyric = Lyrics_Scraping(song,artist)
      full_lyrics = song_lyric.get_lyrics()
      if len(full_lyrics) != 0:
       
       put_html(f'<h2 style="text-align:center">{song.title()} by {artist.title()} Lyrics</h2>')
       for l in full_lyrics[3:]:
        put_html(f"<h3 style='text-align:center; color:#511281'>{l}\n</h3>")
      else:
         put_error('Please enter the details correctly. Cannot find the lyrics of entered song')
     else:
        put_error('Please do not leave any field empty')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p","--port",type=int,default=7700)
    args =parser.parse_args()
    pywebio.start_server(lyrics,port=args.port)
