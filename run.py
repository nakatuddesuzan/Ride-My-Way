from app import app
from app.api.requests import views
from app.api.offers import views
if __name__ == '__main__':
    app.run(debug=True)
