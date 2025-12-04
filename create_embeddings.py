from sentence_transformers import SentenceTransformer
import numpy as np

# 1. 加载一个预训练好的轻量级模型 (它已经读过几亿条中文数据了)
# 'paraphrase-multilingual-MiniLM-L12-v2' 支持中文，且速度很快
print("正在加载 AI 模型 (第一次可能需要下载)....")
model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')

# 2. 准备两个测试词
text_1 = "我想增肌"
text_2 = "高蛋白食物"
text_3 = "我很喜欢喝可乐"

# 3. 变成向量 (Encode)
vec_1 = model.encode(text_1)
vec_2 = model.encode(text_2)
vec_3 = model.encode(text_3)

print("\n转化完成！")
print(f"'{text_1}' 的向量前5位: {vec_1[:5]}")
print(f"向量的总长度 (维度): {len(vec_1)}")

# 4. 计算相似度 (用点积简单模拟余弦相似度)
# 这一步就是 AI 判断的核心：谁的分数高，就推荐谁
score_1_2 = np.dot(vec_1, vec_2) / (np.linalg.norm(vec_1) * np.linalg.norm(vec_2))
score_1_3 = np.dot(vec_1, vec_3) / (np.linalg.norm(vec_1) * np.linalg.norm(vec_3))

print("\n=== AI 的判断结果 ===")
print(f"'{text_1}' vs '{text_2}' 的相似度: {score_1_2:.4f}")
print(f"'{text_1}' vs '{text_3}' 的相似度: {score_1_3:.4f}")