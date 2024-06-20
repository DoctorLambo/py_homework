import requests
from bs4 import BeautifulSoup
import json
import re
from fake_headers import Headers
from re import findall

def get_soup(url,headers):
    response = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")
    return soup

def get_headers(os='win', browser='chrome'):
    return Headers(os, browser).generate()

def keywords_find (text):
    pattern_raw = '((flask)(.*?)(django))|((django)(.*?)(flask))'
    for descritpion in text:
        row = findall(pattern_raw, descritpion.text.lower())
        if len(row)> 0:
           return True

    return False 

def add_info_in_result(vacancy_soup, result):
    tag_vacancy_title = vacancy_soup.find('div', class_='bloko-columns-row')
    tag_company_info = vacancy_soup.find('div', attrs={"data-qa": "vacancy-company"})
    tag_company_name = tag_company_info.find('a', attrs={"data-qa": "vacancy-company-name"})
    company_name = tag_company_name.text
    
    tag_city = tag_company_info.find('p', attrs={"data-qa": "vacancy-view-location"})
    if tag_city == None:
        tag_city = tag_company_info.find('span', attrs={"data-qa": "vacancy-view-raw-address"})
 
    city = tag_city.text
    salary ='Уровень дохода не указан'       
    tag_salary = tag_vacancy_title.find("span", attrs={"data-qa": "vacancy-salary-compensation-type-net"})
    if tag_salary != None:
        salary = tag_salary.text.replace('\xa0', ' ')

    result.append(
        {
            "link":    link,
            "salary":  salary,
            "company": company_name,
            "city":    city,            
        }
    )
    return result

if __name__ == "__main__":
    
    url = 'https://spb.hh.ru/search/vacancy?text=python flask django &area=1&area=2&currency_code=USD&search_field=description'
    headers = get_headers()
    
    main_soup = get_soup(url, headers)

    result = []
    tag_vacancy_list = main_soup.find('main', class_='vacancy-serp-content')
    class_vacancy_item = "bloko-header-section-2"
    tag = 'h2'
    for item in tag_vacancy_list.find_all(tag, class_= class_vacancy_item):
        
        a_tag = item.find('a', class_= 'bloko-link')
        link = a_tag['href']
        
        vacancy_soup = get_soup(link, headers)
        vacancy_description = vacancy_soup.find('div', attrs={"data-qa": "vacancy-description"})
        if not keywords_find(vacancy_description.contents):
            continue
        result = add_info_in_result(vacancy_soup, result)
  

    with open("result.json", "w", encoding="utf8") as file:
        json.dump(result, file, ensure_ascii=False, indent=2)


