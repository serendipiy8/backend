import os
import pytest

from test.unitest.common.request_util import RequestUtil
from test.unitest.utils.read_yaml import read_yaml

base_dir = os.path.dirname(os.path.abspath(__file__))


class TestAdminfunctionsResource:

    @pytest.mark.parametrize("caseInfo", read_yaml(os.path.join(base_dir, "data/get.yaml")))
    def test_get(self, caseInfo, env_dict):
        RequestUtil.test_body(caseInfo, env_dict)

    @pytest.mark.parametrize("caseInfo", read_yaml(os.path.join(base_dir, "data/post.yaml")))
    def test_post(self, caseInfo, env_dict):
        RequestUtil.test_body(caseInfo, env_dict)

    @pytest.mark.parametrize("caseInfo", read_yaml(os.path.join(base_dir, "data/put.yaml")))
    def test_update(self, caseInfo, env_dict):
        RequestUtil.test_body(caseInfo, env_dict)

    @pytest.mark.parametrize("caseInfo", read_yaml(os.path.join(base_dir, "data/delete.yaml")))
    def test_delete(self, caseInfo, env_dict):
        RequestUtil.test_body(caseInfo, env_dict)
        