import cv2
import time
import random
import sys

from etc import settings
from utils.base import *


class Task:
    def __init__(self, hwnd_list):
        self.hwnd_list = hwnd_list
        self.button_xiayi_img = cv2.cvtColor(cv2.imread("images/button_xiayi.png"), cv2.COLOR_BGR2GRAY)
        self.button_close_img = cv2.cvtColor(cv2.imread("images/button_close.png"), cv2.COLOR_BGR2GRAY)
        self.button_shenqing_img = cv2.cvtColor(cv2.imread("images/button_shenqing.png"), cv2.COLOR_BGR2GRAY)
        self.button_chuangjianduiwu_img = cv2.cvtColor(cv2.imread("images/button_chuangjianduiwu.png"), cv2.COLOR_BGR2GRAY)
        self.button_likaiduiwu_img = cv2.cvtColor(cv2.imread("images/button_likaiduiwu.png"), cv2.COLOR_BGR2GRAY)
        self.window_likaiduiwu_img = cv2.cvtColor(cv2.imread("images/window_likaiduiwu.png"), cv2.COLOR_BGR2GRAY)
        #self.button_renwu_xianshi_img = cv2.cvtColor(cv2.imread("images/button_renwu_xianshi.png"), cv2.COLOR_BGR2GRAY)
        self.button_renwu_yincang_img = cv2.cvtColor(cv2.imread("images/button_renwu_yincang.png"), cv2.COLOR_BGR2GRAY)
        self.button_jingxiu_img = cv2.cvtColor(cv2.imread("images/button_jingxiu.png"), cv2.COLOR_BGR2GRAY)
        self.in_battle_img = cv2.cvtColor(cv2.imread("images/in_battle.png"), cv2.COLOR_BGR2GRAY)
        self.button_daoju_img = cv2.cvtColor(cv2.imread("images/button_daoju.png"), cv2.COLOR_BGR2GRAY)
        self.button_renwu_img = cv2.cvtColor(cv2.imread("images/button_renwu.png"), cv2.COLOR_BGR2GRAY)
        self.button_duiwu_img = cv2.cvtColor(cv2.imread("images/button_duiwu.png"), cv2.COLOR_BGR2GRAY)
        self.button_close_jianyi_img = cv2.cvtColor(cv2.imread("images/button_close_jianyi.png"), cv2.COLOR_BGR2GRAY)
        self.button_yaoqing_img = cv2.cvtColor(cv2.imread("images/button_yaoqing.png"), cv2.COLOR_BGR2GRAY)
        self.button_duiwu_pipei_img = cv2.cvtColor(cv2.imread("images/button_duiwu_pipei.png"), cv2.COLOR_BGR2GRAY)
        self.button_queding_img = cv2.cvtColor(cv2.imread("images/button_queding.png"), cv2.COLOR_BGR2GRAY)
        self.press_kongbaiguanbi_img = cv2.cvtColor(cv2.imread("images/press_kongbaiguanbi.png"), cv2.COLOR_BGR2GRAY)

    def get_status(self, hwnd, src_img=None, with_standing=True):
        if src_img is None:
            src_img = capture(hwnd)

        points = get_match_points(src_img, self.in_battle_img)
        if points:
            return "in_battle"

        # 点击空白关闭
        points = get_match_points(src_img, self.press_kongbaiguanbi_img)
        if points:
            px, py = points[0]
            pos = (px + 30, py + 5)
            click(hwnd, pos, 50, 5)
            return "press_kongbaiguanbi"

        # 关闭侠义窗口
        points = get_match_points(src_img, self.button_close_img)
        if points:
            px, py = points[0]
            pos = (px + 7, py + 7)
            click(hwnd, pos)
            return "close_window"

        # 关闭建议弹窗
        points = get_match_points(src_img, self.button_close_jianyi_img)
        if points:
            pos = points[0]
            click(hwnd, pos)
            return "close_window_jianyi"

        # 点击自动
        points = get_match_points(src_img, self.button_daoju_img)
        if points:
            pos = (814, 445)
            click(hwnd, pos)
            return "in_battle"

        # 点击确定
        points = get_match_points(src_img, self.button_queding_img)
        if points:
            px, py = points[0]
            pos = (px + 40, py + 10)
            click(hwnd, pos)
            return "click_queding"

        # 匹配状态
        points = get_match_points(src_img, self.button_duiwu_pipei_img)
        if points:
            return "waiting_pipei"

        if with_standing:
            time.sleep(1)
            src_img2 = capture(hwnd)
            points = get_match_points(src_img2, self.in_battle_img)
            if points:
                return "in_battle"

            points = get_match_points(src_img, src_img2, threshold=0.8)
            if points:
                time.sleep(1)
                src_img3 = capture(hwnd)
                points = get_match_points(src_img3, self.in_battle_img)
                if points:
                    return "in_battle"

                points = get_match_points(src_img2, src_img3, threshold=0.8)
                if points:
                    return "standing"
                else:
                    return "moving"
            else:
                return "moving"

        # 未能匹配上任何状态
        return "unknown"

    def run_xiayi(self):
        while True:
            for hwnd in self.hwnd_list:
                time.sleep(random.uniform(settings.inverval_min, settings.inverval_max))

                # cv2.namedWindow("Image")
                # cv2.imshow("Image", src_img)
                # cv2.waitKey(0)
                status = self.get_status(hwnd)
                print(status)
                if status != "standing":
                    continue

                src_img = capture(hwnd)
                # 在野外挂机
                points = get_match_points(src_img, self.button_renwu_img, threshold=0.96)
                if points:
                    print("renwu_img")
                    # 点开队伍,点两下
                    pos = (838, 172)
                    click(hwnd, pos)
                    time.sleep(random.uniform(0.4, 0.6))
                    click(hwnd, pos)
                else:
                    points = get_match_points(src_img, self.button_duiwu_img, threshold=0.96)
                    if points:
                        print("duiwu")
                        # 点开队伍,点一下
                        pos = (838, 172)
                        click(hwnd, pos)
                    else:
                        # 展开任务栏,也有可能是正在匹配
                        print("展开任务栏")
                        pos = (837, 229)
                        click(hwnd, pos)
                        continue

                # 等待队伍界面打开
                time.sleep(random.uniform(1.8, 2.2))
                src_img = capture(hwnd)
                # 不在队伍中
                points = get_match_points(src_img, self.button_chuangjianduiwu_img)
                if points:
                    print("不在队伍中")
                    # 关闭队伍窗口
                    pos = (834, 208)
                    click(hwnd, pos, 10, 40)
                    time.sleep(random.uniform(1.8, 2.2))
                else:
                    points = get_match_points(src_img, self.button_yaoqing_img)
                    if points:
                        # 人不满，离开队伍
                        points = get_match_points(src_img, self.button_likaiduiwu_img)
                        if points:
                            print("离开队伍")
                            px, py = points[0]
                            # 查看队伍是否满员
                            points = get_match_points(src_img, self.button_yaoqing_img)
                            if points:
                                # 未满员，退出队伍
                                pos = (px + 50, py + 10)
                                click(hwnd, pos)
                                time.sleep(0.5)
                                src_img = capture(hwnd)
                                points = get_match_points(src_img, self.window_likaiduiwu_img)
                                if points:
                                    pos = (493, 329)
                                    click(hwnd, pos, 30, 10)
                                    time.sleep(random.uniform(0.5, 0.6))
                                    pos = (834, 208)
                                    click(hwnd, pos, 10, 40)
                            time.sleep(random.uniform(1.8, 2.2))

                # 侠义button
                pos = (825, 379)
                click(hwnd, pos)
                time.sleep(random.uniform(1.0, 1.2))
                src_img = capture(hwnd)
                # 申请
                points = get_match_points(src_img, self.button_shenqing_img)
                if points:
                    points = get_clean_points(points)
                    for point in points:
                        px, py = point
                        pos = (px + 30, py + 10)
                        click(hwnd, pos)
                        time.sleep(random.uniform(0.15, 0.2))


if __name__ == '__main__':
    task = Task([67206])
    task.run_xiayi()
