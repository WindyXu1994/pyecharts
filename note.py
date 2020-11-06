# 《快速使用文档》
# 参考资料：
# 官方帮助文档 https://pyecharts.org/
# 简易教程 https://www.kesci.com/mw/project/5eb7958f366f4d002d783d4a

#可能引用的模块
from pyecharts.charts import Bar,Line,Scatter,Pie,Sunburst,Timeline,Grid
from pyecharts import options as opts
from pyecharts.charts import Grid
from pyecharts.globals import ThemeType

##============================================================================================================##
##============================================================================================================##
##=============================== 直角坐标系：折线图Line、散点图Scatter、柱状图Bar ==============================##
##============================================================================================================##
##============================================================================================================##

#------------------------------------------ 定义 ------------------------------------------#
line=(
    Line()
    .x()
)
#等效于（除了render）
line=Line()
line.x()

#---------------------------------------- 添加数据 ----------------------------------------#
line=(
    Line()
    .add_xaxis(
    
        # x数据，列表
        xaxis_data    
    )  
    
    .add_yaxis(
    
        # y名称和数据，字符串和列表，多组y数据直接多次添加
        'series_name',y_axis,
        
        # 多轴时使用yaxis_index进行控制
        yaxis_index = 0,
        
        # 是否连接空数据，空数据使用 `None` 填充
        #（在type为value时可用，category时不可用）
        is_connect_nones = True,
    )
    
    # 添加x轴或y轴，extend默认index=1,global默认为index=0
    .extend_axis( yaxis=opts.AxisOpts() )  
)

#---------------------------------------- 配件及控制 ----------------------------------------#
line=(
    Line()
    .add_yaxis(
        
        # 数据标签(总控见global)
        label_opts=opts.LabelOpts(is_show=False),
        
        # 显示 symbol
        is_symbol_show = True,
           
        # 数据堆叠，相同的 stack 值可以堆叠放置
        stack = 'stack1',
        
        # 标记点、线控制
        markpoint_opts=opts.MarkPointOpts(),
        
        # 提示信息
        tooltip_opts=opts.TooltipOpts(),
    )
    
    # 添加坐标轴
    .extend_axis( yaxis=opts.AxisOpts() )
    
    .set_global_opts(
        
        # 数据标签(分控见add_yaxis)
        label_opts=opts.LabelOpts( is_show=False ),
        
        # 标题
        title_opts=opts.TitleOpts( title='TITLE' ),
        
        # 图例
        legend_opts=opts.LegendOpts( is_show=True ),
        
        # 坐标轴
        xaxis_opts=opts.AxisOpts(
            
            # 坐标轴数据格式
            type_="value",
            
            # 坐标轴标签                                               
            axislabel_opts = opts.LabelOpts()
            
            # 坐标轴名称
            name_textstyle_opts = opts.TextStyleOpts()
            
            # pointer
            axispointer_opts=opts.AxisPointerOpts(is_show=True)
            
            # 分隔线
            splitline_opts=opts.SplitLineOpts(is_show=True),
        )
    )
    
    .set_series_opts(
        # 区域标记
        markarea_opts=opts.MarkAreaOpts(
            is_silent=False,
            data=[
                opts.MarkAreaItem(
                    name='',
                    x=(year-0.5,year+0.5),
                    label_opts=opts.LabelOpts(is_show=False),
                    itemstyle_opts=opts.ItemStyleOpts(
                        color="#aaaaaa", opacity=0.1
                    ),
                )
            ]
        )
    )
)

