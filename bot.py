import praw
import random
import datetime
import time

# copy your generate_comment function from the madlibs assignment here
madlibs = [
    "[COMPANY] makes great [ITEMS]. That being said, Apple makes the [DESCRIPTOR] products. My favorite product is the [FAVORITE]. I also really like Apple [SERVICE]. No wonder Apple is the [PRAISE]. Gotta love [PERSON]!",
    "I want to work at Apple, not [COMPANY]. [PERSON] is the [DESCRIPTOR]. Whoever works with him at [LOCATION] is so lucky. I would move from [CITY] to work there.",
    "[COMPANY] should have more offices in [CITY], maybe then they could be the [PRAISE]. Apple has taken over [LOCATION] and claimed the title of [DESCRIPTOR].",
    "In addition to super cool [ITEMS], Apple has awesome service products like Apple [SERVICE]. That's what helped [PERSON] make Apple the [PRAISE]. Now if only they'd make a [COLOR] [FAVORITE].",
    "Everyone, [COLOR] [ITEMS] are the next big thing. For example, [COLOR] [FAVORITE]. Everyone in [LOCATION] knows what they're doing. If only [COMPANY] in [CITY] would understand this.",
    "Apple [SERVICE] is better than [COMPANY] [SERVICE]. It's actually the [DESCRIPTOR]. I am excited to see the new Apple [NEW] which is being presented in [CITY]!",
]

replacements = {
    'COMPANY' : ['Google', 'Amazon', 'Microsoft', 'Samsung', 'Facebook'],
    'ITEMS' : ['phones', 'devices', 'technology', 'tech', 'products'],
    'DESCRIPTOR' : ['coolest', 'best', 'smartest', 'most innovative', 'most respected'],
    'FAVORITE' : ['watch', 'computer', 'homepod', 'phone', 'airpods'],
    'SERVICE' : ['Music', 'TV', 'Fitness+', 'pay', 'photos'],
    'PRAISE' : ['greatest of all time', 'most valuable company', 'leader', 'favorite employer', 'famous firm'],
    'PERSON' : ['Tim Cook', 'Steve Jobs', 'Woz', 'Eddy Cue', 'Luca Maestri'],
    'LOCATION' : ['Infinite Loop', 'Apple Park', 'Cupertino', 'Silicon Valley', 'Bay Area'],
    'CITY' : ['Los Angeles', 'New York', 'Atlanta', 'Chicago', 'Seattle'],
    'COLOR' : ['blue', 'red', 'purple', 'magenta', 'gold'],
    'NEW' : ['helicopter', 'submarine', 'plane','bus', 'boat']
    }


def generate_comment():
    '''
    This function generates random comments according to the patterns specified in the `madlibs` variable.
    To implement this function, you should:
    1. Randomly select a string from the madlibs list.
    2. For each word contained in square brackets `[]`:
        Replace that word with a randomly selected word from the corresponding entry in the `replacements` dictionary.
    3. Return the resulting string.
    For example, if we randomly seleected the madlib "I [LOVE] [PYTHON]",
    then the function might return "I like Python" or "I adore Programming".
    Notice that the word "Programming" is incorrectly capitalized in the second sentence.
    You do not have to worry about making the output grammatically correct inside this function.
    '''
    for i in range(1):
        result = str(random.choice(madlibs))
        result = result.replace('[COMPANY]',random.choice(replacements['COMPANY']))
        result = result.replace('[ITEMS]',random.choice(replacements['ITEMS']))
        result = result.replace('[DESCRIPTOR]',random.choice(replacements['DESCRIPTOR']))
        result = result.replace('[FAVORITE]',random.choice(replacements['FAVORITE']))
        result = result.replace('[SERVICE]',random.choice(replacements['SERVICE']))
        result = result.replace('[PRAISE]',random.choice(replacements['PRAISE']))
        result = result.replace('[PERSON]',random.choice(replacements['PERSON']))
        result = result.replace('[LOCATION]',random.choice(replacements['LOCATION']))
        result = result.replace('[CITY]',random.choice(replacements['CITY']))
        result = result.replace('[COLOR]',random.choice(replacements['COLOR']))
        result = result.replace('[NEW]',random.choice(replacements['NEW']))
        #print(result)
        return(result)

def score_comment(comment):
    comment = random.choice(comments_without_replies)
    comment_score = comment.score
    return comment_score

# connect to reddit 
reddit = praw.Reddit('bot', user_agent='cs40')

# select a "home" submission in the /r/BotTown subreddit to post to,
# and put the url below
submission_url = 'https://old.reddit.com/r/BotTown2/comments/r1hdim/botterflys_test/?'
submission = reddit.submission(url=submission_url)

