import allure

from common.basepage import BasePage
from page_lct.ExhibitionHall import Exhibition_Latest_sample_selection_company_lct


class ExhibitionLatestSampleSelectionCompanyPage(BasePage):
    def Click_Back_button(self):
        # allure添加测试步骤
        with allure.step("点击返回"):
            print("点击返回")
        self.click_element(Exhibition_Latest_sample_selection_company_lct.Back_button)

    def Search(self):
        #allure添加测试步骤
        with allure.step("输入关键词"):
            print("输入关键词")
        self.input_text("义乌",Exhibition_Latest_sample_selection_company_lct.Search_Bar)
        with allure.step("点击搜索按钮"):
            print("点击搜索按钮")
        self.click_element(Exhibition_Latest_sample_selection_company_lct.Search_button)

    def View_search_results(self):
        self.Search()
        with allure.step("点击搜索按钮"):
            print("点击搜索按钮")
        self.click_element(Exhibition_Latest_sample_selection_company_lct.search_result)
