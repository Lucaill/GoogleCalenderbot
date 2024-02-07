このコードは、Discord ボットを使用して Google Calendar のイベント情報を取得し、指定した Discord サーバーの指定したチャンネルに毎日朝7時に通知するものです。README ファイルには、以下のような内容を含めると良いでしょう。

1. プロジェクトの概要と目的：このプロジェクトは、Discord ボットを使用して Google Calendar のイベント情報を取得し、指定した Discord サーバーの指定したチャンネルに毎日朝7時に通知することを目的としています。

2. インストール手順：
   - Python 3.x のインストールが必要です。
   - 必要なパッケージをインストールするために、以下のコマンドを実行してください。
     ```
     pip install discord google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
     ```

3. 使用法：
   - Discord Bot Token を取得し、`DISCORD_TOKEN` 変数に設定してください。
   - Google Calendar API の認証情報を取得し、`GOOGLE_CREDENTIALS` 変数に設定してください。
   - Google Calendar のカレンダー ID を取得し、`GOOGLE_CALENDAR_ID` 変数に設定してください。
   - Discord サーバーの ID を取得し、`guild_id` 変数に設定してください。
   - 通知を送信する Discord チャンネルの名前を設定し、`channel_name` 変数に設定してください。

4. 注意事項：
   - このプログラムを実行するには、Discord Bot Token と Google Calendar API の認証情報が必要です。
   - Google Calendar API を使用するためには、Google Cloud Platform でプロジェクトを作成し、API を有効にし、認証情報をダウンロードする必要があります。

5. その他：
   - このプログラムは、指定された Discord サーバーの指定されたチャンネルに毎日朝7時に予定を通知します。
   - プログラムを実行すると、ログインした Discord ユーザー名とユーザー ID が表示されます。

これらの情報を README ファイルに追加すると、他の開発者やユーザーがプロジェクトを理解し、使用するのに役立ちます。
