# タスク管理アプリ

シンプルで使いやすいタスク管理アプリケーションです。

## 機能

- タスクの追加（タイトル、説明、期限）
- タスクの完了/未完了の切り替え
- タスクの削除
- レスポンシブデザイン

## 技術スタック

- Backend: Python (Flask)
- Database: SQLite
- Frontend: HTML, CSS, JavaScript
- UI Framework: Bootstrap 5

## ローカルでの実行方法

1. リポジトリをクローン
```bash
git clone [リポジトリURL]
cd task_manager
```

2. 依存パッケージのインストール
```bash
pip install -r requirements.txt
```

3. アプリケーションの実行
```bash
python app.py
```

4. ブラウザで以下のURLにアクセス
```
http://localhost:5000
```

## デプロイ

このアプリケーションは[Render](https://render.com)を使用してデプロイできます。
`render.yaml`の設定ファイルが含まれているので、Renderでの自動デプロイが可能です。
