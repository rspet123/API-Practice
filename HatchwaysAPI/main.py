"""Run API app"""
from app import app
#Hello!
if __name__ == "__main__":

    app.run(port=5000, debug=True)
