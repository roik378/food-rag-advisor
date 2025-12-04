import os
import google.generativeai as genai
from search_engine import search_food  # 引入我们刚才写好的搜索模块

# ==========================================
# 1. 配置区域 (Configuration)
# ==========================================

# 🔑 如果你有 Gemini API Key，请在这里填入
# 如果没有，保持为空，代码会自动切换到“模拟模式”
GOOGLE_API_KEY = ""  

# 🌐 如果你在国内且有 VPN，可能需要配置代理 (例如 http://127.0.0.1:7890)
# os.environ["HTTP_PROXY"] = "http://127.0.0.1:7890"
# os.environ["HTTPS_PROXY"] = "http://127.0.0.1:7890"

if GOOGLE_API_KEY:
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-pro')
    print("✨ 已配置 Google Gemini API")
else:
    model = None
    print("⚠️ 未检测到 API Key，将使用本地模拟模式 (Mock Mode)")


# ==========================================
# 2. 核心逻辑：构造 Prompt 并获取回答
# ==========================================

def get_smart_advice(user_query):
    """
    RAG 的核心流程：检索 (Retrieval) -> 增强 (Augmented) -> 生成 (Generation)
    """
    
    # --- A. 检索 (Retrieval) ---
    print(f"\n🤖 思考中: 正在去数据库查询 '{user_query}'...")
    # 调用我们之前的搜索函数，拿前 3 名
    restaurants = search_food(user_query, top_k=3)
    
    if not restaurants:
        return "抱歉，原本的数据库里好像找不到合适的餐厅。"

    # --- B. 增强 (Augmented) - 构建上下文 ---
    # 我们要把结构化的数据，变成一段话，喂给 AI
    context_text = ""
    for i, r in enumerate(restaurants, 1):
        context_text += f"{i}. {r['name']} ({r['category']}): 特色是{r['features']}。描述：{r['description']}。价格：{r['price']}元。\n"

    # 构建最终的提示词 (Prompt Engineering)
    prompt = f"""
    你是一个专业的运动营养师和美食家。
    
    用户现在的需求是："{user_query}"
    
    这是我们数据库里检索到的最匹配的几家餐厅：
    {context_text}
    
    请根据用户的需求和上面的餐厅信息，推荐 1 家最合适的餐厅，并解释为什么。
    语气要轻松、鼓励，像朋友一样。如果用户刚运动完，记得提醒补充水分或蛋白质。
    """

    # --- C. 生成 (Generation) ---
    print("📝 正在组织语言生成建议...")
    
    # 尝试调用真实 AI
    if model:
        try:
            response = model.generate_content(prompt)
            return response.text
        except Exception as e:
            print(f"❌ API 调用失败 (可能是网络问题): {e}")
            print("🔄 切换回本地模拟模式...")
    
    # --- D. 兜底方案 (Mock Mode) ---
    # 如果没有 API，我们就用 Python 简单拼凑一个回答，假装是 AI
    best_match = restaurants[0]
    mock_response = (
        f"\n[本地模拟AI回复]：\n"
        f"嘿！根据你的需求，我强烈推荐你试试 **{best_match['name']}**！\n"
        f"这就位于福田区，只要 {best_match['price']} 元。\n"
        f"既然你想要“{user_query}”，这家店的 **{best_match['features']}** 特色简直太适合你了。\n"
        f"💡 小贴士：{best_match['description']}"
    )
    return mock_response


# ==========================================
# 3. 主程序交互
# ==========================================
if __name__ == "__main__":
    print("="*50)
    print("🥗 福田 AI 饮食顾问已上线 (输入 'q' 退出)")
    print("="*50)

    while True:
        # 获取用户输入
        user_input = input("\n👇 请输入你的需求 (例如: 练完腿想吃肉): ")
        
        if user_input.lower() in ['q', 'quit', 'exit']:
            print("👋以此致敬你的健康生活，拜拜！")
            break
        
        if not user_input.strip():
            continue

        # 获取 AI 建议
        advice = get_smart_advice(user_input)
        
        # 打印结果
        print("\n💬 AI 建议:")
        print("-" * 40)
        print(advice)
        print("-" * 40)