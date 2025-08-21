from flask import Flask, render_template, request

app = Flask(__name__)

appointments = [] 

@app.route("/", methods=["GET", "POST"])
def scheduler():
    if request.method == "POST":
        appt = {
            "id": len(appointments) + 1,
            "patient": request.form["patient"],
            "time": request.form["time"],
            "destination": request.form["destination"]
        }
        appointments.append(appt)
    return render_template("scheduler.html", appointments=appointments)

if __name__ == "__main__":
    app.run(debug=True)
