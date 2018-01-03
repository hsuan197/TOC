#coding=utf-8

from transitions.extensions import GraphMachine

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )

    def go_v(self, update):
        text = update.message.text
        return text == 'vast & hazy'

    def go_i(self, update):
        text = update.message.text
        return text.encode('utf-8') == '次等秘密'

    def go_w(self, update):
        text = update.message.text
        return text.encode('utf-8') == '與浪之間'

    def go_e(self, update):
        text = update.message.text
        return text.encode('utf-8') == '歸屬'

    def go_t(self, update):
        text = update.message.text
        return text.encode('utf-8') == '食人夢'

    def go_introduction(self, update):
        text = update.message.text
        return text.encode('utf-8') == '介紹'
	
    def go_find_album(self, update):
        text = update.message.text
        return text.encode('utf-8') == '專輯'

    def go_find_song(self, update):
        text = update.message.text
        return text.encode('utf-8') == '歌曲'

    def on_enter_introduction(self, update):
        update.message.reply_text("Vast & Hazy\n\n當你滿溢 讓我推送你奔向大海匯流\n當你乾涸 讓我守候你直至再度盈豐\n若你的生命是條河流 我願作你的出口")
        update.message.reply_text("吉他手/團長: 易祺\n主唱: 大咖")
        self.go_back(update)

    def on_exit_introduction(self, update):
        print('Leaving state1')

    def on_enter_find_album(self, update):
        update.message.reply_text("要找哪張專輯呢？\n\nvast & hazy\n次等秘密")

    def on_exit_find_album(self, update):
        print('Leaving find_album')

    def on_enter_a_insignificant_Secret(self, update):
        update.message.reply_text("專輯介紹\n\n如果漸漸失去年少的無畏，那麼懷疑自己、懷疑世界的不安全感就會趁虛而入。你會發現，世界上並沒有所謂非黑即白，多的是灰色地帶與似是而非，而你必須在這沒有邊際的範圍裡做出各種選擇，你通常無從得知等在後頭的是什麼。當慢慢看清前方未知的輪廓時，想後悔也已經來不及，只能隨著時間持續往前走。\n一路上你會有許多想要擁有的東西，但很快地你會知道，不論多努力總會有得不到的時候。你開始懷疑，是不是只要安安份份地過著平凡的日子然後安靜地死去就好了呢？當夢想太大太多太貪心，經歷了那麼多的痛苦，卻並不一定能將它們抓在手裡，那你該怎麼為自己的生命下評斷？\n不是每個夢想都有實現的一天。最想成為的那個模樣，常常只能如同影子般藏在自己身後，最終成為無人知曉的、秘密的第二人格。")
        update.message.reply_text("專輯歌曲\n\n與浪之間 (Waves)\n歸屬 (Eleanor)\n食人夢 (The City is Eating Me Alive)")
        self.go_back(update)

    def on_exit_a_insignificant_Secret(self, update):
        print('Leaving a_insignificant_Secret')

    def on_enter_a_vast_and_hazy(self, update):
        update.message.reply_text("專輯介紹\n\n我們一直停不下來地長大\n每一秒都被什麼追趕著。\n那年曾經偷偷作過的夢，\n和那些大大小小的、藏在心裡一直沒變的渴望，\n你是不是已經快要忘記它們的模樣?\n\nVast & Hazy是在樂團正式成立時同步發表的單曲。\n敘述著在音樂路途上，\n不斷地尋尋覓覓、跌跌撞撞， 最終相遇了的三個人\n一起踏上了這段旅程。")
        update.message.reply_text("專輯歌曲\n\nvast & hazy")
        self.go_back(update)

    def on_exit_a_vast_and_hazy(self, update):
        print('Leaving a_insignificant_Secret')

    def on_enter_find_song(self, update):
        update.message.reply_text("要找哪首歌呢？\n\nvast & hazy\n與浪之間 (Waves)\n歸屬 (Eleanor)\n食人夢 (The City is Eating Me Alive)")

    def on_exit_find_song(self, update):
        print('Leaving find_song')

    def on_enter_s_eleanor(self, update):
		update.message.reply_text("https://www.youtube.com/watch?v=5jFW6PsuJIo")
		update.message.reply_text("歸屬 (Eleanor)\n作詞：顏靜萱    作曲：林易祺\n\n遠方的星火 忽明忽滅\n離開已多少年 我忘了歲月\n轉身想要安慰 才想起世界早已毀滅\n\n遠方的星火 忽明忽滅\n離開已多少年 我忘了歲月\n窺探宇宙邊緣 才發現時間 緊緊糾結\n\n我的一切\n壓抑的偏見 執拗的精確\n愛和後悔 深刻與殘缺\n全都事過境遷\n你的眷戀 腐壞而卑微 也無可避免\n眼淚流下來的瞬間 沒有人看見\n\n遠方的星火 忽明忽滅\n離開已多少年 我忘了歲月\n轉身想要安慰 才想起世界早已毀滅\n\n我的一切\n壓抑的偏見 執拗的精確\n愛和後悔 深刻與殘缺\n該為什麼妥協\n你的眷戀 腐壞而卑微 也無可避免\n漂浮在最寂寞的象限 慢慢地拉遠\n\n我的一切\n壓抑的偏見 執拗的精確\n愛和後悔 深刻與殘缺\n全都事過境遷\n你的眷戀 腐壞而卑微 也無可避免\n眼淚流下來的瞬間 沒有人看見")
		self.go_back(update)

    def on_exit_s_eleanor(self, update):
        print('exit_s_eleanor')

    def on_enter_s_the_city_is_eating_me_live(self, update):
		update.message.reply_text("https://www.youtube.com/watch?v=_mcdnRHrXCQ")
		update.message.reply_text("食人夢 (The City is Eating Me Alive)\n作詞：顏靜萱    作曲：林易祺\n\n游離在城市中 滾燙的渴求\n墜落的可能性 又喚醒了夢\n若這世界還願 收留一點點哀求\n就拜託告訴我盡頭有什麼\n\n看不清誰的面孔 只跟著背影走\n都不想變得普通 卻又害怕不同\n時間離去接著 匡啷摔碎在身後\n還妄想能回頭 重新再來過\n\n漲得太滿太快 供過於求的愛 該往哪兒擺?\n曾經試著剖開 我的靈魂對白 卻一片徒然\n誰都知道一切 從來沒那麼難 也不能說簡單\n我們終究只求 最低門檻的人生解決方案\n\n游離在城市中 滾燙的渴求\n墜落的可能性 又喚醒了夢\n若這世界還願 收留一點點哀求\n就拜託告訴我盡頭有什麼\n\n看不清誰的面孔 只跟著背影走\n都不想變得普通 卻又害怕不同\n星星那樣的美夢 發著光同時殞落\n已來不及逃脫 這城市吃了我\n\n漲得太滿太快 供過於求的愛 該往哪兒擺?\n曾經試著剖開 我的靈魂對白 卻一片徒然\n誰都知道一切 從來沒那麼難 也不能說簡單\n我們終究只求 最低門檻的人生解決方案\n\n漲得太滿太快 供過於求的愛 該往哪兒擺?\n曾經試著剖開 我的靈魂對白 卻一片徒然\n誰都知道一切 從來沒那麼難 也不能說簡單\n我們終究只求 最低門檻的人生解決方案")
		self.go_back(update)

    def on_exit_s_the_city_is_eating_me_live(self, update):
        print('exit_s_the_city_is_eating_me_live')

    def on_enter_s_waves(self, update):
		update.message.reply_text("https://www.youtube.com/watch?v=10DHUqSVu6I")
		update.message.reply_text("與浪之間 (Waves)\n作詞：林易祺    作曲：林易祺\n\n黑色的瘋狂 佔據了黑色的你\n白色的勇氣 親吻著白色的心\n一瞬間 看不清 就想抓住你\n離開了 又回去 只想擁抱你\n\n看不見你 也看不見自己\n看不見你 就看不見自己\n\n與浪之間 承載著秘密\n銀色的光 拉著我跳舞\n血液在竄 思緒混亂 不停轉彎\n誰在呼喊我\n\n與浪之間 說一個故事\n害怕的人 尋一個出口\n越走越暗 微光一閃 才看見你\n我還在\n\n黑色的瘋狂 佔據了黑色的你\n白色的勇氣 親吻著白色的心\n一瞬間 看不清 就想抓住你\n離開了 又回去 只想擁抱你\n\n看不見你 也看不見自己\n看不見你 就看不見自己\n\n與浪之間 承載著秘密\n銀色的光 拉著我跳舞\n血液在竄 思緒混亂 不停轉彎\n誰在呼喊我\n\n與浪之間 說一個故事\n害怕的人 尋一個出口\n越走越暗 微光一閃 才看見你\n我還在\n我還在\n\n與浪之間 承載著秘密\n銀色的光 拉著我跳舞\n血液在竄 思緒混亂 不停轉彎\n誰在呼喊我\n\n與浪之間 說一個故事\n害怕的人 尋一個出口\n越走越暗 微光一閃 才看見你\n我還在")
		self.go_back(update)

    def on_exit_s_waves(self, update):
        print('exit_s_waves')

    def on_enter_s_vast_and_hazy(self, update):
		update.message.reply_text("https://www.youtube.com/watch?v=S6kQPEMhEfM")
		update.message.reply_text("Vast & Hazy\n作詞：Vast & Hazy	 作曲：Vast & Hazy\n\n喧鬧落幕的櫥窗 季節交替了陽光\n寫下片段的呢喃 想告訴你我的生活\n又考慮了 好久\n會不會有點 害羞\n\n我想我也並不是 渴求那虛榮\n在意身上的光影 和當時固執些甚麼\n以為已經 足夠\n下一刻卻想要 更多\n\n放開手不計任何代價的衝動\n抱歉 差點忘記了你的模樣\n拋下 不是心中最渴望 無視他們呼簫而過的猖狂\n在擁擠的星球上\n\n決定為你而唱\n\n放開手不計任何代價的衝動\n抱歉 差點忘記了你的模樣\n拋下 不是心中最渴望 無視他們呼簫而過的猖狂\n原來一直沒有忘\n\n說要去的地方")
		self.go_back(update)

    def on_exit_s_vast_and_hazy(self, update):
        print('exit_s_waves')


