import discord
import random
import datetime
import time
import re
import operator
import asyncio
from pymongo import MongoClient
from discord.ext import tasks
import os

client = discord.Client()
mongo_URL = os.environ["MONGO_URL"]
connection = MongoClient(mongo_URL)
db = connection.get_database("Erin")

prefix = "에린아 "

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("베타테스트")
    Daily.start()
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.author.bot:
        return None
    collection = db.Point
    if message.guild.name == "『카르멘』𝓒𝓐𝓡𝓜𝓔𝓝":
        collection.update_one({"_id": message.author.id}, {"$setOnInsert": {"!name" : message.author.display_name, "lotto" : [] , "count" : 0, "point" : 0, "daily" : False, "dailyCount" : 0, "caution" : []}}, upsert=True)
        collection.update_one({"_id": message.author.id}, {"$set": {"!name": message.author.display_name}},upsert=True)
        collection.update_one({"_id": message.author.id}, {"$inc": {"point": random.randrange(0, 2)}})

    if not(message.content.startswith(prefix)):
        return None

    talk = message.content[len(prefix):]

    if talk.startswith("초기화"):
        await message.channel.send("초기화 되었습니다")
        return None
    if talk.startswith("안녕"):
        Chat = ["안녕", "응?", "왜?", "어?", "왜 불러?"]
        await message.channel.send(Chat [random.randrange(0, len(Chat))])
        return None
    if talk.startswith("뭐해"):
        Chat = ["너 생각", "유튜브 봐", "내 생각", "그냥 있어"]
        await message.channel.send(Chat [random.randrange(0, len(Chat))])
        return None
    if talk.startswith("심심해"):
        Chat = ["내 생각 하면 되지", "나두", "나랑 놀자"]
        await message.channel.send(Chat [random.randrange(0, len(Chat))])
        return None
    if "바보" in ''.join(talk) or "멍청이" in ''.join(talk):
        Chat = [";;", "너는?", "멍청이", "너가 더", "응."]
        await message.channel.send(Chat [random.randrange(0, len(Chat))])
        return None
    if talk.startswith("보고싶었어"):
        Chat = ["나도", "나도 보고 싶었어", "ㅇ0ㅇ!"]
        await message.channel.send(Chat [random.randrange(0, len(Chat))])
        return None
    if talk.startswith("사랑해"):
        Chat = ["나도 사랑해", "응", "!", "어머나", "나도 날 사랑해"]
        await message.channel.send(Chat [random.randrange(0, len(Chat))])
        return None
    if talk.startswith("좋아해"):
        Chat = ["나도", "!", "나도 내가 좋아"]
        await message.channel.send(Chat [random.randrange(0, len(Chat))])
        return None
    if talk.startswith("사귀자"):
        Chat = ["친구부터 천천히 알아가자", "난 지금의 우리가 좋아",
                "아빠가 안된대", "엄마가 안된대", "가족이 반대해"]
        await message.channel.send(Chat [random.randrange(0, len(Chat))])
        return None
    if talk.startswith("결혼하자"):
        Chat = ["우리 너무 이른 거 같아", "나 마음의 시간이 필요해",
                "미안", "아 잠시만 불 안 끄고 왔어 가볼게"]
        await message.channel.send(Chat [random.randrange(0, len(Chat))])
        return None
    if talk.startswith("헤어져"):
        Chat = ["우리 사이에 그런 게 어딨어..",
                "우리가 그럴 만한 사이였니?", "그래"]
        await message.channel.send(Chat [random.randrange(0, len(Chat))])
        return None
    if talk.startswith("반가워"):
        Chat = ["그래", "반가워", "나도"]
        await message.channel.send(Chat[random.randrange(0, len(Chat))])
        return None
    if talk.startswith("손"):
        Chat = ["발", "절", "손"]
        await message.channel.send(Chat [random.randrange(0, len(Chat))])
        return None
    if talk.startswith("물어"):
        Chat = ["내가 왜?" , "싫어", "어딜?"]
        await message.channel.send(Chat [random.randrange(0, len(Chat))])
        return None
    if talk.startswith("배고파"):
        Chat = ["나도", "돼지", "밥은 먹었어?", "뭐라도 먹어"]
        await message.channel.send(Chat [random.randrange(0, len(Chat))])
        return None
    if talk.startswith("졸려"):
        Chat = ["나도 졸려", "그럼 자", "나랑 잘래?"]
        await message.channel.send(Chat[random.randrange(0, len(Chat))])
        return None
    if talk.startswith("누구"):
        Chat = ["날 몰라?", "실망이야", "바보", "멍청이", "나는야 카르멘 서버의 서버 봇!"]
        await message.channel.send(Chat [random.randrange(0, len(Chat))])
        return None
    if talk.startswith("자기소개"):
        Chat = ["나는야 카르멘 서버의 멋진 서버봇! 어때 완전 멋찌지?"]
        await message.channel.send(Chat [random.randrange(0, len(Chat))])
        return None
    if talk.startswith("몇살?") or talk.startswith("나이"):
        Chat = ["나 하유님이랑 동갑", "비밀", "나 몇 살 같아?"]
        await message.channel.send(Chat [random.randrange(0, len(Chat))])
        return None
    if talk.startswith("성별"):
        Chat = ["나 여자같아 남자같아?", "당연히 여자 아냐?", "그 물어봐야 아니?"]
        await message.channel.send(Chat[random.randrange(0, len(Chat))])
        return None
    if talk.startswith("뭐 먹지?"):
        Chat = ["나도 몰라", "먹고 싶은 거 먹어", "나:heart:"]
        await message.channel.send(Chat [random.randrange(0, len(Chat))])
        return None
    if talk.startswith("여보세요"):
        Chat = ["어디야?", "여보세요?", "나 불렀어?", "응 여보"]
        await message.channel.send(Chat[random.randrange(0, len(Chat))])
        return None
    if talk.startswith("이름"):
        await message.channel.send("'아름다운' 이라는 뜻을 가진 라틴어 '에일린' 에서 따왔어")
        return None
    if talk.startswith("카르멘"):
        Chat = ["rpg게임을 모티브로한 멋있는 친목 서버지" , "지금 여기 잖아"]
        await message.channel.send(Chat [random.randrange(0, len(Chat))])
        return None
    if talk.startswith("하유"):
        Chat = ["이 서버 주인, 카르멘 서버 겜마이지"]
        await message.channel.send(Chat [random.randrange(0, len(Chat))])
        return None
    if talk.startswith("청월"):
        Chat = ["미술관장이시지, 예쁜 분, 내 외형을 만들어 주셨어"]
        await message.channel.send(Chat [random.randrange(0, len(Chat))])
        return None
    if talk.startswith("고래"):
        Chat = ["음악관장이시지", "바보"]
        await message.channel.send(Chat [random.randrange(0, len(Chat))])
        return None
    if talk.startswith("피아"):
        Chat = ["1년 임시 대신관이야", "엄청 귀여우셔"]
        await message.channel.send(Chat [random.randrange(0, len(Chat))])
        return None
    if talk.startswith("한울"):
        Chat = ["기사단장이지, 국방의 의무를 다하시는 중","^^7"]
        await message.channel.send(Chat [random.randrange(0, len(Chat))])
        return None
    if talk.startswith("몽글"):
        Chat = ["대마법사셔", "카르멘 학원의 고독한 어둠의 다크루시퍼.."]
        await message.channel.send(Chat [random.randrange(0, len(Chat))])
        return None
    if talk.startswith("시낚") or talk.startswith("시나기") or talk.startswith("시간낚시꾼"):
        Chat = ["군대간 친구 자리를 지키는 1년 임시 기사단장"]
        await message.channel.send(Chat [random.randrange(0, len(Chat))])
        return None
    if talk.startswith("개발팀"):
        Chat = ["내 부모님들이잖아", "내 가족이지", "날 만들어주셨어"]
        await message.channel.send(Chat [random.randrange(0, len(Chat))])
        return None
    if talk.startswith("윤세연"):
        Chat = ["1년 잠수타시는 대신관이자 개발팀!", "곧 오실 거야.."]
        await message.channel.send(Chat [random.randrange(0, len(Chat))])
        return None
    if talk.startswith("상런쳐") or talk.startswith("상런처") or talk.startswith("발사통"):
        await message.channel.send("에린이 아빠에요")
        time.sleep(1)
        await message.channel.send("안녕해요")
        time.sleep(1)
        await message.channel.send("반갑다요?")
        return None
    if talk.startswith("Teacat"):
        Chat = ["나를 개방해주신 분이야!", "홍고"]
        await message.channel.send(Chat[random.randrange(0, len(Chat))])
        return None
    if talk.startswith("안내팀"):
        Chat = ["우리 게임 tutorial진행해주는 팀!"]
        await message.channel.send(Chat [random.randrange(0, len(Chat))])
        return None
    if talk.startswith("밤연"):
        Chat = ["귀여우시고 목소리 예쁘신 안내팀!"]
        await message.channel.send(Chat [random.randrange(0, len(Chat))])
        return None
    if talk.startswith("기획팀"):
        Chat = ["우리 서버 이벤트 기획하는 팀!"]
        await message.channel.send(Chat [random.randrange(0, len(Chat))])
        return None
    if talk.startswith("굴비"):
        Chat = ["기획팀인데", "생선", "밥 먹을 때마다 달아두는 거"]
        await message.channel.send(Chat [random.randrange(0, len(Chat))])
        return None
    if talk.startswith("태건"):
        if (random.randrange(0, 2) == 0):
            await message.channel.send("엄")
            time.sleep(1)
            await message.channel.send("준")
            time.sleep(1)
            await message.channel.send("식")
            time.sleep(1)
            await message.channel.send("화이팅!")
        else:
            await message.channel.send("기획팀이셔")
        return None
    if talk.startswith("세라"):
        Chat = ["귀여운 기획팀 분이야!", "세라님 귀엽지", "세라님 섹시하지"]
        await message.channel.send(Chat [random.randrange(0, len(Chat))])
        return None
    if talk.startswith("디자인팀"):
        Chat = ["우리 게임에 쓰이는 모든 그림을 맡아주는 팀!"]
        await message.channel.send(Chat [random.randrange(0, len(Chat))])
        return None
    if talk.startswith("라호"):
        Chat = ["배경을 도맡아 그려주시는 디자인팀의 금손!"]
        await message.channel.send(Chat [random.randrange(0, len(Chat))])
        return None
    if talk.startswith("도서진"):
        Chat = ["캐릭터를 도맡아 그려주시는 완전 금손 디자인팀!근데....사라지셨어.."]
        await message.channel.send(Chat[random.randrange(0, len(Chat))])
        return None
    if talk.startswith("권지원"):
        Chat = ["소품 위주로 그려주시는 완전 예쁜 디자인팀 겸 안내팀!이었었는데..."]
        await message.channel.send(Chat [random.randrange(0, len(Chat))])
        return None
    if talk.startswith("온점") or talk.startswith("와드") or talk.startswith("담이"):
        Chat = ["귀여운 분", "디자인팀이셔"]
        await message.channel.send(Chat [random.randrange(0, len(Chat))])
        return None
    if talk.startswith("queens"):
        Chat = ["도트 찍으시는 금손 디자인팀 분!"]
        await message.channel.send(Chat [random.randrange(0, len(Chat))])
        return None
    
    if talk.startswith("가온"):
        Chat = ["금수저"]
        await message.channel.send(Chat [random.randrange(0, len(Chat))])
        return None
    if "푸" in ''.join(talk) and "딩" in ''.join(talk):
        Chat = ["🍮", "푸딩은 맛나"]
        await message.channel.send(Chat[random.randrange(0, len(Chat))])
        return None
    if talk.startswith("몽쉘"):
        Chat = ["몽쉘 맛있지"]
        await message.channel.send(Chat [random.randrange(0, len(Chat))])
        return None

    if talk.startswith("노라조"):
        Chat = ["https://www.youtube.com/watch?v=2CGc9Ly11yo", "https://www.youtube.com/watch?v=ezwgRTy8R8U",
                "https://www.youtube.com/watch?v=ao58vQDMVlQ", "https://www.youtube.com/watch?v=JBoqPoqA8mM",
                "https://www.youtube.com/watch?v=AX3nSbKHDQU", "https://www.youtube.com/watch?v=YEYDPgfY-bE"]
        await message.channel.send("이분이랑 노는건 어때?")
        await message.channel.send(Chat[random.randrange(0, len(Chat))])
        return None

    if talk.startswith("나<@") or talk.startswith("나 <@"):
        await message.channel.send("https://www.youtube.com/watch?v=5lSBWirWJgY")
        return None

    if talk.startswith("시간") or talk.startswith("시간은"):
        utcnow = datetime.datetime.utcnow()
        time_gap = datetime.timedelta(hours=9)
        now = utcnow + time_gap
        await message.channel.send(str(now.year) + "년 " + str(now.month) + "월 " + str(now.day) + "일 | " + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second))
        return None
    
    if talk.startswith("춤"):
        dance = ["ㄴㅇ0ㅇㄱ", "ㄴ'^'ㄱ", "ㄴ( ᐛ )ㄱ", "ㄴ(ｏ`皿′ｏ)ㄱ", "ㄴ(≧▽≦)ㄱ", "ㄴ(。•́︿•̀。)ㄱ", "ㄴ( ･ㅂ･)ㄱ"]
        msg = await message.channel.send(dance[random.randrange(0, len(dance))])
        i = 0
        while i < 5:
            time.sleep(0.5)
            table = str.maketrans('ㄴㄱ', 'ㄱㄴ')
            await msg.edit(content=msg.content.translate(table))
            i += 1
        return None
    
    if talk.startswith("랩"):
        rap = ["상처를 치료해줄 사람 어디 없나\n가만히 놔두다간 끊임없이 덧나\n사랑도 사람도 너무나도 겁나\n혼자인게 무서워 난 잊혀질까 두려워"]
        msg = rap[random.randrange(0, len(rap))]
        i = 1
        chat = await message.channel.send(msg[0])
        temp = chat.content
        for i in msg[1:]:
            temp += i
            await chat.edit(content=temp)

    if talk.startswith("도움말"):
        await Help(message)
        return None

    if talk.startswith("사진"):
        await message.channel.send(file = discord.File("에린님.png"))
        return None

    if talk.startswith("로또"):
        await Lotto(message, talk)
        return None

    if talk.startswith("경고"):
        await Caution(message, talk)
        return None

    if talk.startswith("포인트"):
        await Point(message, talk)
        return None

    if talk.startswith("출석"):
        user = collection.find({"_id" : message.author.id})[0]
        if user.get("daily"):
            await message.channel.send("이미 출석했어")
            return None

        count = user.get("dailyCount")
        point = random.randrange(10, 300)
        pointmsg = str(point)
        count += 1
        if count % 50 == 0:
            point += 1000
            pointmsg += " + 1000(%d0일 누적)" % ((count / 50) * 5)
        elif count % 10 == 0:
            point += 100
            pointmsg += " + 100(%d0일 누적)" % (count / 10)
        collection.update_one({"_id" : message.author.id}, {"$inc" : {"point" : point, "dailyCount" : 1}, "$set" : {"daily" : True}})

        embed = discord.Embed(title="%-6s" % message.author.display_name, colour=discord.Colour.red())
        embed.add_field(name="포인트", value=pointmsg, inline=False)
        embed.add_field(name="출석일수", value=count, inline=False)
        embed.add_field(name="총포인트", value=user.get("point") + point, inline=False)
        await message.channel.send(embed=embed)
        return None

    if talk.startswith("닉네임"):
        job = " |" + message.author.display_name.split("|")[1]
        member = message.guild.get_member(message.author.id)
        try:
            await member.edit(nick=talk[4:] + job)
            await message.channel.send(talk[4:] + job + "으로 바꿨어")
        except discord.errors.Forbidden:
            await message.channel.send("너 이름은 못바꿔")
        return None

    if talk.startswith("고양이"):
        #embed = discord.Embed( title="타이틀",description="내용",colour=discord.Colour.red())
        embed = discord.Embed()
        urlBase = 'https://loremflickr.com/320/240?lock='
        randomNum = random.randrange(1, 30977)
        urlF = urlBase + str(randomNum)
        embed.set_image(url=urlF)
        await message.channel.send(embed=embed)
        return None

    if talk.startswith("검색"):
        _url = str(talk[3:].encode("UTF-8"))
        _url = _url.replace("\\x", "%")
        _url = _url.replace("'", "")
        _url = _url[1:]
        _url = "https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query={0}".format(_url)
        embed = discord.Embed(title="검색 결과", colour=discord.Colour.red())
        embed.add_field(name="검색", value=_url, inline=False)
        embed.set_image(url="https://s.pstatic.net/static/www/mobile/edit/2016/0705/mobile_212852414260.png")
        await message.channel.send(embed=embed)
        return None

    if talk.startswith("sns"):
        await Sns(message, talk)
        return None

    if talk.startswith("구매"):
        await Buy(message, talk)
        return None
    
    if talk.startswith("id") or talk.startswith("ID"):
        await message.channel.send(message.author.mention + "님의 ID는 \n" + "```" + str(message.author.id) + "```")
        return None
    
    if talk.startswith("삭제") or talk.startswith("청소") or talk.startswith("지워"):
        utcnow = datetime.datetime.utcnow()
        try:
            time_gap = datetime.timedelta(hours=int(talk.split(" ")[1]))
        except IndexError:
            time_gap = datetime.timedelta(hours=1)
        now = utcnow - time_gap
        await message.add_reaction("⏳")
        messages = await message.channel.history(limit=None, after=now, before=utcnow, oldest_first=True).flatten()
        for m in messages:
            if m.author == message.author:
                if m.content.startswith("에린아 삭제") or m.content.startswith("에린아 청소") or m.content.startswith("에린아 지워"):
                    continue
                await m.delete()
        await message.clear_reactions()
        await message.add_reaction("✅")
        return None
    
    if talk.startswith("가위바위보"):
        def check(m):
            return m.author == message.author and (m.content == "가위" or m.content == "바위" or m.content == "보")
        await message.channel.send("가위 바위 보!")
        try:
            msg = await client.wait_for('message', timeout=10.0, check=check)
        except asyncio.TimeoutError:
            await message.channel.send("너무 오래걸려ㅡnㅡ")
        else:
            rsp_list = ["가위", "바위", "보"]
            rsp = rsp_list[random.randint(0, 2)] # 0 = 가위, 1 = 바위, 2 = 보

            result = ""
            if msg.content == rsp:
                result = "무승부"
            else:
                if rsp == "가위":
                    result = "승리" if msg.content == "바위" else "패배"
                elif rsp == "바위":
                    result = "승리" if msg.content == "보" else "패배"
                elif rsp == "보":
                    result = "승리" if msg.content == "가위" else "패배"

            embed = discord.Embed(title="가위바위보", colour=discord.Colour.red())
            embed.add_field(name=message.author.display_name, value=msg.content, inline=False)
            embed.add_field(name="에린", value=rsp, inline=False)
            embed.set_footer(text=result)
            await message.channel.send(embed=embed)


