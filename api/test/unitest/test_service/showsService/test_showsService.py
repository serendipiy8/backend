#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import pytest

from test.unitest.common.function_test_util import FunctionTestUtil
from test.unitest.utils.read_yaml import read_yaml

base_url = os.path.dirname(os.path.abspath(__file__))


class TestShowsService:
    @pytest.mark.parametrize("caseInfo", read_yaml(os.path.join(base_url, "data.yaml")))
    def test_sub_count(self, caseInfo):
        FunctionTestUtil.test_body(caseInfo)
        