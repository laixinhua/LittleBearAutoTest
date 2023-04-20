from common.basepage import BasePage


class ClearTextPage(BasePage):
    def cleartext(self,locator):
        self.clear_text(locator)
