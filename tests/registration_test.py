from tests.base_test import BaseTest


class RegistrationTest(BaseTest):
    def setup(self):
        super().setUp()
        self.home_page.click_sign_in()

    def testNoSurname(self):
        pass