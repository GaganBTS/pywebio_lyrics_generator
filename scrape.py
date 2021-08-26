driver_path = r"chromedriver.exe"
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
        self.driver = webdriver.Chrome(executable_path=driver_path,options=self.option)

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












