import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


# def test_open_chrome():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.get("https://www.amazon.fr")
#     # barre_recherche = driver.find_element(By.ID, "twotabsearchtextbox")
#     barre_recherche = driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']")
#     barre_recherche.send_keys("Playstation 5" + Keys.ENTER)
#     driver.quit()
#
# def test_tp_xpath():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.get("https://www.carrefour.fr")
#     popup_cookies = driver.find_element(By.XPATH, "//div[@class='banner-actions-container']/button[text()='Tout accepter']")
#     popup_cookies.click()
#     time.sleep(2)
#     barre_recherche = driver.find_element(By.XPATH, "//input[@aria-label='Rechercher parmi le contenu du site']")
#     barre_recherche.send_keys("1664")
#     time.sleep(2)
#     search_bar = driver.find_element(By.XPATH, "//button[@class='pl-button header-search__submit-btn pl-button--primary']")
#     search_bar.click()
#     time.sleep(2)
#     Biere = driver.find_element(By.XPATH, "(//h2[@class='ds-title ds-title--medium ds-title--s'])[1]")
#     Biere.click()
#     time.sleep(2)
#     Acheter = driver.find_element(By.XPATH, "//span[text()='ACHETER']")
#     Acheter.click()
#     time.sleep(2)

# def test_tp_CSS():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.get("https://www.carrefour.fr")
#     popup_cookies = driver.find_element(By.CSS_SELECTOR, ".banner-actions-container > button")
#     popup_cookies.click()
#     time.sleep(2)
#     barre_recherche = driver.find_element(By.CSS_SELECTOR, "[required]")
#     barre_recherche.send_keys("1664")
#     time.sleep(2)
#     search_bar = driver.find_element(By.CSS_SELECTOR, "button[type=submit]")
#     search_bar.click()
#     time.sleep(2)
#     Biere = driver.find_element(By.CSS_SELECTOR, ".product-grid-item:nth-child(1) .main-vertical--image")
#     Biere.click()
#     time.sleep(2)
#     Acheter = driver.find_element(By.CSS_SELECTOR, "span.pl-button__label > span")
#     Acheter.click()
#     time.sleep(2)


def test_css_correction():
    driver = webdriver.Chrome()

    driver.maximize_window()
    driver.get("https://www.carrefour.fr/")

    # driver.implicitly_wait(10)
    # time.sleep(2)

    wait = WebDriverWait(driver, 10)
    close_cookies_button = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".banner-actions-container > button")))

    # close_cookies = driver.find_element(By.CSS_SELECTOR, ".banner-actions-container > button")
    close_cookies_button.click()
    search_bar = driver.find_element(By.CSS_SELECTOR, "input[required]")
    # possibilite utilisation [required]
    search_bar.send_keys("1664")
    search_button = driver.find_element(By.CSS_SELECTOR, "button[type=submit]")
    # possibilite utilisation [type=submit]
    search_button.click()
    first_result = driver.find_element(By.CSS_SELECTOR, ".product-grid-item:nth-child(1) .main-vertical--image")
    first_result.click()
    # time.sleep(1)
    # screenshot
    # driver.get_screenshot_as_file("c:\\temp\\sc.png")
    buy_button = driver.find_element(By.CSS_SELECTOR, ".pdp-button-container")
    # possibilite utilisation [aria-label='ACHETER'] : mais attention au changement de langue
    buy_button.click()
    # time.sleep(2)
    retrait_en_magasin = driver.find_element(By.CSS_SELECTOR, ".push-services--pickers li:nth-child(1) label")
    delivery24 = driver.find_element(By.CSS_SELECTOR, ".push-services--pickers li:nth-child(2) label")
    delivery1 = driver.find_element(By.CSS_SELECTOR, ".push-services--pickers li:nth-child(3) label")
    assert retrait_en_magasin.text == 'Drive\nRetrait gratuit en magasin'
    assert "Drive" in retrait_en_magasin.text
    # print('Selector "retrait en drive" is present')
    assert delivery24.text == 'Livraison\nVotre plein de course en 24h'
    # print('Selector "livraison en 24h" is present')
    assert delivery1.text == 'Livraison 1h\nVos courses d’appoint en 1h'
    # print('Selector "livraison en 1h" is present')
    # presence des 3 selectors
    # time.sleep(2)
    driver.quit()