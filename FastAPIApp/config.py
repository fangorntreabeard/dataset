from fastapi import FastAPI
import psycopg2
from fastapi.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles
import os
from dotenv import load_dotenv
from pathlib import Path
parent_dir_path = os.path.dirname(os.path.realpath(__file__))
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
app = FastAPI()
script_dir = os.path.dirname(__file__)
st_abs_file_path = os.path.join(script_dir, "static/")
app.mount("/static", StaticFiles(directory=st_abs_file_path), name="static")
templates = Jinja2Templates(directory="templates")


conn = psycopg2.connect(
            database="asap",
            user="admin",
            password="1234",
            host="localhost",
            port="5432"
        )

