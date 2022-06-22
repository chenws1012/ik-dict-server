FROM python:3.7.13-slim

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --no-cache-dir -r requirements.txt

COPY . .
CMD [ "python", "./app.py" ]
# CMD [ "waitress-serve", "--port=5000", "app:app" ]