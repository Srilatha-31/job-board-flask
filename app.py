from flask import Flask, render_template, request, abort
import json

app = Flask(__name__)

# Load jobs from JSON file
def load_jobs():
    with open("jobs.json", "r") as file:
        jobs = json.load(file)
    return jobs


# Home Page
@app.route("/")
def home():
    jobs = load_jobs()

    search = request.args.get("search", "").lower()
    location = request.args.get("location", "")
    job_type = request.args.get("job_type", "")

    filtered_jobs = []

    for job in jobs:

        if search:
            if search not in job["title"].lower() and search not in job["company"].lower():
                continue

        if location:
            if job["location"] != location:
                continue

        if job_type:
            if job["type"] != job_type:
                continue

        filtered_jobs.append(job)

    featured_jobs = jobs[:3]
    latest_jobs = jobs

    return render_template(
        "index.html",
        jobs=filtered_jobs,
        featured_jobs=featured_jobs,
        latest_jobs=latest_jobs,
        total_jobs=len(jobs)
    )

# Job Details Page
@app.route("/job/<int:job_id>")
def job_details(job_id):
    jobs = load_jobs()

    for job in jobs:
        if job["id"] == job_id:
            return render_template("job_details.html", job=job)

    abort(404)


# About Page
@app.route("/about")
def about():
    return render_template("about.html")


# Contact Page
@app.route("/contact")
def contact():
    return render_template("contact.html")


# Custom 404 Page
@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)