from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd



def scrape():

    url = "https://redplanetscience.com/"

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    browser.visit(url)

    html = browser.html
    soup = bs(html, 'html.parser')

    results = soup.find_all('div', class_="col-md-8")
    for result in results:
        
        news_title = result.find('div', class_='content_title').text
        
        news_p = result.find('div', class_='article_teaser_body').text

        post = {
            'title': news_title,
            'paragraph': news_p,
        }

    featured_image_url = 'https://spaceimages-mars.com/image/featured/mars1.jpg'

    url_2 = 'https://galaxyfacts-mars.com/'

    table = pd.read_html(url_2)
    df = table[0]
    df = df.rename(columns={'0': '', 'Mars': 'Earth'})
    df.columns = df.iloc[0]
    df = df[1:]
    df = df.set_index('Mars - Earth Comparison')

    df.to_html('table.html')

    dict_1 = {'title': 'Cerberus Hemisphere', 'img_url': 'https://marshemispheres.com/images/full.jpg'} 
    dict_2 = {'title': 'Schiaparelli Hemisphere', 'img_url': 'https://marshemispheres.com/images/schiaparelli_enhanced-full.jpg'}
    dict_3 = {'title': 'Syrtis Major Hemisphere', 'img_url': 'https://marshemispheres.com/images/syrtis_major_enhanced-full.jpg'}
    dict_4 = {'title': 'Valles Marineris Hemisphere', 'img_url': 'https://marshemispheres.com/images/valles_marineris_enhanced-full.jpg'}

    hemisphere_image_urls = [dict_1, dict_2, dict_3, dict_4]

    final_dict = {'news': post,
                'image': featured_image_url,
                'hemispheres': hemisphere_image_urls}

    browser.quit()

    return final_dict