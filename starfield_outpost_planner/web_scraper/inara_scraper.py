import timeit
import json
import os
from time import sleep
from bs4 import BeautifulSoup
import requests


def orm_ify(resource_name):
    # translates the resource name to the ORM Model property
    #   because ORM needs DB compatible class & property names
    #   example:
    #       'Luxury Textile' => 'requiredLuxuryTextile'
    return 'required' + resource_name.replace(' ', '').replace('-', '')


def get_recipe_required_resources(url):
    required_resources = {}

    # getting web content
    start = timeit.default_timer()
    # print(f"requests.get(url={repr(url)})")
    r = requests.get(url)
    if r.status_code != requests.codes.ok:
        print(f"WARNING: Bad Status Code: {r.status_code}")
        return required_resources

    mark = timeit.default_timer() - start
    # print(f"html acquisition took {round(mark, 4)}")

    # parse html
    start = timeit.default_timer()
    soup = BeautifulSoup(r.text, 'html.parser')
    cost_data = soup.find(class_="listitem")
    if not cost_data:
        print(f"WARNING: no required resources were found for {url} (no class='listitem')")
        return required_resources
    nums = [int(num.get_text()) for num in cost_data.find_all(name='span', attrs={'class': 'itemamountnumprefix'})]
    names = [name.get_text() for name in cost_data.find_all(name='a')]
    for name, num in zip(names, nums):
        # print(f'    {orm_ify(name)}: {num}')
        required_resources[orm_ify(name)] = num
    mark = timeit.default_timer() - start
    # print(f"html parsing took {round(mark, 4)}")
    return required_resources


def scrape_outpost_module_data(url=None, recipe_index_start=35):
    module_data = {}
    recipe_data = {}
    # getting web content
    start = timeit.default_timer()
    if url is None:
        url = r'https://inara.cz/starfield/outpost-modules/'

    # print(f"requests.get(url={repr(url)})")
    r = requests.get(url)
    if r.status_code != requests.codes.ok:
        print(f"WARNING: Bad Status Code: {r.status_code}")
        return module_data, recipe_data

    mark = timeit.default_timer() - start
    print(f"html acquisition took {round(mark, 4)}")

    # parsing web content
    start = timeit.default_timer()

    url_parent = r'https://inara.cz'
    soup = BeautifulSoup(r.text, 'html.parser')
    table_rows = soup.find('tbody').find_all('tr')

    s_time = 1
    for i, tr in enumerate(table_rows):
        m_id = i
        m_name, m_type, m_power = (td.get_text() for td in tr.find_all('td'))
        m_link = tr.find('a').get('href')
        r_id = m_id + recipe_index_start
        module_data[m_id] = {'name': m_name,
                             'type': m_type,
                             'power': m_power,
                             'recipeID': r_id}
        # sleep to avoid excessive http requests to url source
        # print(f'sleeping {s_time}')
        sleep(s_time)
        # print(f'getting recipe[{r_id}] required resources from {url_parent + m_link}')
        recipe_data[r_id] = {'description': m_name,
                             'required': get_recipe_required_resources(url_parent + m_link)}
        if not (i % 30):
            print(f"i : {i}")

    mark = timeit.default_timer() - start
    print(f"html parsing took {round(mark, 4)}")
    return module_data, recipe_data


def scrape_manufactured_resources_recipe_data(url=None):
    recipe_data = {}
    # getting web content
    start = timeit.default_timer()

    if url is None:
        url = r'https://inara.cz/starfield/resources/'
    r = requests.get(url)
    if r.status_code != requests.codes.ok:
        print(f"WARNING: Bad Status Code: {r.status_code}")
        return recipe_data

    mark = timeit.default_timer() - start
    print(f"html acquisition took {round(mark, 4)}")

    # parsing web content
    start = timeit.default_timer()

    soup = BeautifulSoup(r.text, 'html.parser')
    if not soup:
        print(f'WARNING: BeautifulSoup unable to parse html')
        return recipe_data

    tbody = soup.find('tbody')
    if not tbody:
        print(f'WARNING: soup was unable to find <tbody>')
        return recipe_data

    # this is not returning any matches
    manufactured_rows = tbody.find_all(name='tr', attrs={'data-tags': "[\"subtype102\"]"})
    if not manufactured_rows:
        print('WARNING: soup was unable to find <tr data-tags="[\"subtype102\"]">')
        return recipe_data
    else:
        print(f"found {len(manufactured_rows)} manufacured_rows (has tag[\"subtype102\"])")
    url_parent = r'https://inara.cz'

    s_time = 1
    for i, tr in enumerate(manufactured_rows):
        r_id = i + 1
        r_name = tr.find('td').get_text()  # the first column is the resource name
        # ormr_name = orm_ify(r_name)
        r_link = tr.find('a').get('href')  # the first link is the recipe link

        # sleep to avoid excessive http requests to url source
        # print(f'sleeping {s_time}')
        sleep(s_time)
        # print(f'getting recipe[{r_id}] required resources from {url_parent + r_link}')
        recipe_resources = get_recipe_required_resources(url_parent + r_link)
        recipe_data[r_id] = {'description': r_name,
                             'required': recipe_resources}
        if not (i % 30):
            print(f"i : {i}")

    mark = timeit.default_timer() - start
    print(f"html parsing took {round(mark, 4)}")
    return recipe_data


def main():
    # get filepaths to write to
    cwd = os.getcwd()
    target_dir = cwd
    if not cwd.endswith('web_scraper'):
        for root, dirs, files in os.walk(cwd):
            if 'web_scraper' in dirs:
                target_dir = os.path.join(root, 'web_scraper')
                break
    print(f"target_dir : {target_dir}")

    # get data
    recipe_data = scrape_manufactured_resources_recipe_data()
    module_data, recipe_data_2 = scrape_outpost_module_data(len(recipe_data))
    recipe_data.update(recipe_data_2)

    # write data to json files
    with open(f'{os.path.join(target_dir, "module_data.json")}', mode='w') as m_jdf:
        m_jdf.write(json.dumps(module_data, indent=4, sort_keys=True))
        m_jdf.close()
    with open(f'{os.path.join(target_dir, "recipe_data.json")}', mode='w') as r_jdf:
        r_jdf.write(json.dumps(recipe_data, indent=4, sort_keys=True))
        r_jdf.close()


if __name__ == "__main__":
    main()
