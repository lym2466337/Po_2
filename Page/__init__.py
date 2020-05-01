from selenium.webdriver.common.by import By

# 搜索功能

search_btn = (By.ID, "com.android.settings:id/search")
search_input = (By.ID, "android:id/search_src_text")
search_back = (By.CLASS_NAME, "android.widget.ImageButton")


#xpath 特别处理
x1= (By.XPATH,"text,设置")  #-->拼接成contains的 xpath语句
x2= (By.XPATH,"text,设置，1") #-->拼接成contains的 xpath语句
x3= (By.XPATH,"text,设置，0")  #-->拼接成不含contains，但按照text进行精确定位的 xpath语句
x4= (By.XPATH,["text,设置，0","text,设置，1"])  # 2条条件同时满足的xpath语句
