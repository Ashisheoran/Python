
from flask import Blueprint, render_template, request, redirect, url_for
from models import db, LibraryMember, LibraryItem, MemberType

app_routes = Blueprint('routes', __name__)

@app_routes.route("/")
def home():
    return render_template("home.html")

@app_routes.route("/add_member", methods=["GET", "POST"])
def add_member():
    if request.method == "POST":
        name = request.form["name"]
        mtype = request.form["type"]
        new_member = LibraryMember(name=name, member_type=MemberType[mtype.upper()])
        db.session.add(new_member)
        db.session.commit()
        return redirect(url_for("routes.view_members"))
    return render_template("add_member.html")

@app_routes.route("/members")
def view_members():
    members = LibraryMember.query.all()
    return render_template("view_members.html", members=members)

@app_routes.route("/add_item", methods=["GET", "POST"])
def add_item():
    if request.method == "POST":
        title = request.form["title"]
        creator = request.form["creator"]
        copies = int(request.form["copies"])
        item_type = request.form["item_type"]
        item = LibraryItem(title=title, creator=creator, copies=copies, item_type=item_type)
        db.session.add(item)
        db.session.commit()
        return redirect(url_for("routes.view_items"))
    return render_template("add_item.html")

@app_routes.route("/items")
def view_items():
    items = LibraryItem.query.all()
    return render_template("view_items.html", items=items)

