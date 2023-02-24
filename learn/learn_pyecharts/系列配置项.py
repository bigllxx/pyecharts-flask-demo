from pyecharts.charts import Line
from pyecharts import options as ops
from pyecharts.faker import Faker

line = Line()  # Line 折线图
line.set_global_opts(
    tooltip_opts=ops.TooltipOpts(
        trigger='axis'
    )
)

line.set_series_opts(
    itemstyle_opts=ops.ItemStyleOpts(
        color='block',
        opacity=0.5,
        border_color='green',
        border_width=2
    ),  # 图元样式配置项

    linestyle_opts=ops.LineStyleOpts(
        is_show=True,
        width=10,
        color='blue',
    ),  # 线样式配置项

    # 太多了，不学了，后面查文档吧
)  # 系列配置项

line.add_xaxis(Faker.choose())
line.add_yaxis("商家A", Faker.values())
line.add_yaxis("商家B", Faker.values())

line.render()
