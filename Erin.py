import discord
import random
import datetime
import time
import pickle
import re
import operator
from discord.ext import tasks
import os

client = discord.Client()
prefix = "에린아 "

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("호스팅 테스트")
    Daily.start()
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if not(message.content.startswith(prefix)) or message.author.bot:
        return None

    talk = message.content[len(prefix):]

    if talk.startswith("초기화"):
        with open("Lotto.pkl", 'w') as f:
            f.write("")
        with open("Lotto.txt", 'w') as f:
            f.write("")
        with open("Caution.txt", 'w') as f:
            f.write("")
        with open("Point.pkl", 'w') as f:
            f.write("")
        with open("Daily.txt", 'w') as f:
            f.write("")
        with open("DailyCount.pkl", 'w') as f:
            f.write("")
        await message.channel.send("초기화 되었습니다")
        return None
    if talk.startswith("안녕"):
        Chat = ["안녕", "응?", "왜?", "어?", "왜 불러?"]
        await message.channel.send(Chat [random.randrange(0, len(Chat))])
        return None
    if talk.startswith("뭐해"):
        Chat = ["니 생각", "유튜브 봐", "내 생각", "그냥 있어"]
        await message.channel.send(Chat [random.randrange(0, len(Chat))])
        return None
    if talk.startswith("심심해"):
        Chat = ["내 생각 하면 되지", "나두", "나랑 놀자"]
        await message.channel.send(Chat [random.randrange(0, len(Chat))])
        return None
    if talk.startswith("바보"):
        Chat = [";;", "너는?", "멍청이", "너가 더", "응."]
        await message.channel.send(Chat [random.randrange(0, len(Chat))])
        return None
    if talk.startswith("멍청이"):
        Chat = [";;", "너는?", "바보", "너가 더", "응."]
        await message.channel.send(Chat [random.randrange(0, len(Chat))])
        return None
    if talk.startswith("보고싶었어"):
        Chat = ["나도", "나도 보고 싶었어", "!"]
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
        Chat = ["나 여자같아 남자같아?", "당연히 여자 아냐?", "그건 물어봐야 아니?"]
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
        Chat = ["음악관장이시지", "골든 리트리버"]
        await message.channel.send(Chat [random.randrange(0, len(Chat))])
        return None
    if talk.startswith("피아"):
        Chat = ["1년 임시 대신관이야", "엄청 귀여우셔"]
        await message.channel.send(Chat [random.randrange(0, len(Chat))])
        return None
    if talk.startswith("바다나라"):
        Chat = ["대마법사셔", "건들면 뭅니다"]
        await message.channel.send(Chat[random.randrange(0, len(Chat))])
        return None
    if talk.startswith("만두"):
        Chat = ["기사단장이지, 곧 간대","^^7"]
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
    if talk.startswith("상런쳐"):
        await message.channel.send("안녕해요")
        time.sleep(1)
        await message.channel.send("반갑다요?")
        return None
    if talk.startswith("권혁"):
        Chat = ["아빠"]
        await message.channel.send(Chat [random.randrange(0, len(Chat))])
        return None
    if talk.startswith("Teacat"):
        Chat = ["나를 개방해주신 분이야!"]
        await message.channel.send(Chat[random.randrange(0, len(Chat))])
        return None
    if talk.startswith("안내팀"):
        Chat = ["우리 게임 tutorial진행해주는 팀!"]
        await message.channel.send(Chat [random.randrange(0, len(Chat))])
        return None
    if talk.startswith("디자인팀"):
        Chat = ["우리 게임에 쓰이는 모든 그림을 맡아주는 팀!"]
        await message.channel.send(Chat [random.randrange(0, len(Chat))])
        return None
    if talk.startswith("기획팀"):
        Chat = ["우리 서버 이벤트 기획하는 팀!"]
        await message.channel.send(Chat [random.randrange(0, len(Chat))])
        return None
    if talk.startswith("라호"):
        Chat = ["배경을 도맡아 그려주시는 디자인팀의 금손!"]
        await message.channel.send(Chat [random.randrange(0, len(Chat))])
        return None
    if talk.startswith("마린"):
        Chat = ["목소리 좋고 너무 예쁜 안내팀!"]
        await message.channel.send(Chat [random.randrange(0, len(Chat))])
        return None
    if talk.startswith("도서진"):
        Chat = ["캐릭터를 도맡아 그려주시는 완전 금손 디자인팀!"]
        await message.channel.send(Chat[random.randrange(0, len(Chat))])
        return None
    if talk.startswith("권지원"):
        Chat = ["소품 위주로 그려주시는 완전 예쁜 디자인팀 겸 안내팀!"]
        await message.channel.send(Chat [random.randrange(0, len(Chat))])
        return None
    if talk.startswith("밤연"):
        Chat = ["귀여우시고 목소리 예쁘신 안내팀!"]
        await message.channel.send(Chat [random.randrange(0, len(Chat))])
        return None
    if talk.startswith("가온"):
        Chat = ["유일한 기획팀인 금수저"]
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
        user_ID = message.author.id
        with open("Daily.txt", 'r') as f:
            for line in f:
                if line.startswith(str(user_ID)):
                    await message.channel.send("이미 출석 했어")
                    return None
        dailylist = []
        with open("DailyCount.pkl", 'rb') as f:
            while True:
                try:
                    data = pickle.load(f)
                except EOFError:
                    break
                dailylist.append(data)
            dailylist = dict(dailylist)
        count = dailylist.get(user_ID)
        point = random.randrange(10, 300)
        pointmsg = str(point)
        if count == None:
            count = 1
        elif count % 50 == 0:
            point += 1000
            pointmsg += " + 1000(%d0일 누적)" % ((count / 50) * 5)
        elif count % 10 == 0:
            point += 100
            pointmsg += " + 100(%d0일 누적)" % (count / 10)
        with open("Point.pkl", "rb") as f:
            datalist = []
            while True:
                try:
                    data = pickle.load(f)
                except EOFError:
                    break
                datalist.append(data)
            datalist = dict(datalist)
            user_point = datalist.get(message.author.id)
            if user_point == None:
                user_point = 0
        with open("Point.pkl", "ab") as f:
            pickle.dump([user_ID, point + user_point], f)
        with open("Daily.txt", 'a') as f:
            f.write(str(user_ID) + "\n")
        with open("DailyCount.pkl", 'ab') as f:
            pickle.dump([user_ID, count + 1], f)

        embed = discord.Embed(title="%-6s" % message.author.display_name, colour=discord.Colour.red())
        embed.add_field(name="포인트", value=pointmsg, inline=False)
        embed.add_field(name="출석일수", value=count, inline=False)
        embed.add_field(name="총포인트", value=point+user_point, inline=False)
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

    #if talk.startswith("음성채팅"):
    #    await VoiceChannel(message, talk)
    #    return None

    if talk.startswith("sns"):
        await Sns(message, talk)
        return None

    if talk.startswith("구매"):
        await Buy(message, talk)
        return None


