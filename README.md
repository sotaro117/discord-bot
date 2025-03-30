![Discord Chat Bot]

## Introduction

Discord bot for personal usage

## Setup

### Create an environment and install dependencies

#### Mac/Linux/WSL

```
$ python3 -m venv bot-env
$ source bot-env/bin/activate
$ pip install -r requirements.txt
```

### Running notebooks

If you don't have Jupyter set up, follow installation instructions [here](https://jupyter.org/install).

```
$ jupyter lab
```

### Setting up env variables

Briefly going over how to set up environment variables. You can also
use a `.env` file with `python-dotenv` library.

#### Mac/Linux/WSL

```
$ export API_ENV_VAR="your-api-key-here"
```

### Libraries

- Huggingface Inference API
- Discord.py
