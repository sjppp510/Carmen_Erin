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

isPlaying = False

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("베타테스트")
    Daily.start()
    await client.change_presence(status=discord.Status.online, activity=game)
    
@client.event
async def on_error(event, *args, **kwargs):
    print(type(args[0]))
    print(args[0][0])
    print(args[0].get(message_id))
    await discord.utils.get(client.get_all_channels(), guild__name="『카르멘』𝓒𝓐𝓡𝓜𝓔𝓝", name="봇-test").send("{0} 에러\n에러메세지 : {1}".format(event, args[0]))
    
@client.event
async def on_message(message):
    print("test")
    if message.author.bot:
        return None
    collection = db.Point
    try:
        if message.guild.name == "『카르멘』𝓒𝓐𝓡𝓜𝓔𝓝":
            utcnow = datetime.datetime.utcnow()
            time_gap = datetime.timedelta(hours=9)
            now = utcnow + time_gap
            collection.update_one({"_id": message.author.id}, {
                "$setOnInsert": {"!name": message.author.display_name, "lotto": [], "count": 0, "point": 0, "daily": False,
                                "dailyCount": 0, "caution": [], "!creation_Date": now}}, upsert=True)
            collection.update_one({"_id": message.author.id}, {"$set": {"!name": message.author.display_name, "!creation_Date": now}, "$inc": {"point": random.randrange(0, 2)}}, upsert=True)
        
            if message.channel.category.name.startswith("SNS"):
                for i in message.role_mentions:
                    if i.name.startswith(message.channel.name):
                        tmp_topic = re.findall("게시물 \[\d+\]", message.channel.topic)[0]
                        number = int(re.findall("\d+", tmp_topic)[0]) + 1
                        _topic = message.channel.topic.replace(tmp_topic, "게시물 [%s]" % str(number))
                        try:
                            await message.channel.edit(topic=_topic)
                        except TypeError:
                            pass
                        return None
    except discord.errors.HTTPException:
        print("에러난거")

            
    if not(message.content.startswith(prefix)):
        return None

    talk = message.content[len(prefix):]

    if talk.startswith("재시작"):
        os.system("python Erin.py")
        await message.channel.send("재시작 되었습니다.")
    if talk.startswith("초기화"):
        utcnow = datetime.datetime.utcnow()
        time_gap = datetime.timedelta(hours=9)
        now = utcnow + time_gap
        #users = collection.find()
        #for i in users:
            #collection.update_one(i, {"$set" : {"!creation_Date": now}}, upsert=True)
        await message.channel.send("초기화 되었습니다")
        return None
    if talk.startswith("안녕"):
        Chat = ["안녕", "응?", "왜?", "어?", "왜 불러?"]
        await message.channel.send(Chat [random.randrange(0, len(Chat))])
        return None
    if talk.startswith("뭐해"):
        Chat = [" 생각", "유튜브 봐", "내 생각", "그냥 있어"]
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
        Chat = ["나도 사랑해", "응", "!", "어머나", "나도 날 사랑해" , "(•᷄⌓•᷅ )"]
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
        Chat = ["나 하유님이랑 동갑", "비밀", "나 몇 살 같아?", "2살"]
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
    if talk.startswith("청월") or talk.startswith("서하린"):
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
    if talk.startswith("상런쳐") or talk.startswith("상런처") or talk.startswith("발사통") or talk.startswith("런처") or talk.startswith("런쳐"):
        await message.channel.send("에린이 아빠에요")
        await asyncio.sleep(1)
        await message.channel.send("안녕해요")
        await asyncio.sleep(1)
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
            await message.channel.send("준")
            await message.channel.send("식")
            await message.channel.send("화이팅!")
        else:
            await message.channel.send("기획팀이셔")
        return None
    if talk.startswith("근우"):
        if (random.randrange(0, 2) == 0):
            await message.channel.send("엄")
            await message.channel.send("준")
            await message.channel.send("식")
            await message.channel.send("화이팅!")
        else:
            await message.channel.send("기획팀이셔")
        return None
    if talk.startswith("세라") or talk.startswith("율아") or talk.startswith("민율아"):
        #Chat = ["귀여운 기획팀 분이야!", "세라님 귀엽지", "세라님 섹시하지", "세라님 섹시하고 깜찍하고 발랄하고 예쁘고 기엽고 매력적이고 이쁘고 에린이꺼❤️"]
        Chat = ["세라님 생일축하해!"]
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
        Chat = ["https://www.youtube.com/watch?v=2CGc9Ly11yo","https://www.youtube.com/watch?v=ao58vQDMVlQ", 
                "https://www.youtube.com/watch?v=JBoqPoqA8mM",
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
            await asyncio.sleep(0.5)
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

    if talk.startswith("도움말") or talk.startswith("명령어"):
        await Help(message)
        return None

    if talk.startswith("사진"):
        await message.channel.send(file=discord.File("에린님.png"))
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
    
    if talk.startswith("프로필"):
        embed = discord.Embed()
        embed.set_image(url=message.author.avatar_url)
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
        def is_me(m):
            if m.author == message.author:
                if not m.content.startswith("에린아 삭제") and not m.content.startswith("에린아 청소") and not m.content.startswith("에린아 지워"):
                    return True
        try:
            talk = talk.split(" ")
            _limit = int(talk[1])
        except (IndexError, ValueError):
            _limit = 100
        await message.add_reaction("⏳")
        await message.channel.purge(limit=_limit+1, check=is_me)
        await message.clear_reactions()
        await message.add_reaction("✅")
        return None
    
    if talk.startswith("팔로우생성"):
        if (message.channel.permissions_for(message.author).value & 0x00000008) != 0x00000008:
            await message.channel.send("권한이 없어")
            return None
        await message.channel.send(talk[6:])
        return None
    if talk.startswith("수정"):
        if (message.channel.permissions_for(message.author).value & 0x00000008) != 0x00000008:
            await message.channel.send("권한이 없어")
            return None
        messages = await message.channel.history(limit=100, oldest_first=False).flatten()
        for m in messages:
            if m.author.bot:
                await m.edit(content=talk[2:])
                await message.add_reaction("✅")
                return None
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
    
    if talk.startswith("역할삭제"):
        if (message.channel.permissions_for(message.author).value & 0x00000008) != 0x00000008:
            await message.channel.send("권한이 없어")
            return None
        role = message.guild.get_role(int(re.findall("\d+", talk.split(" ")[1])[0]))
        snsChannel = discord.utils.get(client.get_all_channels(), guild__name=message.guild.name, name=role.name.split("팔로워")[0])
        tmp_topic = re.findall("팔로워 \[\d+\]", snsChannel.topic)[0]
        for user in role.members:
            await user.remove_roles(role)
        _topic = snsChannel.topic.replace(tmp_topic, "팔로워 [0]")
        await message.add_reaction("✅")
        try:
            await snsChannel.edit(topic=_topic)
        except TypeError:
            pass
        return None
    
    global isPlaying
    if talk.startswith("구구단"):
        if isPlaying:
            await message.channel.send("이미 진행중인 게임이 있습니다.")
            return None
        await GuGuDan(message)
        return None
    
    if talk.startswith("369") or talk.startswith("삼육구"):
        if isPlaying:
            await message.channel.send("이미 진행중인 게임이 있습니다.")
            return None
        await ThreeSixNine(message)
        return None
    
    if talk.startswith("더게임오브데스") or talk.startswith("더 게임 오브 데스"):
        if isPlaying:
            await message.channel.send("이미 진행중인 게임이 있습니다.")
            return None
        await TheGameOfDeth(message)
        return None
    
    if talk.startswith("스탯"):
        await Stat(message, talk)
        return None
    
    if talk.startswith("대결") or talk.startswith("PVP") :
        if isPlaying:
            await message.channel.send("이미 진행중인 게임이 있어")
            return None
        await PVP(message, talk)
        return None
    
    if talk.startswith("능력치"):
        collection = db.Stat
        embed = discord.Embed(title="{0}님의 능력치".format(message.author.display_name), colour=discord.Colour.red())
        player = collection.find({"_id": message.author.id})[0]
        if talk.startswith("능력치 <@"):
            user_ID = int(re.findall("\d+", talk)[0])
            if not list(collection.find({"_id": user_ID})):
                await message.channel.send("능력치가 없어")
                return None
            embed = discord.Embed(title="{0}님의 능력치".format(message.guild.get_member(user_ID).display_name), colour=discord.Colour.red())
            player = collection.find({"_id" : user_ID})[0]
        else:
            if not list(collection.find({"_id": message.author.id})):
                await message.channel.send("능력치가 없어")
                return None
        embed.add_field(name="공격력", value=player.get("STR"), inline=True)
        embed.add_field(name="마력", value=player.get("INT"), inline=True)
        embed.add_field(name="체력", value=player.get("HP"), inline=True)
        embed.add_field(name="방어력", value=player.get("DEF"), inline=True)
        await message.channel.send(content=message.author.mention, embed=embed)
        return None


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

async def Sns(message, talk):
    sns_Talk = talk.split(" ")
    if sns_Talk[1] == "개설":
        if (message.channel.permissions_for(message.author).value & 0x00000008) != 0x00000008:
            await message.channel.send("권한이 없어")
            return None
        try:
            category = discord.utils.get(client.get_all_channels(), guild__name=message.guild.name, name="SNS")
            if len(discord.utils.get(client.get_all_channels(), guild__name=message.guild.name, name="SNS").channels) >= 20:
                count = 2
                while True:
                    category = discord.utils.get(client.get_all_channels(), guild__name=message.guild.name, name="SNS" + str(count))
                    if category == None:
                        if count == 2:
                            position = discord.utils.get(client.get_all_channels(), guild__name=message.guild.name, name="SNS").position + 1
                        else:
                            position = discord.utils.get(client.get_all_channels(), guild__name=message.guild.name, name="SNS" + str(count - 1)).position
                        category = await message.guild.create_category(name="SNS"+str(count))
                        await category.edit(position=position)
                        await category.create_text_channel(name="♥sns팔로우")
                    if len(category.channels) >= 20:
                        continue
                    break
            role = await message.guild.create_role(name="{0}팔로워".format(sns_Talk[2]), mentionable=True)
            topic = ""
            try:
                i = 3
                while True:
                    topic += sns_Talk[i] + " "
                    i+= 1
            except IndexError:
                pass
            new_Channel = await discord.Guild.create_text_channel(message.guild, name=sns_Talk[2],category=category, topic="{0}\n팔로워 [{1}]\n게시물 [0]".format(topic, 0))
        except IndexError:
            await message.channel.send("잘못 입력했어\nex)에린아 sns 개설 {채널이름} {소개}")
    return None

@client.event
async def on_voice_state_update(member, before, after):
    try:
        if member.voice.channel.category.name == "여관":
            await asyncio.sleep(2)
            if after.channel.name == "check in":
                if member in discord.utils.get(client.get_all_channels(), guild__name=member.guild.name, name="check in").members:
                    newChannel = await after.channel.category.create_voice_channel(name=str(random.randint(100,999)) + "호", reason="하바유보")
                    await newChannel.set_permissions(member, manage_channels=True)
                    await member.move_to(newChannel)
            elif after.channel.name == "private check in":
                if member in discord.utils.get(client.get_all_channels(), guild__name=member.guild.name, name="private check in").members:
                    newChannel = await after.channel.category.create_voice_channel(name="비밀방", reason="하바유보")
                    await newChannel.set_permissions(member.guild.get_role(629963963446198292), view_channel=False)
                    await newChannel.set_permissions(member, manage_channels=True)
                    await member.move_to(newChannel)
    except (AttributeError, TypeError):
        None
    try:
        if before.channel.category.name == "여관":
            if before.channel.name != "check in" and len(before.channel.members) == 0 and before.channel.name != "private check in":
                await before.channel.delete()
    except (AttributeError, discord.errors.NotFound):
        return None
                  
async def GuGuDan(message):
    global isPlaying
    isPlaying = True
    embed = discord.Embed(title="구구단을 외자", colour=discord.Colour.red())
    embed.add_field(name="게임 방법", value="\"에린아 참가\"를 입력해서 구구단을 외자에 참가해\n공격은 숫자 두개를 말하면 되고, ex)3 7\n방어는 두 수를 곱한 수를 말하면 돼 ex)21")
    await message.channel.send(embed=embed)
    Players = []
    def checkPlayer(m):
        return not m.author.mention in Players and m.content == "에린아 참가"
    try:
        while True:
            msg = await client.wait_for('message', timeout=10.0,check=checkPlayer)
            Players.append(msg.author.mention)
            await msg.add_reaction("✅")
            if len(Players) == 2:
                break
    except asyncio.TimeoutError:
        await message.channel.send("시간 초과")
        isPlaying = False
        return None
    playerIndex = random.randint(0, 1)
    currentPlayer = Players[playerIndex]
    def check(m):
        answer = list(map(int, m.content.split(" ")))
        return m.author.mention in Players and m.author.mention == currentPlayer and 1 <= answer[0] and answer[1] <= 9
    def check2(m):
        answer = list(map(int, m.content.split(" ")))
        return m.author.mention in Players and m.author.mention == currentPlayer
    embed = discord.Embed(title="구구단을 외자", colour=discord.Colour.red())
    embed.add_field(name="게임 시작", value="선공은 " + currentPlayer + "!!")
    embedMessage = await message.channel.send(embed=embed)
    timeOut = 5.0
    while True:
        try:
            msg = await client.wait_for('message', timeout=timeOut, check=check)
            answer = list(map(int, msg.content.split(" ")))
            await msg.delete()
            rightAnswer = answer[0] * answer[1]
            playerIndex = int(not playerIndex)
            currentPlayer = Players[playerIndex]
            embed.clear_fields()
            embed.add_field(name="{} * {} = ?".format(answer[0], answer[1]), value=currentPlayer)
            embed.set_footer(text="시간제한 : {}초".format(timeOut))
            await embedMessage.edit(embed=embed)
            msg = await client.wait_for('message', timeout=timeOut, check=check2)
            if int(msg.content) == rightAnswer:
                await msg.add_reaction("✅")
                timeOut -= 0.5
                if timeOut < 1:
                    timeOut = 1
                await asyncio.sleep(1)
                await msg.delete()
                embed.clear_fields()
                embed.add_field(name="공격", value=currentPlayer)
                embed.set_footer(text="시간제한 : {}초".format(timeOut))
                await embedMessage.edit(embed=embed)
                continue
            else:
                embed.clear_fields()
                embed.add_field(name="승리", value=Players[int(not playerIndex)])
                embed.add_field(name="패배", value=currentPlayer)
                embed.set_footer(text="정답 : {}".format(rightAnswer))
                await embedMessage.edit(embed=embed)
                break
        except asyncio.TimeoutError:
            embed.clear_fields()
            embed.add_field(name="승리", value=Players[int(not playerIndex)])
            embed.add_field(name="패배", value=currentPlayer)
            embed.set_footer(text="시간 초과")
            await embedMessage.edit(embed=embed)
            break
        except ValueError:
            embed.clear_fields()
            embed.add_field(name="승리", value=Players[int(not playerIndex)])
            embed.add_field(name="패배", value=currentPlayer)
            embed.set_footer(text="다른 값 입력")
            await embedMessage.edit(embed=embed)
            break
    isPlaying = False
    return None

async def ThreeSixNine(message):
    global isPlaying
    isPlaying = True
    embed = discord.Embed(title="369", colour=discord.Colour.red())
    embed.add_field(name="게임 방법", value="\"에린아 참가\"를 입력해서 369에 참가해\n1부터 순서대로 숫자를 입력하면 돼 ex)1\n숫자에 3, 6, 9가 들어가면 들어간 횟수만큼 짝을 입력해 ex)3 -> 짝, 36 -> 짝짝")
    await message.channel.send(embed=embed)
    Players = []
    def checkPlayer(m):
        return not m.author.mention in Players and m.content == "에린아 참가"
    try:
        while True:
            msg = await client.wait_for('message', timeout=10.0,check=checkPlayer)
            Players.append(msg.author.mention)
            await msg.add_reaction("✅")
    except asyncio.TimeoutError:
        if len(Players) < 2:
            await message.channel.send("인원이 부족해.")
            isPlaying = False
            return None
        pass
    currentPlayer = Players[0]
    def check(m):
        return m.author.mention in Players and m.author.mention == currentPlayer
    embed = discord.Embed(title="369", colour=discord.Colour.red())
    order = ""
    num = 1
    for p in Players:
        order += "{0}. {1}".format(num, p)
        num += 1
    embed.add_field(name="게임 시작", value="순서는\n " + order)
    embedMessage = await message.channel.send(embed=embed)
    timeOut = 5.0
    num = 0
    Answer = 1
    JJack = 0
    JJackTF = False
    await asyncio.sleep(1)
    while True:
        try:
            embed.clear_fields()
            embed.add_field(name="이번 순서", value=currentPlayer)
            embed.set_footer(text="시간제한 : {}초".format(timeOut))
            await embedMessage.edit(embed=embed)
            msg = await client.wait_for('message', timeout=timeOut, check=check)
            for i in [3, 6, 9]:
                if str(i) in str(Answer):
                    JJack += 1
                    JJackTF = True
            if (JJackTF and msg.content == ("짝" * JJack)) or (msg.content == str(Answer)):
                await msg.add_reaction("✅")
                timeOut -= 0.5
                if timeOut < 1:
                    timeOut = 1
                await asyncio.sleep(1)
                await msg.delete()
                num += 1
                if num >= len(Players):
                    num = 0
                currentPlayer = Players[num]
                Answer += 1
                JJack = 0
                JJackTF = False
                continue
            else:
                embed.clear_fields()
                embed.add_field(name="패배", value=currentPlayer)
                embed.set_footer(text="")
                await embedMessage.edit(embed=embed)
                break
        except asyncio.TimeoutError:
            embed.clear_fields()
            embed.add_field(name="패배", value=currentPlayer)
            embed.set_footer(text="시간 초과")
            await embedMessage.edit(embed=embed)
            break
        except ValueError:
            embed.clear_fields()
            embed.add_field(name="패배", value=currentPlayer)
            embed.set_footer(text="다른 값 입력")
            await embedMessage.edit(embed=embed)
            break
    isPlaying = False
    return None

async def TheGameOfDeth(message):
    global isPlaying
    isPlaying = True
    embed = discord.Embed(title="더 게임 오브 데스", colour=discord.Colour.red())
    embed.add_field(name="게임 방법", value="\"에린아 참가\"를 입력해서 더 게임 오브 데스에 참가해\n술래는 숫자를 입력해 ex)3" +
                    "\n술래가 입력을 마치면 모든 사람들은 다른 사람을 멘션해 ex)@에린\n술래부터 시작해서 멘션당한 사람에게 넘어가면서 카운트하고 술래가 입력한 숫자에서 멈춘 사람이 패배야")
    embed.add_field(name="주의사항", value="술래는 5초안에 숫자를 입력해야해\n멘션후 메세지에 ✅이모지가 있어야해")
    await message.channel.send(embed=embed)
    Players = []
    def checkPlayer(m):
        return not m.author.mention in Players and m.content == "에린아 참가"
    try:
        while True:
            msg = await client.wait_for('message', timeout=10.0,check=checkPlayer)
            Players.append(msg.author.mention)
            await msg.add_reaction("✅")
    except asyncio.TimeoutError:
        if len(Players) < 2:
            await message.channel.send("인원이 부족해.")
            isPlaying = False
            return None
        pass
    def check(m):
        return m.author.mention in Players
    def check2(m):
        return m.author.mention in Players and m.mentions[0].mention in Players and m.content != m.author.mention
    embed = discord.Embed(title="더 게임 오브 데쓰", colour=discord.Colour.red())
    embed.add_field(name="게임 시작", value="신이난다~")
    embedMessage = await message.channel.send(embed=embed)
    await asyncio.sleep(1)
    embed.clear_fields()
    embed.add_field(name="게임 시작", value="재미난다~")
    await embedMessage.edit(embed=embed)
    await asyncio.sleep(1)
    embed.clear_fields()
    embed.add_field(name="게임 시작", value="더 게임 오브 데쓰~")
    await embedMessage.edit(embed=embed)
    tagger = Players[random.randrange(0, len(Players))]
    await asyncio.sleep(1)
    try:
        embed.clear_fields()
        embed.add_field(name="술래", value=tagger)
        await embedMessage.edit(embed=embed)
        msg = await client.wait_for('message', timeout=10, check=check)
        count = int(msg.content)
        await msg.delete()
        embed.clear_fields()
        embed.add_field(name="횟수 : {}".format(count), value="다른 사람을 멘션해줘")
        await embedMessage.edit(embed=embed)
        playerChoice = {}
        for i in range(0, len(Players)):
            msg = await client.wait_for('message', timeout=10, check=check2)
            playerChoice[msg.author.mention] = msg.mentions[0].mention
            await msg.add_reaction("✅")
                    
        for j in range(0, count):
            embed.clear_fields()
            embed.add_field(name="카운트 시작", value="{} -> {}".format(tagger, playerChoice[tagger]))
            embed.set_footer(text="횟수 : {}/{}".format(j+1, count))
            await embedMessage.edit(embed=embed)
            tagger = playerChoice[tagger]
            await asyncio.sleep(1)
        embed.add_field(name="패배", value=tagger)
        await embedMessage.edit(embed=embed)
    except asyncio.TimeoutError:
        embed.clear_fields()
        embed.add_field(name="오류", value="ㅡnㅡ")
        embed.set_footer(text="시간 초과")
        await embedMessage.edit(embed=embed)
    except ValueError:
        embed.clear_fields()
        embed.add_field(name="오류", value="ㅡnㅡ")
        embed.set_footer(text="시간 초과")
        await embedMessage.edit(embed=embed)
    isPlaying = False
    return None

async def PVP(message, talk):
    global isPlaying
    isPlaying = True
    PVP_Talk = talk.split(" ")
    collection = db.Stat
    player1_id = message.author.id
    player2_id = int(re.findall("\d+", PVP_Talk[1])[0])
    player1 = message.guild.get_member(player1_id)
    player2 = message.guild.get_member(player2_id)
    if not list(collection.find({"_id": player1_id})) or not list(collection.find({"_id": player2_id})):
        await message.channel.send("스탯이 없어")
        return None
    def switch(value):
        # 공 - 마 - 체 - 방
        return {
            0: ["공격력", "STR"],
            1: ["마력", "INT"],
            2: ["체력", "HP"],
            3: ["방어력", "DEF"]
        }.get(value)
    embed = discord.Embed(title="{0}님과 {1}님의 대결".format(player1.display_name, player2.display_name), colour=discord.Colour.red())
    embedMessage = await message.channel.send(embed=embed)
    player1_Stat = collection.find({"_id": player1_id})[0]
    player2_Stat = collection.find({"_id": player2_id})[0]
    winCount = 0 #양수면 player1승리, 음수면 player2승리, 0이면 무승부
    for i in range(0, 4):
        title, stat = switch(i)
        embed.add_field(name=title, value="승자 : ", inline=False)
        embed.add_field(name=player1.display_name, value="{0} : {1}".format(title, player1_Stat.get(stat)), inline=True)
        embed.add_field(name=player2.display_name, value="{0} : {1}".format(title, player2_Stat.get(stat)), inline=True)
        await embedMessage.edit(embed=embed)
        if player1_Stat.get(stat) > player2_Stat.get(stat):
            winCount += 1
            winPlayer = player1
        else:
            winCount -= 1
            winPlayer = player2
        await asyncio.sleep(1)
        embed.set_field_at(i, name=title, value="승자 : {0}".format(winPlayer.display_name), inline=False)
        embed.remove_field(i + 1)
        embed.remove_field(i + 1)
        await embedMessage.edit(embed=embed)
        await asyncio.sleep(1)
    if winCount == 0:
        await message.channel.send("무승부")
    elif winCount > 0:
        await message.channel.send("{} 승리".format(player1.mention))
    else:
        await message.channel.send("{} 승리".format(player2.mention))

    isPlaying = False
    
async def Stat(message, talk):
    #순서는 공격력 - 마력 - 체력 - 방어력
    stat_Talk = talk.split(" ")
    collection = db.Stat
    if len(stat_Talk) < 2:
        embed = discord.Embed(title="{0}님의 스탯".format(message.author.display_name), colour=discord.Colour.red())
        player = collection.find({"_id": message.author.id})[0]
        embed.add_field(name="힘", value=player.get("str"), inline=False)
        embed.add_field(name="체력", value=player.get("hp"), inline=False)
        embed.add_field(name="지능", value=player.get("int"), inline=False)
        embed.add_field(name="마력", value=player.get("mp"), inline=False)
        embed.add_field(name="신성", value=player.get("fth"), inline=False)
        embed.add_field(name="리듬감", value=player.get("ryt"), inline=False)
        embed.add_field(name="손재주", value=player.get("dex"), inline=False)
        embed.set_footer(text="스탯포인트 : {}".format(player.get("!statPoint")))
        await message.channel.send(content=message.author.mention, embed=embed)
        return None

    if stat_Talk[1] == "생성":
        if not list(collection.find({"_id" : message.author.id})):
            utcnow = datetime.datetime.utcnow()
            time_gap = datetime.timedelta(hours=9)
            now = utcnow + time_gap
            collection.update_one({"_id": message.author.id}, {
                "$setOnInsert": {"!name": message.author.display_name, "!creation_Date": now, "!statPoint" : 0, "STR": 0, "INT": 0,
                                 "HP": 0, "DEF": 0, "str": 0, "int": 0, "hp": 0, "mp": 0, "fth" : 0, "ryt" : 0, "dex" : 0}}, upsert=True)#fth : 신성력, ryt : 리듬감, dex : 손재주
            await message.add_reaction("✅")
            return None
        else:
            await message.channel.send("이미 생성되었어")
            return None

    if not list(collection.find({"_id": message.author.id})):
        await message.channel.send("스탯이 없어\n'에린아 스탯 생성' 으로 스탯을 만들어")
        return None

    collection.update_one({"_id": message.author.id}, {"$set": {"!name": message.author.display_name}}, upsert=True)
    if stat_Talk[1] == "힘" or stat_Talk[1] == "체력" or stat_Talk[1] == "지능" or stat_Talk[1] == "마력" or stat_Talk[1] == "신성력" or stat_Talk[1] == "리듬감" or stat_Talk[1] == "손재주":
        if len(stat_Talk) == 2:
            sp = 1
        else:
            sp = int(stat_Talk[2])
        def switch(value):
            #공 - 마 - 체 - 방
            return {
                "힘": ["str", [10, 0, 5, 5]],
                "체력": ["hp", [0, 0, 10, 10]],
                "지능": ["int", [10, 5, 0, 5]],
                "마력": ["mp", [5, 10, 0, 5]],
                "신성력": ["fth", [10, 5, 5, 0]],
                "리듬감": ["ryt", [10, 10, 0, 0]],
                "손재주": ["dex", [10, 0, 10, 0]]
            }.get(value)
        stat, statList = switch(stat_Talk[1])
        player = collection.find({"_id": message.author.id})[0]
        if player.get("!statPoint") < sp:
            await message.channel.send("스탯포인트가 부족해\n스탯포인트 : " + str(player.get("!statPoint")))
            return None
        collection.update_one({"_id": message.author.id}, {"$inc": {stat: sp}}, upsert=True)
        collection.update_one({"_id": message.author.id}, {"$inc": {"STR": statList[0] * sp}}, upsert=True)
        collection.update_one({"_id": message.author.id}, {"$inc": {"INT": statList[1] * sp}}, upsert=True)
        collection.update_one({"_id": message.author.id}, {"$inc": {"HP": statList[2] * sp}}, upsert=True)
        collection.update_one({"_id": message.author.id}, {"$inc": {"DEF": statList[3] * sp}}, upsert=True)
        collection.update_one({"_id": message.author.id}, {"$inc": {"!statPoint": -sp}}, upsert=True)
        await message.add_reaction("✅")
        return None

    if stat_Talk[1].startswith("<@"):
        user_ID = int(re.findall("\d+", stat_Talk[1])[0])
        if not list(collection.find({"_id": user_ID})):
            await message.channel.send("스탯이 없어")
            return None
        embed = discord.Embed(title="{0}님의 스탯".format(message.guild.get_member(user_ID).display_name), colour=discord.Colour.red())
        player = collection.find({"_id" : user_ID})[0]
        embed.add_field(name="힘", value=player.get("str"), inline=False)
        embed.add_field(name="체력", value=player.get("hp"), inline=False)
        embed.add_field(name="지능", value=player.get("int"), inline=False)
        embed.add_field(name="마력", value=player.get("mp"), inline=False)
        embed.add_field(name="신성", value=player.get("fth"), inline=False)
        embed.add_field(name="리듬감", value=player.get("ryt"), inline=False)
        embed.add_field(name="손재주", value=player.get("dex"), inline=False)
        embed.set_footer(text="스탯포인트 : {}".format(player.get("!statPoint")))
        await message.channel.send(content=message.guild.get_member(user_ID).mention,embed=embed)
        return None

@client.event
async def on_reaction_add(reaction, user):
    if user.bot:
        return None
    try:
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
    except (TypeError, IndexError):
        return None
    return None

async def Reaction(payload, user, msg, tf):
    if msg.content.startswith("__SNS 팔로우__"):
        follow = msg.content.split("\n")
        for i in follow:
            i = i.split(":")
            if str(payload.emoji) == i[0]:
                role = user.guild.get_role(int(re.findall("\d+", i[1])[0]))
                snsChannel = discord.utils.get(client.get_all_channels(), guild__name=user.guild.name, name=role.name.split("팔로워")[0])
                tmp_topic = re.findall("팔로워 \[\d+\]", snsChannel.topic)[0]
                if tf:
                    count = 0
                    for c in msg.reactions:
                        if payload.emoji.name == c.emoji:
                            count = c.count
                    if role in user.roles:
                        return None
                    await user.add_roles(role)
                else:
                    count = 0
                    for c in msg.reactions:
                        if payload.emoji.name == c.emoji:
                            count = c.count
                    if not role in user.roles:
                        return None
                    await user.remove_roles(role)
                _topic = snsChannel.topic.replace(tmp_topic, "팔로워 [%s]" % str(count))
                try:
                    await snsChannel.edit(topic=_topic)
                except TypeError:
                    pass
        return None

@client.event
async def on_raw_reaction_add(payload):
    if payload.member.bot:
        return None
    channel = discord.utils.get(client.get_all_channels(), id=payload.channel_id)
    if not channel.category.name.startswith("SNS"):
        return None
    msg = await channel.fetch_message(payload.message_id)
    await Reaction(payload, payload.member, msg, True)
    return None

@client.event
async def on_raw_reaction_remove(payload):
    channel = discord.utils.get(client.get_all_channels(), id=payload.channel_id)
    user = discord.utils.get(client.get_all_members(), id=payload.user_id)
    msg = await channel.fetch_message(payload.message_id)
    await Reaction(payload, user, msg, False)
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
                                     "에린아 로또 선택 <숫자> : <숫자> 번호 로또를 구매합니다\n"
                                     "에린아 로또 확인 : 본인의 로또 번호를 확인합니다", inline=False)
    embed.add_field(name="포인트", value="에린아 포인트 : 자신의 포인트를 확인합니다.\n"
                                     "에린아 출석 : 한번 출석에 10~300의 포인트를 받습니다. 누적되면 추가로 포인트를 얻습니다.\n"
                                     "에린아 포인트 순위 : 서버 내 포인트 순위를 확인합니다.\n"
                                     "에린아 포인트 선물 <멘션> <포인트> :<멘션>에게 <포인트>만큼 포인트를 선물합니다", inline=False)
    embed.add_field(name="기타 기능", value="에린아 삭제 <갯수>, 에린아 초대, 에린아 닉네임 <변경할닉네임>, 에린아 구구단, 에린아 가위바위보, 에린아 검색 <내용>, 에린아 고양이, 에린아 시간, 에린아 369", inline=False)
    await message.channel.send(embed=embed)
    return

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
