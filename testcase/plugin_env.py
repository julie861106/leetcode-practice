import pytest


def pytest_addoption(parser):
    parser.addoption("--env_config_path", action="store", default="", help="")
    parser.addoption("--test_key", action="store", default="", help="")


def pytest_collection_modifyitems(items, config):
    if not config.option.test_key:
        return
    target_list = items[0].config.getoption("--test_key").split(",")
    selected_items = []
    deselected_items = []
    for item in items:
        test_keys = [mark.args[0] for mark in item.iter_markers(name="test_key")]

        if not test_keys:
            deselected_items.append(item)
            continue
        if test_keys[0] not in target_list:
            deselected_items.append(item)
        else:
            selected_items.append(item)

    config.hook.pytest_deselected(items=deselected_items)
    items[:] = selected_items


@pytest.fixture(scope="session")
def env_config_path(request):
    return request.config.getoption("--env_config_path")
