import pytest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

TINHTE_HOMEPAGE = "https://tinhte.vn"


def test_login_success():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    signin_xpath = '//a[@href="https://tinhte.vn/login/"]'
    username_input_xpath = '//input[@id="ctrl_pageLogin_login" and @class="textCtrl"]'
    password_input_xpath = '//input[@id="ctrl_pageLogin_password" and @class="textCtrl"]'
    signin_button_xpath = '//*[@id="pageLogin"]/dl[3]/dd/input'
    username = "nguyen_thi_dau"
    password = "Hung8787"
    delay = 3

    driver.get(TINHTE_HOMEPAGE)
    try:

        # Wait for Sign-In button appears
        signin_button = WebDriverWait(driver, delay).until(
            EC.presence_of_element_located((By.XPATH, signin_xpath)))
        signin_button.click()

        # Check driver in Sign-In page
        assert "Đăng nhập | Tinhte.vn" in driver.title

        # Fill information

        username_input = WebDriverWait(driver, delay).until(
            EC.presence_of_element_located((By.XPATH, username_input_xpath)))
        password_input = WebDriverWait(driver, delay).until(
            EC.element_to_be_clickable((By.XPATH, password_input_xpath)))
        username_input.send_keys(username)
        password_input.send_keys(password)

        # Click sign-in button
        signin_button_xpath = driver.find_element_by_xpath(signin_button_xpath)
        signin_button_xpath.click()

        # Back to homepage
        assert "Cộng đồng Khoa học & Công nghệ | Tinh tế" in driver.title

    except TimeoutException:
        raise TimeoutException("Loading took too much!")

    driver.quit()


def test_login_success_with_google_account():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    signin_xpath = '//a[@href="https://tinhte.vn/login/"]'
    google_login_button_xpath = '//*[@id="pageLogin"]/dl[4]/dd[2]/span/span'
    email_input_xpath = '//input[@type="email"]'
    passowrd_input_xpath = '//input[@type="password"]'
    username_continue_button_xpath = '//*[@id="identifierNext"]'
    password_continue_button_xpath = '//*[@id="passwordNext"]'

    email = "softwaretestingbk2021@gmail.com"
    password = "Hung8787"
    delay = 3
    driver.get(TINHTE_HOMEPAGE)
    try:

        # Wait for Sign-In button appears
        signin_button = WebDriverWait(driver, delay).until(
            EC.presence_of_element_located((By.XPATH, signin_xpath)))
        signin_button.click()

        # Check driver in Sign-In page
        assert "Đăng nhập | Tinhte.vn" in driver.title

        # Choose login with google

        google_signin_button = WebDriverWait(driver, delay).until(
            EC.presence_of_element_located((By.XPATH, google_login_button_xpath)))
        google_signin_button.click()

        current_window = driver.window_handles[0]
        google_login_window = driver.window_handles[1]

        driver.switch_to_window(google_login_window)

        # Fill Google account information
        email_input = WebDriverWait(driver, delay).until(
            EC.presence_of_element_located((By.XPATH, email_input_xpath)))
        email_input.send_keys(email)
        user_continue_button = driver.find_element_by_xpath(
            username_continue_button_xpath)
        user_continue_button.click()

        time.sleep(2)

        password_input = WebDriverWait(driver, delay).until(
            EC.presence_of_element_located((By.XPATH, passowrd_input_xpath)))
        password_input.send_keys(password)
        password_button = driver.find_element_by_xpath(
            password_continue_button_xpath)
        password_button.click()

        # Switch back
        driver.switch_to_window(current_window)

        time.sleep(4)

        assert "Cộng đồng Khoa học & Công nghệ | Tinh tế" in driver.title

    except TimeoutException:
        raise TimeoutException("Loading took too much!")


def test_login_fail_with_invalid_username():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    signin_xpath = '//a[@href="https://tinhte.vn/login/"]'
    username_input_xpath = '//input[@id="ctrl_pageLogin_login" and @class="textCtrl"]'
    password_input_xpath = '//input[@id="ctrl_pageLogin_password" and @class="textCtrl"]'
    signin_button_xpath = '//*[@id="pageLogin"]/dl[3]/dd/input'
    username = "nguyen_thi_dau__"
    password = "Hung8787"
    delay = 3

    driver.get(TINHTE_HOMEPAGE)
    try:

        # Wait for Sign-In button appears
        signin_button = WebDriverWait(driver, delay).until(
            EC.presence_of_element_located((By.XPATH, signin_xpath)))
        signin_button.click()

        # Check driver in Sign-In page
        assert "Đăng nhập | Tinhte.vn" in driver.title

        # Fill information

        username_input = WebDriverWait(driver, delay).until(
            EC.presence_of_element_located((By.XPATH, username_input_xpath)))
        password_input = WebDriverWait(driver, delay).until(
            EC.element_to_be_clickable((By.XPATH, password_input_xpath)))
        username_input.send_keys(username)
        password_input.send_keys(password)

        # Click sign-in button
        signin_button_xpath = driver.find_element_by_xpath(signin_button_xpath)
        signin_button_xpath.click()

        # Back to homepage
        assert "The requested user 'nguyen_thi_dau__' could not be found." in driver.page_source

    except TimeoutException:
        raise TimeoutException("Loading took too much!")


def test_login_fail_with_invalid_password():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    signin_xpath = '//a[@href="https://tinhte.vn/login/"]'
    username_input_xpath = '//input[@id="ctrl_pageLogin_login" and @class="textCtrl"]'
    password_input_xpath = '//input[@id="ctrl_pageLogin_password" and @class="textCtrl"]'
    signin_button_xpath = '//*[@id="pageLogin"]/dl[3]/dd/input'
    username = "nguyen_thi_dau"
    password = "Hung878787"
    delay = 3

    driver.get(TINHTE_HOMEPAGE)
    try:

        # Wait for Sign-In button appears
        signin_button = WebDriverWait(driver, delay).until(
            EC.presence_of_element_located((By.XPATH, signin_xpath)))
        signin_button.click()

        # Check driver in Sign-In page
        assert "Đăng nhập | Tinhte.vn" in driver.title

        # Fill information

        username_input = WebDriverWait(driver, delay).until(
            EC.presence_of_element_located((By.XPATH, username_input_xpath)))
        password_input = WebDriverWait(driver, delay).until(
            EC.element_to_be_clickable((By.XPATH, password_input_xpath)))
        username_input.send_keys(username)
        password_input.send_keys(password)

        # Click sign-in button
        signin_button_xpath = driver.find_element_by_xpath(signin_button_xpath)
        signin_button_xpath.click()

        # Back to homepage
        assert "Nhập sai mật khẩu. Vui lòng thử lại." in driver.page_source

    except TimeoutException:
        raise TimeoutException("Loading took too much!")
