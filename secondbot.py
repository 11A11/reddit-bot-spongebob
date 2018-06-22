import praw
import sys
from supanjibobu import replytext


def main():
    reddit = praw.Reddit(user_agent='NAME_OF_BOT (by YOUR_USER_NAME)',
                         client_id='YOUR_CLIENT_ID', client_secret='YOUR_CLIENT_SECRET',
                         username='YOUR_USER_NAME', password='YOUR_PASSWORD')

    subreddit = reddit.subreddit('AskReddit')
    for submission in subreddit.stream.submissions(): # please add a rate limit. reddit servers will suffer otherwise. be civil.
        process_submission(submission)


def process_submission(submission):
    
    if len(submission.title.split()) > 7:
        return

    normalized_title = submission.title.lower()
    print('Replying to: {}'.format(submission.title))
    rep=replytext(normalized_title)
    finrep=''.join(rep)
    submission.reply(finrep)
    


if __name__ == '__main__':
    main()
