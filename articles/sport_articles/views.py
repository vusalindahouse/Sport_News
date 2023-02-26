from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import ListView
from bs4 import BeautifulSoup
import requests
from .links import *
from .lists import *
from .models import Articles


# лимит парсинга постов
stop_scrap = 12



"""Парсинг постов, которые выводятся на основной странице (main.html)"""
class MainPage(ListView):

    def get_sports(self):

        r = requests.get(sports).text
        soup = BeautifulSoup(r, 'lxml')
        posts = soup.find_all('article', class_= 'js-active js-material-list__blogpost material-list__item clearfix piwikTrackContent')
        for post in posts:
            title = post.find('a', class_='h2').text
            url = post.find('a').get('href')
            time = ''.join(post.find('time').get('datetime'))[11:16]
            img = post.find('img').get('data-src')



            data ={ 'title': title,
                     'url': url,
                     'img': img,
                     'time': time,
                    }
            while len(sport_list) == stop_scrap:
                break
            else:
                sport_list.append(data)
        return sport_list



    def get_express(self):
        r = requests.get(express).text
        soup = BeautifulSoup(r, 'lxml')
        posts = soup.find_all('div', class_='se-press-list-page__item')

        for post in posts:
            url = post.find('a').get('href')
            title = post.find('div', class_ = 'se-material__title se-material__title--size-middle se-material__title--bold se-material-list-page__material se-press-list-page__item-material-title').text
            img = post.find('img').get('src')
            time = post.find('span', class_ = 'se-material-preview-info__datetime').text.split(" ")[-1]


            data ={ 'title': title,
                    'url': url,
                    'img': img,
                    'time': time

            }

            while len(express_list) == stop_scrap:
                break
            else:
                express_list.append(data)
        return express_list



    def sportsTop(self):
        r = requests.get(sports).text
        soup = BeautifulSoup(r, 'lxml')
        post = soup.find('article', class_='super-top__article analyticsTrackView')
        link = post.find('a', class_='super-top__link link link_color_white analyticsTrackClick').get('href')
        title = post.find('h1', class_='super-top__title').text
        img = post.find('img').get('src')

        data = {'title': title,
                'link': link,
                'img': img
                }
        top_sport.append(data)
        return top_sport


    def xpressTop(self):
        r = requests.get(express2).text
        soup = BeautifulSoup(r, 'lxml')
        post = soup.find('div', class_='se-materials-grid-mosaic')
        link = ''.join(post.find('a').get('href'))
        title = post.find('div', class_='se-material__title se-material__title--size-middle').text
        img = post.find('img').get('src')

        data = {'title': title,
                'link': link,
                'img': img
                }
        top_xpress.append(data)
        return top_xpress



    def get_rg(self):
        r = requests.get(rbc2).text
        soup = BeautifulSoup(r, 'lxml')
        posts = soup.find_all('div', class_ ='item js-rm-central-column-item')
        for post in posts:
            url =''.join(post.find('a', class_='item__link rm-cm-item-link js-rm-central-column-item-link ').get('href'))
            title = post.find('span', class_="item__title rm-cm-item-text js-rm-central-column-item-text").text
            img = ''.join(post.find('img').get('src'))
            time = post.find('span', class_="item__category").text.split(",")[-1]


            data = {'title': title,
                        'url': url,
                        'img': img,
                        'time': time
                        }

            while len(rbc_list) == stop_scrap:
                    break
            else:
                    rbc_list.append(data)
        return rbc_list

    def get_ria(self):
            r = requests.get(express_tennis).text
            soup = BeautifulSoup(r, 'lxml')
            posts = soup.find_all('div', class_='list-item')

            for post in posts:
                url =  post.find('a', class_='list-item__image').get('href')
                title = post.find('a',
                                  class_='list-item__title color-font-hover-only').text
                img = post.find('img').get('src')
                time = post.find('div', class_='list-item__date').text.split(",")[-1]
                data = {'title': title,
                        'url': url,
                        'img': img,
                        'time': time
                        }

                while len(tennis_list3) == stop_scrap:
                    break
                else:
                    tennis_list3.append(data)
            return tennis_list3

    def get_rtFottbal(self):
        r = requests.get(xpress_football).text
        soup = BeautifulSoup(r, 'lxml')
        posts = soup.find_all('li', class_='listing__column listing__column_all-new listing__column_js')

        for post in posts:
            url = 'https://russian.rt.com' + post.find('a').get('href')
            title = post.find('a',
                              class_='link link_color').text

            img = post.find('img').get('src')
            time = ''.join(post.find('time', class_='date').text)[19:25]

            data = {'title': title,
                    'url': url,
                    'img': img,
                    'time': time
                    }

            while len(football_list2) == stop_scrap:
                break
            else:
                football_list2.append(data)
        return football_list2








    def get(self, request, *args, **kwargs):
        context = {
            'sport_list': self.get_sports(),
            'express_list': self.get_express(),
            'rbc_list': self.get_rg(),
            'tennis_list3': self.get_ria(),
            'football_list2': self.get_rtFottbal(),
            'top_sport': self.sportsTop(),
            'top_xpress': self.xpressTop(),

        }
        return render(request, 'sport_articles/main.html', context)


