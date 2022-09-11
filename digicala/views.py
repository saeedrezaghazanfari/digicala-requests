from django.shortcuts import render
from django.views.generic import ListView
from selenium import webdriver
from selenium.webdriver.common.by import By
from Extentions.utils import fa_to_en_numbers, clear_string
from .models import CategoryModel, DigicalaModel


# url: /list-data
class DataListView(ListView):
    model = DigicalaModel
    fields = ['link_page', 'title', 'price']
    template_name = 'digicala/data_list.html'


# url: /
def home_page(request):

    if request.POST:
        
        bound = 1 if not request.POST.get('bound') else int(request.POST.get('bound'))

        driver = webdriver.Chrome()
        driver.set_window_size(1250, 1000)

        # urls that were used
        driver.get('https://www.digikala.com/search/category-mobile-phone/apple/')  # digicala > apple category
        # driver.get('https://www.digikala.com/search/category-baby-shampoo/')      # digicala > baby shampoo

        new_products = []
        links = []

        link_items = driver.find_elements(By.CSS_SELECTOR, 'a.VerticalProductCard_VerticalProductCard--hover___3eXg')[:bound]
        for item in link_items:
            links.append(item.get_attribute('href'))

        for link in links:

            if DigicalaModel.objects.filter(link_page__iexact=link):
                continue

            # load product page
            driver.get(link)

            # get category of product
            category = driver.find_element(By.CSS_SELECTOR, '.swiper-container > .swiper-wrapper')
            category_cleared = clear_string(category.get_attribute('innerText'))

            # set product category in db
            product_category = CategoryModel.objects.filter(title__iexact=category_cleared).first()
            if not product_category:
                product_category = CategoryModel.objects.create(
                    title=category_cleared
                )

            # Get Properties of Product
            property_items = driver.find_elements(By.CSS_SELECTOR, 'ul.InfoSection_infoSection__wrapper__5zrfc li.ai-center')
            properties = []
            for item in property_items:
                item_cleared = clear_string(item.get_attribute('innerText'))
                properties.append(item_cleared)
            
            # Get title, page link, image, seller, guarantee and price
            link_page = driver.execute_script('return window.location.href;')
            title = driver.find_element(By.TAG_NAME, 'h1').get_attribute('innerText')
            image = driver.find_element(By.CSS_SELECTOR, '.pos-relative > div > img')
            seller = driver.find_element(By.CSS_SELECTOR, 'div.ai-center p.text-subtitle')
            guarantee = driver.find_element(By.CSS_SELECTOR, 'div.d-flex p.text-button-2')
            price = driver.find_element(By.CSS_SELECTOR, 'div.jc-end span.color-800')

            # add product to list
            new_products.append(
                DigicalaModel(
                    category=product_category,
                    link_page=link_page,
                    image=image.get_attribute('src'),
                    title=title,
                    properties=f'{properties}',
                    seller=seller.get_attribute('innerText'),
                    guarantee=guarantee.get_attribute('innerText'),
                    price=fa_to_en_numbers(price.get_attribute('innerText'))
                )
            )

        driver.close() # close window

        # save products in db
        DigicalaModel.objects.bulk_create(new_products)

    return render(request, 'digicala/home.html', {})
