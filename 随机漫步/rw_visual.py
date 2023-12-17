import matplotlib.pyplot as plt

from random_walk import RandomWalk

#只要程序处于活动状态，就不断模拟随机漫步
while True:
    #创建一个RandomWalk实例
    rw = RandomWalk()
    rw.fill_walk()

    #将所有点绘制起来
    plt.style.use('classic')
    fig, ax = plt.subplots()
    ax.scatter(rw.x_values,rw.y_values,s=15)
    plt.show()

    keep_running = input("再来一次？[y/n]")
    if keep_running == "n":
        break
