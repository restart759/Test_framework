from object.page.base_page.page_function import *


class OfflineAssignPage(BaseFunc):

    def offline_assign_page(self):
        target = '//span[text()=" 工作台"]'
        video = '//div[text()="签约视频"]//following::button[text()="删除"]'
        upload_video = '//button[contains(text(),"请选择签约视频")]'
        success_confirm = '//button[text()="确认"]'

        self.wait_until_visible(target)
        if len(self.find_elements(video)) == 0:
            self.find_element(upload_video).click()
            time.sleep(2)
            os.system("C:\\Users\\Administrator\\PycharmProjects\\Test_framework\\data\\up_video.exe")
            time.sleep(3)
            self.find_element(success_confirm).click()
            time.sleep(1)
        PageFunction(self.driver).upload_picture()
