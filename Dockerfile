# 1. 基础镜像 (保持 3.11 不变)
FROM python:3.11-slim

# 2. 设置工作目录
WORKDIR /app

# 3. 复制依赖并安装
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. 复制所有代码
COPY . .

# 5. 【关键修改】暴露 8080 端口 (虽然这行只是声明，但写上是好习惯)
EXPOSE 8080

# 6. 【关键修改】强制 Streamlit 使用 8080 端口
# 我们直接把 8501 改成了 8080
# 强制使用 8080 端口，并且关闭 CORS 和 XSRF 保护，防止卡死
CMD ["streamlit", "run", "web_app.py", "--server.port=8080", "--server.address=0.0.0.0", "--server.enableCORS=false", "--server.enableXsrfProtection=false"]