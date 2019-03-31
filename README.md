# Discord Echo Bot

Simple, it echos whatever you type from the terminal to Discord. This is for April Fools, and not to be used anywhere else. If you get a stern warning by Discord to stop, stop. Bot is highly botched, in case of error, kill it, relaunch.

## Setting up
You'll need:

* A bot token (which can be acquired here: [https://discordapp.com/developers/applications/](https://discordapp.com/developers/applications/)) by making a bot (Google t you don't know how to make a bot, those guides should also cover getting the token)
* A text editor (notepad or nano)
* The ability to follow instruction

You'll need to:

1. Change the lock-on string
`if (message.content.startswith('Welcome home, EchoBot.')):```
This string, in this case "Welcome home, EchoBot." when typed into any channel will lock the bot to that channel.
2. Change the token from `client.run("Your token here")` to the token you got from the bot 
3. Open `cmd` or your terminal of choice and install `requirement.txt` because EchoBot is on `rewrite`
4. Run the bot, invite the bot to your server, type in the lock-on phrase and start sending from terminal

Just in case:

* You can have multiple lock-on phrases by botching more `or` into the `if`. Ìf you need to relock, kill the bot and start it again, make sure to have multiple phrases so people won't notice. 