async def Lotto(message, talk):
    lotto_Talk = talk.split(" ")
    collection = db.Point
    if lotto_Talk[1] == "초기화":
        all = collection.find()
        for x in all:
            collection.update_one(x, {"$min": {"count" : 0,  "lotto": []}}, upsert=True)
        await message.channel.send("로또를 초기화했습니다")
        return None
    
    try:
        lotto_List = collection.find({"_id": message.author.id})[0].get("lotto")
        count = collection.find({"_id": message.author.id})[0].get("count")
    except IndexError:
        collection.insert_one({"_id": message.author.id, "count": 0, "lotto": []})
        lotto_List = []
        count = 0

    if  lotto_Talk[1] == "랜덤":
        try:
            lotto = int(lotto_Talk[2])
            lotto / 10
        except (ValueError, ZeroDivisionError):
            await message.channel.send("0을 제외한 숫자를 써주세요 \nex) 에린아 로또 랜덤 5")
            return None
        if count > 10 or count + int(lotto_Talk[2]) > 10:
            await message.channel.send("로또는 10개까지만 구매하실 수 있습니다")
            await message.channel.send("<@" + str(message.author.id) + "> 님의 로또 수 : " + str(count))
            return None
        _count = int(lotto_Talk[2])
        for i in range(1, _count + 1):
            while True:
                a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                lotto = ""
                for j in range(0, 6):
                    index = random.randint(0, len(a) - 1)
                    lotto = lotto + str(a[index])
                    del a[index]
                if lotto in lotto_List:
                    continue
                await message.channel.send(lotto)
                lotto_List.append(lotto)
                break

        collection.update_one({"_id": message.author.id}, {"$set": {"_id": message.author.id, "Count": count + _count, "lotto": lotto_List}},upsert=True)
        return None

    if lotto_Talk[1] =="선택":
        if count + 1 > 10:
            await message.channel.send("로또는 하루에 10개까지만 구매하실 수 있습니다")
            await message.channel.send(str(message.author.name) + "님의 로또 수 : " + str(count))
            return None
        try:
            lotto = int(lotto_Talk[2])
            lotto / 10
        except ValueError:
            await message.channel.send("서로다른 숫자 6자리를 입력해주세요.")
            return None
        lotto = str(lotto)
        if not len(lotto) == 6:
            await message.channel.send("0을 제외한 숫자 6자리를 입력해주세요.")
            return None
        lotto_str = ""
        for i in lotto:
            for j in lotto_str:
                if j == i:
                    await message.channel.send("서로다른 숫자 6자리를 입력해주세요.")
                    return None
            lotto_str += i
        for l in lotto_List:
            if l == lotto:
                await message.channel.send("이미 등록된 번호입니다")
                await message.channel.send("<@" + str(message.author.id) + "> 님의 로또 : " + str(lotto_List))
                return None
        lotto_List.append(lotto)
        collection.update_one({"_id": message.author.id}, {"$set": {"_id": message.author.id, "Count": count + 1, "lotto": lotto_List}},upsert=True)
        await message.channel.send(lotto + "\n로또를 입력했습니다")
        return None

    if lotto_Talk[1] == "확인":
        await message.channel.send(str(message.author.name)+ " 님의 로또 : \n" + str(lotto_List))
        return None

    if lotto_Talk[1] == "전체":
        embed = discord.Embed(title="로또 전체", colour=discord.Colour.red())
        embed.set_footer(text="1등하구싶다")
        f = collection.find()
        for line in f:
            User = client.get_user(int(line.get("_id")))
            embed.add_field(name=User.display_name, value= collection.find({"_id" : line.get("_id")})[0].get("lotto"), inline=False)
        await message.channel.send(embed=embed)

