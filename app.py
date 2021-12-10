from flask import Flask, render_template

class Player:
    namn=""
    jersey=0

p1 = Player()
p1.namn = "Stefan"
p1.jersey = 13
p2 = Player()
p2.namn = "Lisa"
p2.jersey = 14

lista = [p1,p2]

app = Flask(__name__)

@app.route("/")
def startpage():
    return render_template("index.html", allPlayers = lista)



if __name__  == "__main__":
    #with app.app_context():
    #    upgrade()
    app.run()
