import pandas as pd

try:
    # 1. 读取 CSV 文件
    # encoding='utf-8' 是为了防止中文乱码
    df = pd.read_csv('restaurants.csv', encoding='utf-8')
    
    print("🎉 成功加载数据！")
    print("="*30)
    
    # 2. 看看数据包含哪些列
    print(f"包含的列名: {df.columns.tolist()}")
    
    print("="*30)
    # 3. 打印前 3 行看看长什么样 (head 代表头部)
    print("前 3 行数据预览：")
    print(df.head(3))

except Exception as e:
    print(f"❌ 读取出错: {e}")