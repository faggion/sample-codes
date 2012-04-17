import logging,json,urllib,md5,time
from flask import Flask,render_template,abort,make_response,request,url_for,redirect
app = Flask(__name__)

@app.route("/authz")
def authz():
    if "appid" not in request.args or \
            "scope" not in request.args or \
            "redirect_url" not in request.args:
        abort(400)

    tmpl = {"appid":request.args["appid"],
            "scope":request.args["scope"],
            "redirect_url":request.args["redirect_url"]}
    return render_template("authz.html",T=tmpl);

@app.route("/token")
def token():
    # validate code
    if "code" in request.args:
        pass
    abort(400)
    return "Hello World!"

@app.route("/submit", methods=['POST'])
def submit():
    code   = "DENIED"
    denied = request.form.get('deny')
    url    = request.form.get('redirect_url')
    if not denied:
        code = md5.new(str(time.time())).hexdigest()
    return redirect(url + "?code=" + code)

@app.errorhandler(400)
def badrequest(error):
    ret = {"header":{"status":4000000,"message":"bad request"}}
    response = app.make_response((json.dumps(ret), 400))
    response.headers['Content-type'] = 'application/json'
    return response

if __name__ == "__main__":
    logging.getLogger().setLevel(logging.DEBUG)
    app.run(debug=True, port=5000)
