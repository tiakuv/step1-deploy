from random import sample
from flask import Flask, render_template
from data import *

app = Flask(__name__)

@app.route('/')
def main():
    random_tours = {}
    rand_list = sample(range(1,tours.__len__()), 6) #генерирую 6 случайных значений без повторений
    for i in rand_list:
        random_tours[i] = tours[i]

    template_context = dict(title=title, subtitle=subtitle, description=description, tours=random_tours, departures=departures)
    output = render_template("index.html", **template_context)
    return output

@app.route('/departures/<departure>')
def show_dep(departure):

    tours_by_dep = {}
    for ind, tour in tours.items():
        if tour['departure'] == departure:
            tours_by_dep[ind] = tour

    tours_count = tours_by_dep.__len__()

    min_price = min(tours_by_dep.values(), key=lambda k: k['price'])['price']
    max_price = max(tours_by_dep.values(), key=lambda k: k['price'])['price']
    min_days = min(tours_by_dep.values(), key=lambda k: k['nights'])['nights']
    max_days = max(tours_by_dep.values(), key=lambda k: k['nights'])['nights']

    template_context = dict(departures=departures, title=title, departure=departure, selected_tours=tours_by_dep, tours_count=tours_count, min_price=min_price, max_price=max_price, min_days=min_days, max_days=max_days)
    output = render_template("departure.html", **template_context)
    return output

@app.route('/tours/<id>')
def show_tour(id):
    tour = tours[int(id)]
    output = render_template("tour.html", departures=departures, title=title, tour=tour)
    return output

if __name__ == '__main__':
    app.run()
