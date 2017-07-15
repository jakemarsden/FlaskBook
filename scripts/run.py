#!venv/bin/python
import config
from flaskbook import app

app.run(host=config.SERVER_HOST, port=config.SERVER_PORT, debug=config.DEBUG)
