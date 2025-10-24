from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import tempfile
import time

try:
    url = "https://www.mercadolibre.com"

    options = Options()
    temp_dir = tempfile.mkdtemp()
    options.add_argument(f"user-data-dir={temp_dir}")
    driver = webdriver.Chrome(options=options)

    # Inicializar el navegador
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)

    # Seleccionar Mexico
    wait = WebDriverWait(driver, 10)
    mx_button = wait.until(EC.element_to_be_clickable((By.ID, "MX")))
    mx_button.click()

    # Seleccionar Playstation
    search_box = wait.until(EC.presence_of_element_located((By.NAME, "as_word")))
    search_box.send_keys("playstation 5")
    search_box.send_keys(Keys.RETURN)

    # Seleccionar filtro nuevos
    time.sleep(10)
    nuevos_filter = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//*[@id='root-app']/div/div[2]/aside/section[2]/div[5]/ul/li[1]/a")
    ))

    driver.execute_script("arguments[0].scrollIntoView();", nuevos_filter)
    time.sleep(1) 
    nuevos_filter.click()

    # Seleccionar Local
    time.sleep(5)
    local_filter = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//*[@id='root-app']/div/div[2]/aside/section[2]/div[11]/ul/li[1]/a")))
    driver.execute_script("arguments[0].scrollIntoView();", local_filter)
    time.sleep(1) 
    local_filter.click()

    # Ordenar Mayor a menor
    order_menu = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class,'andes-dropdown__trigger')]")))
    order_menu.click()
    time.sleep(3)
    high_to_low = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=':Rlilie:-menu-list-option-price_desc']")))
    high_to_low.click()
    time.sleep(5)

    # Obtener el top 5
    product_names = driver.find_elements(By.CSS_SELECTOR, "h3.poly-component__title-wrapper")[:5]
    product_prices = driver.find_elements(By.CSS_SELECTOR, "div.poly-price__current span.andes-money-amount__fraction")[:5]

    print("Top 5 productos (PlayStation 5 - Nuevos - CDMX - Mayor a menor precio):\n")
    for name, price in zip(product_names, product_prices):
        print(f"* {name.text} - ${price.text}")

except Exception as e:
    print("Error durante ejecucion:", e)

finally:
    time.sleep(5)
    driver.quit()
