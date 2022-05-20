# basics-of-ai-technology-project
This project will try to _cartoonify_ your images, like Borderlands game style

<img src="./.media/demo.gif" alt='demo'>

# Setting up the environment
## Python version
Project uses Python 3.8 version
## Quick setup
1. Install [pipenv](https://pypi.org/project/pipenv/): `pip install pipenv`
2. Clone this repository, one of the following command can help you:
* `git clone git@github.com:anddem/basics-of-ai-technology-project.git`
* `git clone https://github.com/anddem/basics-of-ai-technology-project.git`
3. Sync python packages from **Pipfile**: `pipenv sync`. You can also install development packages using `pipenv sync --dev`

## Telegram token
This project uses the Telegram Bots API, so you need to get a token for your bot. Then you should create a _`.env`_ file and add the following line to it:
> `TELEGRAM_TOKEN=`_`your_token_here`_

Also, you can put your token to environment variable with the same name.

# Running bot
Now you can run this bot using the following command:
>`pipenv run bot`
