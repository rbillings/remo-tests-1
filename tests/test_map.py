
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from unittestzero import Assert

from pages.create_event import CreateEvent
from pages.events import Events
from pages.event_detail import EventDetail
from pages.home import Home


class TestCreateEventPage:

    @pytest.mark.nondestructive
    def test_create_event(self, mozwebqa):
        home_page = Home(mozwebqa)
        home_page.login()
        events_page = home_page.header.click_events_link()
        create_event_page = events_page.click_create_event_button()
        create_event_page = CreateEvent(mozwebqa)

        #Create event with all required fields
        create_event_page.set_event_venue_map