class FootballPage(ListView):
        def get_sport(self):
            r = requests.get(sport_football).text
            soup = BeautifulSoup(r, 'lxml')
            posts = soup.find_all('article',
                                  class_='js-active js-material-list__blogpost material-list__item clearfix piwikTrackContent')


            for post in posts:
                title = post.find('a', class_='h2').text
                url = post.find('a').get('href')
                time = ''.join(post.find('time').get('datetime'))[10:16]
                img = post.find('img').get('data-src')

                data = {'title': title,
                        'url': url,
                        'img': img,
                        'time': time,
                        }
                while len(football_list) == stop_scrap:
                    break
                else:
                    football_list.append(data)
            return football_list



        def get_express(self):
            r = requests.get(xpress_football).text
            soup = BeautifulSoup(r, 'lxml')
            posts = soup.find_all('li', class_='listing__column listing__column_all-new listing__column_js')


            for post in posts:
                url = 'https://russian.rt.com' + post.find('a').get('href')
                title = post.find('a',
                                   class_='link link_color').text

                img = post.find('img').get('src')
                time = ''.join(post.find('time', class_='date').text)[19:25]




                data = {'title': title,
                        'url': url,
                        'img': img,
                        'time': time
                        }

                while len(football_list2) == stop_scrap:
                    break
                else:
                    football_list2.append(data)
            return football_list2

        def get_rt(self):
            r = requests.get(rt_football).text
            soup = BeautifulSoup(r, 'lxml')
            posts = soup.find_all('div', class_='list-item')

            for post in posts:
                url = post.find('a').get('href')
                title = post.find('a',
                                  class_='list-item__title color-font-hover-only').text
                img = post.find('img').get('src')
                time = post.find('div', class_="list-item__date").text.split(" ")[-1]


                data = {'title': title,
                        'url': url,
                        'img': img,
                        'time': time
                        }

                while len(football_list3) == stop_scrap:
                    break
                else:
                    football_list3.append(data)
            return football_list3

        def get(self, request, *args, **kwargs):
            context = {
                'football_list': self.get_sport(),
                'football_list2': self.get_express(),
                'football_list3': self.get_rt(),

            }
            return render(request, 'sport_articles/football.html', context)


class HockeyPage(ListView):
    def get_sport(self):
            r = requests.get(sport_hokkey).text
            soup = BeautifulSoup(r, 'lxml')
            posts = soup.find_all('article',
                                  class_='js-active js-material-list__blogpost material-list__item clearfix piwikTrackContent')
            for post in posts:
                title = post.find('a', class_='h2').text
                url = post.find('a').get('href')
                time = ''.join(post.find('time').get('datetime'))[10:16]
                img = post.find('img').get('data-src')


                data = {'title': title,
                        'url': url,
                        'img': img,
                        'time': time,
                        }
                while len(hockey_list) == stop_scrap:
                    break
                else:
                    hockey_list.append(data)
            return hockey_list

    def get_express(self):
                r = requests.get(xpress_hockey).text
                soup = BeautifulSoup(r, 'lxml')
                posts = soup.find_all('li', class_='listing__column listing__column_all-new listing__column_js')

                for post in posts:
                    url = 'https://russian.rt.com' + post.find('a').get('href')
                    title = post.find('a',
                                       class_='link link_color').text

                    img = post.find('img').get('src')
                    time = ''.join(post.find('time', class_='date').text)[19:25]

                    data = {'title': title,
                            'url': url,
                            'img': img,
                            'time': time
                            }

                    while len(hockey_list2) == stop_scrap:
                        break
                    else:
                        hockey_list2.append(data)
                return hockey_list2

    def get_rt(self):
            r = requests.get(rt_hockey).text
            soup = BeautifulSoup(r, 'lxml')
            posts = soup.find_all('div', class_='list-item')

            for post in posts:
                url = post.find('a').get('href')
                title = post.find('a',
                                  class_='list-item__title color-font-hover-only').text
                img = post.find('img').get('src')
                time = post.find('div', class_="list-item__date").text.split(" ")[-1]

                data = {'title': title,
                        'url': url,
                        'img': img,
                        'time': time
                        }

                while len(hockey_list3) == stop_scrap:
                    break
                else:
                    hockey_list3.append(data)
            return hockey_list3

    def get(self, request, *args, **kwargs):
        context = {
            'hockey_list': self.get_sport(),
            'hockey_list2': self.get_express(),
            'hockey_list3': self.get_rt(),

        }
        return render(request, 'sport_articles/hockey.html', context)

