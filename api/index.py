# api/index.py
from app.main import app
from mangum import Mangum  # AWS Lambda adapter

handler = Mangum(app)
