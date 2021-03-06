import time
from bs4 import BeautifulSoup
import requests
import re
import csv

def get_device_manufacturers(device_names):
    list_of_manufacturers_without_tags = []
    for i in device_names:
        i = str(i)
        i = i.replace('<div class="cell device-name">\n','')
        i = i.lstrip()
        i = i.split('<')[0]
        i = i.rstrip()
        list_of_manufacturers_without_tags.append(i)
    return list_of_manufacturers_without_tags

def get_device_models(device_names, soup):
    list_of_models_without_tags = []
    list_of_models = soup.findAll("span", {"class": "selected"})
    for i in list_of_models:
        i = str(i)
        i = i.replace('<span class="selected">','').replace('</span>','')
        list_of_models_without_tags.append(i)
    return list_of_models_without_tags

def format_device_scores(device_scores, soup):
    list_of_scores_without_tag = []
    list_of_scores = soup.findAll("h3")
    for i in list_of_scores:
        i = str(i)
        i = i.replace('<h3>','').replace('</h3>','')
        list_of_scores_without_tag.append(i)
    return list_of_scores_without_tag

def data_from_each(list_of_manufacturers_without_tags, list_of_models_without_tags, list_of_scores_without_tag):
    j = 0
    for i in list_of_manufacturers_without_tags:
        print(list_of_manufacturers_without_tags[j], list_of_models_without_tags[j], list_of_scores_without_tag[j])
        j = j + 1

def insert_into_csv(list_of_manufacturers_without_tags, list_of_models_without_tags, list_of_scores_without_tag, file_name):
    j = 0
    for i in list_of_manufacturers_without_tags:
        with open(file_name, 'a', newline='') as file:
            writer = csv.writer(file)
            print(list_of_manufacturers_without_tags[j], list_of_models_without_tags[j], list_of_scores_without_tag[j])
            writer.writerow([list_of_manufacturers_without_tags[j], list_of_models_without_tags[j], list_of_scores_without_tag[j]])
        j = j + 1

def scrape(link, file_name):
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Manufacturer", "Model", "Score"])
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')
    device_names = soup.findAll("div", {"class": "cell device-name"})
    device_scores = soup.findAll("div", {"class": "cell device-score"})
    list_of_manufacturers_without_tags = get_device_manufacturers(device_names)
    list_of_models_without_tags = get_device_models(device_names, soup)
    list_of_scores_without_tag = format_device_scores(device_scores, soup)
    insert_into_csv(list_of_manufacturers_without_tags, list_of_models_without_tags, list_of_scores_without_tag, file_name)


def main():
    scrape("https://www.ifixit.com/smartphone-repairability", "smartphone.csv")
    scrape("https://www.ifixit.com/laptop-repairability", "laptop.csv")
    scrape("https://www.ifixit.com/tablet-repairability", "tablet.csv")

if __name__ == '__main__':
    main()