#------------------------------------- 配件及其他常用格式详解 -------------------------------------#
line=(
    Line(
        # 初始化                                                                                   https://pyecharts.org/#/zh-cn/global_options?id=initopts%ef%bc%9a%e5%88%9d%e5%a7%8b%e5%8c%96%e9%85%8d%e7%bd%ae%e9%a1%b9
        width = "900px",
        height = "500px",
        page_title = "Awesome-pyecharts",
        theme: str = "white",
        
        bg_color = {
            type: 'linear',
            x: 0,
            y: 0,
            x2: 0,
            y2: 1,
            colorStops: [
                {offset: 0, color: 'red' },// 0% 处的颜色
                {offset: 1, color: 'blue' // 100% 处的颜色
            }],
            global: false // 缺省为 false
        },
        # 线性渐变，前四个参数分别是 x0, y0, x2, y2, 范围从 0 - 1，相当于在图形包围盒中的百分比，径向为x,y,r
        # 如果 globalCoord 为 `true`，则该四个值是绝对的像素位置
        # 纹理填充
        # color: {
        #    image: imageDom, // 支持为 HTMLImageElement, HTMLCanvasElement，不支持路径字符串
        #    repeat: 'repeat' // 是否平铺, 可以是 'repeat-x', 'repeat-y', 'no-repeat'
        # }
        
        # 动画                                                                                     https://pyecharts.org/#/zh-cn/global_options?id=animationopts%ef%bc%9aecharts-%e7%94%bb%e5%9b%be%e5%8a%a8%e7%94%bb%e9%85%8d%e7%bd%ae%e9%a1%b9
        animation_opts = opts.AnimationOpts()
        
    )
    
    .add_yaxis(
        symbol = 'rect',
        symbol_size = 10,
        is_smoth = True,
        
        linestyle_opts = opts.LineStyleOpts(                                                       #https://pyecharts.org/#/zh-cn/series_options?id=linestyleopts%ef%bc%9a%e7%ba%bf%e6%a0%b7%e5%bc%8f%e9%85%8d%e7%bd%ae%e9%a1%b9
            width = 1,
            opacity = 1,
            color = '',
        )
    )
        
        # 图元                                                                                     https://pyecharts.org/#/zh-cn/series_options?id=itemstyleopts%ef%bc%9a%e5%9b%be%e5%85%83%e6%a0%b7%e5%bc%8f%e9%85%8d%e7%bd%ae%e9%a1%b9
        itemstyle_opts=opts.ItemStyleOpts(
            color = '',
            border_color = None,
            border_width = None,
            opacity = 1,
            area_color = None,
        )
        
        # 数据标签(总控见global)                                                                   https://pyecharts.org/#/zh-cn/series_options?id=labelopts%ef%bc%9a%e6%a0%87%e7%ad%be%e9%85%8d%e7%bd%ae%e9%a1%b9
        label_opts=opts.LabelOpts(
            is_show = False,
            position = 'inside',
            color = '#aaaaaa',
            distance = 10,
            font_size = f_size,
            font_family = 'Microsoft YaHei',
            rotate = -15,
            
            formatter = '   {b|{b}}   ',
            background_color="rgba(238,238,238,0.6)",
            border_color="#969191",
            border_width=1,
            border_radius=4,
            rich={
                "b": {
                    "color": "#000000",
                    "fontSize":str(f_size), 
                    "lineHeight": f_size*1.7, 
                    "align": "center"
                },
            },
        ),
        
        # 标记点、线控制                                                                            https://pyecharts.org/#/zh-cn/series_options?id=markpointopts%ef%bc%9a%e6%a0%87%e8%ae%b0%e7%82%b9%e9%85%8d%e7%bd%ae%e9%a1%b9
        markpoint_opts=opts.MarkPointOpts(                                                         #https://gallery.pyecharts.org/#/Line/line_markpoint_custom
            data=[opts.MarkPointItem(
                    name="自定义标记点",
                    coord=[x[2], y[2]], value=y[2]
                    type_='min',    
                )
            ]
        ),
        
        # 提示信息                                                                                 https://pyecharts.org/#/zh-cn/global_options?id=tooltipopts%ef%bc%9a%e6%8f%90%e7%a4%ba%e6%a1%86%e9%85%8d%e7%bd%ae%e9%a1%b9
        tooltip_opts=opts.TooltipOpts(),
    )
    
    # 额外坐标轴                                                                                   https://pyecharts.org/#/zh-cn/global_options?id=axisopts%ef%bc%9a%e5%9d%90%e6%a0%87%e8%bd%b4%e9%85%8d%e7%bd%ae%e9%a1%b9
    .extend_axis( 
        yaxis=opts.AxisOpts( position = 'right' )
    )
    
    .set_global_opts(
        
        # 数据标签(分控见add_yaxis)                                                                 https://pyecharts.org/#/zh-cn/series_options?id=labelopts%ef%bc%9a%e6%a0%87%e7%ad%be%e9%85%8d%e7%bd%ae%e9%a1%b9
        label_opts=opts.LabelOpts( is_show=False ),
        
        # 标题                                                                                     https://pyecharts.org/#/zh-cn/global_options?id=titleopts%ef%bc%9a%e6%a0%87%e9%a2%98%e9%85%8d%e7%bd%ae%e9%a1%b9
        title_opts=opts.TitleOpts(
            title = 'TITLE',
            subtitle = 'subtitle',
            pos_left = 'center',
            pos_top = '20%',
            title_textstyle_opts = opts.TextStyleOpts(                                             #https://pyecharts.org/#/zh-cn/series_options?id=textstyleopts%ef%bc%9a%e6%96%87%e5%ad%97%e6%a0%b7%e5%bc%8f%e9%85%8d%e7%bd%ae%e9%a1%b9
                color = '',
                font_size = 20,
            )
        ),
        
        # 图例                                                                                     https://pyecharts.org/#/zh-cn/global_options?id=legendopts%ef%bc%9a%e5%9b%be%e4%be%8b%e9%85%8d%e7%bd%ae%e9%a1%b9
        legend_opts=opts.LegendOpts(
            is_show=True,
            pos_left = 'left',
            pos_bottom = 20,
            orient = 'vertical',
            item_gap = 10,
            item_width = 25,
        ),
        
        # 坐标轴                                                                                   https://pyecharts.org/#/zh-cn/global_options?id=axisopts%ef%bc%9a%e5%9d%90%e6%a0%87%e8%bd%b4%e9%85%8d%e7%bd%ae%e9%a1%b9
        yaxis_opts=opts.AxisOpts(
            type_ = "value",
            name = 'y axis',
            name_gap = 15,
            is_show = True,
            position = 'left',
            
            split_number = 5,
            min_ = 0,
            max_ = 1000,
            min_interval = 1,
            
            # 坐标轴线                                                                             https://pyecharts.org/#/zh-cn/global_options?id=axislineopts-%e5%9d%90%e6%a0%87%e8%bd%b4%e8%bd%b4%e7%ba%bf%e9%85%8d%e7%bd%ae%e9%a1%b9
            axisline_opts = opts.AxisLineOpts(
                is_show = True,
                symbol = ['none', 'arrow']
                linestyle_opts = opts.LineStyleOpts(                                               #https://pyecharts.org/#/zh-cn/series_options?id=linestyleopts%ef%bc%9a%e7%ba%bf%e6%a0%b7%e5%bc%8f%e9%85%8d%e7%bd%ae%e9%a1%b9
                    width = 1,
                    opacity = 1,
                    color = '',
                )
            )
            
            # 坐标轴刻度                                                                           https://pyecharts.org/#/zh-cn/global_options?id=axistickopts-%e5%9d%90%e6%a0%87%e8%bd%b4%e5%88%bb%e5%ba%a6%e9%85%8d%e7%bd%ae%e9%a1%b9
            axistick_opts = opts.AxisTickOpts(
                is_show = True,
                length = None,
                linestyle_opts = opts.LineStyleOpts()
            )
            
            # 坐标轴标签                                                                           https://pyecharts.org/#/zh-cn/series_options?id=labelopts%ef%bc%9a%e6%a0%87%e7%ad%be%e9%85%8d%e7%bd%ae%e9%a1%b9
            axislabel_opts = opts.LabelOpts(
                is_show = False,
                distance = 10,
                font_size = f_size,
                font_family = 'Microsoft YaHei',
            )
            
            # 坐标轴名称
            name_textstyle_opts = opts.TextStyleOpts(                                              #https://pyecharts.org/#/zh-cn/series_options?id=textstyleopts%ef%bc%9a%e6%96%87%e5%ad%97%e6%a0%b7%e5%bc%8f%e9%85%8d%e7%bd%ae%e9%a1%b9
                color = '',
                font_size = 15,
            )
            
            # 坐标轴次刻度线                                                                       https://pyecharts.org/#/zh-cn/series_options?id=minortickopts%ef%bc%9a%e6%ac%a1%e7%ba%a7%e5%88%bb%e5%ba%a6%e9%85%8d%e7%bd%ae%e9%a1%b9
            minor_tick_opts = opts.MinorTickOpts()
            
            # pointer                                                                              https://pyecharts.org/#/zh-cn/global_options?id=axispointeropts-%e5%9d%90%e6%a0%87%e8%bd%b4%e6%8c%87%e7%a4%ba%e5%99%a8%e9%85%8d%e7%bd%ae%e9%a1%b9
            axispointer_opts=opts.AxisPointerOpts(is_show=True)
            
            # 分割区域                                                                             https://pyecharts.org/#/zh-cn/series_options?id=splitareaopts%ef%bc%9a%e5%88%86%e9%9a%94%e5%8c%ba%e5%9f%9f%e9%85%8d%e7%bd%ae%e9%a1%b9
            splitarea_opts = opts.SplitAreaOpts(is_show=True,)
            
            # 分隔线                                                                               https://pyecharts.org/#/zh-cn/series_options?id=splitlineopts%ef%bc%9a%e5%88%86%e5%89%b2%e7%ba%bf%e9%85%8d%e7%bd%ae%e9%a1%b9
            splitline_opts=opts.SplitLineOpts(is_show=True),
        )
    )
    
    .set_series_opts(
        # 区域标记                                                                                 https://pyecharts.org/#/zh-cn/series_options?id=markareaitem-%e6%a0%87%e8%ae%b0%e5%8c%ba%e5%9f%9f%e6%95%b0%e6%8d%ae%e9%a1%b9
        markarea_opts=opts.MarkAreaOpts(
            is_silent=False,
            data=[
                opts.MarkAreaItem(
                    name='',
                    x=(year-0.5,year+0.5),
                    label_opts=opts.LabelOpts(is_show=False),
                    itemstyle_opts=opts.ItemStyleOpts(color="#aaaaaa", opacity=0.1),
                )
            ]
        )
    )
)

