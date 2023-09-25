from flask import Flask, render_template, request 

app = Flask(__name__)
JOBS =[
    {'title': "software engineer",
    'company': 'google',
    'location': 'Mountain View, CA',
    'salary': '200,000'
    },

    {'title': "software engineer",
    'company': 'Facebook',
    'location': 'Chicago, CA',
    'salary': '120,000'
    },
    {'title': "Senior Developer",
    'company': 'Lockheed Martin ',
    'location': 'Alexandria, VA',
    'salary': '400,000'
    },
    {'title': "Junior Developer",
    'company': 'Microsoft',
    'location': 'Seattle, WA',
    'salary': '95,000'
}
]

@app.route("/")
def index():
    return render_template('index.html', jobs = JOBS, company_name = "google")
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug = True)