from bot_class import RedditBot
from time import sleep
cache_thoughts = []
SUBREDDIT = 'showerthoughts'
Bot = RedditBot()
while True:
    op_user, thought, upvotes, link = Bot.get_from_reddit(SUBREDDIT)
    if thought not in cache_thoughts:
        cache_thoughts.append(thought)
        translated = Bot.translate(thought)
        post = 'Post on r/' + SUBREDDIT + ' by ' + op_user + ' (' + upvotes + ' upvotes)' + '\n\n\n' + thought + '\n\n\n' + 'Перевод на русский от Google Translate:\n' + translated + '\n\n\nLink: ' + link + "\n\n\nЯ бот! Жалобы/предложения писать в лс"
        Bot.post_to_vk('login','password',post)
    sleep(60)