class TennisPage(ListView):
    def get_sport(self):
            r = requests.get(sport_tennis).text
            soup = BeautifulSoup(r, 'lxml')
            posts = soup.find_all('article',
                                  class_='js-active js-material-list__blogpost material-list__item clearfix piwikTrackContent')

            for post in posts:
                title = post.find('a', class_='h2').text
                url = post.find('a').get('href')
                time = ''.join(post.find('time').get('datetime'))[10:16]
                img = post.find('img').get('data-src')


                data = {'title': title,
                        'url': url,
                        'img': img,
                        'time': time,
                        }
                while len(tennis_list) == stop_scrap:
                    break
                else:
                    tennis_list.append(data)
            return tennis_list

    def get_express(self):
                r = requests.get(rt_tennis).text
                soup = BeautifulSoup(r, 'lxml')
                posts = soup.find_all('li', class_='listing__column listing__column_all-new listing__column_js')

                for post in posts:
                    url = 'https://russian.rt.com' + post.find('a').get('href')
                    title = post.find('a',
                                       class_='link link_color').text

                    img = post.find('img').get('src')
                    time = ''.join(post.find('time', class_='date').text).split(",")[-1]

                    data = {'title': title,
                            'url': url,
                            'img': img,
                            'time': time
                            }

                    while len(tennis_list2) == stop_scrap:
                        break
                    else:
                        tennis_list2.append(data)
                return tennis_list2


    def get_rt(self):
            r = requests.get(express_tennis).text
            soup = BeautifulSoup(r, 'lxml')
            posts = soup.find_all('div', class_='list-item')

            for post in posts:
                url =  post.find('a', class_='list-item__image').get('href')
                title = post.find('a',
                                  class_='list-item__title color-font-hover-only').text
                img = post.find('img').get('src')
                time = post.find('div', class_='list-item__date').text.split(",")[-1]
                data = {'title': title,
                        'url': url,
                        'img': img,
                        'time': time
                        }

                while len(tennis_list3) == stop_scrap:
                    break
                else:
                    tennis_list3.append(data)
            return tennis_list3

    def get(self, request, *args, **kwargs):
        return render(request, 'sport_articles/tennis.html', {
            'tennis_list': self.get_sport(),
            'tennis_list2': self.get_express(),
            'tennis_list3': self.get_rt(),
        })

class BoxPage(ListView):
        def get_sport(self):
            r = requests.get(sport_box).text
            soup = BeautifulSoup(r, 'lxml')
            posts = soup.find_all('article',
                                  class_='js-active js-material-list__blogpost material-list__item clearfix piwikTrackContent')
            for post in posts:
                title = post.find('a', class_='h2').text
                url = post.find('a').get('href')
                time = ''.join(post.find('time').get('datetime'))[10:16]
                img = post.find('img').get('data-src')

                data = {'title': title,
                        'url': url,
                        'img': img,
                        'time': time,
                        }
                while len(box_list) == stop_scrap:
                    break
                else:
                    box_list.append(data)
            return box_list

        def get_express(self):
            r = requests.get(rt_box).text
            soup = BeautifulSoup(r, 'lxml')
            posts = soup.find_all('li', class_='listing__column listing__column_all-new listing__column_js')

            for post in posts:
                url = 'https://russian.rt.com' + post.find('a').get('href')
                title = post.find('a',
                                   class_='link link_color').text

                img = post.find('img').get('src')
                time = ''.join(post.find('time', class_='date').text)[19:25]

                data = {'title': title,
                        'url': url,
                        'img': img,
                        'time': time
                        }

                while len(box_list2) == stop_scrap:
                    break
                else:
                     box_list2.append(data)
            return box_list2

        def get_rt(self):
            r = requests.get(express_box).text
            soup = BeautifulSoup(r, 'lxml')
            posts = soup.find_all('div', class_='list-item')

            for post in posts:
                url = post.find('a').get('href')
                title = post.find('a',
                                  class_='list-item__title color-font-hover-only').text
                img = post.find('img').get('src')
                time = post.find('div', class_="list-item__date").text.split(" ")[-1]

                data = {'title': title,
                        'url': url,
                        'img': img,
                        'time': time
                        }

                while len(box_list3) == stop_scrap:
                    break
                else:
                    box_list3.append(data)
            return box_list3

        def get(self, request, *args, **kwargs):
            context = {
                'box_list': self.get_sport(),
                'box_list2': self.get_express(),
                'box_list3': self.get_rt(),

            }
            return render(request, 'sport_articles/box.html', context)


