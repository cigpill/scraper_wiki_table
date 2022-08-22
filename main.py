from urllib.request import urlopen
from bs4 import BeautifulSoup

base_url = 'https://en.wikipedia.org/wiki/'


def wiki_scrape_table(rel_page):
    url = base_url + str(rel_page).replace(' ', '_')

    try:
        site = urlopen(url)
    except Exception as e:
        return str(url + ' ' + str(e))

    soup = BeautifulSoup(site, 'html.parser')

    try:
        table = soup.find_all(class_='infobox')[0]
    except IndexError:
        return 'Error: ' + url + 'contains no info table'

    info_html = table.find_all('tr')
    info_array = [['Name', rel_page]]

    for i in range(0, len(info_html)):
        info_label = info_html[i].find(class_='infobox-label')

        if not info_label == None:
            info_label = info_label.get_text()

            info = info_html[i].find(class_='infobox-data')

            if not info == None:
                info = info.get_text()
                info = info.replace('\xa0', ' ')
                info_array.append([info_label, info])

    return info_array


#name = input('Enter the name of the site you want to scrape: ')
#print(wiki_scrape_table(name))

#input('Press enter to close the program...')

