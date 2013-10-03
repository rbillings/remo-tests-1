#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from pages.base import Base


class EventDetail(Base):

    _edit_event_title_locator = (By.CSS_SELECTOR, '.event-single-title')
    _edit_event_button_locator = (By.CSS_SELECTOR, '.small.button:nth-child(3)')
    _event_description_locator = (By.CSS_SELECTOR, '.large-11.columns > p:nth-child(2)')
    _event_saved_message_locator = (By.CSS_SELECTOR, '.alert-box.success')

    def __init__(self, testsetup):
        Base.__init__(self, testsetup)
        WebDriverWait(self.selenium, self.timeout).until(
            lambda s: len(s.find_elements(*self._edit_event_title_locator)))

    def click_edit_event_button(self):
        self.selenium.find_element(*self._edit_event_button_locator).click()
        from pages.edit_event import EditEvent
        return EditEvent(self.testsetup)

    @property
    def description(self):
        return self.selenium.find_element(*self._event_description_locator).text

    @property
    def is_event_saved_message_visible(self):
        return self.is_element_visible(*self._event_saved_message_locator)
