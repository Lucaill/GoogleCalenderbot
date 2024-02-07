import discord
import datetime
from google.oauth2 import service_account
from googleapiclient.discovery import build
import asyncio

# Discord Bot Token
DISCORD_TOKEN = 'xxxxxxxxxxxxxxxxxx'# DiscordTOKEN

# Google Calendar API情報
GOOGLE_CREDENTIALS = r'./path/calender-api-000000'  # 相対パス
GOOGLE_CALENDAR_ID = 'XXXXXXXXXXXXXXXXX'  # GoogleカレンダーのID

# 接続に必要なオブジェクトを生成
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# Google Calendar APIのセットアップ
credentials = service_account.Credentials.from_service_account_file(
    GOOGLE_CREDENTIALS,
    scopes=['https://www.googleapis.com/auth/calendar.readonly']
)
calendar_service = build('calendar', 'v3', credentials=credentials)

# 今日の予定を取得する関数
def get_today_events():
    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z'はUTCの意味
    events_result = calendar_service.events().list(
        calendarId=GOOGLE_CALENDAR_ID,
        timeMin=now,
        timeMax=(datetime.datetime.utcnow() + datetime.timedelta(days=1)).isoformat() + 'Z',
        maxResults=10,
        singleEvents=True,
        orderBy='startTime'
    ).execute()
    events = events_result.get('items', [])
    return events

# 朝7時に予定を通知する処理
async def send_daily_schedule():
    guild_id = 0000000000000000  # サーバーのID
    channel_name = "カレンダー" # チャンネルの名前

    guild = discord.utils.get(client.guilds, id=guild_id)
    if not guild:
        print(f"Error: Could not find guild with ID {guild_id}")
        return

    channel = discord.utils.get(guild.channels, name=channel_name)
    if not channel:
        print(f"Error: Could not find channel with name {channel_name} in guild {guild.name}")
        return

    # 今日の予定を取得
    events = get_today_events()

    if not events:
        await channel.send('今日の予定はありません。')
    else:
        schedule_message = "今日の予定:\n"
        for event in events:
            start_time = event['start'].get('dateTime', event['start'].get('date'))
            summary = event['summary']
            schedule_message += f"{start_time} - {summary}\n"
        
        await channel.send(schedule_message)

# Botの起動時に実行される処理
@client.event
async def on_ready():
    print(f'Logged in as {client.user.name} ({client.user.id})')
    # 毎日朝7時に予定を通知
    await schedule_daily_notifications()

# 毎日朝7時に通知するためのスケジューリング
async def schedule_daily_notifications():
    while True:
        now = datetime.datetime.utcnow()
        target_time = datetime.datetime(now.year, now.month, now.day, 7, 0, 0)  # 朝7時の時間
        if now.hour >= 7:
            # 今日の7時が過ぎている場合、次の日の7時をターゲットにする
            target_time += datetime.timedelta(days=1)
        delta = target_time - now
        await asyncio.sleep(delta.total_seconds())

        await send_daily_schedule()

# Botの起動とDiscordサーバーへの接続
client.run(DISCORD_TOKEN)
