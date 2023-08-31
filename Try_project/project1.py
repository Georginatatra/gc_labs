from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def Home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/routine')
def foo():
    return render_template('routine.html')


@app.route('/modify')
def modify():
    return render_template('modify.html')

# @app.error_handler(404)
# def page_not_found(e):
#     return render_template('404.html')
              
if __name__=='__main__':
    app.run(debug=True)