from flask import Flask, jsonify, render_template, request, redirect, url_for

app = Flask(__name__)

SPORTS = [
  {
    'id': 1,
    'title': 'Box Cricket',
    'about': 'Box cricket is a bat-and-ball game played between two teams of eleven players on a field at the centre of which is a 22-yard (20-metre) pitch with a wicket at each end, each comprising two bails balanced on three stumps.',
    'image': 'Image 1.jpg'
  }, 
  {
    'id': 2,
    'title': '7 a side Football',
    'about': 'Football, also called association football or soccer, is a game involving two teams of 11 players who try to maneuver the ball into the other teams goal without using their hands or arms. The team that scores more goals wins.',
    'image': 'Image 2.jpg'
  }
]



JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 10,00,000'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Delhi, India',
    'salary': 'Rs. 15,00,000'
  },
  {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Remote',
    'salary': 'Rs. 12,00,000'
  },
  {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'San Francisco, USA',
    'salary': '$120,000'
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, sports=SPORTS)

@app.route("/booking")
def load_booking():
  return jsonify(SPORTS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
