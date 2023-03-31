from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pytest
from pathlib import Path
from datetime import date



class Test_OdevClass:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        #self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com")
        self.folderPath = str(date.today())
        Path(self.folderPath).mkdir(exist_ok=True)
    def teardown_method(self):
        self.driver.quit()
    def test_username_password_not_filled(self):
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        userNameInput = self.driver.find_element(By.ID,"user-name")
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        passwordInput = self.driver.find_element(By.ID,"password")
        userNameInput.send_keys("")
        passwordInput.send_keys("")
        loginButtonClick(self)
        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']")
        self.driver.save_screenshot(self.folderPath+"/test-username-password-not-filled.png")
        assert errorMessage.text == "Epic sadface: Username is required"
    def test_just_password_not_filled(self):
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        userNameInput = self.driver.find_element(By.ID,"user-name")
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        passwordInput = self.driver.find_element(By.ID,"password")
        userNameInput.send_keys("standard_user")
        passwordInput.send_keys("")
        loginButtonClick(self)
        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']")
        self.driver.save_screenshot(self.folderPath+"/test-just-password-not-filled.png")
        assert errorMessage.text == "Epic sadface: Password is required"
    def test_user_locked_out(self):
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "user-name")))
        userNameInput = self.driver.find_element(By.ID,"user-name")
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "password")))
        passwordInput = self.driver.find_element(By.ID,"password")
        userNameInput.send_keys("locked_out_user")
        passwordInput.send_keys("secret_sauce")
        loginButtonClick(self)
        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']")
        self.driver.save_screenshot(self.folderPath+"/test-user-locked-out.png")
        assert errorMessage.text == "Epic sadface: Sorry, this user has been locked out."
    def test_username_password_not_filled_red_cross_button(self):
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        userNameInput = self.driver.find_element(By.ID,"user-name")
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        passwordInput = self.driver.find_element(By.ID,"password")
        userNameInput.send_keys("")
        passwordInput.send_keys("")
        loginButtonClick(self)
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.CSS_SELECTOR,"#login_button_container > div > form > div:nth-child(1) > svg")))
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.CSS_SELECTOR,"#login_button_container > div > form > div:nth-child(2) > svg")))
        errorMessageUserRedCross = self.driver.find_element(By.CSS_SELECTOR,"#login_button_container > div > form > div:nth-child(1) > svg")
        errorMessagePasswordRedCross = self.driver.find_element(By.CSS_SELECTOR,"#login_button_container > div > form > div:nth-child(2) > svg")
        closeWarningMessage = self.driver.find_element(By.CLASS_NAME,"error-button")
        closeWarningMessage.click()
        self.driver.save_screenshot(self.folderPath+"/test-username-password-not-filled-red-cross-button.png")
        assert WebDriverWait(self.driver,2).until(ec.invisibility_of_element((By.CSS_SELECTOR,"#login_button_container > div > form > div:nth-child(1) > svg"))) and WebDriverWait(self.driver,2).until(ec.invisibility_of_element((By.CSS_SELECTOR,"#login_button_container > div > form > div:nth-child(2) > svg")))
    def test_go_inventory_adress(self):
        self.driver.maximize_window()
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        userNameInput = self.driver.find_element(By.ID,"user-name")
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        passwordInput = self.driver.find_element(By.ID,"password")
        userNameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        loginButtonClick(self)
        inventoryItems = self.driver.find_elements(By.CLASS_NAME,"inventory_item")
        nowUrl =self.driver.current_url
        self.driver.save_screenshot(self.folderPath+"/test-go-inventory-adress.png")
        assert nowUrl=="https://www.saucedemo.com/inventory.html" and len(inventoryItems)==6
    def test_add_cart_button_click(self):
        succesfulLogIn(self)
        self.driver.maximize_window()
        loginButtonClick(self)
        WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.CLASS_NAME,"btn_primary")))
        addToCartButtons = self.driver.find_elements(By.CLASS_NAME,"btn_primary")
        addButtonsQuantity = len(addToCartButtons)
        for addButtons in addToCartButtons:
            addButtons.click()
        removeAllButtons = self.driver.find_elements(By.CLASS_NAME,"btn_secondary")
        self.driver.save_screenshot(self.folderPath+"/test-add-cart-button-click1.png")
        assert (len(removeAllButtons)) == addButtonsQuantity
    def test_remove_button_click(self):
        succesfulLogIn(self)
        self.driver.maximize_window()
        loginButtonClick(self)
        WebDriverWait(self.driver,3).until(ec.visibility_of_element_located((By.CLASS_NAME,"btn_primary")))
        addToCartButtons = self.driver.find_elements(By.CLASS_NAME,"btn_primary")
        addButtonsQuantity = len(addToCartButtons)
        for addButtons in addToCartButtons:
            addButtons.click()
        removeAllButtons = self.driver.find_elements(By.CLASS_NAME,"btn_secondary")
        for removeButtons in removeAllButtons:
            removeButtons.click()
        self.driver.save_screenshot(self.folderPath+"/test-remove-button-click1.png")
        removeQuantity = (len(removeAllButtons))
        assert removeQuantity == addButtonsQuantity
    @pytest.mark.parametrize("username,password",[("1","1"),("kullaniciadim","sifrem"),("adim","utku")])
    def invalid_login(self,username,password):
        self.waitForElementVisible(By.ID,"user-name")
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        userNameInput = self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisible(By.ID,"password")
        passwordInput = self.driver.find_element(By.ID,"password")
        userNameInput.send_keys(username)
        passwordInput.send_keys(password)
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']")
        self.driver.save_screenshot(f"{self.folderPath}/test-invalid-login.{username}-{password}.png")
        assert errorMessage.text == "Epic sadface: Username and password do not match any user in this service"

    def waitForElementVisible(self,locator,timeout=5):
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located(locator))

#Hangi foksiyondaysa o fonksiyonun ismini f stringle ScreenShot a ekle de yapılabilir.



def succesfulLogIn(self):
    WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
    userNameInput = self.driver.find_element(By.ID,"user-name")
    WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
    passwordInput = self.driver.find_element(By.ID,"password")
    userNameInput.send_keys("standard_user")
    passwordInput.send_keys("secret_sauce")

def loginButtonClick(self):
    loginBtn = self.driver.find_element(By.ID,"login-button")
    loginBtn.click()
