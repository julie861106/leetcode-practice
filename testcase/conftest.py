import base64
import json
import os
import re

import markdown
import pytest

# from baymax.infra.dut_mgr import DUTMgr
# from baymax.infra.equip_mgr import EquipMgr
# from baymax_product.baymax_dlm.src.helper.dlm_restful_helper import DLMRestfulUser


# pylint: disable=protected-access


# @pytest.fixture(scope="session")
# def equips(env_config_path):
#     equip_mgr_inst = EquipMgr.get_inst(env_config_path)
#     return equip_mgr_inst


# @pytest.fixture(scope="session")
# def duts(env_config_path):
#     dut_mgr_inst = DUTMgr.get_inst(env_config_path)
#     return dut_mgr_inst


@pytest.fixture(scope="session")
def env_config(env_config_path):
    if not os.path.exists(env_config_path):
        return None
    with open(env_config_path) as json_file:
        env_config_inst = json.load(json_file)
        return env_config_inst
    return None


# @pytest.fixture(scope="session", autouse=True)
# def session_finish_yield(env_config_path):
#     yield
#     equip_mgr_inst = EquipMgr.get_inst(env_config_path)
#     equip_mgr_inst.uninit()


# @pytest.fixture(scope="session")
# def dlm_restful_user(duts):  # pylint: disable=redefined-outer-name
#     restful_user = DLMRestfulUser(False, **duts["DLM_G2"].get_env_config())
#     restful_user.login()
#     return restful_user


def pytest_html_results_table_header(cells):
    cells.pop()


def pytest_html_results_table_row(report, cells):  # pylint: disable=unused-argument
    try:
        cells.pop()
    except Exception as exception:
        print(exception)


def remove_indent(content):
    content = content.split("\n")
    content = [line.lstrip() for line in content]
    content = "\n".join(content)
    return content


def handle_test_desc(src):
    return markdown.markdown(remove_indent(src), extensions=["md_in_html", "markdown.extensions.tables"])


# def handle_web_fail_image(src):
#     if src.longrepr is not None:
#         # if failed test is web test
#         # only web test has screenshot when failed currently
#         screenshot_info = re.search(r"\'screenshot saved at (.*\.png)\'", src.longreprtext)
#         if screenshot_info is not None:
#             with open(screenshot_info.group(1), "rb") as image_file:
#                 image_base64 = base64.b64encode(image_file.read())
#                 html_code = (
#                     f'<div id="failed_image_{src.nodeid}"><img src="data:image/png;base64,{image_base64.decode()}'
#                     f'" alt="screenshot" align="right"/></div>'
#                 )
#                 return html_code
#     return None


def rm_std(report_sections):
    new_report_sections = []
    for when, key, content in report_sections:
        if key == "log":
            new_report_sections.append((when, key, content))
    return new_report_sections


# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     item._report_sections = rm_std(item._report_sections)
#     pytest_html = item.config.pluginmanager.getplugin("html")
#     outcome = yield
#     report = outcome.get_result()

#     report.start = call.start
#     # report.test_id = item.get_closest_marker("test_id").args[0]
#     extra = getattr(report, "extra", [])
#     if report.when == "call":
#         html_desc = handle_test_desc(str(item.function.__doc__))
#         extra.append(pytest_html.extras.html(html_desc))

#         # when test failed
#         xfail = hasattr(report, "wasxfail")
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             # only when catch 'screenshot saved at xxx.png' in fail message
#             if handle_web_fail_image(report) is not None:
#                 extra.append(pytest_html.extras.html(handle_web_fail_image(report)))

#         report.extra = extra

#     if report.when == "setup" or report.when == "teardown":
#         # when setup or teardown failed
#         xfail = hasattr(report, "wasxfail")
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             # only when catch 'screenshot saved at xxx.png' in fail message
#             if handle_web_fail_image(report) is not None:
#                 extra.append(pytest_html.extras.html(handle_web_fail_image(report)))

#         report.extra = extra