# each iteration of this loop will post a single comment;
# since this loop runs forever, your bot will continue posting comments forever;
# (this is what makes it a deamon);
# recall that you can press CTRL-C in the terminal to stop your bot
#
# HINT:
# while you are writing and debugging your code, 
# you probably don't want it to run in an infinite loop;
# you can change this while loop to an if statement to make the code run only once

# fix following line
while True: #while

    # printing the current time will help make the output messages more informative
    # since things on reddit vary with time
    print()
    print('new iteration at:',datetime.datetime.now())
    print('submission.title=',submission.title)
    print('submission.url=',submission.url)

    # FIXME (task 0): get a list of all of the comments in the submission
    # HINT: this requires using the .list() and the .replace_more() functions

# fix following line
    submission.comments.replace_more(limit=None)
    all_comments = []
    all_comments = submission.comments.list()
   
    # HINT: 
    # we need to make sure that our code is working correctly,
    # and you should not move on from one task to the next until you are 100% sure that 
    # the previous task is working;
    # in general, the way to check if a task is working is to print out information 
    # about the results of that task, 
    # and manually inspect that information to ensure it is correct; 
    # in this specific case, you should check the length of the all_comments variable,
    # and manually ensure that the printed length is the same as the length displayed on reddit;
    # if it's not, then there are some comments that you are not correctly identifying,
    # and you need to figure out which comments those are and how to include them.
    print('len(all_comments)=',len(all_comments))

    # (task 1): filter all_comments to remove comments that were generated by your bot
    # HINT: 
    # use a for loop to loop over each comment in all_comments,
    # and an if statement to check whether the comment is authored by you or not
    not_my_comments = []
    for comment in all_comments:
        #print('comment.author=', comment.author)
        #print('type(comment.author)=', type(comment.author))
        if str(comment.author) != 'BOTterfly4':
            not_my_comments.append(comment)
# have someone go comment on my reddit submission

    # HINT:
    # checking if this code is working is a bit more complicated than in the previous tasks;
    # reddit does not directly provide the number of comments in a submission
    # that were not gerenated by your bot,
    # but you can still check this number manually by subtracting the number
    # of comments you know you've posted from the number above;
    # you can use comments that you post manually while logged into your bot to know 
    # how many comments there should be. 
    print('len(not_my_comments)=',len(not_my_comments))

    # if the length of your all_comments and not_my_comments lists are the same,
    # then that means you have not posted any comments in the current submission;
    # (your bot may have posted comments in other submissions);
    # your bot will behave differently depending on whether it's posted a comment or not
    has_not_commented = len(not_my_comments) == len(all_comments)
    print('has_not_commented=', has_not_commented)

    if has_not_commented:
        #(task 2)
        # if you have not made any comment in the thread, then post a top level comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit;
        # a top level comment is created when you reply to a post instead of a message
        text = generate_comment()
        submission.reply(text)

    else:
        # (task 3): filter the not_my_comments list to also remove comments that 
        # you've already replied to
        # HINT:
        # there are many ways to accomplish this, but my solution uses two nested for loops
        # the outer for loop loops over not_my_comments,
        # and the inner for loop loops over all the replies of the current comment from the outer loop,
        # and then an if statement checks whether the comment is authored by you or not
        comments_without_replies = []
        for comment in not_my_comments:
            did_reply = False
            for replies in comment.replies:
                if str(replies.author) == 'BOTterfly4':
                    did_reply = True
            if did_reply == False:
                comments_without_replies.append(comment)

        #comments_without_replies = not_my_comments
        # HINT:
        # this is the most difficult of the tasks,
        # and so you will have to be careful to check that this code is in fact working correctly
        print('len(comments_without_replies)=',len(comments_without_replies))

        # (task 4): randomly select a comment from the comments_without_replies list,
        # and reply to that comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit;
        # these will not be top-level comments;
        # so they will not be replies to a post but replies to a message
        try:
            #comment = random.choice(comments_without_replies)
            comment = sorted(comments_without_replies,key=score_comment, reverse=True)[0]
            print(comment)
            comment.reply(generate_comment())
        except praw.exceptions.APIException: # don't use a naked 'except'
            print('not replying to a comment that has been deleted')
        except IndexError:
            print('not replying to a post where I have already commented')

    # (task 5): select a new submission for the next iteration;
    # your newly selected submission should be randomly selected from the 5 hottest submissions
    submission = random.choice(list(reddit.subreddit("BotTown2").hot(limit=5))) #praw website
    print('submission=', submission)
    # We sleep just for 1 second at the end of the while loop.
    # This doesn't avoid rate limiting
    # (since we're not sleeping for a long period of time),
    # but it does make the program's output more readable.
    time.sleep(15) #need at least 10 minutes
    # control c to stop program from running