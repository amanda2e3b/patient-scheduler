from flask import Blueprint, render_template, request

scheduler_bp = Blueprint("scheduler", __name__, template_folder="../templates")

schedules = [] 

@scheduler_bp.route("/scheduler", methods=["GET", "POST"])
def scheduler():
    if request.method == "POST":
        schedule = {
            "id": len(schedules) + 1,
            "patient": request.form["patient"],
            "time": request.form["time"],
            "destination": request.form["destination"]
        }
        schedules.append(schedule)
    return render_template("scheduler.html", schedules=schedules)
