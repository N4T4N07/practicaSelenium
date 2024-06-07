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
        driver.find_element(By.ID, "fname").click()
        driver.find_element(By.ID, "fname").send_keys("Samuel")
        driver.find_element(By.ID, "lname").click()
        driver.find_element(By.ID, "lname").send_keys("Citalan")
        driver.find_element(By.ID, "male").click()
        driver.find_element(By.ID, "option").click()

        dropdown = driver.find_element(By.ID, "option")
        dropdown.find_element(By.XPATH, "//option[. = 'Option 1']").click()

        dropdown = driver.find_element(By.ID, "owc")
        dropdown.find_element(By.XPATH, "//option[. = 'Option 2']").click()

        driver.find_element(By.ID, "moption").click()
        driver.find_element(By.ID, "day").click()
        driver.find_element(By.ID, "day").send_keys("6/06/2024")
    


if __name__ == "__main__":
    unittest.main()