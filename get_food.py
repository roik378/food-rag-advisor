import requests
from bs4 import BeautifulSoup  # <--- 新增：引入翻译官

url = "https://www.dianping.com/shenzhen/ch10/r1949"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

try:
    print("正在尝试访问...")
    response = requests.get(url, headers=headers)
    
    print(f"状态码: {response.status_code}")
    
    if response.status_code == 200:
        # --- 新增部分开始 ---
        # 1. 把源码交给 BeautifulSoup 解析
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 2. 提取 <title> 标签的内容
        if soup.title:
            print(f"网页标题: {soup.title.string}")
        else:
            print("警告: 没有找到网页标题，可能被反爬虫拦截了。")
            
        # 3. 看看有没有我们要找的关键字（比如 '美食'）
        if "美食" in response.text:
            print("成功检测到 '美食' 关键字！")
        else:
            print("未检测到 '美食' 关键字，可能内容不对。")
        # --- 新增部分结束 ---
            
    else:
        print("访问被拒绝。")

except Exception as e:
    print(f"发生错误: {e}")