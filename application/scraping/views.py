from django.shortcuts import render
from django.http import HttpResponse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

def acceder_a_mercadolibre(request):
    # Crear el directorio screenshots si no existe en la raiz de la aplicacion
    if not os.path.exists("static/screenshots"):
        os.makedirs("static/screenshots")
    
    # Configuración del navegador y acceso a la pagina de Mercado Libre desde chrome 
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=options)

    driver.get("https://www.mercadolibre.com")
    time.sleep(3)
    driver.save_screenshot("screenshots/step1_home_page.png")  # Paso 1

    try:
        # Cambio a la versión de Mexico desde la url principal
        mexico_link = driver.find_element(By.PARTIAL_LINK_TEXT, "México")
        mexico_link.click()
        time.sleep(3)
        driver.save_screenshot("screenshots/step2_mexico_page.png")  # Paso 2

        # Búsqueda de productos (playstation5)
        search_box = driver.find_element(By.NAME, "as_word")
        search_box.send_keys("playstation5")
        search_box.send_keys(Keys.RETURN)
        time.sleep(3)
        driver.save_screenshot("screenshots/step3_search_results.png")  # Paso 3

        # Cierre del banner de cookies(nos da acceso y cierre de ventanas internas)
        try:
            cookie_banner = driver.find_element(By.CLASS_NAME, "cookie-consent-banner-opt-out__container")
            close_button = cookie_banner.find_element(By.XPATH, ".//button")
            close_button.click()
            time.sleep(2)
        except Exception:
            print("Banner de cookies no encontrado o no se pudo cerrar.")
        driver.save_screenshot("screenshots/step4_cookie_banner_closed.png")  # Paso 4

        # Extraccion y ordenación de los 5 productos
        productos = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@class='poly-card__content']"))
        )

        productos_list = []
        for producto in productos[:5]:
            titulo = producto.find_element(By.XPATH, ".//h2[@class='poly-box poly-component__title']/a").text
            precio_str = producto.find_element(By.XPATH, ".//span[@class='andes-money-amount__fraction']").text
            precio_num = float(precio_str.replace("$", "").replace(",", ""))
            productos_list.append({"titulo": titulo, "precio": precio_num})

        # Ordenar productos
        productos_list.sort(key=lambda x: x['precio'], reverse=True)
        driver.save_screenshot("screenshots/step5_products.png")  # Paso 5

        # Pasar los productos a un templade index
        context = {
            "productos": productos_list
        }
        
        return render(request, 'templade/index.html', context)

    except Exception as e:
        print(f"Error: {e}")
        return HttpResponse("Error al intentar acceder a la versión de México")
    
    finally:
        driver.quit()
