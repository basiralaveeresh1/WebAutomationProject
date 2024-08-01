## Python Web Automation Programs 
## 'pip install pytest pytest-html selenium allure-pytest openpyxl'

## Selenium Topics

### - To generate the Allure-reports. Please follow the steps

#### pytest -s test_Lab009.py --alluredir=allure-results 
#### allure server allure-results


## To Generate a Screenshots in  Allure reports. Please use the below command
### allure.attach(driver.get_screenshot_as_png(),name="Failed Login description",attachment_type=AttachmentType.PNG)
### Methods	                                   Description
### save_screenshot('path/to/save/screenshot') -->	This method allows you to specify the path to save the screenshot.
### get_screenshot_as_file('filename.png') -->	This will save the screenshot as a PNG file.
### get_screenshot_as_png() -->	This method returns the screenshot as binary data, which can be useful for on-the-fly image processing or analysis.

