# Image Hosting TelegramBot

Telegram Bot created in Python that you can interact with by sending command to take photo and uploads it to imgbb.com and gives back link.

When starting/restarting Bot you send ```/start``` command **only once** after that Bot will ask you to send him ```/Upload_picture``` command.
After that you send him photo you would like to host on your profile on imgbb.com.

Docker building

```docker build -t imghostbot .\Image-Hosting-TelegramBot\ ```

``` docker run --restart always imghostbot```

If by any chance Bot runs into unexpected errors and breaks docker will automatically restart it with ```--restart always``` attribute

Go to https://imgbb.com site and create free account after that go to https://api.imgbb.com/ and press **Add API Key** copy that key and paste it in line 36

```
payload = {
            "key": "AUTH KEY FROM IMGBB", # here you should add your api key for imgbb
            "image": filephoto.file_path
          }
```