async def Caution(message, talk):
    caution_Talk = talk.split(" ")

    #에린아 경고
    if len(caution_Talk) < 2:
        cautionMessage = ""
        with open("Caution.txt", 'r') as f:
            for line in f:
                if (line.startswith(str(message.author.id))):
                    cautionMessage += "{0}월 {1}일 경고\n".format(line[19], line[20:len(line) - 1])
        if cautionMessage == "":
            await message.channel.send(message.author.name + "님은 경고가 없습니다")
            return None
        embed = discord.Embed(title="{0}님의 경고".format(message.author.name), colour=discord.Colour.red())
        embed.add_field(name="경고", value=cautionMessage, inline=False)
        await message.channel.send(embed=embed)
        return None
    
    if caution_Talk[1].startswith("<@"):
        cautionMessage = ""
        User_ID = int(re.findall("\d+", caution_Talk[1])[0])
        with open("Caution.txt", 'r') as f:
            for line in f:
                if (line.startswith(str(User_ID))):
                    cautionMessage += "{0}월 {1}일 경고\n".format(line[19], line[20:len(line) - 1])
        if cautionMessage == "":
            await message.channel.send(message.guild.get_member(User_ID).name + "님은 경고가 없습니다")
            return None
        embed = discord.Embed(title="{0}님의 경고".format(message.guild.get_member(User_ID).name), colour=discord.Colour.red())
        embed.add_field(name="경고", value=cautionMessage, inline=False)
        await message.channel.send(embed=embed)

    if caution_Talk[1] == "지급":
        if (message.channel.permissions_for(message.author).value & 0x00000008) != 0x00000008:
            await message.channel.send("권한이 없어")
            return None
        User_ID = re.findall("\d+", caution_Talk[2])
        with open("Caution.txt", 'a') as f:
            now = datetime.datetime.now()
            for i in range(0, int(caution_Talk[3])):
                f.write(User_ID[0] + " " + str(now.month) + str(now.day) + "\n")
        User = client.get_user(int(User_ID[0]))
        await message.channel.send("{0}에게 경고를 {1}회 줬어".format(User.name, caution_Talk[3]))
        return None

