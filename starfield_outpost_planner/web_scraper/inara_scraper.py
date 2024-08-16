import timeit
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
    r = requests.get(url)
    if r.status_code != requests.codes.ok:
        print(f"Bad Status Code: {r.status_code}")
        return

    mark = timeit.default_timer() - start
    print(f"html acquisition took {round(mark, 4)}")

    # parse html
    start = timeit.default_timer()
    soup = BeautifulSoup(r.text, 'html.parser')
    cost_data = soup.find(class_="listitem")
    spans = [span.get_text() for span in cost_data.find_all('span')]
    ahrefs = [ahref.get_text() for ahref in cost_data.find_all('a')]
    for name, num in zip(ahrefs, spans):
        required_resources[orm_ify(name)] = int(num)
    mark = timeit.default_timer() - start
    print(f"html parsing took {round(mark, 4)}")
    return required_resources


def scrape_outpost_module_data(url=None):
    module_data = {}
    recipe_data = {}
    # getting web content
    start = timeit.default_timer()
    if url is None:
        url = r'https://inara.cz/starfield/outpost-modules/'

    r = requests.get(url)
    if r.status_code != requests.codes.ok:
        print(f"Bad Status Code: {r.status_code}")
        return

    mark = timeit.default_timer() - start
    print(f"html acquisition took {round(mark, 4)}")

    # parsing web content
    start = timeit.default_timer()

    soup = BeautifulSoup(r.text, 'html.parser')
    table_rows = soup.find('tbody').find_all('tr')

    for i, tr in enumerate(table_rows):
        m_id = i + 1
        m_name, m_type, m_power = (td.get_text() for td in tr.find_all('td'))
        m_link = tr.find('a').get('href')
        r_id = m_id + 34
        module_data[m_id] = {'name': m_name,
                             'type': m_type,
                             'power': m_power,
                             'recipeID': r_id}
        # TODO: make this asynchronous or on a delayed timer
        #   it will not be fun to have to wait for it to complete
        #   with artifically inflated runtimes, but it will keep
        #   from hosing their server or getting me blacklisted.
        # recipe_data[r_id] = get_recipe_required_resources(m_link)

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
        print(f"Bad Status Code: {r.status_code}")
        return

    mark = timeit.default_timer() - start
    print(f"html acquisition took {round(mark, 4)}")

    # parsing web content
    start = timeit.default_timer()

    soup = BeautifulSoup(r.text, 'html.parser')
    manufactured_rows = soup.find('tbody').find_all(tags="[\"subtype102\"]")

    for i, tr in enumerate(manufactured_rows):
        r_id = i + 1
        r_name = tr.find('td').get_text()  # the first column is the resource name
        r_name = orm_ify(r_name)
        r_link = tr.find('a').get('href')  # the first link is the recipe link
        recipe_data[r_id] = {'name': r_name,
                             'required': None}
    mark = timeit.default_timer() - start
    print(f"html parsing took {round(mark, 4)}")

    return recipe_data


def main():
    pass


if __name__ == "__main__":
    main()
