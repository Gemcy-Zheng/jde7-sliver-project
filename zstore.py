import pandas as pd
import time
from random import randint
import datetime
# 載入selenium相關模組
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By # By是selenium裏面的一個類別。
from selenium.webdriver.chrome.options import Options
#建立Driver物件實體，用程式操作瀏覽器運作
driver = webdriver.Chrome()

#要爬的網址
# url = "https://www.ztore.com/tc/category/all/diapers-and-pants/diapers"
# url = "https://www.ztore.com/tc/category/all/diapers-and-pants/pants"
# url = "https://www.ztore.com/tc/category/all/diapers-and-pants/case-offer"
# url = "https://www.ztore.com/tc/category/all/mama-care/maternity-pad-waistband"
# url = "https://www.ztore.com/tc/category/all/baby-care/baby-skincare"
url = "https://www.ztore.com/tc/category/all/mama-care/body-care"
# url = "https://www.ztore.com/tc/category/all/milk-formula-food/formula-1"
# url = "https://www.ztore.com/tc/category/all/milk-formula-food/formula-2"
# url = "https://www.ztore.com/tc/category/all/milk-formula-food/formula-3"
# url = "https://www.ztore.com/tc/category/all/milk-formula-food/formula-4"
# url = "https://www.ztore.com/tc/category/all/milk-formula-food/food/healthy-snacks"

# 如果想要在vs code這裏看網頁的原始碼，則
# print(driver.page_source) #取得網頁的原始碼 

try:
    driver.get(url) #找到網址
except:
    print('url not found') #找不到退出
    exit

# time.sleep(10) # 如果找到不要秒退，停留10秒鐘
# target_num_result = 100 # our target product message is 100
#below code is remove the advertising
try:
    adv_button1= driver.find_element(By.XPATH, '//button[@type="button"]')
    adv_button1.click()
except:
    pass

product_title = []  #  ---***DONE***---
vendor_name = []  #  ---***DONE***---
regular_price = []  #  ---***DONE***---
sale_price = []  #  ---***DONE***---
promotion = []  #  ---***DONE***---  
product_in_stock = []   #  ---***DONE***--- 
product_out_stock = []   #  ---***DONE***--- 
# product_page = []
product_image = []  #  ---***DONE***---
every_product_url=[]  #  ---***DONE***---
product_urls = []  #  ---***DONE***---
product_original =[]  #  ---***DONE***---
comment_star = []  #  ---***DONE***---
# product_comments = []  #  ---***DONE***---
sources = []  #  ---***DONE***---
categories = []  #  ---***DONE***---
comment_quantity = []  #  ---***DONE***---


safe_brake = 10 #optional
count = 0 # optional
target_num_result = 300 #我們的目標是要列出300個產品信息


result01_list = driver.find_elements(By.XPATH, '//div[@class="jsx-4061644943 ProductList root"]')
for result in result01_list:
    print(result)
num_of_result = len(result01_list) #使用len來數result01_list裏面有多少個產品
count += 1 #optional

#below code is download all product in every page
try:
    while(num_of_result < target_num_result):
        show_more_results_button = driver.find_element(By.XPATH, '//div[@class="viewAllButton"]')
        show_more_results_button.click()
        time.sleep(5)
except: 
    pass

#***** 只是測試使用****
# try:
#     show_more_results_button = driver.find_element(By.XPATH, '//div[@class="viewAllButton"]')
#     show_more_results_button.click()
# except:
#     pass
#***** 只是測試使用****

#get every product url for loop
product_elements = driver.find_elements(By.XPATH, '//div[@class="jsx-2014215213 jsx-1363614283 label-ctnr"]')
for product in product_elements:
    a_page_urls = product.find_elements(By.TAG_NAME, 'a')
    if len(a_page_urls) > 0:
        per_product_url = a_page_urls[0].get_attribute('href')  #[0]是因爲提取出來的每個產品有有1~3個url，是同一個list裏面。我要提取每個list裏面的index[0]
        if per_product_url not in product_urls:   #為了檢測沒有重複的url
            product_urls.append(per_product_url)
# print(product_urls)
# print(len(product_urls))

# #*****這個循環不用打開，否則會一直循環進入每一個產品主頁****
# # for url in product_urls:
# #     driver.get(url)
# #     time.sleep(5)
# #*****這個循環不用打開，否則會一直循環進入每一個產品主頁****

#get every product url for dataframe
product_elements1 = driver.find_elements(By.XPATH, '//div[@class="jsx-2014215213 jsx-1363614283 ProductItem  windowing-layout  "]')
for product1 in product_elements1:
    a_page_urls1 = product1.find_elements(By.TAG_NAME, 'a')
    if len(a_page_urls1) > 0:
        per_product_url1 = a_page_urls1[0].get_attribute('href')  #[0]是因爲提取出來的每個產品有有1~3個url，是同一個list裏面。我要提取每個list裏面的index[0]
        if per_product_url1 not in every_product_url:   #為了檢測沒有重複的url
            every_product_url.append(per_product_url1)
# print(len(every_product_url))
# print(every_product_url) 

