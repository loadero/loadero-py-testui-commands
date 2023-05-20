# loadero-py-testui-commands

## Installation

Installation is as simple as adding this line to your requirements.txt 
(or equalivent) file.

```bash
git+https://github.com/loadero/loadero-py-testui-commands.git@master
```

After which you will be able to install all of the dependencies using pip.
```bash
pip install -r requirements.txt
```

The latest tag (or master) always will be the most up-to-date version when 
compared to the commands used in Loadero environment.

## Usage

These Py-TestUI custom commands were made to simplify local script development 
for usage in Loadero environment. By using these commands, you can write your 
Loadero script locally and then upload it to Loadero without any changes. This 
also allows for more rapid development because it can be debugged and ran 
locally. 

To use the commands in your tests, you need to download apply this dependency 
and only then import the functions in your script file. Keep in mind, that when 
migrating the script to Loadero, you do not need to import the functions there 
as-well, that will be done automatically.

This is how you can import the functions in your script file:
```py
from commands.set_file import set_file
from commands.set_request_header import set_request_header
from commands.set_user_agent import set_user_agent
from commands.ignore_alert import ignore_alert
from commands.update_network import update_network
from commands.wait_for_download_finished import wait_for_download_finished
from commands.time_execution import time_execution
```

After which they can be used in your script file as any other function. 
Script example:
```py
def test_on_loadero(driver: TestUIDriver):
    really_long_pause = 300
    driver.navigate_to("https://duckduckgo.com/")

    def locate_search_bar_and_wait():
        e(
            driver, "css", "#search_form_input_homepage"
        ).wait_until_visible().send_keys("loadero")
        e(driver, "css", "#search_button_homepage").wait_until_visible().click()
        e(driver, "css", "#r1-0 > div > h2").wait_until_visible()
        time.sleep(really_long_pause)

    # Example of timing execution without specifying a timeout.
    time_execution("locate_search_bar_and_wait", locate_search_bar_and_wait)
```


## Commands

Not all commands behave the same way as they do in Loadero environment. Some of 
them are modified to work in local environment. Such as `updateNetwork` and 
`setRequestHeader`. The following table shows all available commands and if they 
will behave the same in both environments.

| Command                   | Differences                                                                            |
| ------------------------- | -------------------------------------------------------------------------------------- |
| `ignoreAlert`             | No differences                                                                         |
| `setFile`                 | Any local file can be used, Loadero constant can be used if the same file name is used |
| `setRequestHeader`        | No request header will be set                                                          |
| `setUserAgent`            | User agent won't be changed                                                            |
| `timeExecution`           | Execution time will be logged, but not saved                                           |
| `updateNetwork`           | Network settings will not be updated                                                   |
| `waitForDownloadFinished` | Function will finish instantly and not wait for download to be finished                |

Full descriptions for each function and their usage can be found in 
[Loadero wiki](https://wiki.loadero.com/testui-python/custom-commands/) page.
