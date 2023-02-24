from pyecharts.charts import Bar
from pyecharts import options as ops

from pyecharts.faker import Faker
from pyecharts.globals import ThemeType, RenderType
from pyecharts.render import make_snapshot
from snapshot_selenium import snapshot

bar = Bar(
    init_opts=ops.InitOpts(
        width='1000px',
        height='600px',  # 图表的画布大小
        renderer=RenderType.CANVAS,  # 渲染风格： CANVAS、SVG等
        page_title='网页标题',  # HTML网页标题
        theme=ThemeType.DARK,  # 主题配置
        bg_color='white'  # 背景颜色
    )  # 初始化配置项
)  # Bar 柱形图

bar.set_global_opts(
    title_opts=ops.TitleOpts(
        title="主标题",  # 主标题
        title_link='https://www.baidu.com',  # 主标题超链接
        title_target='blank',  # 跳转方式：blank新窗口，self当前窗口
        subtitle="副标题",  # 副标题
        subtitle_link='https://www.baidu.com',
        subtitle_target='self',
        pos_left='200px',  # 标题左间距
        pos_top='200px',  # 标题上间距
        item_gap=20  # 主标题和副标题间距
    ),  # 标题配置项

    datazoom_opts=ops.DataZoomOpts(
        is_show=True,  # 是否显示缩放组件
        type_='slider',  # 缩放组件样式：slider、inside
        is_realtime=True,  # 拖动是否实时更新图表
        range_start=40,  # 缩放组件起始位置，百分比
        range_end=100,  # 缩放组件的结束位置，百分比
        orient='horizontal',  # 缩放组件垂直还是水平放置，horizontal、vertical
        is_zoom_lock=True  # 是否锁定缩放组件
    ),  # 区域缩放配置项

    legend_opts=ops.LegendOpts(
        type_='plain',  # 图例类型，普通plain、可滚动翻页scroll
        is_show=True,  # 是否显示图例
        pos_left='20%',  # 图例位置
        orient='vertical',  # 图例垂直还是水平放置，horizontal、vertical
        selected_mode='multiple',  # 选择模式，True开始图例点击，False关闭图例点击，single单选，multiple多选
        align='right',  # 图标和文字的位置
        item_gap=20,  # 图例之间的间距
        item_width=30,  # 图例的大小
        legend_icon='rect'  # 图例的icon，circle、rect、roundRect、triangle、diamond、arrow
    ),  # 图例配置项

    visualmap_opts=ops.VisualMapOpts(
        is_show=True,
        type_='color',  # 类型，color、size
        min_=0,
        max_=150,  # 最大值
        range_opacity=0.7,  # 透明度
        range_text=['max', 'min'],  # 两端文本
        range_color=['blue', 'green', 'red'],  # 过渡颜色
        orient='vertical',  # 图例垂直还是水平放置，horizontal、vertical
        pos_right='5%',  # 位置
        is_piecewise=True,  # 是否分段
        is_inverse=False  # 是否反转
    ),  # 视觉映射配置项

    tooltip_opts=ops.TooltipOpts(
        is_show=True,
        trigger='item',  # 触发类型：item数据项提示（散点、柱形、饼图），axis坐标轴提示线（条形图、折线图）
        trigger_on='mousemove|click',  # 触发条件：mousemove、click、mousemove|click
        is_show_content=True,  # 是否显示提示框浮层
        formatter='{a}: {b}-{c}',  # 标签内容格式：{a}系列名  {b}数据名  {c}值
        background_color='black',  # 背景色
        border_color='white',  # 边框颜色
        border_width=1  # 边框宽度
    ),  # 提示框配置项

    xaxis_opts=ops.AxisOpts(
        is_show=True,  # 是否显示x轴
        type_='category',  # 坐标轴类型：value数值轴（用于连续性数据）、category类目轴（用于离散数据）、time时间轴
    ),  # x坐标轴配置项

    yaxis_opts=ops.AxisOpts(
        is_show=True,
        axisline_opts=ops.AxisLineOpts(is_show=False),  # 显示时y轴的线
        axistick_opts=ops.AxisTickOpts(is_show=False),  # 不显示y轴的刻度
    )  # y坐标轴配置项
)  # set_global_opts 全局配置

bar.add_xaxis(Faker.choose())  # Faker.choose()  生成同一属性的随机7个值（list），便于调试造数据
bar.add_yaxis("商家A", Faker.values())  # Faker.choose()  生成随机7个数字（list）
bar.add_yaxis("商家B", Faker.values())

# make_snapshot(snapshot, bar.render(), 'bar.png')  # 生成图片文件

# render 会生成本地 HTML 文件，默认会在当前目录生成 render.html 文件
# 也可以传入路径参数，如 bar.render("mycharts.html")
bar.render()
