driver_path = r"C:\Users\gsing\PycharmProjects\chromedriver.exe"
import selenium
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver


class Lyrics_Scraping:
    def __init__(self,song,artist):

        self.lyric=[]
        self.url = 'https://www.google.com'
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.driver.get(self.url)
        self.search = self.driver.find_element_by_class_name('gLFyf')
        self.search.click()
        self.search.send_keys(f'{song} {artist} lyrics')
        self.search.send_keys(Keys.ENTER)

        self.lyrics = self.driver.find_elements_by_css_selector(("span[jsname='YS01Ge']"))

        for l in self.lyrics:
            self.lyric.append(l.text)
        self.driver.quit()

    def get_lyrics(self):

      return self.lyric












