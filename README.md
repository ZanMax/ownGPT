# ownGPT

Create your own GPT chat.

## Clone the repository

```
git clone https://github.com/ZanMax/ownGPT.git
```

## Installation

```
pyton3 -m venv venv
```

```
source venv/bin/activate
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
SHOW_SOURCES=true
SOURCE_DIRECTORY = /Users/user/Downloads/ducs
```

## Upload documents to the database

```
python3 upload_documents.py
```

### Supported extensions are:

- `.csv`: CSV,
- `.docx`: Word Document,
- `.doc`: Word Document,
- `.enex`: EverNote,
- `.eml`: Email,
- `.epub`: EPub,
- `.html`: HTML File,
- `.md`: Markdown,
- `.msg`: Outlook Message,
- `.odt`: Open Document Text,
- `.pdf`: Portable Document Format (PDF),
- `.pptx` : PowerPoint Document,
- `.ppt` : PowerPoint Document,
- `.txt`: Text file (UTF-8),

## Run console chat

```
python3 chat.py
```

## Run webserver

```
python3 chat.py --web
```

# Thanks

GPT4all
privateGPT