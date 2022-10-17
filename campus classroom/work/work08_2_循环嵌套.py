#一个农民朋友手中有100元，想买100只鸡回来喂养，公鸡每只2元，母鸡每只3元，小鸡每只0.5元，希望你来帮助下这位农民朋友，100元可以买100只鸡的方案有哪些?
count = 0
for x in range(0, 101):
    for y in range(0, 34):
        for z in range(0, 101):
            if x + y + z == 100 and x + 3 * y + 0.5 * z == 100:
                count += 1
                print("买法" + str(count) + "：公鸡" + str(x) + "只，" + "母鸡" + str(y) + "只，" + "小鸡" + str(z) + "只。")