async def Point(message, talk):
    point_Talk = talk.split(" ")
    collection = db.Point
    
    if len(point_Talk) < 2:
        point = collection.find({"_id": message.author.id})[0].get("point")
        embed = discord.Embed(title=message.author.display_name, colour=discord.Colour.red())
        embed.add_field(name="포인트", value="{0} 포인트".format(point), inline=False)
        await message.channel.send(embed=embed)
        return None

    if point_Talk[1].startswith("<@"):
        User_ID = int(re.findall("\d+", point_Talk[1])[0])
        point = collection.find({"_id": User_ID})[0].get("point")
        embed = discord.Embed(title=client.get_user(User_ID).display_name, colour=discord.Colour.red())
        embed.add_field(name="포인트", value="{0} 포인트".format(point), inline=False)
        await message.channel.send(embed=embed)
        return None

    if point_Talk[1] == "지급":
        if (message.channel.permissions_for(message.author).value & 0x00000008) != 0x00000008:
            await message.channel.send("권한이 없어")
            return None
        User_ID = int(re.findall("\d+", point_Talk[2])[0])
        collection.update_one({"_id": message.author.id}, {"$inc" : {"point" : int(point_Talk[3])}})
        await message.channel.send("{0}에게 {1}포인트 지급했어".format(client.get_user(User_ID).name, int(point_Talk[3])))
        return None

    if point_Talk[1] == "반환":
        if (message.channel.permissions_for(message.author).value & 0x00000008) != 0x00000008:
            await message.channel.send("권한이 없어")
            return None
        User_ID = int(re.findall("\d+", point_Talk[2])[0])
        collection.update_one({"_id": User_ID}, {"$inc": {"point": -int(point_Talk[3])}})
        await message.channel.send("{0}에게 {1}포인트를 반환했어".format(client.get_user(User_ID).name, point_Talk[3]))
        return None

    if point_Talk[1] == "선물":
        User_ID = int(re.findall("\d+", point_Talk[2])[0])
        User = collection.find({"_id": User_ID})
        if collection.find({"_id" : message.author.id})[0].get("point") <= int(point_Talk[3]):
            await message.channel.send("포인트가 부족해")
            return None

        collection.update_one({"_id" : message.author.id}, {"$inc" : {"point" : - int(point_Talk[3])}})
        collection.update_one({"_id": User_ID}, {"$inc": {"point": int(point_Talk[3])}})
        await message.channel.send("{0}에게 {1}포인트를 선물했어".format(client.get_user(User_ID).name, point_Talk[3]))
        return None

    if point_Talk[1] == "순위":
        point_List = collection.find().sort([("point" , -1)]).limit(10)
        embed = discord.Embed(title="포인트 순위", colour=discord.Colour.red())
        rank = 1
        for i in point_List:
            embed.add_field(name=str(rank) + "등 " + i.get("!name"), value=str(i.get("point")) + " 포인트", inline=False)
            rank += 1
        await message.channel.send(embed=embed)
        return None

    if point_Talk[1] == "상점":
        embed = discord.Embed()
        embed.set_author(name="1.경고 면제권", icon_url=message.guild.icon_url)
        embed.set_thumbnail(url= message.guild.icon_url)
        embed.add_field(name="경고 면제권이다", value="10,000 point", inline=False)
        shopMessage = await message.channel.send(embed=embed)
        await shopMessage.add_reaction("◀️")
        await shopMessage.add_reaction("▶️")
        return None