for page in range(0,len(product_urls)):
    # print('第 '+ str(page) + ' 個商品')
    # 儲存網址
    product_urls.append(product_urls[page])
    # print(per_product_url)

    # #去到你想要的網頁
    driver.get(product_urls[page])
    time.sleep(5) #意思是，在執行到這行代碼時，程式會暫停執行並休眠一段隨機時間（範圍為 X秒之間），然後再繼續執行下一行代碼。

    try:
        adv_button2= driver.find_element(By.XPATH, '//div[@class="jsx-388599633 close-img"]')
        adv_button2.click()
    except:
        pass

    sources_name = 'ztore'
    sources.append(sources_name)

    # categories_name = 'maternity'
    # categories_name = 'formula'
    categories_name = 'skincare'
    # categories_name = 'snacks'
    # categories_name = 'diapers'
    # categories_name = 'post_partum_care'
    categories.append(categories_name)
   

    # find out product_title  ---***DONE***---
    product_titles = driver.find_elements(By.XPATH, '//h2[@class="jsx-1420873894"]')
    for product_name in product_titles: #for 裏面的名字不能跟[]重複
        title_text = product_name.text #將内容轉換成text，即係可顯示的資料。
        product_title.append(title_text) #這個步驟是把data放進product_title = []裏面        
    # print(len(product_title))
    # print(product_title)

    # find out vendor_name  ---***DONE***---
    vendor_names = driver.find_elements(By.XPATH, '//div[@class="jsx-1420873894 brand"]')
    for vendor in vendor_names: #for 裏面的名字不能跟[]重複
        vendor_name.append(vendor.text) #將内容轉換成text，即係可顯示的資料。再把data放進product_title = []裏面        
    # print(len(vendor_name))
    # print(vendor_name)

    # find out product_original  ---***DONE***---
    product_originals = driver.find_elements(By.XPATH, '//div[@class="jsx-1420873894 info-row-country"]')
    for p_original in product_originals: #for 裏面的名字不能跟[]重複
        product_original.append(p_original.text) #這個步驟是把data放進product_original = []裏面   
    # print(product_original)    
    # print(len(product_original))

    # find out sale_price  ---***DONE***---
    sale_prices = driver.find_elements(By.XPATH, '//div[@class="jsx-1420873894 price"]')
    for sale_price_list in sale_prices:
        try:
            sale_price.append(sale_price_list.find_element(By.XPATH, '//span[@class="jsx-1420873894 promotion"]').text.replace('$', ''))
        except:
            sale_price.append('null')
    # print(sale_price)
    # print(len(sale_price))

    # find out regular_price  ---***DONE***---
    if len(driver.find_elements(By.XPATH, '//div[@class="jsx-1420873894 price"]//span[@class="jsx-1420873894"]')) <= 0 :
        regular_price.append('null')
    else:
        if driver.find_element(By.XPATH, '//div[@class="jsx-1420873894 price"]//span[@class="jsx-1420873894"]').text == '': #通過觀察，顯示的是''，所以可以試試用''來做指定搜尋
            regular_price.append('null')
        else:
            regular_price.append(driver.find_element(By.XPATH, '//div[@class="jsx-1420873894 price"]//span[@class="jsx-1420873894"]').text.replace('$', ''))
    # print(regular_price)
    # print(len(regular_price))

    #find out product image  ---***DONE***---
    product_elements_ima =  driver.find_elements(By.XPATH, '//div[@class="jsx-3207502832 product-image-wrapper"]')
    # print("Number of product elements found:", len(product_elements_ima))       #可以用來檢測時候有找到提取的資料
    for product_im in product_elements_ima:
        product_im_image = product_im.find_elements(By.TAG_NAME, 'img')
        if len(product_im_image ) > 0:
            src = product_im_image[0].get_attribute('src')  #[0]是因爲提取出來的每個產品有有1~3個url，是同一個list裏面。我要提取每個list裏面的index[0]
            if src not in product_image:
                product_image.append(src)
    # print(product_image)
    # print(len(product_image))

    # find out promotion  ---***DONE***---          
    if len(driver.find_elements(By.XPATH, '//div[@class="jsx-1420873894 info-row-promotion-item"]')) <= 0 :
        promotion.append('null')
    else:
        if driver.find_element(By.XPATH, '//div[@class="jsx-1420873894 info-row-promotion-item"]').text == '': #通過觀察，顯示的是''，所以可以試試用''來做指定搜尋
            promotion.append('null')
        else:
            promotion.append(driver.find_element(By.XPATH, '//div[@class="jsx-1420873894 info-row-promotion-item"]').text.replace('+', '加'))
    # print(promotion)
    # print(len(promotion))

    # find out product_in_stock  ---***DONE***---          
    if len(driver.find_elements(By.XPATH, '//span[@class="jsx-2241259421"]')) <= 0 :
        product_in_stock.append('null')
    else:
        if driver.find_element(By.XPATH, '//span[@class="jsx-2241259421"]').text == '': #通過觀察，顯示的是''，所以可以試試用''來做指定搜尋
            product_in_stock.append('null')
        else:
            product_in_stock.append(driver.find_element(By.XPATH, '//span[@class="jsx-2241259421"]').text)
    # print(product_in_stock)
    # print(len(product_in_stock))

    # find out product_out_stock  ---***DONE***---          
    if len(driver.find_elements(By.XPATH, '//span[@class="jsx-863277391 jsx-2241259421"]')) <= 0 :
        product_out_stock.append('null')
    else:
        product_out_stock.append(driver.find_element(By.XPATH, '//span[@class="jsx-863277391 jsx-2241259421"]').text)
    # print(product_out_stock)
    # print(len(product_out_stock))

    # find out comment_star  ---***DONE***---          
    if len(driver.find_elements(By.XPATH, '//span[@class="jsx-1420873894 rating"]')) <= 0 :
        comment_star.append('null')
    else:
        if driver.find_element(By.XPATH, '//span[@class="jsx-1420873894 rating"]').text == '': #通過觀察，顯示的是''，所以可以試試用''來做指定搜尋
            comment_star.append('null')
        else:
            comment_star.append(driver.find_element(By.XPATH, '//span[@class="jsx-1420873894 rating"]').text)
    # print(comment_star)
    # print(len(comment_star))

    # find out comment_quantity  ---***DONE***---          
    if len(driver.find_elements(By.XPATH, '//span[@class="jsx-1420873894 rating-count"]')) <= 0 :
        comment_quantity.append('null')
    else:
        if driver.find_element(By.XPATH, '//span[@class="jsx-1420873894 rating-count"]').text == '': #通過觀察，顯示的是''，所以可以試試用''來做指定搜尋
            comment_quantity.append('null')
        else:
            comment_quantity.append(driver.find_element(By.XPATH, '//span[@class="jsx-1420873894 rating-count"]').text.replace('(', '').replace(')', '').replace('個評價', ''))
    # print(comment_quantity)
    # print(len(comment_quantity))

    # try:
    #     comments_button1= driver.find_element(By.XPATH, '//span[@class="MuiTouchRipple-root"]')
    #     comments_button1.click() #點擊產品評論的按鈕
    # except:
    #     pass

        # # find out comments  ---***DONE***--- 
        # comments = driver.find_elements(By.XPATH, '//div[@class="jsx-4188503936 ProductReview "]')
        # if len(comments) <= 0:
        #     product_comments.append('null')
        # else:
        #     for comment in comments: #div[@class="jsx-4188503936 ProductReview "]裏面是有很多div[@class="jsx-166288804 Review "]，for循環的目的是要令全部div[@class="jsx-166288804 Review "]的資料都顯示出來
        #         if comment.text == '':
        #             product_comments.append('null')
        #         else:
        #             product_comments.append(comment.text)
        # # print(product_comments)
        # # print(len(product_comments))

        # # find out comments ******這個要研究如何把一個list變成多個list。******
        # review= driver.find_element(By.XPATH, '//div[@id="review"]')
        # comments = review.find_elements(By.XPATH, '//div[@class="jsx-4188503936 ProductReview "]//div[@class="jsx-166288804 Review "]')
        # if len(comments) <= 0:
        #     product_comments.append(['null']) 
        # else:
        #     for comment in comments: #div[@class="jsx-4188503936 ProductReview "]裏面是有很多div[@class="jsx-166288804 Review "]，for循環的目的是要令全部div[@class="jsx-166288804 Review "]的資料都顯示出來
        #         if comment.text == '':
        #             product_comments.append(['null'])
        #         else:
        #             product_comments.append(comment.text)
        # print(product_comments)
        # print(len(product_comments))
        # # find out comments ******這個要研究如何把一個list變成多個list。******

