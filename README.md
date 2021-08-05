# Image Hosting TelegramBot

Telegram Bot created in Python that you can interact with by sending command to take photo and uploads it to imgbb.com and gives back link.

When starting Bot you send ```/start``` command **only once** after that Bot will ask you to send him ```/Upload_picture``` command.
After that you send him photo you would like to host on your profile on imgbb.com.

Docker building
```docker build -t imghostbot .\Image-Hosting-TelegramBot\ ```
``` docker run --restart always imghostbot```

If by any chance Bot runs into unexpected errors and breaks docker will automatically restart it with ```--restart always``` attribute