async def Lotto(message, talk):
    lotto_Talk = talk.split(" ")
    if lotto_Talk[1] == "초기화":
        with open("Lotto.pkl", 'w') as f:
            f.write("")
        with open("Lotto.txt", 'w') as f:
            f.write("")
        await message.channel.send("로또를 초기화했습니다")
        return None
    lotto_List = []
    with open("Lotto.txt", 'r') as f:
        for line in f:
            if line.startswith(str(message.author.id)):
                lotto_List.append(str(line[19:25]))
    with open("Lotto.pkl", "rb") as f:
        datalist = []
        while True:
            try:
                data = pickle.load(f)
            except EOFError:
                break
            datalist.append(data)
        datalist = dict(datalist)
        count = datalist.get(str(message.author.id) + "Count")
        if count==None:
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
        with open("Lotto.txt", 'a') as f:
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
                    f.write(str(message.author.id) + " " + lotto + "\n")
                    break
            with open("Lotto.pkl", "ab") as f:
                pickle.dump([str(message.author.id) + "Count" , count + _count] , f)
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
        with open("Lotto.txt", "a") as f:
            f.write(str(message.author.id) + " " + lotto + "\n", f)
            await message.channel.send(lotto + "\n로또를 입력했습니다")
            with open("Lotto.pkl", "ab") as f:
                pickle.dump([str(message.author.id) + "Count" , count + 1] , f)
    if lotto_Talk[1] == "확인":
        await message.channel.send(str(message.author.name)+ " 님의 로또 : \n" + str(lotto_List))
        return None
    if lotto_Talk[1] == "전체":
        lottoText = ""
        lottos = []
        with open("Lotto.txt", 'r') as f:
            for line in f:
                User = client.get_user(int(line[:18]))
                for l in lottos:
                    if l.startswith(User.name):
                        lottos[lottos.index(l)] += ", [" + str(line[19:25]) + "]"
                        break
                else:
                    lottos.append(User.name + " : [" + str(line[19:25]) + "]")
            for i in range(0, len(lottos)):
                lottoText += lottos[i] + "\n"
        embed = discord.Embed(title="로또 전체", colour=discord.Colour.red())
        embed.add_field(name="로또", value= lottoText, inline=False)
        embed.set_footer(text="1등하구싶다")
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
    if len(point_Talk) < 2:
        with open("Point.pkl", "rb") as f:
            datalist = []
            while True:
                try:
                    data = pickle.load(f)
                except EOFError:
                    break
                datalist.append(data)
            datalist = dict(datalist)
            point = datalist.get(message.author.id)
            if point == None:
                point = 0
            embed = discord.Embed(title=message.author.display_name, colour=discord.Colour.red())
            embed.add_field(name="포인트", value="{0} 포인트".format(point), inline=False)
            await message.channel.send(embed=embed)
            return None

    if point_Talk[1].startswith("<@"):
        User_ID = int(re.findall("\d+", point_Talk[1])[0])
        with open("Point.pkl", "rb") as f:
            datalist = []
            while True:
                try:
                    data = pickle.load(f)
                except EOFError:
                    break
                datalist.append(data)
            datalist = dict(datalist)
            point = datalist.get(User_ID)
            if point == None:
                point = 0
            embed = discord.Embed(title=client.get_user(User_ID).display_name, colour=discord.Colour.red())
            embed.add_field(name="포인트", value="{0} 포인트".format(point), inline=False)
            await message.channel.send(embed=embed)
            return None

    if point_Talk[1] == "지급":
        if (message.channel.permissions_for(message.author).value & 0x00000008) != 0x00000008:
            await message.channel.send("권한이 없어")
            return None
        User_ID = int(re.findall("\d+", point_Talk[2])[0])
        datalist = []
        with open("Point.pkl", "rb") as f:
            while True:
                try:
                    data = pickle.load(f)
                except EOFError:
                    break
                datalist.append(data)
        datalist = dict(datalist)
        try:
            point = datalist.get(User_ID)
        except TypeError:
            point = 0
            pass
        with open("Point.pkl", "ab") as f:
            if point == None:
                point = 0
            pickle.dump([User_ID , point + int(point_Talk[3])], f)
        await message.channel.send("{0}에게 {1}포인트 지급했어".format(client.get_user(User_ID).name, int(point_Talk[3])))
        return None

    if point_Talk[1] == "반환":
        if (message.channel.permissions_for(message.author).value & 0x00000008) != 0x00000008:
            await message.channel.send("권한이 없어")
            return None
        User_ID = int(re.findall("\d+", point_Talk[2])[0])
        datalist = []
        with open("Point.pkl", "rb") as f:
            while True:
                try:
                    data = pickle.load(f)
                except EOFError:
                    break
                datalist.append(data)
            datalist = dict(datalist)
        with open("Point.pkl", "ab") as f:
            point = datalist.get(User_ID)
            if point == None:
                point = 0
            point -= int(point_Talk[3])
            if point < 0:
                point = 0
            pickle.dump([User_ID, point], f)
        await message.channel.send("{0}에게 {1}포인트를 반환했어".format(client.get_user(User_ID).name, point_Talk[3]))
        return None

    if point_Talk[1] == "선물":
        User_ID = int(re.findall("\d+", point_Talk[2])[0])
        if User_ID == message.author.id:
            await message.channel.send("너가 너한테 선물주게..?")
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
        if datalist.get(message.author.id) == None or datalist.get(message.author.id) >= int(point_Talk[3]):
            await message.channel.send("포인트가 부족해")
            return None

        with open("Point.pkl", "ab") as f:
            point1 = datalist.get(User_ID)
            if point1 == None:
                point1 = 0
            pickle.dump([User_ID , point1 + int(point_Talk[3])], f)
            point2 = datalist.get(message.author.id)
            if point2 == None:
                point2 = 0
            pickle.dump([message.author.id ,  point2 - int(point_Talk[3])], f)
        await message.channel.send("{0}에게 {1}포인트를 선물했어".format(client.get_user(User_ID).name, point_Talk[3]))
        return None

    if point_Talk[1] == "순위":
        datalist = []
        with open("Point.pkl", "rb") as f:
            while True:
                try:
                    data = pickle.load(f)
                except EOFError:
                    break
                datalist.append(data)
            datalist = dict(datalist)
        sdict = sorted(datalist.items(), reverse=True, key=operator.itemgetter(1))
        embed = discord.Embed(title="포인트 순위", colour=discord.Colour.red())
        ranking = 1
        rank = ""
        for i in sdict:
            if i[1] == 0:
                continue
            member = message.guild.get_member(i[0])
            rank += "{0}. {1}포인트 - {2}\n".format(ranking , str(i[1]), member.display_name)
            ranking += 1
        embed.add_field(name="(포인트) - (유저)", value=rank, inline=False)
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

