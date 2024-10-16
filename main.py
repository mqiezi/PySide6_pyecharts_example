import sys
import os
from PySide6.QtCore import QUrl
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PySide6.QtWebEngineWidgets import QWebEngineView
from pyecharts.globals import ThemeType
from pyecharts.charts import Bar, Line
from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.commons.utils import JsCode


x_data = ["14", "15", "16", "17", "18", "19", "20", "21", "22", "23"]
y_data = [393, 438, 485, 631, 689, 824, 987, 1000, 1100, 1200]

background_color_js = (
    "new echarts.graphic.LinearGradient(0, 0, 0, 1, "
    "[{offset: 0, color: '#c86589'}, {offset: 1, color: '#06a7ff'}], false)"
)
area_color_js = (
    "new echarts.graphic.LinearGradient(0, 0, 0, 1, "
    "[{offset: 0, color: '#eb64fb'}, {offset: 1, color: '#3fbbff0d'}], false)"
)


# 创建应用窗口
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PySide6 + PyEcharts 示例")
        self.setGeometry(100, 100, 800, 600)

        # 创建中心部件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.layout = QVBoxLayout(central_widget)

        # 生成 pyecharts 图表
        # 更多图标参考 https://gallery.pyecharts.org/#/README
        chart = (
            # Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT, js_host="./"))
            # .add_xaxis(["A", "B", "C", "D"])
            # .add_yaxis("销量", [5, 20, 36, 10])
            # .set_global_opts(
            #     title_opts=opts.TitleOpts(title="柱状图", subtitle="简单例子")
            # )
            # Line(init_opts=opts.InitOpts(theme=ThemeType.LIGHT, js_host="./"))
            # .add_xaxis(Faker.choose())
            # .add_yaxis("商家A", Faker.values())
            # .add_yaxis("商家B", Faker.values())
            # .set_global_opts(title_opts=opts.TitleOpts(title="Line-基本示例"))
            # Line(init_opts=opts.InitOpts(theme=ThemeType.LIGHT, js_host="./"))
            # .add_xaxis(Faker.choose())
            # .add_yaxis("商家A", Faker.values(), is_smooth=True)
            # .add_yaxis("商家B", Faker.values(), is_smooth=True)
            # .set_global_opts(title_opts=opts.TitleOpts(title="Line-smooth"))
            Line(
                init_opts=opts.InitOpts(
                    theme=ThemeType.LIGHT,
                    js_host="./",
                    bg_color=JsCode(background_color_js),
                )
            )
            .add_xaxis(xaxis_data=x_data)
            .add_yaxis(
                series_name="注册总量",
                y_axis=y_data,
                is_smooth=True,
                is_symbol_show=True,
                symbol="circle",
                symbol_size=6,
                linestyle_opts=opts.LineStyleOpts(color="#fff"),
                label_opts=opts.LabelOpts(is_show=True, position="top", color="white"),
                itemstyle_opts=opts.ItemStyleOpts(
                    color="red", border_color="#fff", border_width=3
                ),
                tooltip_opts=opts.TooltipOpts(is_show=False),
                areastyle_opts=opts.AreaStyleOpts(
                    color=JsCode(area_color_js), opacity=1
                ),
            )
            .set_global_opts(
                title_opts=opts.TitleOpts(
                    title="OCTOBER 2015",
                    pos_bottom="5%",
                    pos_left="center",
                    title_textstyle_opts=opts.TextStyleOpts(color="#fff", font_size=16),
                ),
                xaxis_opts=opts.AxisOpts(
                    type_="category",
                    boundary_gap=False,
                    axislabel_opts=opts.LabelOpts(margin=30, color="#ffffff63"),
                    axisline_opts=opts.AxisLineOpts(is_show=False),
                    axistick_opts=opts.AxisTickOpts(
                        is_show=True,
                        length=25,
                        linestyle_opts=opts.LineStyleOpts(color="#ffffff1f"),
                    ),
                    splitline_opts=opts.SplitLineOpts(
                        is_show=True,
                        linestyle_opts=opts.LineStyleOpts(color="#ffffff1f"),
                    ),
                ),
                yaxis_opts=opts.AxisOpts(
                    type_="value",
                    position="right",
                    axislabel_opts=opts.LabelOpts(margin=20, color="#ffffff63"),
                    axisline_opts=opts.AxisLineOpts(
                        linestyle_opts=opts.LineStyleOpts(width=2, color="#fff")
                    ),
                    axistick_opts=opts.AxisTickOpts(
                        is_show=True,
                        length=15,
                        linestyle_opts=opts.LineStyleOpts(color="#ffffff1f"),
                    ),
                    splitline_opts=opts.SplitLineOpts(
                        is_show=True,
                        linestyle_opts=opts.LineStyleOpts(color="#ffffff1f"),
                    ),
                ),
                legend_opts=opts.LegendOpts(is_show=False),
            )
        )

        # 保存图表为 HTML 文件
        chart_path = os.path.join(os.getcwd(), "chart.html")
        chart.render(chart_path)
        # chart.render(r"chart.html")

        # 将 HTML 加载到 QWebEngineView 中
        # 创建 QWebEngineView 小部件
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl.fromLocalFile(f"{chart_path}"))

        # self.browser.load(QUrl.fromLocalFile("file:///chart.html"))
        # self.browser.setUrl(QUrl("file:///chart.html"))

        self.browser.show()
        # self.browser.setUrl(QUrl("https://www.baidu.com"))
        # self.browser.setHtml(
        #     "<html><body><h1>Hello World... Hello World</h1></body></html>"
        # )

        self.layout.addWidget(self.browser)


# 运行应用
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
