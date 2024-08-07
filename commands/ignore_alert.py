from testui.support.testui_driver import TestUIDriver
from selenium.common.exceptions import NoAlertPresentException

from testui.support import logger


def ignore_alert(driver: TestUIDriver) -> None:
    try:
        driver.get_driver().switch_to.alert.accept()
    except NoAlertPresentException:
        logger.log_debug("[INFO] Loadero: No alert is open.")

        pass
