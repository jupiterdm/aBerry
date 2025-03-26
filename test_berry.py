import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="module")
def driver():
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver

#Проверка открытия сайта berrywood
def test_open_site(driver):
    driver.get('https://berrywoodfamily.ru/')
    logo = driver.find_element(By.CLASS_NAME, 'hero--title')
    assert 'hero--title' in logo.get_attribute("class")
    print('Страница найдена')

#Проверка открытия видео на главной странице berrywood
def test_vid(driver):
    driver.get('https://berrywoodfamily.ru/')
    time.sleep(2)
    vid = driver.find_element(By.TAG_NAME, 'video')
    source = vid.find_element(By.TAG_NAME,'source')
    source_url = source.get_attribute('src')
    assert source_url == ('https://berrywoodfamily.ru/wp-content/themes/berrywood/'
                          'assets/video/page-main/P1083898.mp4')
    print('Видос найден')

#Проверка открытия раздела "Карьера" через боковое меню
def test_career(driver):
    driver.get('https://berrywoodfamily.ru/')
    munu_bottom1 = driver.find_element(By.LINK_TEXT, 'Карьера')
    munu_bottom1.click()
    time.sleep(2)
    career_page = driver.find_element(By.CLASS_NAME, 'hero--title')
    assert 'hero--title' in career_page.get_attribute('class')
    print('Страница найдена')

#Проверка открытия раздела "Вакансии" через боковое меню
def test_vakansii(driver):
    driver.get('https://berrywoodfamily.ru/')
    munu_bottom2 = driver.find_element(By.LINK_TEXT, 'Вакансии')
    munu_bottom2.click()
    time.sleep(2)
    vakansii_page = driver.find_element(By.XPATH, '/html/body/main/section/div[1]/div')
    top = vakansii_page.text #text on page
    assert top == 'сейчас ищем'
    print('Страница найдена')

#Проверка открытия раздела "Новости" через боковое меню
def test_news(driver):
    driver.get('https://berrywoodfamily.ru/')
    munu_bottom3 = driver.find_element(By.LINK_TEXT, 'Новости')
    munu_bottom3.click()
    time.sleep(2)
    news_page = driver.find_element(By.XPATH, '/html/body/main/section[2]/div/div[1]/div/div')
    top = news_page.text #text on page
    assert top == 'Следи за компанией'
    print('Страница найдена')

#Проверка открытия раздела "Программа лояльности" через боковое меню
def test_bonus(driver):
    driver.get('https://berrywoodfamily.ru/')
    munu_bottom4 = driver.find_element(By.LINK_TEXT, 'Программа лояльности')
    munu_bottom4.click()
    time.sleep(2)
    bonus_page = driver.find_element(By.XPATH, '/html/body/main/a/div/h1/span[1]')
    top = bonus_page.text #text on page
    assert top == 'Программа лояльности'
    print('Страница найдена')

#Проверка открытия раздела "Агенство событий" через боковое меню
def test_events(driver):
    driver.get('https://berrywoodfamily.ru/')
    munu_bottom5 = driver.find_element(By.LINK_TEXT, 'Агентство событий')
    munu_bottom5.click()
    time.sleep(2)
    events_page = driver.find_element(By.XPATH, '/html/body/main/section[1]/div/div/div[1]/span')
    top = events_page.text #text on page
    assert top == 'События, которые помнишь'
    print('Страница найдена')

#Проверка кликабельности лого berrywood
def test_logo(driver):
    driver.get('https://berrywoodfamily.ru/')
    time.sleep(2)
    logo = driver.find_element(By.CLASS_NAME, 'header--logo')
    logo.click()
    assert driver.current_url == 'https://berrywoodfamily.ru/'
    print('Логотип кликабелен')

#Проверка открытия Тунгуски через меню "Рестораны"
def test_menu_tungus(driver):
    driver.get('https://berrywoodfamily.ru/')
    tung = driver.find_element(By.LINK_TEXT, value='Tunguska')
    main_window = driver.current_window_handle
    tung.click()
    time.sleep(3)
    new_window = [window for window in driver.window_handles if window != main_window][0]
    driver.switch_to.window(new_window)
    assert "tunguska" in driver.current_url
    print('Открылся сайт Тунгуски')
