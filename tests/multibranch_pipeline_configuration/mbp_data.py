from selenium.webdriver.common.by import By


class Project:
    PROJECT_NAME = "Multibranch_Pipeline_Project"


class Toggle:
    TOGGLE = (By.ID, "toggle-switch-enable-disable-project")
    TOGGLE_TOOLTIP_PREFS = (
        "tippy-10",
        "(No new builds within this Multibranch Pipeline will be executed until it is re-enabled)"
    )
    TOGGLE_ENABLED_TEXT = "Enabled"
    TOGGLE_DISABLED_TEXT = "Disabled"
    TOGGLE_ENABLED_ERROR_TEXT = "The toggle switch must be enabled!"
    TOGGLE_TOOLTIP_ERROR_TEXT = "Something went wrong with the tooltip!"
    TOGGLE_TOOLTIP_ATTRIBUTE = ("aria-describedby", "tooltip")


class BranchSources:
    EXPECTED_SOURCES = [
        'Git',
        'GitHub',
        'Single repository & branch'
    ]