async def Buy(message, talk):
    buyTalk = talk.split(" ")
    if len(buyTalk) == 1:
        await Point(message, "포인트 상점")
        return None

    if buyTalk[1].startswith("경고"):
        cautions = []
        with open("Caution.txt", 'r') as f:
            for line in f:
                cautions.append(line)

        for caution in cautions:
            if caution.startswith(str(message.author.id)):
                cautions.remove(caution)
                break
        else:
            await message.channel.send("받은 경고가 없어")
            return None
        datalist = []
        with open("Point.pkl", "rb") as f:
            while True:
                try:
                    data = pickle.load(f)
                except EOFError:
                    break
                datalist.append(data)
            datalist = dict(datalist)
        if datalist.get(message.author.id) == None or datalist.get(message.author.id) < 10000:
            await message.channel.send("포인트가 부족해")
            return None

        with open("Point.pkl", "ab") as f:
            point1 = datalist.get(message.author.id)
            if point1 == None:
                point1 = 0
            pickle.dump([message.author.id, point1 - 10000], f)
        with open("Caution.txt", 'w') as f:
            for line in cautions:
                f.write(line)
        caution = caution.replace("\n", "")
        await message.channel.send("{0}월 {1}일 경고가 면제됐어".format(caution[19], caution[20:len(line) - 1]))
        return None
    return None


