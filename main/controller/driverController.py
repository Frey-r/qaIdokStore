import pandas as pd
import selenium
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import datetime

import resultController

driver = selenium.webdriver.Chrome()
class TiendaIdok():

    def __init__(self, url):
        self.url = url
        self.date = datetime.datetime.now().strftime('%d/%m/%Y')
        self.project_name = "Tienda Idok"
        self.type_test = "Automatizada"
        self.eviroment = "Producción"
        self.device = "Chromium Selenium"
        self.level_test = "Sistema"

    def banner_click(self):
        type_issue = "Componente"
        module = "Landing - carrusel"
        driver.get(self.url)
        imagen_banner = driver.find_element(By.XPATH,'/html/body/main/div/div[2]/div[3]/img')
        pre_url = driver.current_url
        try:
            imagen_banner.click()
            act_url = driver.current_url
            if pre_url != act_url:
                result = resultController.Result(
                    type_issue,
                    self.date,
                    self.project_name,
                    module,
                    self.type_test,
                    self.eviroment,
                    self.device,
                    self.level_test,
                    self.url,
                    True
                )
                return result.get_result()
            else:
                result = resultController.Result(
                    type_issue,
                    self.date,
                    self.project_name,
                    module,
                    self.type_test,
                    self.eviroment,
                    self.device,
                    self.level_test,
                    self.url,
                    False
                )
                return result.get_result()
        except Exception as e:
            url = driver.current_url
            result = resultController.Result(
                type_issue,
                self.date,
                self.project_name,
                module,
                self.type_test,
                self.eviroment,
                self.device,
                self.level_test,
                self.url,
                False
            )
            print(f"""
                        ERROR: {e}
                        URL: {url} 
                        RESULT: {result.get_result()}
                   """)
            return result.get_result()

    def banner_button(self):
        driver.get(self.url)
        banner_divs = driver.find_elements(By.CLASS_NAME,'carousel-item')
        pre_url = driver.current_url
        for banner in banner_divs:
            try:
                button = banner.find_element(By.XPATH, './/button')
                button.click()
                url = driver.current_url
                return True if url != pre_url else False
            except Exception as e:
                print(f"""
                    ERROR: {e}
                    """)
                try:
                    a_link = banner.find_element(By.XPATH, './/a')
                    a_link.click()
                    url = driver.current_url
                    return True if url != pre_url else False
                except Exception as e:
                    return False
                    print(f"""
                        ERROR: {e}
                        """)
    def carrousel_select(self):
        driver.get(self.url)
        driver.find_element(By.XPATH)
    def redirect_preguntas(self):
        driver.get(self.url)
        driver.find_element(By.XPATH, '//*[@id="info2-tab"]').click()
        redirect_url = driver.find_element(By.XPATH,'//*[@id="info2"]/div/div/div/a').get_attribute('href')
        if redirect_url != driver.current_url and redirect_url != "https://firmaya.idok.cl":
            return True
        else:
            return False
    def otros_productos(self):
        driver.get(self.url)
        div_productos = driver.find_element(By.XPATH, '//*[@id="default"]/main/section[3]/div')
        try:
            div_productos.find_element(By.XPATH, '//div')
            return True
        except Exception as e:
            return False
    def h1_enum(self):
        driver.get(self.url)
        h1_elements = driver.find_elements(By.TAG_NAME, "h1")
        h1_texts = [h1_element.text for h1_element in h1_elements]
        contains_otros_productos = any("OTROS PRODUCTOS" in text for text in h1_texts)
        return True if contains_otros_productos else False
        df = pd.DataFrame({"H1": h1_texts})
        print(df)
    def dropdown_menu(self):
        driver.get(self.url)
        dropdown_element = driver.find_element(By.XPATH, '//*[@id="default"]/header/div[2]/div/nav/div/ul/li[2]/div')
        ActionChains(driver).move_to_element(dropdown_element).perform()
        driver.execute_script("window.scrollBy(0, 100);")

test = TiendaIdok('https://store.idok.cl')
print(test.banner_click())