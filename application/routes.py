from flask import redirect, url_for
from application._init_ import app, db
from application.models import Todo, Project
from datetime import date, timedelta