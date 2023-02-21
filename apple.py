class GoldenApple:

    def __init__(self):
        self.MaturityTime = 5280
        self.CultivationTime = 720

def time_count(pour_num, pour_minute, fruit_color, plant_num):
    pour_count = int(pour_num) * int(pour_minute)
    plant_time_day = 1440 + pour_count
    if fruit_color == "golden":
        MaturityTime = 5280
        CultivationTime = 720
    elif fruit_color == "purple":
        MaturityTime = 2400
        CultivationTime = 360
    one_land_food_time_day = (plant_time_day / MaturityTime) * CultivationTime
    one_land_food_time_week = one_land_food_time_day * 7
    all_land_food_time_week = one_land_food_time_week * int(plant_num)
    print("每周种植可收获道法果闭关修炼时长： " + str(all_land_food_time_week) + "分钟")
    print("每周种植可收获道法果闭关修炼时长： " + str((all_land_food_time_week) / 60) + "小时")
    return all_land_food_time_week



if __name__ == "__main__":
    pour_num = input("请输入浇灌次数（整数）")
    pour_minute = input("请输入每次浇灌的时长（分钟）")
    fruit_color = input("请输入种植道法果类型（golden、purple）")
    plant_num = input("请输入种植道法果株数（1-12）")
    time_count(pour_num, pour_minute, fruit_color, plant_num)




