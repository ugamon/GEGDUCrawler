#encoding=utf-8
import os
from time import sleep

from selenium import webdriver
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

class SeleniumBase():
    """
    Базовый класс, выполняющий взаимодействие с DOM Service Manager посредством Selenium
    """
    def __init__(self,task="",timer=25):
        self.webdriver = webdriver.Chrome(os.path.join(appconfig.os_base,'service_manager_module','chromedriver.exe'))
        self.action_chain = action_chains.ActionChains(self.webdriver)
        self.timer = timer
        self.task = task

    def __to_log(self,message):
        print("performing: <<{message} function>>".format(message=message))

    def start(self,url=r"http://sm/sm/index.do"):
        """
        Метод, реализующий переход на страницу. Увеличение размера окна до максимума.
        """
        self.__to_log("start function")
        self.webdriver.get(url)
        self.webdriver.maximize_window()

    def get_ACH(self):
        """
        Метод, возвращающий объект Action Chain в свойстве self.action_chain
        """
        self.__to_log("get action chain object")
        return self.action_chain

    def get_element_clickable(self, value, time_to_wait_before=1):
        """
        Метод, возвращающий по XPATH кликабельный элемент DOM после секунды ожидания потока выполнения.
        """
        self.__to_log("get clickable element")
        self.wait(time_to_wait_before)
        element = WebDriverWait(self.webdriver, self.timer).until(
                ec.element_to_be_clickable((By.XPATH, value))
            )
        return element

    def get_element_presented(self, value, time_to_wait_before=1):
        """
        Метод, возвращающий по XPATH доступный элемент DOM после секунды ожидания потока выполнения.
        """
        self.__to_log("get presented element")
        self.wait(time_to_wait_before)
        element = WebDriverWait(self.webdriver, self.timer).until(
                ec.presence_of_element_located((By.XPATH, value))
            )
        return element

    def get_element_visible(self, value, time_to_wait_before=1):
        """
        Метод, возвращающий по XPATH видимый элемент DOM после секунды ожидания потока выполнения.
        """
        self.__to_log("get visible element")
        self.wait(time_to_wait_before)
        element = WebDriverWait(self.webdriver, self.timer).until(
            ec.visibility_of_element_located((By.XPATH, value))
        )
        return element

    def switch_to_frame(self, value, time_to_wait_before=0):
        """
        Метод, выполняющий переход в frame на странице.
        """
        self.__to_log("get the frame and switch to it")
        self.wait(time_to_wait_before)
        frame = WebDriverWait(self.webdriver, self.timer).until(
            ec.frame_to_be_available_and_switch_to_it((By.XPATH, value))
        )
        return frame

    def get_elements_presented(self, value, time_to_wait_before=0):
        """
        Метод, возвращающий список доступных элементов DOM по XPATH
        """
        self.__to_log("get presented elements")
        self.wait(time_to_wait_before)
        elements = WebDriverWait(self.webdriver, self.timer).until(
            ec.presence_of_all_elements_located((By.XPATH, value))
        )
        return elements

    def switch_to_last_frame(self, value, time_to_wait_before=0):
        """
        Переход в последний фрейм DOM из списка, выбранного по XPATH
        """
        self.__to_log("get the frame and switch to it")
        self.wait(time_to_wait_before)

        frames = self.get_elements_presented(value, time_to_wait_before)
        self.webdriver.switch_to.frame(frames[-1])


    def scroll_to_bottom(self, time_to_wait_before=0):
        """
        Грязный хак по переходу в низ страницы.
        window.scrollTo(0, document.body.scrollHeight);
        """
        self.__to_log("scroll to bottom of the page")
        self.wait(time_to_wait_before)
        self.webdriver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def return_to_default(self,time_to_wait_before=0):
        """
        Переход из фрейма обратно в главную область страницы.
        """
        self.__to_log("return to default context")
        self.wait(time_to_wait_before)
        self.webdriver.switch_to.default_content()

    def get_webelement_attribute(self, webelement, attribute, time_to_wait_before=0.5):
        """
        Метод, возвращающий аттрибут элемента. Например `innerHTML`
        """
        self.__to_log("get the webelement attribute")
        self.wait(time_to_wait_before)
        return webelement.get_attribute(attribute)

    def wait(self, time):
        """
        Метод, останавливающий поток на заданное кол-во секунд.
        """
        sleep(time)

    def close_browser(self, time_to_wait_before=0):
        """
        Метод, закрывающий браузер и прерывающий сессию. ref webdriver >> dev/null/
        """
        self.__to_log("closing browser")
        self.wait(time_to_wait_before)
        self.webdriver.quit()