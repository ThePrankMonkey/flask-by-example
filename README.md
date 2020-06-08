# Notes

## Setup

```bash
export app_stage=wordcount-theprankmonkey-stage
export app_prod=wordcount-theprankmonkey-pro
```

## Pushing to Heroku

```bash
git push stage master
git push pro master
```

## CLI Run in Heroku

```bash
heroku run python app.py --app $app_prod
heroku run python app.py --app $app_stage
```