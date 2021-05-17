import pytest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from util.util import Util

TINHTE_HOMEPAGE = "https://tinhte.vn"


def test_register_success():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    util = Util(driver, 15)
    signin_xpath = '//a[@href="https://tinhte.vn/login/"]'
    radio_not_register_xpath = '//*[@id="ctrl_pageLogin_not_registered"]'
    register_button_xpath = '//*[@id="pageLogin"]/dl[3]/dd/input'
    input_name_xpath = '//*[contains(text(), "Tên:")]//ancestor::dl[@class="ctrlUnit"]/dd/input'
    input_email_xpath = '//*[@type="email"]//ancestor::dl[@class="ctrlUnit"]/dd/input'
    input_password_xpath = '//*[contains(text(), "Mật khẩu:")]//ancestor::dl[@class="ctrlUnit"]/dd/input'
    input_re_password_xpath = '//*[contains(text(), "Xác nhận mật khẩu:")]//ancestor::dl[@class="ctrlUnit"]/dd/input'
    day_of_birth_xpath = '//*[@id="helper_birthday"]/li[1]/select'
    month_of_birth_xpath = '//*[@id="helper_birthday"]/li[2]/input'
    year_of_birth_xpath = '//*[@id="helper_birthday"]/li[3]/input'
    policy_agree_button_xpath = '//*[@id="ctrl_agree"]'
    register_submit_button_xpath = '//*[@id="SubmitButton"]'

    name = "nguyen_thi_dau"
    email = "softwaretestingbk2021@gmail.com"
    password = "Hung8787"
    day_of_birth = "Tháng 9"
    month_of_birth = "04"
    year_of_birth = "1999"

    driver.get(TINHTE_HOMEPAGE)
    try:

        # Wait for Sign-In button appears
        signin_button = util.find_element_by_xpath(signin_xpath)
        signin_button.click()

        # Check driver in Sign-In page
        assert "Đăng nhập | Tinhte.vn" in driver.title

        # Fill information

        radio_not_register = util.find_element_by_xpath(
            radio_not_register_xpath)
        register_button = util.find_element_by_xpath(register_button_xpath)
        radio_not_register.click()
        register_button.click()

        # Fill information
        input_name = util.find_element_by_xpath(input_name_xpath)
        input_email = util.find_element_by_xpath(input_email_xpath)
        input_password = util.find_element_by_xpath(input_password_xpath)
        input_re_password = util.find_element_by_xpath(input_re_password_xpath)
        select_day_of_birth = Select(
            util.find_element_by_xpath(day_of_birth_xpath))
        input_month_of_birth = util.find_element_by_xpath(month_of_birth_xpath)
        input_year_of_birth = util.find_element_by_xpath(year_of_birth_xpath)
        # WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it(
        #     (By.CSS_SELECTOR, "iframe[name^='a-'][src^='https://www.google.com/recaptcha/api2/anchor?']")))
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//span[@id='recaptcha-anchor']"))).click()
        policy_agree_button = util.find_element_by_xpath(
            policy_agree_button_xpath)
        register_submit_button = util.find_element_by_xpath(
            register_submit_button_xpath)

        input_name.send_keys(name)
        input_email.send_keys(email)
        input_password.send_keys(password)
        input_re_password.send_keys(password)
        select_day_of_birth.select_by_visible_text(day_of_birth)
        input_month_of_birth.send_keys(month_of_birth)
        input_year_of_birth.send_keys(year_of_birth)

        time.sleep(3.8)
        recaptcha_button.click()
        policy_agree_button.click()
        register_submit_button.click()

        # Back to homepage
        assert "Cộng đồng Khoa học & Công nghệ | Tinh tế" in driver.title

    except TimeoutException:
        raise TimeoutException("Loading took too much!")

    driver.quit()


