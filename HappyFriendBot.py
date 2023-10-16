import praw
import random
import time

reddit = praw.Reddit(
    client_id="pU-DiEZlaVpoETgQyxM6-g",
    client_secret="bsVNuWaTet1mYC4Ax5_24KjiYOPl6g",
    user_agent="<console:FRIEND:1.0>",
    username='HappyFriendBot',
    password='benLippen43'
)
subreddit = reddit.subreddit("sneakers")

kanye_quotes: list[str] = ["And I’d rather be hated for what I am, than loved for what I’m not. -Kanye West", "People liking me or me liking myself — I chose the latter. -Kanye West", "You know what calms me down the most? Success. -Kanye West", "I refuse to follow those rules that society has set up and the way that they control people with low self-esteem. -Kanye West", "And the only thing real is your family, your loved ones, the time that you have, the only luxury is time and the only thing promised is that you gonna die one day. -Kanye West",
                           "Don’t be afraid to be wrong, don’t be too proud to be wrong. You know, you can’t learn anything from a compliment. -Kanye West", "I was taught I could do everything. -Kanye West", "Mentally I’m so focused, there’s nothing anyone can say or do to me to stop the music, the product that I’m going to put out. -Kanye West", "Did I not make Louis Vuitton’s, did people not line up at the Yeezy Store? -Kanye West", "If I see an opportunity I’m gonna go for it. -Kanye West"]

for submission in subreddit.hot(limit=10):
    # print("************")
    # print(submission.title)

    for comment in submission.comments:
        if hasattr(comment, "body"):
            comment_lower = comment.body.lower()
            if " yeezy " in comment_lower:
                print("____________")
                print(comment.body)
                random_index = random.randint(0, len(kanye_quotes) - 1)
                comment.reply(kanye_quotes[random_index])
                time.sleep(600)
