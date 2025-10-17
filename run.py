import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import create_app, db         
from app.models import Video  

app = create_app()

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)