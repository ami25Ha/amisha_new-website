from flask import Flask, render_template#to use template we use render template function.

app=Flask(__name__) #created flask applicaation

@app.route("/")#now create a route
def hello_world(): #defining a function
  return render_template("home.html") #retrun template

if __name__=='__main__':
  app.run(host='0.0.0.0',debug=True) #local host (host=0.0.0.0)
#1-Create a project on Github
#2-open up the project on replit
#3-create and run a flask web server
#4-push changes back to Github
