FROM python:3.10

RUN apt update && apt install -y \
    ca-certificates \
    libgl1-mesa-glx

COPY . /app
WORKDIR /app

RUN pip install --upgrade pip setuptools
RUN pip install -r requirements.txt

EXPOSE 7077

CMD ["streamlit", "run", "main.py", "--server.port", "7077", "--browser.gatherUsageStats", "false", "--server.headless", "true"]