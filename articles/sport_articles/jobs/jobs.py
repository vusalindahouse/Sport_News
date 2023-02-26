from urllib.request import urlopen
from bs4 import BeautifulSoup
from sport_articles.models import Articles

def schedule_api():
    html = urlopen('https://www.sports.ru')
    soup = BeautifulSoup(html, 'html.parser')
    posts = soup.find_all('article',
                          class_='js-active js-material-list__blogpost material-list__item clearfix piwikTrackContent')
    for post in posts:
        title = post.find('a', class_='h2').text
        url = ''.join(post.find('a').get('href'))
        time = ''.join(post.find('time').get('datetime'))[11:16]
        img = ''.join(post.find('img').get('data-src'))

        Articles.objects.create(
            title=title,
            url=url,
            published_time=time,
            img=img
        )

    html = urlopen('https://sportrbc.ru/money/')
    soup = BeautifulSoup(html, 'html.parser')
    posts = soup.find_all('div', class_='item item_image-mob js-category-item')
    for post in posts:
        url = ''.join(post.find('a', class_='item__link').get('href'))
        title = post.find('span', class_="item__title rm-cm-item-text").text
        img = ''.join(post.find('img').get('src'))
        time = post.find('span', class_="item__category").text[8:13]

        Articles.objects.create(
            title=title,
            url=url,
            published_time=time,
            img=img
        )

    html = urlopen('https://www.sport-express.ru/reviews/')
    soup = BeautifulSoup(html, 'html.parser')
    posts = soup.find_all('div', class_='se-press-list-page__item')
    for post in posts:
        url = post.find('a').get('href')
        title = post.find('div',
                          class_='se-material__title se-material__title--size-middle se-material__title--bold se-material-list-page__material se-press-list-page__item-material-title').text
        img = post.find('img').get('src')
        time = post.find('span', class_='se-material-preview-info__datetime').text

        Articles.objects.create(
            title=title,
            url=url,
            published_time=time,
            img=img
        )

    html = urlopen('https://www.sports.ru/football/')
    soup = BeautifulSoup(html, 'html.parser')
    posts = soup.find_all('article',
                          class_='js-active js-material-list__blogpost material-list__item clearfix piwikTrackContent')

    for post in posts:
        title = post.find('a', class_='h2').text
        url = post.find('a').get('href')
        time = ''.join(post.find('time').get('datetime'))[10:16]
        img = post.find('img').get('data-src')

        Articles.objects.create(
            title=title,
            url=url,
            published_time=time,
            img=img
        )

    html = urlopen('https://russian.rt.com/trend/334889-futbol')
    soup = BeautifulSoup(html, 'html.parser')
    posts = soup.find_all('li', class_='listing__column listing__column_all-new listing__column_js')
    for post in posts:
        url = 'https://russian.rt.com' + post.find('a').get('href')
        title = post.find('a',
                          class_='link link_color').text

        img = post.find('img').get('src')
        time = ''.join(post.find('time', class_='date').text)[19:25]

        Articles.objects.create(
            title=title,
            url=url,
            published_time=time,
            img=img
        )

    html = urlopen('https://sportrbc.ru/football/')
    soup = BeautifulSoup(html, 'html.parser')
    posts = soup.find_all('div', class_='item item_image-mob js-category-item')

    for post in posts:
        url = post.find('a', class_='item__link').get('href')
        title = post.find('span',
                          class_='item__title rm-cm-item-text').text
        img = post.find('img', class_='smart-image__img').get('src')
        time = post.find('span', class_="item__category").text

        Articles.objects.create(
            title=title,
            url=url,
            published_time=time,
            img=img
        )