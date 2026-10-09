from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_cart():
    driver = webdriver.Edge()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://www.saucedemo.com/")

        usuario = wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
        password = wait.until(EC.visibility_of_element_located((By.ID, "password")))
        boton_login = wait.until(EC.element_to_be_clickable((By.ID, "login-button")))

        usuario.send_keys("standard_user")
        password.send_keys("secret_sauce")
        boton_login.click()

        wait.until(EC.url_contains("/inventory.html"))
        primer_producto = wait.until(EC.visibility_of_element_located((By.CLASS_NAME,"inventory_item")))

        nombre_producto = primer_producto.find_element(By.CLASS_NAME, "inventory_item_name").text
        boton_agregar = primer_producto.find_element(By.TAG_NAME, "button")
        assert boton_agregar.text == "Add to cart"
        boton_agregar.click()

        contador_carrito = wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
        )
        assert contador_carrito.text == "1"

        carrito = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link")))
        carrito.click()
        wait.until(EC.url_contains("/cart.html"))

        nombre_producto_carrito = wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item_name"))
        ).text
        assert nombre_producto == nombre_producto_carrito

    finally:
        driver.quit()