from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import NoSuchElementException


class BaseFunc(object):

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, selector):
        """
        submit_btn = "id=>su"
        login_lnk = "xpath => //*[@id='u1']/a[7]"
        :param selector:
        :return: element
        """
        # element = ''
        if '=>' not in selector:
            return self.driver.find_element_by_xpath(selector)
        selector_by = selector.split('=>')[0]
        selector_value = selector.split('=>')[1]

        if selector_by == "i" or selector_by == 'id':
            element = self.driver.find_element_by_id(selector_value)
            # try:
            #     element = self.driver.find_element_by_id(selector_value)
            #     logger.info("Had find the element \' %s \' successful "
            #                 "by %s via value: %s " % (element.text, selector_by, selector_value))
            # except NoSuchElementException as e:
            #     logger.error("NoSuchElementException: %s" % e)
            #     self.get_windows_img()  # take screenshot
        elif selector_by == "n" or selector_by == 'name':
            element = self.driver.find_element_by_name(selector_value)
        elif selector_by == "c" or selector_by == 'class_name':
            element = self.driver.find_element_by_class_name(selector_value)
        elif selector_by == "l" or selector_by == 'link_text':
            element = self.driver.find_element_by_link_text(selector_value)
        elif selector_by == "p" or selector_by == 'partial_link_text':
            element = self.driver.find_element_by_partial_link_text(selector_value)
        elif selector_by == "t" or selector_by == 'tag_name':
            element = self.driver.find_element_by_tag_name(selector_value)
        elif selector_by == "x" or selector_by == 'xpath':
            element = self.driver.find_element_by_xpath(selector_value)
            # try:
            #     element = self.driver.find_element_by_xpath(selector_value)
            #     logger.info("Had find the element \' %s \' successful "
            #                 "by %s via value: %s " % (element.text, selector_by, selector_value))
            # except NoSuchElementException as e:
            #     logger.error("NoSuchElementException: %s" % e)
            #     self.get_windows_img()
        elif selector_by == "s" or selector_by == 'selector_selector':
            element = self.driver.find_element_by_css_selector(selector_value)
        else:
            raise NameError("Please enter a valid type of targeting elements.")

        return element

    def find_elements(self, selector):
        # element = ''
        if '=>' not in selector:
            return self.driver.find_elements_by_xpath(selector)
        selector_by = selector.split('=>')[0]
        selector_value = selector.split('=>')[1]

        if selector_by == "i" or selector_by == 'id':
            element = self.driver.find_elements_by_id(selector_value)
            # try:
            #     element = self.driver.find_elements_by_id(selector_value)
            #     logger.info("Had find the element \' %s \' successful "
            #                 "by %s via value: %s " % (element.text, selector_by, selector_value))
            # except NoSuchElementException as e:
            #     logger.error("NoSuchElementException: %s" % e)
            #     self.get_windows_img()  # take screenshot
        elif selector_by == "n" or selector_by == 'name':
            element = self.driver.find_elements_by_name(selector_value)
        elif selector_by == "c" or selector_by == 'class_name':
            element = self.driver.find_elements_by_class_name(selector_value)
        elif selector_by == "l" or selector_by == 'link_text':
            element = self.driver.find_elements_by_link_text(selector_value)
        elif selector_by == "p" or selector_by == 'partial_link_text':
            element = self.driver.find_elements_by_partial_link_text(selector_value)
        elif selector_by == "t" or selector_by == 'tag_name':
            element = self.driver.find_elements_by_tag_name(selector_value)
        elif selector_by == "x" or selector_by == 'xpath':
            element = self.driver.find_elements_by_xpath(selector_value)
            # try:
            #     element = self.driver.find_elements_by_xpath(selector_value)
            #     logger.info("Had find the element \' %s \' successful "
            #                 "by %s via value: %s " % (element.text, selector_by, selector_value))
            # except NoSuchElementException as e:
            #     logger.error("NoSuchElementException: %s" % e)
            #     self.get_windows_img()
        elif selector_by == "s" or selector_by == 'selector_selector':
            element = self.driver.find_elements_by_css_selector(selector_value)
        else:
            raise NameError("Please enter a valid type of targeting elements.")

        return element

    def wait_until_clickable(self, selector):
        # element = ''
        if '=>' not in selector:
            element = selector
        else:
            element = selector.split('=>')[1]
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, element)))
        # try:
        #     WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, element)))
        #     logger.info("Wait until element with %s clickable" % element)
        # except NameError as e:
        #     logger.error("Failed to wait with %s" % e)
        #     self.get_windows_img()

    def wait_until_visible(self, selector):
        element = ''
        if '=>' not in selector:
            element = selector
        else:
            element = selector.split('=>')[1]
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.XPATH, element)))
        # try:
        #     WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.XPATH, element)))
        #     logger.info("Wait until element with %s visible" % element)
        # except NameError as e:
        #     logger.error("Failed to wait with %s" % e)
        #     self.get_windows_img()

    def wait_until_invisible(self, selector):
        element = ''
        if '=>' not in selector:
            element = selector
        else:
            element = selector.split('=>')[1]
        WebDriverWait(self.driver, 60).until(EC.invisibility_of_element_located((By.XPATH, element)))

    def click(self, selector):
        el = self.find_element(selector)
        el.click()
        # try:
        #     el.click()
        # #            logger.info("The element \' %s \' was clicked." % el.text)
        # except NameError as e:
        #     logger.error("Failed to click the element with %s" % e)