class BiatlonPage(ListView):
    def get_sport(self):
        r = requests.get(sport_biatlon).text
        soup = BeautifulSoup(r, 'lxml')
        posts = soup.find_all('article',
                              class_='js-active js-material-list__blogpost material-list__item clearfix piwikTrackContent')
        for post in posts:
            title = post.find('a', class_='h2').text
            url = post.find('a').get('href')
            time = ''.join(post.find('time').get('datetime'))[10:16]
            img = post.find('img').get('data-src')

            data = {'title': title,
                    'url': url,
                    'img': img,
                    'time': time,
                    }
            while len(biatlone_list) == stop_scrap:
                break
            else:
                biatlone_list.append(data)
        return  biatlone_list

    def get_express(self):
        r = requests.get(rt_biatlon).text
        soup = BeautifulSoup(r, 'lxml')
        posts = soup.find_all('li', class_='listing__column listing__column_all-new listing__column_js')

        for post in posts:
            url = 'https://russian.rt.com' + post.find('a').get('href')
            title = post.find('a',
                               class_='link link_color').text

            img = post.find('img').get('src')
            time = ''.join(post.find('time', class_='date').text)[19:25]

            data = {'title': title,
                    'url': url,
                    'img': img,
                    'time': time
                    }

            while len(biatlone_list2) == stop_scrap:
                break
            else:
                biatlone_list2.append(data)
        return biatlone_list2

    def get_rt(self):
        r = requests.get(express_biatlon).text
        soup = BeautifulSoup(r, 'lxml')
        posts = soup.find_all('div', class_='list-item')

        for post in posts:
            url = post.find('a').get('href')
            title = post.find('a',
                              class_='list-item__title color-font-hover-only').text
            img = post.find('img').get('src')
            time = post.find('div', class_="list-item__date").text.split(" ")[-1]
            data = {'title': title,
                    'url': url,
                    'img': img,
                    'time': time
                    }

            while len(biatlone_list3) == stop_scrap:
                break
            else:
                biatlone_list3.append(data)
        return biatlone_list3

    def get(self, request, *args, **kwargs):
        context = {
            'biatlone_list': self.get_sport(),
            'biatlone_list2': self.get_express(),
            'biatlone_list3': self.get_rt(),

        }
        return render(request, 'sport_articles/biatlone.html', context)


class BasketbolPage(ListView):
    def get_sport(self):
        r = requests.get(sport_basketbol).text
        soup = BeautifulSoup(r, 'lxml')
        posts = soup.find_all('article',
                              class_='js-active js-material-list__blogpost material-list__item clearfix piwikTrackContent')
        for post in posts:
            title = post.find('a', class_='h2').text
            url = post.find('a').get('href')
            time = ''.join(post.find('time').get('datetime'))[10:16]
            img = post.find('img').get('data-src')

            data = {'title': title,
                    'url': url,
                    'img': img,
                    'time': time,
                    }
            while len(basketbol_list) == stop_scrap:
                break
            else:
                basketbol_list.append(data)
        return  basketbol_list

    def get_ria(self):
            r = requests.get(ria_basketbol).text
            soup = BeautifulSoup(r, 'lxml')
            posts = soup.find_all('div', class_='list-item')

            for post in posts:
                url =  post.find('a', class_='list-item__image').get('href')
                title = post.find('a',
                                  class_='list-item__title color-font-hover-only').text
                img = post.find('img').get('src')
                time = post.find('div', class_='list-item__date').text.split(",")[-1]
                data = {'title': title,
                        'url': url,
                        'img': img,
                        'time': time
                        }

                while len(basketbol_list2) == stop_scrap:
                    break
                else:
                    basketbol_list2.append(data)
            return basketbol_list2



    def get(self, request, *args, **kwargs):
            context = {
                'basketbol_list': self.get_sport(),
                'basketbol_list2': self.get_ria()

            }
            return render(request, 'sport_articles/basketbol.html', context)


