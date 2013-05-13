#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from pages.base import Base
from pages.profile import Profile


class EditProfile(Base):

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
