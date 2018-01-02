# TOC Project 2017
介紹樂團 vast & hazy

## Finite State Machine
![fsm](./img/show-fsm.png)

## Usage
The initial state is set to `start`.

* start

	* Input: "介紹"
		* Reply: vast & hazy 介紹、團員

	* Input: "專輯"
		* Reply: "要找哪張專輯呢？"、專輯列表

	* Input: "歌曲"
		* Reply: "要找哪首歌呢？"、歌曲列表

* find_album

	* Input: "vast & hazy"
		* Reply: vast & hazy 專輯介紹、歌曲列表

	* Input: "次等秘密"
		* Reply: 次等秘密專輯介紹、歌曲列表

* find_song

	* Input: "vast & hazy"
		* Reply: 歌曲youtube 網址、歌詞

	* Input: "歸屬"
		* Reply: 歌曲youtube 網址、歌詞
		
	* Input: "食人夢"
		* Reply: 歌曲youtube 網址、歌詞

	* Input: "與浪之間"
		* Reply: 歌曲youtube 網址、歌詞
