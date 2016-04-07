import sys
import json
import time
import requests

from BeautifulSoup import BeautifulSoup
from pymongo import MongoClient


client = MongoClient('localhost', 27017)
db = client.restaurants 
collection = db.restaurant_list
ta_url = "https://www.tripadvisor.com"
restaurant_links = []
# getting list of restaturants


def trip_advisor(loc_code):
    if loc_code == 'bang':
        code = 297628
    elif loc_code == 'sfo':
        code = 60713
    else:
        print "Area not in the list"
        return
    url = "https://www.tripadvisor.com/RestaurantSearch?Action=PAGE&geo="+str(code)+"&ajax=1&itags=10591&sortOrder=popularity&availSearchEnabled=false"
    html = requests.get(url)
    bs = BeautifulSoup(html.text)
    data = int(bs.find('div', {"class":"popIndexBlock"}).text.split(' ')[2].replace(',', ''))
    print data
    print "no of restaurants"
    for i in range(660, data, 30):
        if i == 0:
            offset = ''
        else:
            offset = '&o=a' + str(i)
        url = "https://www.tripadvisor.com/RestaurantSearch?Action=PAGE&geo="+str(code)+"&ajax=1&itags=10591&sortOrder=popularity&availSearchEnabled=false" + offset
        try:
            html = requests.get(url).text
        except:
            time.sleep(5)
            html = requests.get(url).text
        bs = BeautifulSoup(html)
        titles = bs.findAll('a', {"class": "property_title"})
        for restaurant in titles:
            title = restaurant.text
            link = ta_url + restaurant['href']
            print "+++++++++++++++++++++++++++++++++++++++" + title + "+++++++++++++++++++++++++++++++++++++++++++++++"
            # obj = {"title": restaurant.text, "link":restaurant['href']}
            try:
                html = requests.get(link).text
            except:
                time.sleep(5)
                html = requests.get(link).text
            bs = BeautifulSoup(html)
            try:
                lat_long = bs.find('div', {'class': 'mapContainer'})
                latitude = lat_long['data-lat']
                longitude = lat_long['data-lng']
            except:
                latitude = None
                longitude = None
            full_address = bs.find('span', {'class': 'format_address'}).text
            details = bs.find('div', {'class': 'table_section'}).findAll('div', {"class": "row"})
            try:
                image = bs.find('img',{'class':'flexibleImage'})['src']
            except:
                image = "https://s-media-cache-ak0.pinimg.com/736x/78/94/2d/78942d680831e783d9c7662badec5afe.jpg"
            timing = []
            for rows in details:
                try:
                    if rows.find('div', {'class': 'title'}).text == "Average prices":
                        avg_price = rows.find('div', {'class': 'content'}).text
                        print "AVERAGE PRICE"
                except:
                    pass
                try:
                    if rows.find('div', {'class': 'title'}).text == "Cuisine":
                        cuisine = rows.find('div', {'class': 'content'}).text.lower()
                        print "CUISINE"
                except:
                    pass
                try:
                    if rows.find('div', {'class': 'title'}).text == "Dining options":
                        tags = rows.find('div', {'class': 'content'}).text.lower()
                        print "DINING OPTIONS"
                except:
                    pass
                # try:

                # except:
                #     open_hours = None
            # my_time = bs.find('div', {'class': 'hours title'})
            # print my_time
            try:
                open_hours = bs.find('div', {"class": "hours content"}).findAll('div', {"class": "detail"})
                for days in open_hours:
                    if days.find('span',{"class":"day"}).text == "Sunday":
                        all_timings = days.findAll('div', {'class':'hoursRange'})
                        timings = [x.text for x in all_timings]
                        obj = {"sunday": timings}
                        timing.append(obj)
                        print obj
                    if days.find('span',{"class":"day"}).text == "Monday":
                        all_timings = days.findAll('div', {'class':'hoursRange'})
                        timings = [x.text for x in all_timings]
                        obj = {"monday": timings}
                        timing.append(obj)
                        print obj
                    if days.find('span',{"class":"day"}).text == "Tuesday":
                        all_timings = days.findAll('div', {'class':'hoursRange'})
                        timings = [x.text for x in all_timings]
                        obj = {"tuesday": timings}
                        timing.append(obj)
                        print obj
                    if days.find('span',{"class":"day"}).text == "Wednesday":
                        all_timings = days.findAll('div', {'class':'hoursRange'})
                        timings = [x.text for x in all_timings]
                        obj = {"wednesday": timings}
                        timing.append(obj)
                        print obj
                    if days.find('span',{"class":"day"}).text == "Thursday":
                        all_timings = days.findAll('div', {'class':'hoursRange'})
                        timings = [x.text for x in all_timings]
                        obj = {"thursday": timings}
                        timing.append(obj)
                        print obj
                    if days.find('span',{"class":"day"}).text == "Friday":
                        all_timings = days.findAll('div', {'class':'hoursRange'})
                        timings = [x.text for x in all_timings]
                        obj = {"friday": timings}
                        timing.append(obj)
                        print obj
                    if days.find('span',{"class":"day"}).text == "Saturday":
                        all_timings = days.findAll('div', {'class':'hoursRange'})
                        timings = [x.text for x in all_timings]
                        obj = {"saturday": timings}
                        timing.append(obj)
                        print obj
            except:
                pass
            restaurant_obj = {
                "name": title.lower(),
                "link": link,
                "latitude": latitude,
                "longitude": longitude,
                "full_address": full_address,
                "avg_price": avg_price,
                "cuisine": cuisine,
                "tags": tags,
                "open_hours": timing,
                "image":image,
                "source":"tripadvisor",
            }
            if collection.find_one({"name": restaurant_obj["name"], "latitude":restaurant_obj["latitude"],"longitude":restaurant_obj["longitude"]}):
                print "passed this data already was there!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
                pass
            else:
                collection.insert(restaurant_obj)



if __name__ == '__main__':
    trip_advisor(sys.argv[1])
