import discord

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith("!updata"):
        if client.user != message.author:
            updata=discord.Embed(title='前回のアメダスBOTのアップデート情報', description='前回のアップデート(ver.0.0.0→0.0.1α)', color=0x00ff40)
            updata.set_author(name='アメダスBOT', icon_url='https://github.com/Yuu0918/test/blob/master/ayanami.png?raw=true')
            updata.add_field(name='アップデート！', value='なし', inline=False)
            updata.add_field(name='アップデート！2', value='なし。', inline=False)
            updata.add_field(name='アメダスBOT', inline=False)
            updata.set_footer(text='AMEDASUBOT ver.0.0.1α')
            await client.send_message(message.channel, embed=updata)
    if message.content.startswith("!nextupdata"):
        if client.user != message.author:
            nextupdata=discord.Embed(title="次回のアメダスBOTのアップデート予定", description="日時未定 (ver.0.0.1α→0.0.1β)\r日時が変更になる可能性がございます。あらかじめご了承ください。", color=0xff6c26)
            nextupdata.set_author(name="アメダスBOT", icon_url="https://github.com/Yuu0918/test/blob/master/ayanami.png?raw=true")
            nextupdata.add_field(name='追加予定', value='アメダス情報を追加する (できたら)天気予報を追加する', inline=False)
            nextupdata.add_field(name='削除予定', value='未定', inline=False)
            nextupdata.add_field(name='バグ削除予定', value='なし', inline=False)
            nextupdata.set_footer(text='AMEDASUBOT ver.0.0.1α')
            await client.send_message(message.channel, embed=nextupdata)
    if message.content.startswith("!help"):
        if client.user != message.author:
            help = discord.Embed(title = 'アメダスBOTの使い方', description = 'Yuu_0918が勉強用に作ったBOTです\r詳しい使い方はYuu_0918に聞いてください...', color=0x189c1f)
            help.set_author(name = '綾波BOT', icon_url = 'https://github.com/Yuu0918/test/blob/master/ayanami.png?raw=true')
            help.add_field(name='!help', value='ヘルプを表示します。', inline=False)
            help.add_field(name='!update', value='前回のアップデート内容を表示します', inline=False)
            help.add_field(name='!nextupdate', value='次回のアップデートの日付と内容を表示します', inline=False)
            help.add_field(name='!AME1 (地点)', value='(地点)の場所の1時間の降水量を表示します', inline=False)
            help.add_field(name='!AME3 (地点)', value='(地点)の場所の3時間の降水量を表示します', inline=False)
            help.add_field(name='!AME6 (地点)', value='(地点)の場所の6時間の降水量を表示します', inline=False)
            help.add_field(name='!AME12 (地点)', value='(地点)の場所の12時間の降水量を表示します', inline=False)
            help.add_field(name='!AME24 (地点)', value='(地点)の場所の24時間の降水量を表示します', inline=False)
            help.add_field(name='!AME Wind', value='(地点)の場所の最大風速を表示します', inline=False)
            help.add_field(name='!AME IWind', value='(地点)の場所の瞬間最大風速を表示します', inline=False)
            help.add_field(name='!AME maxTemp', value='(地点)の場所の最高気温を表示します', inline=False)
            help.add_field(name='!AME minTemp', value='(地点)の場所の最底気温を表示します', inline=False)
            help.add_field(name='機能募集！', value='このBOTに追加してほしい機能を募集しております\rありましたらYuu_0918にいってください。可能な限り実装していきます。', inline=False)
            help.add_field(name='注意', value='※ この機能はまだ実装されてないので打つだけ無駄です。\r※2 次回のVer.では消される可能性がありますご了承ください。\r※3 コマンドの連打などで再起不能な状態に陥ったりした場合は特定して後ろから鉈で刺しに行きます。', inline=True)
            help.set_footer(text='AMEDASUBOT ver.0.0.1α')
            await client.send_message(message.channel, embed=help)

client.run("NzE1NDE3MTMxNjI1MjE4MTE4.Xtnf_Q.v5awWJo1bX7VqCdsWcl7wndfjEQ")