# #         # Check if next page button exists   ****點擊下一頁提取下一頁評論未實驗成功***
# #         # next_page_buttons = driver.find_elements(By.XPATH, '//div[@class="jsx-4188503936 pagination text-center flex-center"]//button[@class="jsx-3501911408 NextBtn next button_styleSquare"]') #'
# #         # if len(next_page_buttons) > 0:
# #         #     # Click next page button
# #         #     next_page_button = next_page_buttons[0]
# #         #     next_page_button.click()
# #         # Check if next page button exists   ****點擊下一頁提取下一頁評論未實驗成功***


df = pd.DataFrame({
    'sources':sources,
    'categories':categories,
    'vendor_name':vendor_name,
    'categories':categories,
    'product_title':product_title, 
    'product_original':product_original,
    'regular_price':regular_price, 
    'sale_price':sale_price, 
    'promotion':promotion,
    'product_in_stock':product_in_stock, 
    'product_out_stock':product_out_stock,
    'comment_star':comment_star,
    'comment_quantity':comment_quantity,
    'product_image':product_image,
    'every_product_url':every_product_url})
print(df)

# 獲取當前日期和時間
current_datetime = datetime.datetime.now()

# 格式化日期和時間字符串
datetime_string = current_datetime.strftime("%Y%m%d_%H%M")

# file名字
file_name = f'ztore_{categories_name}_{datetime_string}.csv'

df.to_csv(
        file_name, # 檔案名稱
        encoding = 'utf-8-sig', # 編碼
        index=False # 是否保留index
        )





