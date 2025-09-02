from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

keyword = '阮梅'
url = f'https://s.weibo.com/weibo/{keyword}?topnav=1&wvr=6&b=1'

# 使用Chrome浏览器
driver = webdriver.Chrome()
driver.get(url)

# 等待搜索结果加载完成
time.sleep(5)

# 模拟向下滚动，加载更多评论
body = driver.find_element('tag name', 'body')
for _ in range(1):
    body.send_keys(Keys.END)
    time.sleep(8)

# 获取所有评论元素
comment_elements = driver.find_elements('css selector', '.txt')

# 提取评论文本并写入文件
with open('春晚.txt', 'w', encoding='utf-8') as f:
    for comment_element in comment_elements:
        comment_text = comment_element.text.strip()
        if len(comment_text) > 0:
            f.write(comment_text + '\n')
            
# 关闭浏览器
driver.quit()
