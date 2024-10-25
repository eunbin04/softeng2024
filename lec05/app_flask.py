from flask import Flask, render_template
import pandas as pd
app = Flask(__name__)


@app.route('/')
def landing_page():
    return render_template('landing.html', title='Home')


@app.route('/blog')
def blog_list():

    df = pd.read_csv("data.csv")
    post_list = []
    for i, row in df.iterrows():
        post_list.append({
            "title": row["title"],
            "content": row["content"],
        })

    print(post_list)
    return render_template('blog.html', title="blog post", posts=post_list)


@app.route('/about')
def about_page():
    return render_template('about_me.html', title="about me")


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
