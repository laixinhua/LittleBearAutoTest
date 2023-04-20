import random


class RandomName:
    def RandomNames(self):
        name_list = {"赵": ["子龙", "信", "恨桃", "依波", "幻巧"],
                     "钱": ["美倩", "安寒", "惜玉", "怜雪", "紫夏"],
                     "孙": ["芷梦", "涵易", "念蕾", "凌旋", "梦竹"],
                     "李": ["白"],
                     "周": ["紫萱", "白亦", "碧春", "听南", "凌旋"],
                     "吴": ["千凡", "凌寒", "瀚文", "浩博", "海荣"],
                     "郑": ["鸿波", "浩宕", "浩思", "瀚钰", "涵煦"]
                     }
        lastname = random.choice(list(name_list))
        name = random.choice(name_list[lastname])
        customer_name = lastname + name
        print("名称为:"+customer_name)
        return customer_name

    def RandomEmail(self):
        Email_list = {"450044150": ["@qq.com", "@163.com", "@sina.com", "@126.com"],
                     "450044151": ["@qq.com", "@163.com", "@sina.com", "@126.com"],
                     "450044152": ["@qq.com", "@163.com", "@sina.com", "@126.com"],
                     "450044153": ["@qq.com", "@163.com", "@sina.com", "@126.com"],
                     "450044154": ["@qq.com", "@163.com", "@sina.com", "@126.com"],
                     "450044155": ["@qq.com", "@163.com", "@sina.com", "@126.com"],
                     "450044156": ["@qq.com", "@163.com", "@sina.com", "@126.com"]
                     }
        e_mail = random.choice(list(Email_list))
        address = random.choice(Email_list[e_mail])
        Email = e_mail + address
        print("邮箱地址为:"+Email)
        return Email

    def RandomCompanyName(self):
        name_list = {"宸海": ["玩具", "科技", "玩具厂", "科技有限公司"],
                     "宏宇": ["玩具", "科技", "玩具厂", "科技有限公司"],
                     "孙印": ["玩具", "科技", "玩具厂", "科技有限公司"],
                     "成卓": ["玩具", "科技", "玩具厂", "科技有限公司"],
                     }
        lastname = random.choice(list(name_list))
        name = random.choice(name_list[lastname])
        company_name = lastname + name
        print(company_name)
        return company_name

    def RandomPhoneNumber(self):
        phone_list = ['139', '138', '137', '136', '135', '134', '159', '158', '157', '150', '151', '152', '188', '187', '182',
               '183', '184', '178', '130', '131', '132', '156', '155', '186', '185', '176', '133', '153', '189', '180',
               '181', '177']
        phone = random.choice(list(phone_list))
        listnumber = '1234567890'
        newlist = []
        for i in range(8):
            newlist.append(random.choice(listnumber))
        number = ''.join(newlist)
        phone_number = phone+number
        print("手机号码为："+phone_number)
        return phone_number

    def RandomLandlineNumber(self):
        listnumber = '1234567890'
        newlist = []
        for i in range(7):
            newlist.append(random.choice(listnumber))
        landlinenumber = ''.join(newlist)
        print("电话座机为："+landlinenumber)
        return landlinenumber

    def RandomQQNumber(self):
        listnumber = '1234567890'
        newlist = []
        for i in range(10):
            newlist.append(random.choice(listnumber))
        QQnumber = ''.join(newlist)
        print("QQ号码为：" + QQnumber)
        return QQnumber

    def RandomAddress(self):
        address_list = {"广东省": ["广州市", "韶关市", "深圳市", "珠海市","汕头市","佛山市","江门市","湛江市","茂名市","肇庆市","惠州市","梅州市","汕尾市","河源市","阳江市","清远市","东莞市","中山市","潮州市","揭阳市","云浮市"]
                     }
        province = random.choice(list(address_list))
        city = random.choice(address_list[province])
        address = province + city
        print(address)
        return address

    def RandomInformation(self):
        company_name = RandomName.RandomCompanyName(self)
        Information_list = ["{companyname}于1993年成立，是一家集研发、制造益智玩具的企业。生产基地位于佛山南海区，地处珠三角福地交通，四通八达。","{companyname}于2016年09月21日成立，公司位于江苏省，苏州市，园区中国北京市大兴区工业园区，主要生产经营广告促销礼品;节庆用品等产品，公司多年致力于产业，切实推进与各大企业、厂家的合资、合作，用产业化发展的思路服务于社会和广大用户。","{companyname}是儿童助步车等产品专业生产加工的公司，拥有完整、科学的质量管理体系。宁海县长街施儿乐玩具厂的诚信、实力和产品质量获得业界的认可。欢迎各界朋友莅临参观、指导和业务洽谈。".format(companyname = company_name)]
        Information = random.choice(list(Information_list))
        print(Information)
        return Information

    def RandomCancelorConfirm(self):
        Cancel_or_Confirm_list = ["取消","确定"]
        Cancel_or_Confirm = random.choice(list(Cancel_or_Confirm_list))
        print("结果为："+Cancel_or_Confirm)
        return Cancel_or_Confirm

    def RandomGender(self):
        Male_or_Female_list = ["男","女"]
        Male_or_Female = random.choice(list(Male_or_Female_list))
        print("性别为："+Male_or_Female)
        return Male_or_Female

    def RandomRole(self):
        Role_list = ["展厅","公司","厂商"]
        Role = random.choice(list(Role_list))
        print("角色为："+Role)
        return Role

    def RandomKeyword(self):
        keyword_list = ["娃娃","机器","遥控","娃娃 积木","遥控 惯性"]
        keyword = random.choice(list(keyword_list))
        print("关键字为："+keyword)
        return keyword

    def RandomSelectProductType(self):
        ProductTypeList = ["所有产品","推荐产品","视频产品","3D产品","最新产品"]
        ProductType = random.choice(list(ProductTypeList))
        print("产品类型为："+ProductType)
        return ProductType

    def RandomSelectNewProduct(self):
        NewProductTypeList = ["最新产品","24小时新品"]
        ProductType = random.choice(list(NewProductTypeList))
        print("新品类型为："+ProductType)
        return ProductType

    def RandomSelectType(self):
        Select_Type_list = ["全部","货号","名称","编号","平台编号"]
        Select_Type = random.choice(list(Select_Type_list))
        print("搜索类型为："+Select_Type)
        return Select_Type

    def RandomSelectFuzzy_or_not(self):
        Fuzzy_or_not_list = ["模糊","精准"]
        Fuzzy_or_not = random.choice(list(Fuzzy_or_not_list))
        print("是否模糊："+Fuzzy_or_not)
        return Fuzzy_or_not

    def RandomPrice(self):
        minimum_price = str(random.randint(90,100))
        maximum_price = str(random.randint(1,10))
        return minimum_price,maximum_price

    def RandomSelectType1(self):
        Select_Type_list = ["是否有图","授权类型","产品类型"]
        Select_Type = random.choice(list(Select_Type_list))
        print("搜索类型为："+Select_Type)
        return Select_Type

    def RandomPackagingMethod(self):
        Select_Packaging_Method_list = ['展示盒','开窗盒','彩盒','吸板','PVG圆筒']
        Packaging_Method = random.choice(list(Select_Packaging_Method_list))
        print("包装方式为："+Packaging_Method)
        return Packaging_Method


    def RandomSecondaryClassification(self):
        Secondary_Classification_list = ["电动机器人","电动车","电动飞机","电动船","电动动物","电动摩托","电动坦克","电动娃娃"]
        Secondary_Classification = random.choice(list(Secondary_Classification_list))
        print("二级分类为："+Secondary_Classification)
        return Secondary_Classification

    def RandomRemarks(self):
        remarks_list = ["我是备注1","我是备注2","我是备注3","我是备注4","华东大客户","华南大客户","华西大客户","华北大客户"]
        remarks = random.choice(list(remarks_list))
        print("备注为:"+remarks)
        return remarks

    def RandomNotice(self):
        Notice_list = ["普通公告","采购公告","供应公告"]
        Notice = random.choice(list(Notice_list))
        print("公告类型为:"+Notice)
        return Notice

    def RandomToyCircleContent(self):
        Content_list = ["我不敢苟同他的观点，我个人认为这个意大利面就应该拌42号混凝土，因为这个螺丝钉的长度，它很容易会直接影响到挖掘机的扭矩，你知道吧?你往里砸的时候，一瞬间它就会产生大量的高能蛋白，俗称UFO，会严重影响经济的发展，甚至对这个太平洋以及充电器都会造成一定的核污染。","我站在你左侧，却像隔着银河"]
        Content = random.choice(list(Content_list))
        print("发布的内容是:"+Content)
        return Content