# async def VoiceChannel(message, talk):
#     voice_Talk = talk.split(" ")
#     if voice_Talk[1]=="만들기":
#         try:
#             new_Channel = await discord.Guild.create_voice_channel(message.guild, voice_Talk[2],category=message.channel.category)
#             if len(voice_Talk) == 4:
#                 await new_Channel.edit(user_limit=int(voice_Talk[3]))
#         except IndexError:
#             await message.channel.send("채널 이름을 입력해\nex)에린아 음성채널 만들기 카르멘")

#     if voice_Talk[1] == "삭제":
#         channel = discord.utils.get(client.get_all_channels(), guild__name=message.guild.name, name=voice_Talk[2])
#         await channel.delete()
#     return None

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
    if now.hour == 0:
        with open("Lotto.pkl", 'w') as f:
            f.write("")
        with open("Daily.txt", 'w') as f:
            f.write("")

async def Help(message):
    embed = discord.Embed(title= "에린이 도움말",colour=discord.Colour.red())
    embed.add_field(name="로또", value="에린아 로또 랜덤 <숫자> : 로또를 <숫자>번 랜덤으로 뽑습니다.\n"
                                     "에린아 로또 선택 <숫자> : <숫자> 번호 로또를 구매합니다?\n"
                                     "에린아 로또 확인 : 본인의 로또 번호를 확인합니다", inline=False)
    embed.set_footer(text="셋푸터")
    await message.channel.send(embed=embed)
    return

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
