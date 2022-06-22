encoding="utf_8_sig"
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
# from currency_converter import CurrencyConverter 
import time

opt = Options()
opt.page_load_strategy = "eager"
opt.add_experimental_option("debuggerAddress", "localhost:9222")
driver = webdriver.Chrome(options=opt)

my_file = open("company_2.txt", "r", encoding="utf-8")
content_list = my_file.readlines()
print(content_list)

# open("RE100.txt", "w", encoding="utf-8")

# c = CurrencyConverter

def scrawler(company):
    allData = []
    ro = []
    # WebDriverWait(driver, 20).until(
    # EC.element_to_be_clickable((By.XPATH, "/html/body/c-wiz/div/div[4]/div/div/main/div[2]/div[1]/c-wiz/div/table/tr[2]/td[2]")))
    if driver.find_elements_by_xpath('/html/body/c-wiz/div/div[4]/div/div/main/div[2]/div[1]/c-wiz/div/table/tr[2]/td[2]'):
        ActionChains(driver).move_to_element(driver.find_element_by_xpath('/html/body/c-wiz/div/div[4]/div/div/main/div[2]/div[1]/c-wiz/div/table/tr[2]/td[2]')).perform()
        element = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/c-wiz/div/div[4]/div/div/main/div[2]/div[1]/c-wiz/div/div[1]/div/span[2]/div/button/div[3]")))
        driver.find_element_by_xpath("/html/body/c-wiz/div/div[4]/div/div/main/div[2]/div[1]/c-wiz/div/div[1]/div/span[2]").click()
        # CompanyName
        ro.append(driver.find_element_by_xpath("/html/body/c-wiz[2]/div/div[4]/div/div/main/div[1]/div[1]/div[2]").text)
        ro.append("\t")
        
        if driver.find_elements_by_xpath("//*[contains(text(), 'Founded')]//following-sibling::div"):
            ro.append(driver.find_element_by_xpath("//*[contains(text(), 'Founded')]//following-sibling::div").text)
            ro.append("\t")
        else:
            ro.append("\tempty\t")
        if driver.find_elements_by_xpath("//*[contains(text(), 'Headquarters')]//following-sibling::div"):
            Headquarters = driver.find_element_by_xpath("//*[contains(text(), 'Headquarters')]//following-sibling::div").text
        # ro.append(driver.find_element_by_xpath("//*[contains(text(), 'Headquarters')]//following-sibling::div").text)
            ro.append(str(Headquarters).replace("\n"," \ "))
            ro.append("\t")
        else:
            ro.append("\tempty\t")
        if driver.find_elements_by_xpath("//*[contains(text(), 'Employees')]//following-sibling::div"):
            ro.append(driver.find_element_by_xpath("//*[contains(text(), 'Employees')]//following-sibling::div").text)
            ro.append("\t")
        else:
            ro.append("\tempty\t")
        # Currency
        currency = driver.find_element_by_xpath("/html/body/c-wiz[2]/div/div[4]/div/div/main/div[2]/div[1]/c-wiz/div/table/tr[1]/th[1]").text
        ro.append(currency)
        ro.append("\t")
        if driver.find_elements_by_xpath("/html/body/c-wiz/div/div[4]/div/div/main/div[2]/div[1]/c-wiz/div/div[3]/div[5]"):
            year_1 = driver.find_element_by_xpath("/html/body/c-wiz[2]/div/div[4]/div/div/main/div[2]/div[1]/c-wiz/div/div[3]/div[5]/div/button/span").text
            if year_1 == "2018":
                ro.append("\tempty\t")
        if driver.find_elements_by_xpath("/html/body/c-wiz/div/div[4]/div/div/main/div[2]/div[1]/c-wiz/div/div[3]/div[1]"):
            year_5 = driver.find_element_by_xpath("/html/body/c-wiz[2]/div/div[4]/div/div/main/div[2]/div[1]/c-wiz/div/div[3]/div[1]/div/button/span").text
        
        for a in range(5,0,-1):
            if driver.find_elements_by_xpath("/html/body/c-wiz/div/div[4]/div/div/main/div[2]/div[1]/c-wiz/div/div[3]/div["+str(a)+"]"):
                driver.find_element_by_xpath("/html/body/c-wiz/div/div[4]/div/div/main/div[2]/div[1]/c-wiz/div/div[3]/div["+str(a)+"]").click()
                
                ro.append(driver.find_element_by_xpath("/html/body/c-wiz/div/div[4]/div/div/main/div[2]/div[1]/c-wiz/div/table/tr[2]/td[2]").text)
                ro.append("\t")
                ro.append(driver.find_element_by_xpath("/html/body/c-wiz/div/div[4]/div/div/main/div[2]/div[1]/c-wiz/div/table/tr[3]/td[2]").text)
                ro.append("\t")
            else:
                ro.append("\tempty\t")
        if year_5 == "2021":
            ro.append("\tempty\t")
        # add the row data to allData of the self.table
        ro.append("\n")
        allData.append(ro)
        print(allData)
        with open(r'RE100.txt','a', encoding="utf-8")as fp:
            for item in allData:
                fp.write(str(company).replace("\n"," "))
                fp.write("\t")
                for i in item:
                    fp.write(i)
            print("done")
    else:
        # CompanyName
        ro.append(driver.find_element_by_xpath("/html/body/c-wiz[2]/div/div[4]/div/div/main/div[1]/div[1]/div[2]").text)
        ro.append("\t")

        if driver.find_elements_by_xpath("//*[contains(text(), 'Founded')]//following-sibling::div"):
            ActionChains(driver).move_to_element(driver.find_element_by_xpath("//*[contains(text(), 'Founded')]//following-sibling::div")).perform()
            ro.append(driver.find_element_by_xpath("//*[contains(text(), 'Founded')]//following-sibling::div").text)
            ro.append("\t")
        else:
            ro.append("\tempty\t")
        if driver.find_elements_by_xpath("//*[contains(text(), 'Headquarters')]//following-sibling::div"):
            ActionChains(driver).move_to_element(driver.find_element_by_xpath("//*[contains(text(), 'Headquarters')]//following-sibling::div")).perform()
            Headquarters = driver.find_element_by_xpath("//*[contains(text(), 'Headquarters')]//following-sibling::div").text
        # ro.append(driver.find_element_by_xpath("//*[contains(text(), 'Headquarters')]//following-sibling::div").text)
            ro.append(str(Headquarters).replace("\n"," \ "))
            ro.append("\t")
        else:
            ro.append("\tempty\t")
        if driver.find_elements_by_xpath("//*[contains(text(), 'Employees')]//following-sibling::div"):
            ActionChains(driver).move_to_element(driver.find_element_by_xpath("//*[contains(text(), 'Employees')]//following-sibling::div")).perform()
            ro.append(driver.find_element_by_xpath("//*[contains(text(), 'Employees')]//following-sibling::div").text)
            ro.append("\t")
        else:
            ro.append("\tempty\t")
        ro.append("\n")
        allData.append(ro)
        print(allData)
        with open(r'RE100.txt','a', encoding="utf-8")as fp:
            for item in allData:
                fp.write(str(company).replace("\n"," "))
                fp.write("\t")
                for i in item:
                    fp.write(i)
            print("done")

for company in content_list:
    driver.get("https://www.google.com/finance")
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/c-wiz/div/div[3]/div[3]/div/div/div/div[1]/input[2]")))
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/c-wiz/div/div[3]/div[3]/div/div/div/div[1]/input[2]").send_keys(company)
    driver.find_element_by_xpath("/html/body/c-wiz/div/div[3]/div[3]/div/div/div/div[1]/input[2]").send_keys(Keys.ENTER)
    time.sleep(4)
    current_url = driver.current_url
    if current_url == "https://www.google.com/finance/":
        with open(r'RE100.txt','a', encoding="utf-8")as fp:
            fp.write(str(company).replace("\n"," "))
            fp.write("\tempty\n")
            print("done")
        continue
    else:
        scrawler(company)