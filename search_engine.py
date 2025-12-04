import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# ==========================================
# 1. 初始化阶段
# ==========================================
print("正在初始化系统，加载模型和数据...")

try:
    df = pd.read_csv('restaurants.csv', encoding='utf-8')
except Exception as e:
    print(f"❌ 错误: 找不到 restaurants.csv 文件。请确保文件在同一目录下。报错: {e}")
    exit()

model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')

# 预处理文本
df['combined_text'] = df.apply(
    lambda row: f"名称: {row['name']}; 类别: {row['category']}; 特色: {row['features']}; 描述: {row['description']}", 
    axis=1
)

print("正在生成向量索引...")
restaurant_vectors = model.encode(df['combined_text'].tolist())
print("✅ 系统初始化完成！\n" + "="*40)


# ==========================================
# 2. 核心功能函数 (被 ai_chef 调用)
# ==========================================

def search_food(query, top_k=3):
    """
    输入用户需求，返回推荐结果列表。
    注意：这里必须包含 ai_chef 需要的所有字段 (category, price)
    """
    # A. 向量化与计算
    query_vector = model.encode([query])
    scores = cosine_similarity(query_vector, restaurant_vectors)[0]
    top_indices = np.argsort(scores)[-top_k:][::-1]
    
    results = []
    print(f"\n🔍 你的需求: '{query}'")
    print("-" * 30)

    for idx in top_indices:
        score = scores[idx]
        row = df.iloc[idx]
        
        # 收集结果 (确保这里包含 category 和 price！)
        results.append({
            'name': row['name'],
            'category': row['category'],    # ✅ 必须有
            'features': row['features'],
            'description': row['description'],
            'price': float(row['price']),   # ✅ 必须有
            'score': float(score)
        })
        
        # 打印日志
        print(f"推荐指数: {score:.4f} | 🏠 {row['name']} ({row['category']})")

    return results


def plot_results(results, query):
    """
    可视化函数：绘制 价格 vs 推荐分数
    """
    if not results: 
        return

    prices = [r['price'] for r in results]
    scores = [r['score'] for r in results]
    names = [r['name'] for r in results]

    # 字体设置
    plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'SimHei', 'Microsoft YaHei', 'sans-serif']
    plt.rcParams['axes.unicode_minus'] = False

    plt.figure(figsize=(8, 6))
    plt.scatter(prices, scores, color='green', s=100)

    for i, txt in enumerate(names):
        plt.annotate(txt, (prices[i], scores[i]), fontsize=10, xytext=(5, 5), textcoords='offset points')

    plt.xlabel('人均价格 (元)')
    plt.ylabel('AI 推荐匹配度')
    plt.title(f"‘{query}’ 前{len(results)}名推荐")
    plt.grid(True)
    plt.show()


# ==========================================
# 3. 本地测试入口
# ==========================================
if __name__ == "__main__":
    # 这段代码只有在直接运行 search_engine.py 时才会执行
    test_query = "有没有适合吃素的地方"
    my_results = search_food(test_query, top_k=5)
    plot_results(my_results, test_query)