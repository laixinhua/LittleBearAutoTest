from common import Random_name
from page_obj.common.personal_information_page import PersonalInformationPage


class ModifyPersonalInformation:
    def ModifyPersonalInformation(self,app_page):
        PersonalInformationPage(app_page).Modify_Avatar()
        new_name = Random_name.RandomName.RandomNames(app_page)
        PersonalInformationPage(app_page).Modify_Name(app_page, new_name)
        PersonalInformationPage(app_page).Modify_Gender(app_page)
        PersonalInformationPage(app_page).Modify_Birthday(app_page)