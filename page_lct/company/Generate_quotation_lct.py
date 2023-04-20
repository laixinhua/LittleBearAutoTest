#存放生成报价页面元素
#返回按钮
Back_button = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.ImageView'
#退出编辑是否保存-确定
determine = '//*[starts-with(@text,"确认")]'
#退出编辑是否保存-取消
cancel = '//*[starts-with(@text,"取消")]'
#选择业务员
Select_salesperson = '//*[starts-with(@text,"业务员")]'
#业务员一
Salesman_I = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.TextView'
#业务员二
Salesman_II = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[2]/android.widget.TextView'
#业务员三
Salesman_III = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[3]/android.widget.TextView'
#选择客户
Select_customer = '//*[starts-with(@text,"客户名称")]'
#客户列表
Customer_list = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout'
#客户一
Customer_I = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout/android.widget.TextView'
#客户空
Customer_empty = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView'
#客户管理
customer_management = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.TextView'
#备注
remarks = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.view.ViewGroup/android.widget.FrameLayout/android.widget.EditText'
#默认方式
Default_mode = '//*[starts-with(@text,"默认方式")]'
#报出厂价
Quoted_factory_price = '//*[starts-with(@text,"报出厂价")]'
#美元
dollar = '//*[starts-with(@text,"美元")]'
#人民币
RMB = '//*[starts-with(@text,"人民币")]'
#报价方式
Quotation_method = '//*[starts-with(@text,"报价方式")]'
#FOB
FOB = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.TextView'
#FOB SHANTOU
FOB_SHANTOU = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[2]/android.widget.TextView'
#FOB SHENZHEN
FOB_SHENZHEN = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[3]/android.widget.TextView'
#出厂价
Ex_factory_price = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[4]/android.widget.TextView'
#利润
profit = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[6]/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.EditText'
#币种
currency = '//*[starts-with(@text,"币种")]'
#币种-RMB
currency_RMB = '//*[starts-with(@text,"RMB")]'
#币种-USD
currency_USD = '//*[starts-with(@text,"USD")]'
#币种-HKD
currency_HKD = '//*[starts-with(@text,"HKD")]'
#币种-EUR
currency_EUR = '//*[starts-with(@text,"EUR")]'
#总费用
Total_cost = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[8]/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.EditText'
#汇率
exchange_rate = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[9]/android.view.ViewGroup/android.widget.FrameLayout/android.widget.EditText'
#每车尺码
Size_per_car = '//*[starts-with(@text,"每车尺码")]'
#每车尺码-28
Size_per_car_28 = '//*[starts-with(@text,"28")]'
#每车尺码-54
Size_per_car_54 = '//*[starts-with(@text,"54")]'
#每车尺码-68
Size_per_car_68 = '//*[starts-with(@text,"68")]'
#每车尺码-86
Size_per_car_86 = '//*[starts-with(@text,"86")]'
#小数位数
Decimal_places = '//*[starts-with(@text,"小数位数")]'
#小数位数-0
Decimal_places_0 = '//*[starts-with(@text,"0")]'
#小数位数-1
Decimal_places_1 = '//*[starts-with(@text,"1")]'
#小数位数-2
Decimal_places_2 = '//*[starts-with(@text,"2")]'
#小数位数-3
Decimal_places_3 = '//*[starts-with(@text,"3")]'
#小数位数-4
Decimal_places_4 = '//*[starts-with(@text,"4")]'
#取舍方式
Choice_method = '//*[starts-with(@text,"取舍方式")]'
#取舍方式-全收
Choice_method_Full_collection = '//*[starts-with(@text,"全收")]'
#取舍方式-四舍五入
Choice_method_rounding = '//*[starts-with(@text,"四舍五入")]'
#取舍方式-全舍
Choice_method_Whole_house = '//*[starts-with(@text,"全舍")]'
#价格小于
Price_less_than = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[8]/android.view.ViewGroup/android.widget.FrameLayout/android.widget.EditText'
#价格小于-小数位数
Price_less_than_decimal_places = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[9]/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.ImageView'
#价格小于-小数位数-0
Price_less_than_decimal_places_0 = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.TextView'
#价格小于-小数位数-1
Price_less_than_decimal_places_1 = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[2]/android.widget.TextView'
#价格小于-小数位数-2
Price_less_than_decimal_places_2 = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[3]/android.widget.TextView'
#价格小于-小数位数-3
Price_less_than_decimal_places_3 = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[4]/android.widget.TextView'
#价格小于-小数位数-4
Price_less_than_decimal_places_4 = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[5]/android.widget.TextView'
#确定生成报价
Confirm_to_generate_quotation = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.RelativeLayout[2]/android.widget.TextView'
