import requests
import json

# 设置API访问凭证
access_token = '2.00sjVpbI0XVq3S83e365f194aCrVYE'

# 设置要搜索的关键词
keyword = input("请输入搜索关键词：")

# 设置要爬取的微博数量
count = input("输入要取的微博数量：")

# 发起API请求进行搜索
url = f'https://api.weibo.com/2/statuses/user_timeline.json?access_token={access_token}&count={count}'
response = requests.get(url)
data = json.loads(response.text)

# 检查是否存在微博数据
if 'statuses' in data:
    statuses = data['statuses']

    # 打印微博内容
    for status in statuses:
        print("用户ID:", status['id'])
        print("微博内容:", status['text'])
        print("---")

    # 保存微博数据到文件
    output_file = 'weibo_data.txt'
    with open(output_file, 'w', encoding='utf-8') as file:
        for status in statuses:
            file.write(f"用户ID: {status['user']['id']}\n")
            file.write(f"用户名: {status['user']['screen_name']}\n")
            file.write(f"微博内容: {status['text']}\n")
            file.write("---\n")

    print("微博数据已保存到文件:", output_file)
else:
    print("未找到微博数据，请检查关键词和数量的设置。")
print(data)