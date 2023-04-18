from PyQt5.QtWidgets import QMainWindow,QApplication
from img.MainWindow import Ui_MainWindow
import sys  #导入系统模块
import house_analysis   #导入自定义房子数据分析模块
import chart  #导入自定义绘图模块

#主窗体初始化类
class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Main,self).__init__()
        self.setupUi(self)

    # 显示各区二手房均价分析图
    def show_average_price(self):
        region,average_price= house_analysis.get_average_price() # 获取
        chart.average_price_bar(region, average_price,'各区二手房均价分析')
    def show_house_number(self):
        region,percentage= house_analysis.get_house_number() # 获取
        chart.house_number_pie(percentage,region,'获取各区房子数量比例')
    def show_renovation(self):
        type, number= house_analysis.get_renovation() # 获取
        chart.renovation_bar(type, number,'获取全市二手房装修程度对比')
    def show_house_type(self):
        type,price= house_analysis.get_house_type() # 获取
        chart.house_type_barh(type,price,'获取二手房热门户型均价')
    def show_price_forecast(self):
        y, y_pred= house_analysis.get_price_forecast() # 获取
        chart.price_forecast_plot(y, y_pred,'获取价格预测')


if __name__== "__main__":
    app = QApplication (sys.argv)
    #主窗体对象
    main = Main()#显示主窗体
    main.ton_1.triggered.connect(main.show_average_price)
    main.ton_2.triggered.connect(main.show_house_number)
    main.ton_3.triggered.connect(main.show_renovation)
    main.ton_4.triggered.connect(main.show_house_type)
    main.ton_5.triggered.connect(main.show_price_forecast)
    main.show ()
    sys.exit(app.exec_()) # 当窗口创建完成,需要结束主循环过程