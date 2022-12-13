<h1 align="center">
    Citation Station
</h1>

<h3 align="center">
  A Discord bot that will send a quote to your server every morning
</h3>


In its current form _Citation Station_ will send a random quote to the channel specified in the `env` variable. It is a task that runs every 60 minutes and only fires when the current hour matches the `HOUR_TO_SEND` variable.

## Roadmap
- Add database
    - Support choosing channel
    - Set timezone and time to send
- `/quote` command to send a random quote
- Add more quote sources

## Getting started
- Make sure python is installed
- Install [poetry](https://python-poetry.org/docs/)
- Run `poetry install`
- Create an application through the Discord developer portal and get yourself a token
  - Add this application (the bot) to your server. You need to make sure it has the `Send messages` permission
- Create an `.env` file based off `.env.example` and fill out the values
- Install the depenencies with your package manager of choice
- Run either `python -m citation_station` or `poetry run python -m citation_station`