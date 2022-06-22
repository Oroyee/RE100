from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

opt = Options()
opt.page_load_strategy = "eager"
opt.add_experimental_option("debuggerAddress", "localhost:9222")
driver = webdriver.Chrome(options=opt)

driver.get("https://www.there100.org/re100-members?items_per_page=All")
    
def get_all_data():
    # get number of rows
    noOfRows = len(driver.find_elements_by_xpath("/html/body/div[2]/div/main/div/article/div[2]/div[1]/div/div[1]/div[4]/div/div/div/table/tbody/tr"))
    # get number of columns
    noOfColumns = len(driver.find_elements_by_xpath("/html/body/div[2]/div/main/div/article/div[2]/div[1]/div/div[1]/div[4]/div/div/div/table/tbody/tr[3]/td"))
    allData = []
    # iterate over the rows, to ignore the headers we have started the i with '1'
    for i in range(1, noOfRows , 2):
        # reset the row data every time
        ro = []
        ro.append(driver.find_element_by_xpath("/html/body/div[2]/div/main/div/article/div[2]/div[1]/div/div[1]/div[4]/div/div/div/table/tbody/tr["+str(i)+"]/td[1]/a/div/div[2]").text)
        ro.append("\t")
        # iterate over columns
        for j in range(3, noOfColumns+1) :
            # get text from the i th row and j th column
            # ro.append(self.table.find_element_by_xpath("//tr["+str(i)+"]/td["+str(j)+"]").text)
            ro.append(driver.find_element_by_xpath("/html/body/div[2]/div/main/div/article/div[2]/div[1]/div/div[1]/div[4]/div/div/div/table/tbody/tr["+str(i)+"]/td["+str(j)+"]").text)
            ro.append("\t")

        # add the row data to allData of the self.table
        ro.append("\n")
        allData.append(ro)
    with open(r'RE100.txt','w')as fp:
        for item in allData:
            for i in item:
                fp.write(i)
        print("done") 
    return allData


print("All table data : ", get_all_data())