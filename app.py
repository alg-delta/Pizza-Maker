# app.py
from flask import Flask, render_template, redirect, url_for, session, request
from create_db import create_db
from models import db, Dough, Main, Dop


app = Flask(__name__)

# --- КОНФІГУРАЦІЯ FLASK ---
app.config['SECRET_KEY'] = 'your_super_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


# --- МАРШРУТИ (ROUTES) ---

@app.route('/')
def home():
    """
    Головна сторінка додатку.
    """
    return render_template('index.html')

@app.route("/step1", methods=["GET", "POST"])
def step1():
    #post when Dali is clicked
    if request.method == "POST":
        dough_id=request.form.get("dough")
        session["dough_id"] = int(dough_id)
        #print(session)
        return redirect(url_for('step2'))


#GET when entering web
    session.clear()

    doughs = Dough.query.all() #take all data from Dough
    return render_template("step1.html", doughs=doughs)





@app.route("/step2", methods=["GET", "POST"])
def step2():
    if "dough_id" not in session:
        return redirect(url_for('step1'))
    #post when Dali is clicked
    if request.method == "POST":
        main_id=request.form.get("main")
        session["main_id"] = int(main_id)
        #print(session)
        return redirect(url_for('step3'))


#GET when entering web
    dough_id = session.get('dough_id')
    dough_sel = Dough.query.get(dough_id)
    selected_main_id=session.get("main_id")
    mains = Main.query.all() #take all data from Dough
    return render_template("step2.html", mains=mains, selected_main_id=selected_main_id, dough_sel=dough_sel)








@app.route("/step3", methods=["GET", "POST"])
def step3():
    if "main_id" not in session:
        return redirect(url_for('step2'))
    #post when Dali is clicked
    if request.method == "POST":


        dop_ids=[int(value) for value in request.form.getlist("dop")]
        session["dop_ids"]=dop_ids

        dop_quantities={}
        for dop_id in dop_ids:
            number=request.form.get(f"count_{dop_id}")
            dop_quantities[dop_id]=int(number)
        session["dop_quantities"]=dop_quantities

        #print(session)
        return redirect(url_for('step4'))

    dough_id = session.get('dough_id')
    dough_sel = Dough.query.get(dough_id)
    main_id = session.get('main_id')
    main_sel = Main.query.get(main_id)

    selected_dop_ids=session.get('dop_ids', [])
    selected_quantities=selected_quantities = {
        int(key): value for key, value in session.get('dop_quantities', {}).items()
    }


#GET when entering web
    dops = Dop.query.all() #take all data from Dough
    return render_template("step3.html", dops=dops, selected_dop_ids=selected_dop_ids, selected_quantities=selected_quantities, dough_sel=dough_sel, main_sel=main_sel)

@app.route("/step4", methods=["GET", "POST"])
def step4():

    if request.method == "POST":
        name = request.form.get("name")
        phone = request.form.get("phone")
        comment = request.form.get("comment")
        session["name"] = name
        session["phone"] = phone
        session["comment"] = comment

    dough_id= session.get('dough_id')
    dough=Dough.query.get(dough_id)
    main_id= session.get('main_id', '')
    main = Main.query.get(main_id)
    dop_ids= session.get("dop_ids")
    dops= Dop.query.filter(Dop.id.in_(dop_ids)).all()
    selected_quantities = {
        int(key): value for key, value in session.get('dop_quantities', {}).items()
    }
    total_price = dough.price+main.price
    for dop in dops:
        count=selected_quantities.get(dop.id, 1)
        total_price+=dop.price*count
    name = session.get('name', '')
    phone = session.get('phone', '')
    comment = session.get('comment', '')

    # for dop in dops:


    return render_template("sum.html", total_price=total_price, name=name, phone=phone, comment=comment, dough=dough, main=main, dops=dops, selected_quantities=selected_quantities)


@app.route("/confirm", methods=["GET", "POST"])
def confirm():
    session.clear()
    return redirect(url_for('thank_you'))

@app.route("/thank_you", methods=["GET", "POST"])
def thank_you():
    return render_template("thank_you.html")


# --- ЗАПУСК ДОДАТКА ---
if __name__ == '__main__':
    # create_db()
    app.run(debug=True)