class AutoPage(ListView):
    def get_sport(self):
        r = requests.get(sport_auto).text
        soup = BeautifulSoup(r, 'lxml')
        posts = soup.find_all('article',
                              class_='js-active js-material-list__blogpost material-list__item clearfix piwikTrackContent')
        for post in posts:
            title = post.find('a', class_='h2').text
            url = post.find('a').get('href')
            time = ''.join(post.find('time').get('datetime'))[10:16]
            img = post.find('img').get('data-src')

            data = {'title': title,
                    'url': url,
                    'img': img,
                    'time': time,
                    }
            while len(auto_list) == stop_scrap:
                break
            else:
                auto_list.append(data)
        return  auto_list

    def get_ria(self):
            r = requests.get(ria_auto).text
            soup = BeautifulSoup(r, 'lxml')
            posts = soup.find_all('div', class_='list-item')

            for post in posts:
                url =  post.find('a', class_='list-item__image').get('href')
                title = post.find('a',
                                  class_='list-item__title color-font-hover-only').text
                img = post.find('img').get('src')
                time = post.find('div', class_='list-item__date').text.split(",")[-1]
                data = {'title': title,
                        'url': url,
                        'img': img,
                        'time': time
                        }

                while len(auto_list2) == stop_scrap:
                    break
                else:
                    auto_list2.append(data)
            return auto_list2



    def get(self, request, *args, **kwargs):
            context = {
                'auto_list': self.get_sport(),
                'auto_list2': self.get_ria()

            }
            return render(request, 'sport_articles/auto.html', context)




class VolleybalPage(ListView):
    def get_rt(self):
        r = requests.get(rt_volleyball).text
        soup = BeautifulSoup(r, 'lxml')
        posts = soup.find_all('li', class_='listing__column listing__column_all-new listing__column_js')

        for post in posts:
            url = 'https://russian.rt.com' + post.find('a').get('href')
            title = post.find('a',
                              class_='link link_color').text

           # img = post.find('img', class_='cover__image cover__image_ratio').get('src') + '.jpeg'
            time = ''.join(post.find('time', class_='date').text)[19:25]

            data = {'title': title,
                    'url': url,
            #        'img': img,
                    'time': time
                    }
            while len(volleyball_list) == stop_scrap:
                break
            else:
                volleyball_list.append(data)
        return  volleyball_list


    def get_ria(self):
            r = requests.get(ria_volleyball).text
            soup = BeautifulSoup(r, 'lxml')
            posts = soup.find_all('div', class_='list-item')

            for post in posts:
                url =  post.find('a', class_='list-item__image').get('href')
                title = post.find('a',
                                  class_='list-item__title color-font-hover-only').text
                img = post.find('img').get('src')
                time = post.find('div', class_='list-item__date').text.split(",")[-1]
                data = {'title': title,
                        'url': url,
                        'img': img,
                        'time': time
                        }

                while len(volleyball_list2) == stop_scrap:
                    break
                else:
                    volleyball_list2.append(data)
            return volleyball_list2



    def get(self, request, *args, **kwargs):
            context = {
                'volleyball_list': self.get_rt(),
                'volleyball_list2': self.get_ria()
            }
            return render(request, 'sport_articles/volleyball.html', context)





"""Функция поиска по сайту"""
@login_required
def searchBar(request):
    if request.method == "POST":
        searched = request.POST['searched']
        posts = Articles.objects.filter(title__icontains=searched)
        return render(request,
                      'sport_articles/searchbar.html',
                      {'searched': searched, 'posts': posts})

    else:
        return render(request, 'sport_articles/searchbar.html', {} )





"""Функция регистрации на сайте"""
def registerPage(request):
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Аккаунт успешно зарегестрирован')
                return redirect('login')

        context = {'form': form}
        return render(request, 'sport_articles/register.html', context)


"""Логин на сайте"""
def loginPage(request):
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('base')
            else:
                messages.info(request, 'Имя или пароль неверны')

        context = {}
        return render(request, 'sport_articles/login.html', context)


"""Разлогин"""
def log_out(request):
        logout(request)
        return redirect('login')