#------------其他案例------------#
'''Bar: Bar_histogram_color'''
'''Line: 
Line_connect_null
Line_color_with_js_func
Distribution_of_electricity
'''

##=============================================================================================##
##=============================================================================================##
##============================== 极坐标系：饼图Pie、旭日图Sunburst ==============================##
##=============================================================================================##
##=============================================================================================##

#---------------------------------------- 定义及添加数据 ----------------------------------------#
sunburst=(
    Sunburst()
    .add(
        # 名称
        'name',
        
        # 数据
        data_pair=[
            {'name':'a','children':[data_pair2]},
            {'name':'a','value':1},
        ],
    )
    
    # 标题
    .set_global_opts(title_opts=opts.TitleOpts(title="示例"))
    
    # 标签
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}"))
)

pie=(
    Pie()
    .add(
        # 名称
        'name',
        
        # 数据
        data_pair=[(key1,value1),(key2,value2)]
        
        .set_global_opts(
            # 标题
            title_opts=opts.TitleOpts(title="Pie"),
            
            # 图例
            legend_opts=opts.LegendOpts(type_="scroll", orient="vertical"),
        )
    )
)
#---------------------------------------- 常用格式详解 ----------------------------------------#
sunburst=(
    Sunburst()
    .add(
        # 数据
        data_pair=[
            {'name':'a',"itemStyle": {"color": "#da0d68"},'children':[data_pair2]},
        ],
        
        # 中心坐标
        center = ['50%','50%']
        
        # 半径
        radius = [0,"95%"]
        
        # 层级格式
        levels = [
            {
                // 留给数据下钻点的空白配置
            },
            {
                // 最靠内测的第一层
                "r0": "15%",
                "r": "35%",
                itemStyle: { "borderWidth": 2 },
                label: { "rotate": "tangential", "align": "right" }
            },
            {
                // 第二层 ...
            }
        ]
    )
    
    # 标题                                                                                         https://pyecharts.org/#/zh-cn/global_options?id=titleopts%ef%bc%9a%e6%a0%87%e9%a2%98%e9%85%8d%e7%bd%ae%e9%a1%b9
    .set_global_opts(title_opts=opts.TitleOpts(title="示例"))
    
    # 标签                                                                                         https://pyecharts.org/#/zh-cn/series_options?id=labelopts%ef%bc%9a%e6%a0%87%e7%ad%be%e9%85%8d%e7%bd%ae%e9%a1%b9
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}"))
)

