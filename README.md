# Instabot

## What is it?

Instabot is a bot coded in python used to organically grow your Instagram page.

## How does it work?

The bot follows, likes and comments (1 out of 10 random comments) on the first 1000 pictures within each hashtag,
if you don't currently follow the user. 

The bot uses the hashtags.txt file to recgonize which hashtags to scrape.

A username_users.txt file is created which tracks people followed using the bot,
in case you want to manually unfollow them at some point in the future. Don't 
forget to delete entries in this file as you unfollow people.

Manually change the comments in the generateComments(n) function within bot.py.  Currently, it is 
configured for a fitness page based instabot. 


## How do I use it?

Navigate to the desired directory and run the following command to install the package.

```bash
git clone https://github.com/sumermalhotra/instabot.git
```

Once you've installed the repository, navigate to credentials.py and put in your instagram credentials (username and password) - don't worry, no one will have access to it apart from you. 

Next, navigate to hashtags.txt and key in a list of hashtags for which you want the bot to scrape.

Finally, run bot.py using a python3 interpreter, preferably python 3.7.x.

```bash
python bot.py 
    (or)
python3 bot.py
```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)