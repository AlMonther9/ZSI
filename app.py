from settings import app
from views import *
from models import *

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)