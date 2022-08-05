import time
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

def openProduct(driver, index):
    liste_produits = driver.find_elements(By.CSS_SELECTOR, ".product-grid-item:not(.storetail) h2")
    liste_produits[index].click()

def test_carrefour_wait():
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)

    # ouverture Home Page carrefour
    driver.get("https://www.carrefour.fr/")

    # Fermeture cookies popup
    close_cookies_button = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "#onetrust-accept-btn-handler")))
    close_cookies_button.click()

    # Click Hamburger Button
    Hamburger_button = wait.until(expected_conditions.element_to_be_clickable
                                  ((By.CSS_SELECTOR, ".mainbar__nav-toggle-icon")))
    Hamburger_button.click()
    time.sleep(2)
    # Click épicerie salée
    epicerie_salee_menu = driver.find_element(By.CSS_SELECTOR, ".nav-item__menu-link [alt='Epicerie salée']")
    action = ActionChains(driver)
    # move to épicerie salée
    action.move_to_element(epicerie_salee_menu)
    action.perform()
    # move to pates, riz etc
    pates_riz_feculents = wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "#data-menu-level-1_R12 > li:nth-child(7)")))
    action.move_to_element(pates_riz_feculents)
    action.perform()
    # selectionner pates
    pates = wait.until(expected_conditions.element_to_be_clickable
                       ((By.CSS_SELECTOR, "#data-menu-level-2_R12F05 > li:nth-child(3)")))
    pates.click()
    # selectioner le quatriéme article
    openProduct(driver, 3)
    #Acheter le produit selectionne
    acheter = wait.until(expected_conditions.element_to_be_clickable
                         ((By.CSS_SELECTOR, "#data-produit-acheter")))
    acheter.click()
    # click drive
    choix_drive = wait.until(expected_conditions.element_to_be_clickable
                            ((By.CSS_SELECTOR, "div.pl-visual-picker.service-picker.pl-visual-picker--size-m:nth-child(1)")))
    choix_drive.click()
    #time.sleep(2)
    # type 75001 + enter key
    adresse = wait.until(expected_conditions.visibility_of_element_located(
        (By.CSS_SELECTOR, ".suggestions-input input[data-testid='input-control']")))
    adresse.send_keys("75001")
    time.sleep(2)
    adresse.send_keys(Keys.ENTER)
    # select first store (city paris Richelieu)
    Paris_richelieu = wait.until(expected_conditions.element_to_be_clickable
                                 ((By.CSS_SELECTOR, "button[aria-label='Choisir le Retrait en magasin, magasin City Paris Richelieu'] span")))
    Paris_richelieu.click()
    # assert product is not available
    Message = wait.until(expected_conditions.visibility_of_element_located
                         ((By.CSS_SELECTOR, ".ds-body-text.ds-body-text--weight-bold.ds-body-text--size-m.ds-body-text--color-inherit")))
    assert Message.text == "1 produit indisponible dans ce magasin."
    # Screen shot
    driver.get_screenshot_as_file("C:\\Users\\ib\\Desktop\\Formation\\Selenium\\capture.png")
    # fermer navigateur
    driver.quit()

