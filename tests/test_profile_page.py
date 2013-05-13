#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from unittestzero import Assert

from pages.edit_profile import EditProfile
from pages.home import Home
from pages.profile import Profile


class TestProfilePage:

    @pytest.mark.credentials
    @pytest.mark.nondestructive
    def test_edit_profile(self, mozwebqa):
        home = Home(mozwebqa)
        home.go_to_homepage()
        home.login()
        profile_page = Profile(mozwebqa)
        profile_page.go_to_profile_page()
        Assert.true(profile_page.is_username_visible)
        profile_page.click_edit_profile_button()
        edit_profile_page = EditProfile(mozwebqa)
        new_username = "TestUser"
        new_lastname = "Lastname"
        new_firstname = "First"
        edit_profile_page.set_username(new_username)
        edit_profile_page.set_last_name(new_lastname)
        edit_profile_page.set_first_name(new_firstname)
        edit_profile_page.click_save_profile_button()
        username = profile_page.username_text()
        lastname = profile_page.lastname_text()
        firstname = profile_page.firstname_text()
        Assert.equal(username, new_username)
        Assert.equal(lastname, new_lastname)
        Assert.equal(firstname, new_firstname)
