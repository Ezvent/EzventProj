import json
import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
class Allusers(db.Model):


@app.route("/callback")
def authorize():

if __name__ == "__main__":
    app.run(
        host=os.getenv("IP", "0.0.0.0"), port=int(os.getenv("PORT", 8081)), debug=True
    )

