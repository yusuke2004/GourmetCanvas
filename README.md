# IzakayaReco

居酒屋検索・レビュー用のシンプルな Django/Vite アプリケーション。

## 概要
バックエンドは Django REST Framework を利用し、HotPepper API から居酒屋情報を取得します。フロントエンドは Vite+Vanilla JS で SPA 形式。ユーザーは店舗検索、評価、コメント、共有などが可能です。

## セットアップ (ローカル開発)
1. リポジトリをクローン
   ```bash
   git clone <repo-url>
   cd izakaya-reco
   ```
2. Python 仮想環境を作成・有効化
   ```bash
   python -m venv backend/.venv
   source backend/.venv/Scripts/activate   # Windows
   ```
3. 依存パッケージをインストール
   ```bash
   pip install -r backend/requirements.txt
   cd frontend
   npm install
   ```
4. `.env` を作成して必要な環境変数を設定
   ```bash
   cp .env.example .env
   # SECRET_KEY や HOTPEPPER_API_KEY などを編集
   ```
5. マイグレーションと静的ファイル収集
   ```bash
   cd backend
   python manage.py migrate
   python manage.py collectstatic --noinput
   ```
6. サーバーを起動
   ```bash
   # フロントエンド開発の場合
   cd frontend && npm run dev
   # またはバックエンド単体
   cd backend && python manage.py runserver
   ```

## デプロイ (Render)
1. Render アカウントを作成し GitHub リポジトリを接続。
2. 新規 Web Service を作成し、Docker を選択。
3. 環境変数を設定:
   - `SECRET_KEY` (本番用)
   - `DATABASE_URL` (Neon PostgreSQL)
   - `ALLOWED_HOSTS` (Render のドメインなど)
   - `HOTPEPPER_API_KEY`
   - `DEBUG=false`
4. デプロイ後、マイグレーションを実行（Render の Shell から）。
5. 必要なら `collectstatic` コマンドも実行。

## env ファイル
- `.env.example` を参考にしてローカル用 `.env` を作成。
- 本番では Render の環境変数画面で値を設定するため `.env` は不要。

## ライセンス
このプロジェクトは [MIT ライセンス](LICENSE) の下で公開されています。

---

その他の詳細や拡張機能はコード内コメントや GitHub Issues を参照してください。