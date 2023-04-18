import matplotlib # 导入图表模块
import matplotlib.pyplot as plt # 导入绘图模块
# #避免中文乱码
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams ['axes.unicode_minus'] = False
#显示均价条形图
def average_price_bar(x,y, title):
    plt.figure ()
    plt.bar(x,y, alpha=0.8)
    plt.xlabel("区域")
    plt.ylabel("均价")
    plt.title(title)
    #为每一个图形加数值标签
    for x, y in enumerate (y):
        plt.text(x, y + 100, y, ha='center')
    plt.show()

# 3.2.2 将区域二手房数量所占比例通过饼图显示
def house_number_pie(size,label,title):
    # group_number = data.groupby('区域').size()  # 房子区域分组数量
    # print('各区域的房子数量:', group_number)
    # region = group_number.index  # 区域
    # numbers = group_number.values  # 获取每个区域内房子出售的数量
    # percentage = numbers / numbers.sum() * 100  # 计算每个区域房子数量的百分比
    # size = percentage
    # label = region
    # title = '各区二手房数量所占比例分析'
    plt.pie(size, labels=label,labeldistance=1.05,
                autopct="%1.1f%%", shadow=True,
                startangle=0, pctdistance=0.6)
    plt.axis('equal')  # 设置横轴和纵轴大小相等，这样饼才是圆的
    plt.title(title, fontsize=12)
    plt.legend(bbox_to_anchor=(0.03, 1)) #设置图例显示位置
    plt.show()    # 显示饼图
# 3.3.2  将全市二手房装修类型通过纵向条形统计图显示
def renovation_bar(x,y, title):
    # title = '各区二手房装修类型分析'
    plt.bar(x,y, alpha=0.8)  # 绘制条形图
    plt.xlabel("装修类型") # 区域文字
    plt.ylabel("数量") # 均价文字
    plt.title(title) # 表标题文字
    # 为每一个图形加数值标签
    for x, y in enumerate(y):
        plt.text(x, y + 10, y, ha='center')
    plt.show()

# 3.4.2 将热门户型的数量用水平条形图显示
def house_type_barh(type, price,title):
    # title = '热门户型均价分析'
    plt.barh(type, price, height=0.3,
             color='r', alpha=0.8)  #从下往上画水平条形图
    plt.xlim(0, 15000)      # X轴的均价0~15000
    plt.xlabel("均价")
    plt.title(title)
    # 为每一个图形加数值标签
    for y, x in enumerate(price):
        plt.text(x + 10, y,str(x) + '元', va='center')
    plt.show()
# 3.5.2 显示预测房价折线图
def price_forecast_plot(y,y_pred,title):
    # title = '二手房售价预测'
    # 绘制折线，并在折点添加蓝色圆点
    plt.plot(y, color='r', marker='o',label='真实房价')
    plt.plot(y_pred, color='b', marker='*', label='预测房价')
    plt.xlabel('房子数量')
    plt.ylabel('房子总价')
    plt.title(title)  # 表标题文字
    plt.legend()  # 显示图例
    plt.grid()  # 显示网格
    plt.show()  # 显示图表