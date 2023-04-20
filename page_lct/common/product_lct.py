#存放产品列表页面元素
#返回按钮
Back_button = '//android.widget.FrameLayout/android.view.ViewGroup/android.widget.ImageView[1]'
#相机按钮
Camera_button = '//android.widget.FrameLayout/android.view.ViewGroup/android.widget.ImageView[2]'
#搜索栏-输入关键词+空格可模糊搜索
Search_bar = '//*[starts-with(@text,"输入关键词+空格可模糊搜索")]'
#搜索栏1
Search_bar1 = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.EditText'
#搜索按钮
Search_button = '//*[starts-with(@text,"搜索")]'
#搜索按钮1
Search_button1 = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TextView'
#综合搜索按钮
Comprehensive_search_button = '//*[contains(@text,"综合搜索")]'
#请输入关键词
Please_enter_keywords = '//*[contains(@text,"请输入名称/货号")]'
#搜索类型-货号
Search_type_article_number = '//*[starts-with(@text,"货号")]'
#搜索类型-名称
Search_type_name = '//*[starts-with(@text,"名称")]'
#搜索类型-编号
Search_type_number = '//*[starts-with(@text,"编号")]'
#搜索类型-平台编号
Search_type_platform_number = '//*[starts-with(@text,"平台编号")]'
#是否精准-模糊
Accurate_Fuzzy = '//*[starts-with(@text,"模糊")]'
#是否精准-精准
Accurate_accurate = '//*[starts-with(@text,"精准")]'
#产品货号-展开
Product_article_number_expand = '//*[starts-with(@text,"产品货号")]'
#产品货号-多货号查询;以,隔开
Multiple_article_number_query_Separated_by = '//*[starts-with(@text,"多货号查询;以,隔开")]'
#产品货号-收起
Product_article_number_stowed = '//*[starts-with(@text,"产品货号")]'
#厂商名称-展开
Vendor_name_expand = '//*[starts-with(@text,"厂商名称")]'
#厂商名称-请输入
Vendor_name_please_enter = '//android.widget.RelativeLayout/android.widget.EditText[text(),"请输入"]'
#厂商名称-收起
Vendor_name_stowed = '//*[starts-with(@text,"厂商名称")]'
#价格区间-展开
Price_range_expand = '//*[starts-with(@text,"价格区间")]'
#价格区间-最低价
Price_range_lowest_price = '//*[starts-with(@text,"最低价")]'
#价格区间-最高价
Price_range_maximum_price = '//*[starts-with(@text,"最高价")]'
#价格区间-最低价-输入后
Price_range_lowest_price_after_entry = '//android.widget.RelativeLayout[4]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.EditText[1]'
#价格区间-最高价-输入后
Price_range_maximum_price_after_entry = '//android.widget.RelativeLayout[4]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.EditText[2]'
#价格区间-收起
Price_range_close = '//*[starts-with(@text,"价格区间")]'
#时间段-展开
Time_period_expand = '//*[starts-with(@text,"时间段")]'
#时间段-开始时间
Time_period_start_time = '//android.widget.RelativeLayout[5]/android.widget.FrameLayout/android.widget.RadioGroup/android.widget.RadioButton[1]'
#时间段-结束时间
Time_period_end_time = '//android.widget.RelativeLayout[5]/android.widget.FrameLayout/android.widget.RadioGroup/android.widget.RadioButton[2]'
#时间段-取消 旧的时间段控件
#Time_period_cancel = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.TextView[1]'
#时间段-保存
Time_period_save = '//*[starts-with(@text,"保存")]'
#时间段-收起
Time_period_Stow = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout[3]/android.widget.RelativeLayout/android.widget.TextView[2]'
#包装方式-展开
Packaging_method_expand = '//*[starts-with(@text,"包装方式")]'
#包装方式-下拉
#Packaging_method_drop_down = '//*[starts-with(@text,"请选择")]' 样式已弃用
#包装方式-从平台选择
Packaging_method_Select_from_platform = '//*[starts-with(@text,"从平台选择")]'
#请输入关键词
Packaging_method_Please_enter_keywords = '//*[starts-with(@text,"请输入关键词")]'
#直接搜索包装方式
Search_packaging_method_directly = '//*[starts-with(@text,"请输入")]'
#包装方式-搜索按钮
Packaging_method_Search_button = '//android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.ImageView'
#包装方式-全部
Packaging_method_All = '//*[starts-with(@text,"全部")]'
#包装方式-展示盒
Packaging_method_display_box = '//*[starts-with(@text,"展示盒")]'
#包装方式-开窗盒
Packaging_method_window_box = '//*[starts-with(@text,"开窗盒")]'
#包装方式-彩盒
Packaging_method_color_box = '//*[starts-with(@text,"彩盒")]'
#包装方式-吸板
Packaging_method_suction_plate = '//*[starts-with(@text,"吸板")]'
#包装方式-PVC圆筒
Packaging_method_PVC_cylinder = '//*[starts-with(@text,"PVC圆筒")]'
#包装方式-双吸塑
Packaging_method_double_blister = '//*[starts-with(@text,"双吸塑")]'
#包装方式-确认
Packaging_method_confirm = '//*[starts-with(@text,"确认")]'
#包装方式-取消
Packaging_method_cancel = '//*[starts-with(@text,"取消")]'
#包装方式-收起
Packaging_method_stowed = '//*[starts-with(@text,"包装方式")]'
#证书认证-展开
Certificate_authentication_expand = '//*[starts-with(@text,"证书认证")]'
#证书认证-请输入
Certificate_authentication_please_enter = '//*[starts-with(@text,"请输入")]'
#证书认证-收起
Certificate_authentication_Stow = '//*[starts-with(@text,"证书认证")]'
#外箱装量-展开
Outer_container_loading_expand = '//*[starts-with(@text,"外箱装量")]'
#外箱装量-最低
Outer_container_capacity_Minimum = '//*[starts-with(@text,"最低")]'
#外箱装量-最高
Outer_container_capacity_max = '//*[starts-with(@text,"最高")]'
#外箱装量-最低-输入后
Outer_container_capacity_Minimum_After_input = '//android.widget.RelativeLayout[8]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.EditText[1]'
#外箱装量-最高-输入后
Outer_container_capacity_max_After_input = '//android.widget.RelativeLayout[8]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.EditText[2]'
#外箱装量-收起
Outer_container_loading_stowed = '//*[starts-with(@text,"外箱装量")]'
#外箱规格-展开
Outer_box_specification_expand = '//*[starts-with(@text,"外箱规格")]'
#外箱规格-长
Outer_box_specification_long = '//*[starts-with(@text,"长")]'
#外箱规格-宽
Outer_box_specification_width = '//*[starts-with(@text,"宽")]'
#外箱规格-高
Outer_box_specification_high = '//*[starts-with(@text,"高")]'
#外箱规格-收起
Outer_box_specification_stowed = '//*[starts-with(@text,"外箱规格")]'
#搜索类型-是否有图-展开
Search_type_is_there_a_graph_expand = '//*[starts-with(@text,"是否有图")]'
#搜索类型-是否有图-下拉
Search_type_is_there_a_graph_drop_down = '//*[starts-with(@text,"请选择")]'
#搜索类型-是否有图-全部
Search_type_is_there_a_graph_all = '//*[starts-with(@text,"全部")]'
#搜索类型-是否有图-无图
Search_type_is_there_a_graph_No_picture = '//*[starts-with(@text,"无图")]'
#搜索类型-是否有图-有图
Search_type_is_there_a_graph_With_pictures = '//*[starts-with(@text,"有图")]'
#搜索类型-是否有图-确认
Search_type_is_there_a_graph_confirm = '//*[starts-with(@text,"确认")]'
#搜索类型-是否有图-取消
Search_type_is_there_a_graph_cancel = '//*[starts-with(@text,"取消")]'
#搜索类型-是否有图-收起
Search_type_is_there_a_graph_stowed = '//*[starts-with(@text,"是否有图")]'
#授权类型-展开
Product_Authorization_expand = '//*[starts-with(@text,"是否授权")]'
#搜索类型-授权类型-下拉
Product_Authorization_drop_down = '//*[starts-with(@text,"请选择")]'
#产品授权-全部
Product_Authorization_all = '//*[starts-with(@text,"全部")]'
#产品授权-已授权
Product_Authorization_authorized = '//*[starts-with(@text,"已授权")]'
#产品授权-未授权
Product_Authorization_unauthorized = '//*[starts-with(@text,"未授权")]'
#产品授权-不侵权
Product_Authorization_non_infringement = '//*[starts-with(@text,"不侵权")]'
#产品授权-其他
Product_Authorization_other = '//*[starts-with(@text,"其他")]'
#搜索类型-产品授权-确认
Product_Authorization_confirm = '//*[starts-with(@text,"确认")]'
#搜索类型-产品授权-取消
Product_Authorization_cancel = '//*[starts-with(@text,"取消")]'
#搜索类型-产品授权-收起
Product_Authorization_stowed = '//*[starts-with(@text,"是否授权")]'
#产品类型-展开
product_type_expand = '//*[starts-with(@text,"产品类型")]'
#产品类型-3D产品
product_type_3D_product = '//*[starts-with(@text,"3D产品")]'
#产品类型-最新产品
product_type_Latest_products = '//*[starts-with(@text,"最新产品")]'
#产品类型-现货产品
product_type_Spot_Products = '//*[starts-with(@text,"现货产品")]'
#产品类型-收起
product_type_stowed = '//*[starts-with(@text,"产品类型")]'
#重置
Reset = '//*[starts-with(@text,"重置")]'
#确定
determine = '//*[starts-with(@text,"确定")]'
#热度排序
Heat_ranking = '//*[starts-with(@text,"热度")]'
#单价排序
Unit_price_sorting = '//*[starts-with(@text,"热度")]'
#时间排序
Time_sorting = '//*[starts-with(@text,"时间")]'
#分类
classification = '//*[starts-with(@text,"分类")]'
#分类-电动玩具
Classification_electric_toys = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/androidx.recyclerview.widget.RecyclerView[1]/android.widget.TextView[2]'
#分类-电动玩具-电动机器人
Classification_electric_toys_electric_robots = '//*[starts-with(@text,"电动机器人")]'
#分类-电动玩具-电动车
Classification_electric_toys_electric_vehicles = '//*[starts-with(@text,"电动车")]'
#分类-电动玩具-电动飞机
Classification_electric_toys_electric_aircraft = '//*[starts-with(@text,"电动飞机")]'
#分类-电动玩具-电动船
Classification_electric_toys_electric_boats = '//*[starts-with(@text,"电动船")]'
#分类-电动玩具-电动动物
Classification_electric_toys_electric_animals = '//*[starts-with(@text,"电动动物")]'
#分类-电动玩具-电动摩托
Classification_electric_toys_electric_motorcycles = '//*[starts-with(@text,"电动摩托")]'
#分类-电动玩具-电动坦克
Classification_electric_toys_electric_tanks = '//*[starts-with(@text,"电动坦克")]'
#分类-电动玩具-电动娃娃
Classification_electric_toys_electric_dolls = '//*[starts-with(@text,"电动娃娃")]'
#产品图片
Product_picture = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.ImageView[1]'
#加购
Additional_purchase = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.FrameLayout[2]/android.widget.FrameLayout[2]/android.widget.ImageView'
#切换视图
Switch_views = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/androidx.appcompat.widget.LinearLayoutCompat/androidx.appcompat.widget.LinearLayoutCompat/android.widget.CheckBox'
#收藏按钮
Favorite_button = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.widget.ImageView[2]'
#聊天按钮
chat = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/androidx.appcompat.widget.LinearLayoutCompat[3]/android.widget.LinearLayout/android.widget.ImageView[2]'
#加入购物车
add_to_cart = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.FrameLayout[2]/android.widget.FrameLayout[2]/android.widget.TextView'
#购物车按钮
Shopping_cart_button = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.ImageView'
#购物车数量
Shopping_cart_number = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.Button'
#置顶按钮
Top_button = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ImageView'
#toast
toast = '/hierarchy/android.widget.Toast'
#确认
confirm = '//*[starts-with(@text,"确认")]'
#取消
cancel = '//*[starts-with(@text,"取消")]'


