# ownGPT

Create your own GPT chat.

## Installation

```
pyton3 -m venv venv
```

```
pip3 install -r requirements.txt
```

## Download models

```
./download_models.sh
```

## Settings

create .env file with the following content:

```
PERSIST_DIRECTORY=db
MODEL_TYPE=GPT4All
MODEL_PATH=models/ggml-gpt4all-j-v1.3-groovy.bin
EMBEDDINGS_MODEL_NAME=all-MiniLM-L6-v2
MODEL_N_CTX=1000
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50
SOURCE_DIRECTORY = /Users/user/Downloads/ducs
```

## Upload documents to the database

```
```

## Run console chat

```
```

## Run webserver

```
```

# Thanks

GPT4all
privateGPT