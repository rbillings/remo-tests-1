#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from pages.base import Base
from pages.page import Page

class Profile(Base):

    _page_title = (By.CSS_SELECTOR, 'title:contains("Mozilla Reps - Profile*")')
    _page_source = (By.CSS_SELECTOR, '#wrapper')
    _edit_profile_locator = (By.CSS_SELECTOR, 'div.twelve a.small')
    _email_locator = (By.CSS_SELECTOR, 'div.eleven p.profile-item')
    _firstname_locator = (By.CSS_SELECTOR, 'div.eleven h4')
    _lastname_locator = (By.CSS_SELECTOR, 'div.eleven h4:nth-of-type(2)')
    _username_locator = (By.CSS_SELECTOR, 'div.eleven h5.grayed:nth-of-type(2)')

    def go_to_profile_page(self):
        self.selenium.get(self.base_url + '/me/')

    def click_edit_profile_button(self):
        self.selenium.find_element(*self._edit_profile_locator).click()

    def email_text(self):
        return self.selenium.find_element(*self._email_locator).text

    def username_text(self):
        return self.selenium.find_element(*self._username_locator).text

    def firstname_text(self):
        return self.selenium.find_element(*self._firstname_locator).text

    def lastname_text(self):
        return self.selenium.find_element(*self._lastname_locator).text

    @property
    def is_username_visible(self):
        return self.is_element_visible(*self._username_locator)

    @property
    def is_text_present(self):
        return self.selenium.find_element(*self._page_source).text

    class EditProfile(Page):

        _first_name_locator = (By.CSS_SELECTOR, 'div.eleven input.input-text:nth-of-type(3)')
        _last_name_locator = (By.CSS_SELECTOR, 'div.eleven input.input-text:nth-of-type(2)')
        _save_profile_locator = (By.CSS_SELECTOR, 'div.four button.small')
        _username_locator = (By.CSS_SELECTOR, 'div.eleven input.input-text')

        @property
        def username(self):
            return self.selenium.find_element(*self._username_locator).text

        def click_save_profile_button(self):
            self.selenium.find_element(*self._save_profile_locator).click()
            return Profile(self.testsetup)

        def set_first_name(self, firstname):
            element = self.selenium.find_element(*self._first_name_locator)
            element.clear()
            element.send_keys(firstname)

        def set_last_name(self, lastname):
            element = self.selenium.find_element(*self._last_name_locator)
            element.clear()
            element.send_keys(lastname)

        def set_username(self, username):
            element = self.selenium.find_element(*self._username_locator)
            element.clear()
            element.send_keys(username)
