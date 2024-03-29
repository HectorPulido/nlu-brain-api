# NLU BRAIN API WITH DJANGO

This is an API made with django that uses Snips NLU to understand the user's intent, contains a database to store the user's data and a web server to serve the user's data.

## Features

## TODO


## How it works
This is a heroku based project

### Setup Django

1. Configure your heroku project, save the name, you will need the Heroku Postgresql addon

2. Build the docker development and run it to make sure everything is ok

```
docker build -t web:latest .
docker run -d --name <herokuname> -e "PORT=8765" -e "DEBUG=0" -p 8007:8765 web:latest
```

3. You can deactivate like this
```
docker stop <herokuname>
docker rm <herokuname>
```

4. You can upload your project with this commands
```
docker run -d --name <herokuname> -e "PORT=8765" -e "DEBUG=0" -p 8007:8765 web:latest
heroku container:login
heroku container:push web -a <herokuname>
heroku container:release web -a <herokuname>
```

5. Create your user with
```
heroku run python manage.py createsuperuser -a <herokuname>
```

6. Enter to your proyect from this url
```
http://<herokuname>.herokuapp.com/admin
```

7. Create an Key to interact with the API

8. You are ready


## More interesting projects
I have a lot of fun projects, check this:

### Machine learning
- https://github.com/HectorPulido/Evolutionary-Neural-Networks-on-unity-for-bots
- https://github.com/HectorPulido/Imitation-learning-in-unity
- https://github.com/HectorPulido/Chatbot-seq2seq-C-

### Games
- https://github.com/HectorPulido/Unity-MMO-Framework
- https://github.com/HectorPulido/Contra-Like-game-made-with-unity
- https://github.com/HectorPulido/Pacman-Online-made-with-unity

### Random
- https://github.com/HectorPulido/Arithmetic-Parser-made-easy
- https://github.com/HectorPulido/Simple-php-blog
- https://github.com/HectorPulido/Decentralized-Twitter-with-blockchain-as-base


## Licence
This proyect uses Django, tweepy, dropbox libraries, also was made to work with heroku but everything else was totally handcrafted by me, so the licence is MIT, use it as you want.

<div align="center">
<h3 align="center">Let's connect 😋</h3>
</div>
<p align="center">
<a href="https://www.linkedin.com/in/hector-pulido-17547369/" target="blank">
<img align="center" width="30px" alt="Hector's LinkedIn" src="https://www.vectorlogo.zone/logos/linkedin/linkedin-icon.svg"/></a> &nbsp; &nbsp;
<a href="https://twitter.com/Hector_Pulido_" target="blank">
<img align="center" width="30px" alt="Hector's Twitter" src="https://www.vectorlogo.zone/logos/twitter/twitter-official.svg"/></a> &nbsp; &nbsp;
<a href="https://www.twitch.tv/hector_pulido_" target="blank">
<img align="center" width="30px" alt="Hector's Twitch" src="https://www.vectorlogo.zone/logos/twitch/twitch-icon.svg"/></a> &nbsp; &nbsp;
<a href="https://www.youtube.com/channel/UCS_iMeH0P0nsIDPvBaJckOw" target="blank">
<img align="center" width="30px" alt="Hector's Youtube" src="https://www.vectorlogo.zone/logos/youtube/youtube-icon.svg"/></a> &nbsp; &nbsp;