@client.event
async def on_reaction_add(reaction, user):
    if user.bot:
        return None
    count = int(reaction.message.embeds[0].author.name[0])
    if reaction.emoji == "◀️":
        count -= 1
    elif reaction.emoji == "▶️":
        count += 1

    if count < 1 or count > 3:
        return None

    if count == 1:
        embed = discord.Embed()
        embed.set_author(name="1.경고 면제권", icon_url=reaction.message.guild.icon_url)
        embed.set_thumbnail(url=reaction.message.guild.icon_url)
        embed.add_field(name="경고 면제권이다", value="10,000 point", inline=False)
        await reaction.message.clear_reactions()
        await reaction.message.edit(embed=embed)
        await reaction.message.edit(embed=embed)
        await reaction.message.add_reaction("◀️")
        await reaction.message.add_reaction("▶️")

    if count == 2:
        embed = discord.Embed()
        embed.set_author(name="2.로또 10개", icon_url=reaction.message.guild.icon_url)
        embed.set_thumbnail(url=reaction.message.guild.icon_url)
        embed.add_field(name="로또 10개다", value="1,000,000,000,000 point", inline=False)
        await reaction.message.clear_reactions()
        await reaction.message.edit(embed=embed)
        await reaction.message.add_reaction("◀️")
        await reaction.message.add_reaction("▶️")

    if count == 3:
        embed = discord.Embed()
        embed.set_author(name="3.하유님 바부", icon_url=reaction.message.guild.icon_url)
        embed.set_thumbnail(url=reaction.message.guild.icon_url)
        embed.add_field(name="멍청이 'u'", value="메롱메롱", inline=False)
        await reaction.message.edit(embed=embed)
        await reaction.message.clear_reactions()
        await reaction.message.add_reaction("◀️")
        await reaction.message.add_reaction("▶️")

    return None

