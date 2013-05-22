#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
import random
import string
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

        profile_page.click_edit_profile_button()
        edit_profile_page = Profile.EditProfile(mozwebqa)

        # save initial values to restore them after the test is finished
        fields_no = len(profile_page._name_fields_locator) - 1
        initial_value = [None] * fields_no

        # enter new profile values
        new_username = "TestUser%s" % random.randint(0, 100)
        new_lastname = "Lastname%s" % random.choice(string.ascii_letters)
        new_firstname = "First%s" % random.choice(string.ascii_letters)
        edit_profile_page.set_username(new_username)
        edit_profile_page.set_last_name(new_lastname)
        edit_profile_page.set_first_name(new_firstname)
        edit_profile_page.click_save_profile_button()
        username = profile_page.username()
        lastname = profile_page.lastname()
        firstname = profile_page.firstname()
        Assert.equal(username, new_username)
        Assert.equal(lastname, new_lastname)
        Assert.equal(firstname, new_firstname)

        # restore initial values
        profile_page.click_edit_profile_button()
        for i in range(0, fields_no):
            edit_profile_page._profile_fields[i].type_value(initial_value[i])
        edit_profile_page.click_save_profile_button()
