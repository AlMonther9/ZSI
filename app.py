from settings import app, SEREVER_ADDRESS, PORT
from views import *
from models import *

if __name__ == '__main__':
    app.run(host=SEREVER_ADDRESS, port=PORT)