# Daily Scripture Generator

VERY fun project I made for a coding challenge with some friends --

Built with React, Next JS and Tailwind CSS. Deployed with Vercel.

Used NPM for icons and sharing.

The scriptures are housed within an array of objects.

I wanted a really simple and clean UI and I believe I achieved that here.

I am passionate about reading scriptures that are historically accurate.

All of the scriptures have the Hebrew name for "The Lord".

I built this in one day and you can view the project below

I'm looking forward to improving this as time goes along!

## Deploy Frontend with Vercel

[Daily Scripture Generator via Vercel](https://daily-scripture-generator.vercel.app/)

## Deploy Frontend on Mac

```zsh
brew install node

npm install

npm start
```

## Deploy Backend on Mac

```zsh
cd backend-api/

. venv/bin/activate

pip install -m requirements.txt

python app.py
```

## Backend API Guide

### GET random scripture

Request

```
http://<IP ADDRESS>/randomScripture/
```

Response

```json
{
  "action": "an action",
  "scripture": "a scripture",
  "verse": "a verse"
}
```

### Add new scripture

Request

Response

### Update scripture

Request

Response

### Delete scripture

Request

Response
