# Python 3.9のベースイメージを使用
FROM python:3.9-slim

# 作業ディレクトリを設定
WORKDIR /app

# 依存関係ファイルをコピー
COPY requirements.txt .

# 依存関係をインストール
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションのソースコードをコピー
COPY . .

# 環境変数を設定
ENV PORT=8080

# Cloud Run用にポート8080を公開
EXPOSE 8080

# アプリケーションを実行
CMD exec gunicorn --bind :$PORT app:app
