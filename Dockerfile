# 1. 基础镜像 (轻量级 Python)
FROM python:3.11-slim

# 2. 设置工作目录
WORKDIR /app

# 3. 复制依赖并安装
# (确保你生成了 requirements.txt，如果没有，看下面的提示)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. 复制所有代码
COPY . .

# 5. 暴露 Streamlit 的默认端口
EXPOSE 8501

# 6. 启动命令
CMD ["streamlit", "run", "web_app.py", "--server.port=8501", "--server.address=0.0.0.0"]