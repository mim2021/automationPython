class Locator:

    def locator(self, driver):
        self.driver = driver
        self.profile_icon = "//div[@class='image flex-img d-flex align-items-center justify-content-center']"
        self.login_text = "//li[normalize-space()='Log In']"
        self.email_box = "email"
        self.password_box = "password"
        self.login_button_xpath = "//button[@type='submit']"
        self.logout_text = "//li[normalize-space()='Log Out']"