def test_register_fail_miss_input_birthday():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    util = Util(driver, 15)
    signin_xpath = '//a[@href="https://tinhte.vn/login/"]'
    radio_not_register_xpath = '//*[@id="ctrl_pageLogin_not_registered"]'
    register_button_xpath = '//*[@id="pageLogin"]/dl[3]/dd/input'
    input_name_xpath = '//*[contains(text(), "Tên:")]//ancestor::dl[@class="ctrlUnit"]/dd/input'
    input_email_xpath = '//*[@type="email"]//ancestor::dl[@class="ctrlUnit"]/dd/input'
    input_password_xpath = '//*[contains(text(), "Mật khẩu:")]//ancestor::dl[@class="ctrlUnit"]/dd/input'
    input_re_password_xpath = '//*[contains(text(), "Xác nhận mật khẩu:")]//ancestor::dl[@class="ctrlUnit"]/dd/input'
    policy_agree_button_xpath = '//*[@id="ctrl_agree"]'
    register_submit_button_xpath = '//*[@id="SubmitButton"]'

    name = "nguyen_thi_dau"
    email = "softwaretestingbk2021@gmail.com"
    password = "Hung8787"

    driver.get(TINHTE_HOMEPAGE)
    try:

        # Wait for Sign-In button appears
        signin_button = util.find_element_by_xpath(signin_xpath)
        signin_button.click()

        # Check driver in Sign-In page
        assert "Đăng nhập | Tinhte.vn" in driver.title

        # Fill information

        radio_not_register = util.find_element_by_xpath(
            radio_not_register_xpath)
        register_button = util.find_element_by_xpath(register_button_xpath)
        radio_not_register.click()
        register_button.click()

        # Fill information
        input_name = util.find_element_by_xpath(input_name_xpath)
        input_email = util.find_element_by_xpath(input_email_xpath)
        input_password = util.find_element_by_xpath(input_password_xpath)
        input_re_password = util.find_element_by_xpath(input_re_password_xpath)
        # WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it(
        #     (By.CSS_SELECTOR, "iframe[name^='a-'][src^='https://www.google.com/recaptcha/api2/anchor?']")))
        # recaptcha_button = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//span[@id='recaptcha-anchor']")))
        policy_agree_button = util.find_element_by_xpath(
            policy_agree_button_xpath)
        register_submit_button = util.find_element_by_xpath(
            register_submit_button_xpath)

        input_name.send_keys(name)
        input_email.send_keys(email)
        input_password.send_keys(password)
        input_re_password.send_keys(password)
        # time.sleep(3.8)
        # recaptcha_button.click()
        policy_agree_button.click()

        time.sleep(11)

        register_submit_button.click()

        time.sleep(1)

        # Back to homepage
        assert "Please enter a valid date of birth." in driver.page_source

    except TimeoutException:
        raise TimeoutException("Loading took too much!")

    driver.quit()


def test_register_fail_miss_tick_robot():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    util = Util(driver, 15)
    signin_xpath = '//a[@href="https://tinhte.vn/login/"]'
    radio_not_register_xpath = '//*[@id="ctrl_pageLogin_not_registered"]'
    register_button_xpath = '//*[@id="pageLogin"]/dl[3]/dd/input'
    input_name_xpath = '//*[contains(text(), "Tên:")]//ancestor::dl[@class="ctrlUnit"]/dd/input'
    input_email_xpath = '//*[@type="email"]//ancestor::dl[@class="ctrlUnit"]/dd/input'
    input_password_xpath = '//*[contains(text(), "Mật khẩu:")]//ancestor::dl[@class="ctrlUnit"]/dd/input'
    input_re_password_xpath = '//*[contains(text(), "Xác nhận mật khẩu:")]//ancestor::dl[@class="ctrlUnit"]/dd/input'
    day_of_birth_xpath = '//*[@id="helper_birthday"]/li[1]/select'
    month_of_birth_xpath = '//*[@id="helper_birthday"]/li[2]/input'
    year_of_birth_xpath = '//*[@id="helper_birthday"]/li[3]/input'
    policy_agree_button_xpath = '//*[@id="ctrl_agree"]'
    register_submit_button_xpath = '//*[@id="SubmitButton"]'

    name = "nguyen_thi_dau"
    email = "softwaretestingbk2021@gmail.com"
    password = "Hung8787"
    day_of_birth = "Tháng 9"
    month_of_birth = "04"
    year_of_birth = "1999"

    driver.get(TINHTE_HOMEPAGE)
    try:

        # Wait for Sign-In button appears
        signin_button = util.find_element_by_xpath(signin_xpath)
        signin_button.click()

        # Check driver in Sign-In page
        assert "Đăng nhập | Tinhte.vn" in driver.title

        # Fill information

        radio_not_register = util.find_element_by_xpath(
            radio_not_register_xpath)
        register_button = util.find_element_by_xpath(register_button_xpath)
        radio_not_register.click()
        register_button.click()

        # Fill information
        input_name = util.find_element_by_xpath(input_name_xpath)
        input_email = util.find_element_by_xpath(input_email_xpath)
        input_password = util.find_element_by_xpath(input_password_xpath)
        input_re_password = util.find_element_by_xpath(input_re_password_xpath)
        select_day_of_birth = Select(
            util.find_element_by_xpath(day_of_birth_xpath))
        input_month_of_birth = util.find_element_by_xpath(month_of_birth_xpath)
        input_year_of_birth = util.find_element_by_xpath(year_of_birth_xpath)
        policy_agree_button = util.find_element_by_xpath(
            policy_agree_button_xpath)
        register_submit_button = util.find_element_by_xpath(
            register_submit_button_xpath)

        input_name.send_keys(name)
        input_email.send_keys(email)
        input_password.send_keys(password)
        input_re_password.send_keys(password)
        select_day_of_birth.select_by_visible_text(day_of_birth)
        input_month_of_birth.send_keys(month_of_birth)
        input_year_of_birth.send_keys(year_of_birth)

        policy_agree_button.click()

        time.sleep(11)

        register_submit_button.click()

        time.sleep(1)

        # Back to homepage
        assert "You did not complete the CAPTCHA verification properly. Please try again." in driver.page_source

    except TimeoutException:
        raise TimeoutException("Loading took too much!")

    driver.quit()