pie=(
    Pie()
    .add(
        # 名称
        'name',
        
        # 数据
        data_pair=[(key1,value1),(key2,value2)]
        
        .set_global_opts(
            # 标题                                                                                 https://pyecharts.org/#/zh-cn/global_options?id=titleopts%ef%bc%9a%e6%a0%87%e9%a2%98%e9%85%8d%e7%bd%ae%e9%a1%b9
            title_opts=opts.TitleOpts(title="Pie"),
            
            # 图例                                                                                 https://pyecharts.org/#/zh-cn/global_options?id=legendopts%ef%bc%9a%e5%9b%be%e4%be%8b%e9%85%8d%e7%bd%ae%e9%a1%b9
            legend_opts=opts.LegendOpts(type_="scroll", orient="vertical"),
        )
        
        # 标签                                                                                     https://pyecharts.org/#/zh-cn/series_options?id=labelopts%ef%bc%9a%e6%a0%87%e7%ad%be%e9%85%8d%e7%bd%ae%e9%a1%b9
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}"))
    )
)

##=============================================================================================##
##=============================================================================================##
##==================================== 地理图表：坐标图Geo =====================================##
##=============================================================================================##
##=============================================================================================##

#---------------------------------------- 定义及添加数据 ----------------------------------------#
geo=(
    # 地图类型
    .add_schema(maptype="china")
    
    # 地图点系列名称+数据
    .add(
        "geo",
        [('city1', value1),('city2', value2)],
    )
        
    # 添加位置点信息
    .add_coordinate_json('POS.JSON')

    ''' 以下保存为文件POS.JSON
    {
    "chengdu":[104.06, 30.67],
    "beijing":[116.407526, 39.904030],
    "shenyang":[123.38, 41.8]
    }
    '''

    # 标签
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    
    .set_global_opts(
        
        # 渐变图例
        visualmap_opts=opts.VisualMapOpts(), 
        
        # 标题
        title_opts=opts.TitleOpts(title="Geo")
    )
    
)
    
