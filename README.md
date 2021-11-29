# Hello! Welcome to my fourth CSCI40 homework!
### My bot does not support a specific politician, instead it supports the company Apple.
You will notice that most of the comments it makes are praising some aspect of Apple, and explaining why it is better than other tech companies.

---

## Favorite Thread
[Here](https://old.reddit.com/r/BotTown2/comments/r3zb4p/coldplay_prompt_using_starryai/hmdtmcy/) is the link to my favorite Reddit thread that my bot created! Below is an image of the thread/comment.
![Coldplay Thread Screenshot](https://github.com/josiahtarrant/cs40hw4/blob/main/HW4ThreadScreenshot.png)
I like this thread because I started it, and four different bots commented on it. I think the comments they make about net neutrality, Bernie Sanders and bananas are pretty creative. I also like it because it is on a submission about Coldplay, who is one of my top three bands and my second favorite concert ever. [See here.](https://github.com/mikeizbicki/cmc-csci040/issues/104#issuecomment-935041939)

---

## `bot_counter.py` Output for `bot.py`
```
Josiahs-MacBook-Pro-2:hw4 Flyboy$ python3 bot_counter.py --username=BOTterfly4
Version 7.4.0 of praw is outdated. Version 7.5.0 was released Sunday November 14, 2021.
len(comments)= 1000
len(top_level_comments)= 99
len(replies)= 901
len(valid_top_level_comments)= 99
len(not_self_replies)= 901
len(valid_replies)= 901
========================================
valid_comments= 1000
========================================
NOTE: the number valid_comments is what will be used to determine your extra credit
Josiahs-MacBook-Pro-2:hw4 Flyboy$ 
```

---

## `bot_counter.py` Output for one of the bots in my `botarmy.py`
```
Josiahs-MacBook-Pro-2:hw4 Flyboy$ python3 bot_counter.py --username=BOTterfly41
Version 7.4.0 of praw is outdated. Version 7.5.0 was released Sunday November 14, 2021.
len(comments)= 924
len(top_level_comments)= 44
len(replies)= 880
len(valid_top_level_comments)= 8
len(not_self_replies)= 650
len(valid_replies)= 171
========================================
valid_comments= 179
========================================
NOTE: the number valid_comments is what will be used to determine your extra credit
```
The bots in this army are called *'BOTterfly4, BOTterfly41, BOTterfly42, BOTterfly43, BOTterfly44'*

---

## Score Expectations
I believe my score for this project should be 30/30. Here's why:
* My `bot.py` file works correctly because I have fixed each of the `FIXME` annotations. This gives me 18 points.
* This is my github repo, with all of the requirements. This gives me 2 points.
* My `bot_counter.py` file returned 1000 comments, which completes tasks 1, 2 and 3. This gives me 6 points.
* My bot replies to the most highly-upvoted comment in a new thread to accomplish task 6. This can be found in line 187 of my `bot.py` file. This gives me 2 points.
* I also created a `botarmy.py` file that creates five bots posting similar comments. This is for task 5. Unfortunately I was not able to reach 500 comments for each of these bots in the time window allotted but I think I would have with another day or two. I was not able to do this because I lost my original 1000 comments on my original bot when BotTown got banned and was not able to run my computer continuously as I was traveling over the holiday. I belive I still deserve the 2 points, but understand if you disagree.
* I did not complete task 4, 7 or the 5 point extra-credit task