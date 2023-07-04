from flask import Flask, render_template

app=Flask(__name__)

jobs=[
  {
    "ID":1,
    "Title":"Python Developer",
    "Location":"Bengaluru, India",
    "Salary":"Rs. 6,00,000"
  },
  {
    "ID":2,
    "Title":"Flask Developer",
    "Location":"Delhi, India"
  },
  {
    "ID":3,
    "Title":"Backend Developer",
    "Location":"Bengaluru, India",
    "Salary":"Rs. 16,00,000"
  }
]

@app.route("/")
def helloworld():
  return render_template("home.html", jobs=jobs,company="JobShala")

if __name__=="__main__":
  app.run(host="0.0.0.0", debug=True)