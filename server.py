from flask import Flask,render_template
import random
import datetime
import requests
app = Flask(__name__)


@app.route('/')
def home():
    random_number = random.randint(1,10)
    current_year = datetime.datetime.now().year
    return render_template("index.html", num=random_number,year=current_year)

@app.route("/guess/<name>")
def guess(name):
    gender_url =f"https://api.genderize.io?name={name}"
    gender_data = requests.get(gender_url).json()
    gender = gender_data['gender']

    age_url = f"https://api.agify.io?name={name}"
    age_data = requests.get(age_url).json()
    age = age_data['age']

    return render_template("guess.html",person_name=name,age=age,gender=gender)


@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    blog_url= "https://api.npoint.io/c790b4d5cab58020d391"
    all_posts = requests.get(blog_url).json()
    return render_template("blog.html",posts=all_posts)


if __name__ =="__main__":
    app.run(debug=True)

