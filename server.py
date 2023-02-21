import os
from flask import Flask, request, render_template, redirect, flash


app = Flask(__name__)
app.secret_key = 'some_secret'


@app.route('/')
def apple():
    return render_template('default.html')


@app.route('/result/', methods=['GET', 'POST'])
def time_count():
    if request.method == 'GET':
        return render_template('default.html')
    else:
        poor_num = request.form.get('pour_num')
        print(poor_num)
        pour_minute = request.form.get('pour_minute')
        print(pour_minute)
        fruit_color = request.values.get('fruit_color')
        print(fruit_color)
        golden_mt = 5280
        golden_ct = 720
        purple_mt = 2400
        purple_ct = 360
        if fruit_color == "金色":
            MaturityTime = golden_mt
            CultivationTime = golden_ct
        elif fruit_color == "紫色":
            MaturityTime = purple_mt
            CultivationTime = purple_ct
        plant_num = request.form.get('plant_num')
        print(plant_num)
        pour_count = int(poor_num) * int(pour_minute)
        plant_time_day = 1440 + pour_count
        one_land_food_time_day = (plant_time_day / MaturityTime) * CultivationTime
        one_land_food_time_week = one_land_food_time_day * 7
        all_land_food_time_week = one_land_food_time_week * int(plant_num)
        print("每周种植可收获道法果闭关修炼时长： " + str(all_land_food_time_week) + "分钟")
        print("每周种植可收获道法果闭关修炼时长： " + str((all_land_food_time_week) / 60) + "小时")
        flash("每周种植可收获道法果闭关修炼时长为" + str((all_land_food_time_week) / 60) + "小时")
        return render_template('result.html')


if __name__ == '__main__':
    app.run(port=5000, debug=True)