
from matplotlib import pyplot as plt





#선그래프
def pltLine(xs, ys, title='None', color='green', marker='o', line_style='solid', x_label='x label', y_label='y label'):
    """선그래프로 표시하기"""
    plt.plot(xs, ys, color, marker)
    plt.title(title)
    plt.show()

#막대그래프
def pltBar(xs, ys, title='None', color='green', marker='o', line_style='solid', x_label='x label', y_label='y label'):
    """막대 그래프로 표시하기"""    
    #데이터 입력, 막대가 가운데 옴
    plt.bar([i for i, _ in enumerate(xs)], ys)
    plt.ylabel(y_label)
    plt.title(title)
    #x값마다 레이블 표시
    plt.xticks([i for i, _ in enumerate(xs)], xs)
    plt.show()


X=[1,2,3,4,5]
Y=[100,150,200,250,400]

pltBar(X, Y)
#pltLine(X, Y)