@client.event
async def on_voice_state_update(member, before, after):
    try:
        if member.voice.channel.category.name == "여관":
            time.sleep(2)
            if after.channel.name == "check in":
                if member in discord.utils.get(client.get_all_channels(), guild__name=member.guild.name, name="check in").members:
                    newChannel = await member.guild.create_voice_channel("제목을 입력해주세요.")
                    await newChannel.edit(category=after.channel.category)
                    await newChannel.set_permissions(member, manage_channels=True)
                    await member.move_to(newChannel)
            elif after.channel.name == "private check in":
                if member in discord.utils.get(client.get_all_channels(), guild__name=member.guild.name, name="private check in").members:
                    newChannel = await member.guild.create_voice_channel("제목을 입력해주세요.")
                    await newChannel.edit(category=after.channel.category)
                    await newChannel.set_permissions(member.guild.get_role(629963963446198292), view_channel=False)
                    await newChannel.set_permissions(member, manage_channels=True)
                    await member.move_to(newChannel)
    except AttributeError:
        None
    try:
        if before.channel.category.name == "여관":
            if before.channel.name != "check in" and len(before.channel.members) == 0 and before.channel.name != "private check in":
                await before.channel.delete()
    except AttributeError:
        None

async def Sns(message, talk):
    sns_Talk = talk.split(" ")
    if sns_Talk[1] == "개설":
        try:
            category = discord.utils.get(client.get_all_channels(), guild__name=message.guild.name, name="SNS")
            new_Channel = await discord.Guild.create_text_channel(message.guild, name=sns_Talk[2],category=category, topic="%s\n%s\n게시물 [0]" % (sns_Talk[3], "팔로워 [7]")) #수정 팔로워 수 어떻게늘리고 줄이지
            role = await message.guild.create_role(name="{0}팔로워".format(sns_Talk[2]), mentionable=True)
            await  new_Channel.send(message.author.mention)
            await new_Channel.send(role.mention)
            await message.channel.send("{0}채널을 만들었어".format(sns_Talk[2]))
        except IndexError:
            await message.channel.send("잘못 입력했어\nex)에린아 sns 개설 {채널이름} {소개}")
    return None

