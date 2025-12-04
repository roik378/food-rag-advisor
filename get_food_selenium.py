from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options  # <--- 引入 Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# 1. 配置隐身选项
options = Options()
# 关键参数：移除“受到自动化控制”的标记
options.add_argument('--disable-blink-features=AutomationControlled')
# 伪装 User-Agent (虽然之前设过，但在 Selenium 里最好直接写在 Options 里)
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36')

# 可选：有些检测机制会看窗口大小，全屏通常更像真人
options.add_argument("--start-maximized") 

# 2. 启动浏览器 (把 options 传进去)
print("正在启动加装了隐身衣的浏览器...")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

try:
    # 3. 再次尝试访问
    url = "https://www.dianping.com/shenzhen/ch10/r1949"
    print(f"正在打开网页: {url}")
    driver.get(url)

    # 4. 人工干预时间
    print("\n" + "="*40)
    print("👉 请观察浏览器：")
    print("1. 如果还在报错，说明对方防御很高。")
    print("2. 如果出现了验证码，请手动完成验证。")
    input("🔴 无论结果如何，观察完后按 [回车键] 回到这里...") 
    print("="*40 + "\n")

    print(f"当前标题: {driver.title}")

except Exception as e:
    print(f"发生错误: {e}")

finally:
    # driver.quit() 
    print("脚本结束。")