def test_register_fail_miss_tick_policy():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    util = Util(driver, 15)
    signin_xpath = '//a[@href="https://tinhte.vn/login/"]'
    radio_not_register_xpath = '//*[@id="ctrl_pageLogin_not_registered"]'
    register_button_xpath = '//*[@id="pageLogin"]/dl[3]/dd/input'
    input_name_xpath = '//*[contains(text(), "Tên:")]//ancestor::dl[@class="ctrlUnit"]/dd/input'
    input_email_xpath = '//*[@type="email"]//ancestor::dl[@class="ctrlUnit"]/dd/input'
    input_password_xpath = '//*[contains(text(), "Mật khẩu:")]//ancestor::dl[@class="ctrlUnit"]/dd/input'
    input_re_password_xpath = '//*[contains(text(), "Xác nhận mật khẩu:")]//ancestor::dl[@class="ctrlUnit"]/dd/input'
    day_of_birth_xpath = '//*[@id="helper_birthday"]/li[1]/select'
    month_of_birth_xpath = '//*[@id="helper_birthday"]/li[2]/input'
    year_of_birth_xpath = '//*[@id="helper_birthday"]/li[3]/input'
    policy_agree_button_xpath = '//*[@id="ctrl_agree"]'
    register_submit_button_xpath = '//*[@id="SubmitButton"]'

    name = "nguyen_thi_dau"
    email = "softwaretestingbk2021@gmail.com"
    password = "Hung8787"
    day_of_birth = "Tháng 9"
    month_of_birth = "04"
    year_of_birth = "1999"

    driver.get(TINHTE_HOMEPAGE)
    try:

        # Wait for Sign-In button appears
        signin_button = util.find_element_by_xpath(signin_xpath)
        signin_button.click()

        # Check driver in Sign-In page
        assert "Đăng nhập | Tinhte.vn" in driver.title

        # Fill information

        radio_not_register = util.find_element_by_xpath(
            radio_not_register_xpath)
        register_button = util.find_element_by_xpath(register_button_xpath)
        radio_not_register.click()
        register_button.click()

        # Fill information
        input_name = util.find_element_by_xpath(input_name_xpath)
        input_email = util.find_element_by_xpath(input_email_xpath)
        input_password = util.find_element_by_xpath(input_password_xpath)
        input_re_password = util.find_element_by_xpath(input_re_password_xpath)
        select_day_of_birth = Select(
            util.find_element_by_xpath(day_of_birth_xpath))
        input_month_of_birth = util.find_element_by_xpath(month_of_birth_xpath)
        input_year_of_birth = util.find_element_by_xpath(year_of_birth_xpath)
        policy_agree_button = util.find_element_by_xpath(
            policy_agree_button_xpath)
        register_submit_button = util.find_element_by_xpath(
            register_submit_button_xpath)

        input_name.send_keys(name)
        input_email.send_keys(email)
        input_password.send_keys(password)
        input_re_password.send_keys(password)
        select_day_of_birth.select_by_visible_text(day_of_birth)
        input_month_of_birth.send_keys(month_of_birth)
        input_year_of_birth.send_keys(year_of_birth)

        register_class_names = register_submit_button.get_attribute("class")

        # Back to homepage
        assert "disabled" in register_class_names

    except TimeoutException:
        raise TimeoutException("Loading took too much!")

    driver.quit()
