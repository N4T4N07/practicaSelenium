import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class TryTestingThisSite(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_interact_with_try_testing_site(self):
        driver = self.driver
        driver.get("https://trytestingthis.netlify.app/")
        driver.set_window_size(1532, 816)

        # Interactuar con los elementos de la página
        #Pedro
        driver.find_element(By.ID, "fname").click()
        driver.find_element(By.ID, "fname").clear()
        driver.find_element(By.ID, "fname").send_keys("Pedro")
        driver.find_element(By.ID, "lname").click()
        driver.find_element(By.ID, "lname").clear()
        driver.find_element(By.ID, "lname").send_keys("Canil")
        driver.find_element(By.ID, "male").click()
        driver.find_element(By.ID, "option").click()

        dropdown = driver.find_element(By.ID, "option")
        dropdown.find_element(By.XPATH, "//option[. = 'Option 1']").click()

        dropdown = driver.find_element(By.ID, "owc")
        dropdown.find_element(By.XPATH, "//option[. = 'Option 1']").click()

        driver.find_element(By.ID, "moption").click()
        driver.find_element(By.ID, "day").click()
        driver.find_element(By.ID, "day").send_keys("2024-6-1")

        #Pablo
        # Interactuar con los elementos de la página
        driver.find_element(By.ID, "fname").click()
        driver.find_element(By.ID, "fname").clear()
        driver.find_element(By.ID, "fname").send_keys("Pablo")
        driver.find_element(By.ID, "lname").click()
        driver.find_element(By.ID, "lname").clear()
        driver.find_element(By.ID, "lname").send_keys("Alemán")
        driver.find_element(By.ID, "male").click()
        driver.find_element(By.ID, "option").click()

        dropdown = driver.find_element(By.ID, "option")
        dropdown.find_element(By.XPATH, "//option[. = 'Option 2']").click()

        dropdown = driver.find_element(By.ID, "owc")
        dropdown.find_element(By.XPATH, "//option[. = 'Option 1']").click()

        driver.find_element(By.ID, "moption").click()
        driver.find_element(By.ID, "day").click()
        driver.find_element(By.ID, "day").send_keys("2024-6-2")

        #Juan
        # Interactuar con los elementos de la página
        driver.find_element(By.ID, "fname").click()
        driver.find_element(By.ID, "fname").clear()
        driver.find_element(By.ID, "fname").send_keys("Juan")
        driver.find_element(By.ID, "lname").click()
        driver.find_element(By.ID, "lname").clear()
        driver.find_element(By.ID, "lname").send_keys("Ixcamparic")
        driver.find_element(By.ID, "male").click()
        driver.find_element(By.ID, "option").click()

        dropdown = driver.find_element(By.ID, "option")
        dropdown.find_element(By.XPATH, "//option[. = 'Option 1']").click()

        dropdown = driver.find_element(By.ID, "owc")
        dropdown.find_element(By.XPATH, "//option[. = 'Option 1']").click()

        driver.find_element(By.ID, "moption").click()
        driver.find_element(By.ID, "day").click()
        driver.find_element(By.ID, "day").send_keys("2024-6-3")

        #Natan
        # Interactuar con los elementos de la página
        driver.find_element(By.ID, "fname").click()
        driver.find_element(By.ID, "fname").clear()
        driver.find_element(By.ID, "fname").send_keys("Natan")
        driver.find_element(By.ID, "lname").click()
        driver.find_element(By.ID, "lname").clear()
        driver.find_element(By.ID, "lname").send_keys("Saquic")
        driver.find_element(By.ID, "male").click()
        driver.find_element(By.ID, "option").click()

        dropdown = driver.find_element(By.ID, "option")
        dropdown.find_element(By.XPATH, "//option[. = 'Option 1']").click()

        dropdown = driver.find_element(By.ID, "owc")
        dropdown.find_element(By.XPATH, "//option[. = 'Option 2']").click()

        driver.find_element(By.ID, "moption").click()
        driver.find_element(By.ID, "day").click()
        driver.find_element(By.ID, "day").send_keys("2024-6-4")

        #Samuel
        # Interactuar con los elementos de la página
        driver.find_element(By.ID, "fname").click()
        driver.find_element(By.ID, "fname").clear()
        driver.find_element(By.ID, "fname").send_keys("Samuel")
        driver.find_element(By.ID, "lname").click()
        driver.find_element(By.ID, "lname").clear()
        driver.find_element(By.ID, "lname").send_keys("Citalán")
        driver.find_element(By.ID, "male").click()
        driver.find_element(By.ID, "option").click()

        dropdown = driver.find_element(By.ID, "option")
        dropdown.find_element(By.XPATH, "//option[. = 'Option 2']").click()

        dropdown = driver.find_element(By.ID, "owc")
        dropdown.find_element(By.XPATH, "//option[. = 'Option 1']").click()

        driver.find_element(By.ID, "moption").click()
        driver.find_element(By.ID, "day").click()
        driver.find_element(By.ID, "day").send_keys("2024-6-1")
    
    
    
    

if __name__ == "__main__":
    unittest.main()