@tasks.loop(seconds=60*60)
async def Daily():
    #로또 초기화
    utcnow = datetime.datetime.utcnow()
    time_gap = datetime.timedelta(hours=9)
    now = utcnow + time_gap
    if now.hour == 6:
        collection = db.Point
        users = collection.find()
        for i in users:
            if not i.get("daily"):
                collection.update_one(i, {"$set": {"dailyCount": 0}})
            collection.update_one(i , {"$set" : {"count" : 0, "daily" : False}})
        await discord.utils.get(client.get_all_channels(), guild__name="『카르멘』𝓒𝓐𝓡𝓜𝓔𝓝", name="봇-test").send("에린 초기화")

async def Help(message):
    embed = discord.Embed(title= "에린이 도움말",colour=discord.Colour.red())
    embed.add_field(name="로또", value="에린아 로또 랜덤 <숫자> : 로또를 <숫자>번 랜덤으로 뽑습니다.\n"
                                     "에린아 로또 선택 <숫자> : <숫자> 번호 로또를 구매합니다?\n"
                                     "에린아 로또 확인 : 본인의 로또 번호를 확인합니다", inline=False)
    embed.add_field(name="포인트", value="에린아 포인트 : 자신의 포인트를 확인합니다.\n"
                                     "에린아 출석 : 한번 출석에 10~300의 포인트를 받습니다. 누적되면 추가로 포인트를 얻습니다.\n"
                                     "에린아 순위 : 서버 내 포인트 순위를 확인합니다."
                                     "에린아 선물 <멘션> <포인트> :<멘션>에게 <포인트>만큼 포인트를 선물합니다 ", inline=False)
    embed.add_field(name="기타 기능", value="에린아 삭제 : 현재 채널에서 <시간>시간 전 ~ 현재 까지의 자신이 쓴 글을 삭제합니다\n", inline=False)
    await message.channel.send(embed=embed)
    return

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
