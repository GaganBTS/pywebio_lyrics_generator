
desired_cap = {
 'os_version': '10',
 'resolution': '1920x1080',
 'browser': 'Chrome',
 'browser_version': 'latest',
 'os': 'Windows',
 'name': 'BStack-[Python] Sample Test', # test name
 'build': 'BStack Build Number 1' # CI/CD job or build name
}
import argparse
import pywebio
from pywebio.input import input, FLOAT,TEXT
from pywebio.output import put_text,put_error,put_warning,put_loading,put_html
import selenium
from selenium import webdriver   # for webdriver
from selenium.webdriver.support.ui import WebDriverWait  # for implicit and explict waits
from selenium.webdriver.chrome.options import Options  # for suppressing the browser
from selenium.webdriver.common.keys import Keys



class Lyrics_Scraping:
    def __init__(self,song,artist):

        self.lyric=[]
        self.url = 'https://www.google.com'
        self.option = Options()
        self.option.add_argument('--headless')
        self.driver = webdriver.Remote(command_executor='https://name:key@hub-cloud.browserstack.com/wd/hub',
                                       desired_capabilities=desired_cap)

        self.driver.get(self.url)
        self.search = self.driver.find_element_by_class_name('gLFyf')
        self.search.click()
        self.search.send_keys(f'{artist} {song} lyrics')
        self.search.send_keys(Keys.ENTER)

        self.lyrics = self.driver.find_elements_by_css_selector(("span[jsname='YS01Ge']"))

        for l in self.lyrics:
            self.lyric.append(l.text)
        self.driver.quit()

    def get_lyrics(self):

      return self.lyric




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