#---------------------------------------- 常用格式详解 ----------------------------------------#
geo=(
    
    .add_schema(
        
        # 视角的中心点，用经纬度表示
        center = [95,10],
        
        # 缩放
        zoom = 0.85,
        
        # 地图区域样式                                                                             https://pyecharts.org/#/zh-cn/series_options?id=itemstyleopts%ef%bc%9a%e5%9b%be%e5%85%83%e6%a0%b7%e5%bc%8f%e9%85%8d%e7%bd%ae%e9%a1%b9
        itemstyle_opts = opts.ItemStyleOpts( color="rgba(170,170,170,0.5)" )
    )
    
    .add(
        
        # 标记类型
        type_ = "scatter",
        
        # 标记图形形状
        symbol = '',
        
        # 标记的大小
        symbol_size = 12,
        
        # 标记图形样式                                                                             https://pyecharts.org/#/zh-cn/series_options?id=itemstyleopts%ef%bc%9a%e5%9b%be%e5%85%83%e6%a0%b7%e5%bc%8f%e9%85%8d%e7%bd%ae%e9%a1%b9
        itemstyle_opts = opts.ItemStyleOpts(color=col1.format(0.8))
        
        # 标签配置项(分)                                                                           https://pyecharts.org/#/zh-cn/series_options?id=labelopts%ef%bc%9a%e6%a0%87%e7%ad%be%e9%85%8d%e7%bd%ae%e9%a1%b9
        label_opts  = opts.LabelOpts(
            is_show = True,
            background_color = '',
            border_color = '',
            border_width = 1，
            border_radius = 4,
            font_size = 15,
            distance = 5,
            rich = '',
            formatter = '',
        )
    )

    # 标签(总)                                                                                     https://pyecharts.org/#/zh-cn/series_options?id=labelopts%ef%bc%9a%e6%a0%87%e7%ad%be%e9%85%8d%e7%bd%ae%e9%a1%b9
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    
    .set_global_opts(
        # 渐变图例                                                                                 https://pyecharts.org/#/zh-cn/global_options?id=visualmapopts%ef%bc%9a%e8%a7%86%e8%a7%89%e6%98%a0%e5%b0%84%e9%85%8d%e7%bd%ae%e9%a1%b9
        visualmap_opts=opts.VisualMapOpts(), 
        
        # 标题
        title_opts=opts.TitleOpts(
            title="Geo"，
            pos_left='35%',pos_top='20',
            title_textstyle_opts=opts.TextStyleOpts(
                font_size=25,
            )
        )
    )
)


##==================================================================================================##
##==================================================================================================##
##============================== 组合图表：时间轴Timeline、并行多图Grid ==============================##
##==================================================================================================##
##==================================================================================================##

#---------------------------------------- 定义及添加数据 ----------------------------------------#
tl=Timeline()
for t in range(2000,2020):
    
    # 添加时间点切片：表格+名称
    tl.add(chart,f'str(t)年' )
    
    

g=(
    Grid()
    # 添加图标，Geo、Pie和Sunburnt不支持grid_opts调整位置大小，需要使用自身center、zoom等调整
    .add(
        chart1, 
        grid_opts=opts.GridOpts(
            pos_left="10", pos_right="45%", pos_top="50%", pos_bottom="5"
        ),
    )
)
    
#---------------------------------------- 常用格式详解 ----------------------------------------#
timeline.add_schema(                                                                               #https://pyecharts.org/#/zh-cn/composite_charts?id=timeline%ef%bc%9a%e6%97%b6%e9%97%b4%e7%ba%bf%e8%bd%ae%e6%92%ad%e5%a4%9a%e5%9b%be
    orient="vertical",
    is_auto_play=True,
    is_inverse=True,
    play_interval=5000,
    pos_left="null",
    pos_right="5",
    pos_top="20",
    pos_bottom="20",
    width="60",
    label_opts=opts.LabelOpts(is_show=True, color="#fff"),
)

#x轴数据
x_data = [f"11月{str(i)}日" for i in range(1, 12) if i!=5] #带时间





