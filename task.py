import sys
from datetime import datetime

from utils.base import *
from utils.wechat import senddata


class Task:
    def __init__(self, hwnd_list):
        self.hwnd_list = hwnd_list
        self.button_xiayi_img = cv2.cvtColor(cv2.imread("images/button_xiayi.png"), cv2.COLOR_BGR2GRAY)
        #self.button_shenqing_img = cv2.cvtColor(cv2.imread("images/button_shenqing.png"), cv2.COLOR_BGR2GRAY)
        self.icon_xingxiazhangyi_img = cv2.cvtColor(cv2.imread("images/icon_xingxiazhangyi.png"), cv2.COLOR_BGR2GRAY)
        self.button_chuangjianduiwu_img = cv2.cvtColor(cv2.imread("images/button_chuangjianduiwu.png"), cv2.COLOR_BGR2GRAY)
        self.button_likaiduiwu_img = cv2.cvtColor(cv2.imread("images/button_likaiduiwu.png"), cv2.COLOR_BGR2GRAY)
        self.window_likaiduiwu_img = cv2.cvtColor(cv2.imread("images/window_likaiduiwu.png"), cv2.COLOR_BGR2GRAY)
        #self.button_renwu_xianshi_img = cv2.cvtColor(cv2.imread("images/button_renwu_xianshi.png"), cv2.COLOR_BGR2GRAY)
        self.button_renwu_yincang_img = cv2.cvtColor(cv2.imread("images/button_renwu_yincang.png"), cv2.COLOR_BGR2GRAY)
        self.button_beibao_img = cv2.cvtColor(cv2.imread("images/button_beibao.png"), cv2.COLOR_BGR2GRAY)
        self.in_battle_img = cv2.cvtColor(cv2.imread("images/in_battle.png"), cv2.COLOR_BGR2GRAY)
        self.button_daoju_img = cv2.cvtColor(cv2.imread("images/button_daoju.png"), cv2.COLOR_BGR2GRAY)
        self.button_renwu_img = cv2.cvtColor(cv2.imread("images/button_renwu.png"), cv2.COLOR_BGR2GRAY)
        self.button_duiwu_img = cv2.cvtColor(cv2.imread("images/button_duiwu.png"), cv2.COLOR_BGR2GRAY)
        self.button_close_jianyi_img = cv2.cvtColor(cv2.imread("images/button_close_jianyi.png"), cv2.COLOR_BGR2GRAY)
        self.button_yaoqing_img = cv2.cvtColor(cv2.imread("images/button_yaoqing.png"), cv2.COLOR_BGR2GRAY)
        self.button_duiwu_pipei_img = cv2.cvtColor(cv2.imread("images/button_duiwu_pipei.png"), cv2.COLOR_BGR2GRAY)
        self.button_queding_img = cv2.cvtColor(cv2.imread("images/button_queding.png"), cv2.COLOR_BGR2GRAY)
        self.press_kongbaiguanbi_img = cv2.cvtColor(cv2.imread("images/press_kongbaiguanbi.png"), cv2.COLOR_BGR2GRAY)
        self.duihua_qianwangzudui_img = cv2.cvtColor(cv2.imread("images/duihua_qianwangzudui.png"), cv2.COLOR_BGR2GRAY)
        self.button_buzhen_img = cv2.cvtColor(cv2.imread("images/button_buzhen.png"), cv2.COLOR_BGR2GRAY)
        self.duihua_qianwangcanyu_img = cv2.cvtColor(cv2.imread("images/duihua_qianwangcanyu.png"), cv2.COLOR_BGR2GRAY)
        self.button_kaishirenwu_img = cv2.cvtColor(cv2.imread("images/button_kaishirenwu.png"), cv2.COLOR_BGR2GRAY)
        self.duihua_jitianxia_img = cv2.cvtColor(cv2.imread("images/duihua_jitianxia.png"), cv2.COLOR_BGR2GRAY)
        self.duihua_jiequ_img = cv2.cvtColor(cv2.imread("images/duihua_jiequ.png"), cv2.COLOR_BGR2GRAY)
        self.duihua_likai_img = cv2.cvtColor(cv2.imread("images/duihua_likai.png"), cv2.COLOR_BGR2GRAY)
        self.icon_tiaoguoduihua_img = cv2.cvtColor(cv2.imread("images/icon_tiaoguoduihua.png"), cv2.COLOR_BGR2GRAY)
        self.duihua_queding_img = cv2.cvtColor(cv2.imread("images/duihua_queding.png"), cv2.COLOR_BGR2GRAY)
        self.button_jixu_img = cv2.cvtColor(cv2.imread("images/button_jixu.png"), cv2.COLOR_BGR2GRAY)
        self.button_shiyong_img = cv2.cvtColor(cv2.imread("images/button_shiyong.png"), cv2.COLOR_BGR2GRAY)
        self.duihua_duihua_img = cv2.cvtColor(cv2.imread("images/duihua_duihua.png"), cv2.COLOR_BGR2GRAY)
        self.duihua_duihua2_img = cv2.cvtColor(cv2.imread("images/duihua_duihua2.png"), cv2.COLOR_BGR2GRAY)
        self.duihua_zhandou_img = cv2.cvtColor(cv2.imread("images/duihua_zhandou.png"), cv2.COLOR_BGR2GRAY)
        self.button_paiwei_img = cv2.cvtColor(cv2.imread("images/button_paiwei.png"), cv2.COLOR_BGR2GRAY)
        self.button_queding_paiwei_img = cv2.cvtColor(cv2.imread("images/button_queding_paiwei.png"), cv2.COLOR_BGR2GRAY)
        self.duihua_zhenmo_end_img = cv2.cvtColor(cv2.imread("images/duihua_zhenmo_end.png"), cv2.COLOR_BGR2GRAY)
        self.button_tongyirudui_img = cv2.cvtColor(cv2.imread("images/button_tongyirudui.png"),cv2.COLOR_BGR2GRAY)
        self.xiayi_end_img = cv2.cvtColor(cv2.imread("images/xiayi_end.png"), cv2.COLOR_BGR2GRAY)
        self.button_tuichu_img = cv2.cvtColor(cv2.imread("images/button_tuichu.png"), cv2.COLOR_BGR2GRAY)
        self.button_qianwangtiaozhan_img = cv2.cvtColor(cv2.imread("images/button_qianwangtiaozhan.png"),
                                                        cv2.COLOR_BGR2GRAY)
        self.button_qianwangtiaozhan2_img = cv2.cvtColor(cv2.imread("images/button_qianwangtiaozhan2.png"),
                                                        cv2.COLOR_BGR2GRAY)
        self.button_quxiao_img = cv2.cvtColor(cv2.imread("images/button_quxiao.png"), cv2.COLOR_BGR2GRAY)
        self.title_xianshishilian_img = cv2.cvtColor(cv2.imread("images/title_xianshishilian.png"), cv2.COLOR_BGR2GRAY)
        self.title_jingyingjudian_img = cv2.cvtColor(cv2.imread("images/title_jingyingjudian.png"), cv2.COLOR_BGR2GRAY)
        self.button_qianwang_img = cv2.cvtColor(cv2.imread("images/button_qianwang.png"), cv2.COLOR_BGR2GRAY)
        self.duihua2_qianwang_img = cv2.cvtColor(cv2.imread("images/duihua2_qianwang.png"), cv2.COLOR_BGR2GRAY)
        self.duihua_queren_img = cv2.cvtColor(cv2.imread("images/duihua_queren.png"), cv2.COLOR_BGR2GRAY)
        self.button_faqitiaozhan_img = cv2.cvtColor(cv2.imread("images/button_faqitiaozhan.png"), cv2.COLOR_BGR2GRAY)
        self.window_jiaoyi_img = cv2.cvtColor(cv2.imread("images/window_jiaoyi.png"), cv2.COLOR_BGR2GRAY)

        self.button_close_img_color = cv2.cvtColor(cv2.imread("images/button_close.png"), cv2.IMREAD_COLOR)
        self.icon_duiwu_shenqing1_img_color = cv2.cvtColor(cv2.imread("images/icon_duiwu_shenqing1.png"),
                                                           cv2.IMREAD_COLOR)
        self.icon_duiwu_shenqing2_img_color = cv2.cvtColor(cv2.imread("images/icon_duiwu_shenqing2.png"),
                                                           cv2.IMREAD_COLOR)
        self.num_members_1_img_color = cv2.cvtColor(cv2.imread("images/num_members_1.png"), cv2.IMREAD_COLOR)
        self.num_members_2_img_color = cv2.cvtColor(cv2.imread("images/num_members_2.png"), cv2.IMREAD_COLOR)
        self.num_members_3_img_color = cv2.cvtColor(cv2.imread("images/num_members_3.png"), cv2.IMREAD_COLOR)
        self.num_members_4_img_color = cv2.cvtColor(cv2.imread("images/num_members_4.png"), cv2.IMREAD_COLOR)
        self.num_members_5_img_color = cv2.cvtColor(cv2.imread("images/num_members_5.png"), cv2.IMREAD_COLOR)
        self.button_renwu_img_color = cv2.cvtColor(cv2.imread("images/button_renwu.png"), cv2.IMREAD_COLOR)
        self.button_duiwu_img_color = cv2.cvtColor(cv2.imread("images/button_duiwu.png"), cv2.IMREAD_COLOR)
        self.button_daoju_img_color = cv2.cvtColor(cv2.imread("images/button_daoju.png"), cv2.IMREAD_COLOR)

    def get_members_num(self, hwnd):
        src_img_color = capture(hwnd, color=cv2.IMREAD_COLOR)

        # ?????????????????????
        points = get_match_points(src_img_color, self.button_daoju_img_color)
        if points:
            # ?????????????????????
            print("?????????????????????????????????????????????")
            return None

        points = get_match_points(src_img_color, self.button_renwu_img_color, threshold=0.96)
        if points:
            # ?????????????????????
            print("?????????????????????")
            pos = (838, 162)
            click(hwnd, pos)
            time.sleep(random.uniform(0.6, 0.8))
            pos = (810, 230)
            click(hwnd, pos)
            time.sleep(random.uniform(1.0, 1.2))
            src_img_color = capture(hwnd, color=cv2.IMREAD_COLOR)
        else:
            points = get_match_points(src_img_color, self.button_duiwu_img_color, threshold=0.96)
            if not points:
                # ???????????????
                print("???????????????")
                pos = (837, 229)
                click(hwnd, pos)
                time.sleep(random.uniform(1.0, 1.2))
                src_img_color = capture(hwnd, color=cv2.IMREAD_COLOR)
                points = get_match_points(src_img_color, self.button_renwu_img_color, threshold=0.96)
                if points:
                    # ?????????????????????
                    print("?????????????????????")
                    pos = (838, 162)
                    click(hwnd, pos)
                    time.sleep(random.uniform(0.6, 0.8))
                    pos = (810, 230)
                    click(hwnd, pos)
                    time.sleep(random.uniform(1.0, 1.2))
                    src_img_color = capture(hwnd, color=cv2.IMREAD_COLOR)

        left = 793
        top = 112
        w = 68
        h = 150
        opponent_img_color = src_img_color[top:top + h, left:left + w]

        points = get_match_points(opponent_img_color, self.num_members_1_img_color, threshold=0.95)
        if points:
            num = 1
        else:
            points = get_match_points(opponent_img_color, self.num_members_2_img_color, threshold=0.95)
            if points:
                num = 2
            else:
                points = get_match_points(opponent_img_color, self.num_members_3_img_color, threshold=0.95)
                if points:
                    num = 3
                else:
                    points = get_match_points(opponent_img_color, self.num_members_4_img_color, threshold=0.95)
                    if points:
                        num = 4
                    else:
                        points = get_match_points(opponent_img_color, self.num_members_5_img_color, threshold=0.95)
                        if points:
                            num = 5
                        else:
                            print("???????????????")
                            num = 0
        if num:
            print("??????????????????:{}".format(num))
        return num

    def open_window_huodong(self, hwnd, src_img=None):
        if src_img is None:
            src_img = capture(hwnd)
        for i in range(3):
            points = get_match_points(src_img, self.button_beibao_img)
            if points:
                # ????????????
                pos = (37, 103)
                click(hwnd, pos)
                time.sleep(random.uniform(0.8, 1.2))
                return True
            else:
                status = self.get_status(hwnd, src_img)
                print(status)
                time.sleep(random.uniform(0.8, 1.2))
                src_img = capture(hwnd)
        return False

    def get_status(self, hwnd, src_img=None):
        if src_img is None:
            src_img = capture(hwnd)

        # points = get_match_points(src_img, self.in_battle_img)
        # if points:
        #     return "in_battle"

        # ??????????????????
        points = get_match_points(src_img, self.press_kongbaiguanbi_img)
        if points:
            px, py = points[0]
            pos = (px + 30, py + 5)
            click(hwnd, pos, 50, 5)
            return "press_kongbaiguanbi"

        # ??????????????????
        points = get_match_points(src_img, self.button_close_jianyi_img, threshold=0.98)
        if points:
            pos = points[0]
            click(hwnd, pos)
            return "close_window_jianyi"

        # # ????????????
        # points = get_match_points(src_img, self.duihua_jiequ_img)
        # if points:
        #     px, py = points[0]
        #     pos = (px + 40, py + 5)
        #     click(hwnd, pos)
        #     return "click_jiequrenwu"
        #
        # # ????????????
        # points = get_match_points(src_img, self.button_queding_img)
        # if points:
        #     px, py = points[0]
        #     pos = (px + 40, py + 10)
        #     click(hwnd, pos)
        #     return "click_queding"

        # 30?????????????????????????????????????????????????????????
        points = get_match_points(src_img, self.button_daoju_img)
        if points:
            # pos = (814, 445)
            # click(hwnd, pos)
            return "in_battle"

        # ?????????????????????
        points = get_match_points(src_img, self.window_jiaoyi_img)
        if points:
            return "standing"

        # ????????????
        points = get_match_points(src_img, self.button_duiwu_pipei_img)
        if points:
            return "waiting_pipei"

        # ?????????
        points = get_match_points(src_img, self.duihua_zhandou_img)
        if points:
            px, py = points[0]
            pos = (px + 40, py + 5)
            click(hwnd, pos)
            return "click_battle"

        # ?????????????????????????????????
        points = get_match_points(src_img, self.button_qianwangtiaozhan_img)
        if not points:
            points = get_match_points(src_img, self.button_qianwangtiaozhan2_img)
        if points:
            print("???????????????")
            px, py = points[0]
            pos = (px + 50, py + 15)
            click(hwnd, pos)
            return "click_qianwangtiaozhan"

        points = get_match_points(src_img, self.duihua_duihua_img)
        if not points:
            points = get_match_points(src_img, self.duihua_duihua2_img)
        if points:
            print("???????????????get_status????????????")
            return "standing"

        # ????????????????????????
        points = get_match_points(src_img, self.button_quxiao_img)
        if points:
            print("?????????")
            px, py = points[0]
            pos = (px + 230, py + 15)
            click(hwnd, pos)
            return "click_queding"

        # ????????????????????????
        points = get_match_points(src_img, self.button_kaishirenwu_img)
        if points:
            print("?????????????????????")
            px, py = points[0]
            pos = (px + 30, py + 5)
            click(hwnd, pos, 50, 10)
            return "click_kaishirenwu"

        # ??????????????????
        src_img_color = capture(hwnd, color=cv2.IMREAD_COLOR)
        points = get_match_points(src_img_color, self.button_close_img_color, threshold=0.95)
        if points:
            px, py = points[0]
            pos = (px + 7, py + 7)
            click(hwnd, pos)
            return "close_window"

        left = 793
        top = 112
        w = 68
        h = 150
        opponent_img_color = src_img_color[top:top + h, left:left + w]

        # cv2.namedWindow("Image")
        # cv2.imshow("Image", opponent_img_color)
        # cv2.waitKey(0)
        # sys.exit(1)
        # ???????????????????????????????????????
        points = get_match_points(opponent_img_color, self.icon_duiwu_shenqing1_img_color)
        if points:
            # ???????????????,???????????????????????????
            print("???????????????")
            pos = (837, 229)
            click(hwnd, pos)
            return "zhankai_duiwulan"

        # ?????????????????????????????????????????????
        points = get_match_points(opponent_img_color, self.icon_duiwu_shenqing2_img_color)
        if points:
            print("????????????????????????")
            points = get_match_points(src_img, self.button_renwu_img, threshold=0.96)
            if not points:
                points = get_match_points(src_img, self.button_duiwu_img, threshold=0.96)
            if points:
                print("????????????????????????")
                # ????????????,?????????
                pos = (838, 172)
                click(hwnd, pos)
            else:
                print("??????????????????")
                return "error"

            # ??????????????????
            time.sleep(random.uniform(0.8, 1.2))
            src_img = capture(hwnd)
            points = get_match_points(src_img, self.button_tongyirudui_img)
            points = get_clean_points(points)
            if points:
                print("???????????????")
                px, py = points[0]
                pos = (px + 30, py + 5)
                click(hwnd, pos)
                time.sleep(random.uniform(0.4, 0.6))
                # ???????????????
                pos = (486, 399)
                click(hwnd, pos, 30, 10)
            return "access_join"

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
                # points = get_match_points(src_img3, self.duihua_duihua_img)
                # if not points:
                #     points = get_match_points(src_img3, self.duihua_zhandou_img)
                # if points:
                #     px, py = points[0]
                #     pos = (px + 40, py + 5)
                #     click(hwnd, pos)
                #     return "click_weizhiduihua"

                points = get_match_points(src_img3, self.button_beibao_img)
                if not points:
                    print("????????????")
                    for i in range(5):
                        pos = (3, 377)
                        click(hwnd, pos)
                        time.sleep(random.uniform(0.2, 0.3))
                    return "standing"
                else:
                    return "standing"
            else:
                return "moving"
        else:
            return "moving"

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
                # # ????????????
                # points = get_match_points(src_img, self.button_queding_img)
                # if points:
                #     print("????????????")
                #     px, py = points[0]
                #     pos = (px + 40, py + 10)
                #     click(hwnd, pos)
                #     continue

                # ???????????????????????????
                points = get_match_points(src_img, self.button_tuichu_img, threshold=0.88)
                if points:
                    print("??????????????????")
                    px, py = points[0]
                    pos = (px + 10, py + 20)
                    click(hwnd, pos)
                    # ???3s????????????
                    time.sleep(random.uniform(3.5, 4.0))
                    pos = (498, 329)
                    click(hwnd, pos, 30, 10)
                    continue

                # ??????????????????
                points = get_match_points(src_img, self.duihua_duihua_img)
                if points:
                    print("???????????????")
                    px, py = points[0]
                    pos = (px + 40, py + 5)
                    click(hwnd, pos)
                    continue

                num = self.get_members_num(hwnd)
                if num is None:
                    print("???????????????????????????????????????")
                    continue
                else:
                    # ????????????????????????
                    if num == 0:
                        print("????????????????????????????????????")
                        pos = (825, 379)
                        click(hwnd, pos)
                        time.sleep(random.uniform(1.0, 1.2))
                        src_img = capture(hwnd)
                        # ??????
                        points = get_match_points(src_img, self.icon_xingxiazhangyi_img)
                        if not points:
                            time.sleep(random.uniform(1.0, 1.2))
                            # ?????????
                            pos = (713, 442)
                            click(hwnd, pos, 25, 10)
                            time.sleep(random.uniform(1.0, 1.2))
                            src_img = capture(hwnd)
                            points = get_match_points(src_img, self.icon_xingxiazhangyi_img)
                        if points:
                            print("????????????")
                            points = get_clean_points(points, reverse=False)
                            for i in range(5):
                                try:
                                    px, py = points[i]
                                except:
                                    break
                                # pos = (px + 30, py + 10)
                                pos = (px + 426, py + 25)
                                click(hwnd, pos, 25, 10)
                                time.sleep(random.uniform(0.15, 0.2))
                    elif num < 5:
                        print("????????????????????????")
                        # ????????????,?????????
                        pos = (838, 172)
                        click(hwnd, pos)
                        # ????????????????????????
                        time.sleep(random.uniform(1.0, 1.2))
                        src_img = capture(hwnd)
                        points = get_match_points(src_img, self.button_likaiduiwu_img)
                        if points:
                            print("????????????")
                            px, py = points[0]
                            # ????????????
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
                            continue
                        else:
                            print("??????????????????????????????")
                            continue
                    else:
                        print("???????????????????????????")
                        continue

    def run_yitiao_single(self):
        num_standing = 0
        while True:
            if num_standing >= 5:
                src_img = capture(hwnd)
                # ??????????????????
                points = get_match_points(src_img, self.duihua_duihua_img)
                if points:
                    print("???????????????")
                    px, py = points[0]
                    pos = (px + 40, py + 5)
                    click(hwnd, pos)
                    num_standing = 0
                    continue
                return

            for hwnd in self.hwnd_list:
                time.sleep(random.uniform(settings.inverval_min, settings.inverval_max))

                status = self.get_status(hwnd)
                print(status)
                if status != "standing":
                    num_standing = 0
                    continue
                else:
                    num_standing += 1

                src_img = capture(hwnd)
                # ???????????????
                points = get_match_points(src_img, self.duihua_qianwangcanyu_img)
                if points:
                    px, py = points[0]
                    pos = (px + 40, py + 5)
                    click(hwnd, pos)
                    return "click_qianwangcanyu"

    def run_wuxianzhenmo(self):
        hwnd = self.hwnd_list[0]
        num_standing = 0
        is_new_battle = True
        num_members = None
        num_waiting = 0
        while True:
            if num_waiting >= 120:
                print("120s????????????")
                return
            if num_standing >= 8:
                src_img = capture(hwnd)
                # ??????????????????
                points = get_match_points(src_img, self.duihua_duihua_img)
                if points:
                    print("???????????????")
                    px, py = points[0]
                    pos = (px + 40, py + 5)
                    click(hwnd, pos)
                    num_standing = 0
                    continue
                # ?????????
                pos = (36, 28)
                click(hwnd, pos, 25, 25)
                time.sleep(random.uniform(1.0, 1.2))
                # ?????????
                pos = (74, 156)
                click(hwnd, pos, 50, 5)
                time.sleep(random.uniform(1.0, 1.2))
                # ?????????
                pos = (437, 239)
                click(hwnd, pos, 20, 20)
                time.sleep(random.uniform(1.0, 1.2))
                # ????????????
                pos = (424, 268)
                click(hwnd, pos, 2, 2)
                num_standing = 0
                continue

            time.sleep(random.uniform(settings.inverval_min, settings.inverval_max))
            num_waiting += 1

            status = self.get_status(hwnd)
            print(status)
            if status != "standing":
                num_standing = 0
                if status == "in_battle":
                    num_waiting = 0
                    # ?????????????????????????????????????????????
                    if is_new_battle:
                        is_new_battle = False
                        num = self.get_members_num(hwnd)
                        if num:
                            if num_members is None:
                                num_members = num
                            print("??????????????????:{}".format(num_members))
                            print("??????????????????:{}".format(num))
                            if num < num_members:
                                print("?????????????????????????????????")
                                senddata("???????????????????????????????????????:{}".format(num), "")
                            num_members = num
                else:
                    is_new_battle = True
                continue
            else:
                num_standing += 1
                is_new_battle = True

            src_img = capture(hwnd)

            points = get_match_points(src_img, self.duihua_zhenmo_end_img,threshold=0.85)
            if points:
                print("?????????????????????")
                return
                #senddata("????????????????????????????????????????????????:{}".format(str(datetime.now())), "")

            # ????????????
            points = get_match_points(src_img, self.duihua_jiequ_img)
            if points:
                px, py = points[0]
                pos = (px + 40, py + 5)
                click(hwnd, pos)
                continue

            points = get_match_points(src_img, self.duihua_jitianxia_img)
            if points:
                print("??????????????????")
                px, py = points[0]
                pos = (px + 40, py + 5)
                click(hwnd, pos)
                time.sleep(random.uniform(1.0, 1.2))
                continue

            points = get_match_points(src_img, self.duihua_queding_img)
            if points:
                print("?????????")
                px, py = points[0]
                pos = (px + 40, py + 5)
                click(hwnd, pos)
                continue

    def run_xianshi(self, hwnd):
        num_err = 0
        while True:
            if num_err >= 3:
                print("?????????????????????????????????????????????")
                return

            time.sleep(random.uniform(1.0, 1.2))

            src_img = capture(hwnd)

            status = self.get_status(hwnd)
            print(status)
            if status != "standing":
                continue

            # ????????????
            points = get_match_points(src_img, self.duihua2_qianwang_img)
            if points:
                print("?????????")
                px, py = points[0]
                pos = (px + 40, py + 5)
                click(hwnd, pos)
                continue

            # ???????????????????????????
            points = get_match_points(src_img, self.duihua_queren_img)
            if points:
                print("?????????")
                px, py = points[0]
                pos = (px + 40, py + 5)
                click(hwnd, pos)
                continue

            result = self.open_window_huodong(hwnd, src_img)
            if result:
                num_err = 0
            else:
                num_err += 1
                print("????????????????????????")
                continue

            time.sleep(random.uniform(settings.inverval_min, settings.inverval_max))

            src_img = capture(hwnd)
            points = get_match_points(src_img, self.title_xianshishilian_img)
            if not points:
                print("?????????????????????????????????????????????.")
                return

            left, top = points[0]
            w = 250
            h = 80
            opponent_img = src_img[top:top + h, left:left + w]
            # cv2.namedWindow("Image")
            # cv2.imshow("Image", opponent_img)
            # cv2.waitKey(0)
            # sys.exit(1)
            points = get_match_points(opponent_img, self.button_qianwang_img)
            if points:
                # ????????????
                x, y = points[0]
                px = x + left
                py = y + top
                pos = (px + 30, py + 10)
                click(hwnd, pos)
                continue
            else:
                print("?????????????????????????????????????????????.")
                return

    def run_jingying(self, hwnd):
        num_err = 0
        while True:
            if num_err >= 3:
                print("?????????????????????????????????????????????")
                return

            time.sleep(random.uniform(settings.inverval_min, settings.inverval_max))

            src_img = capture(hwnd)

            status = self.get_status(hwnd)
            print(status)
            if status != "standing":
                continue

            # # ????????????
            # points = get_match_points(src_img, self.duihua2_qianwang_img)
            # if points:
            #     print("?????????")
            #     px, py = points[0]
            #     pos = (px + 40, py + 5)
            #     click(hwnd, pos)
            #     continue

            # # ???????????????????????????
            # points = get_match_points(src_img, self.duihua_queren_img)
            # if points:
            #     print("?????????")
            #     px, py = points[0]
            #     pos = (px + 40, py + 5)
            #     click(hwnd, pos)
            #     continue

            # ????????????
            points = get_match_points(src_img, self.button_faqitiaozhan_img)
            if points:
                print("???????????????")
                px, py = points[0]
                pos = (px + 60, py + 10)
                click(hwnd, pos)
                continue

            result = self.open_window_huodong(hwnd, src_img)
            if result:
                num_err = 0
            else:
                num_err += 1
                print("????????????????????????")
                continue

            time.sleep(random.uniform(1.0, 1.2))

            src_img = capture(hwnd)
            points = get_match_points(src_img, self.title_jingyingjudian_img)
            if not points:
                print("?????????????????????????????????????????????.")
                return

            left, top = points[0]
            w = 250
            h = 80
            opponent_img = src_img[top:top + h, left:left + w]
            # cv2.namedWindow("Image")
            # cv2.imshow("Image", opponent_img)
            # cv2.waitKey(0)
            # sys.exit(1)
            points = get_match_points(opponent_img, self.button_qianwang_img)
            if points:
                # ????????????
                x, y = points[0]
                px = x + left
                py = y + top
                pos = (px + 30, py + 10)
                click(hwnd, pos)
                continue
            else:
                print("?????????????????????????????????????????????.")
                return

    def run_zudui_yitiao(self):
        hwnd = self.hwnd_list[0]
        num_standing = 0
        while True:
            if num_standing >= 10:
                print("??????????????????????????????????????????????????????")
                self.run_xianshi(hwnd)
                self.run_jingying(hwnd)
                print("??????????????????")
                return

            time.sleep(random.uniform(settings.inverval_min, settings.inverval_max))

            status = self.get_status(hwnd)
            print(status)
            if status != "standing":
                num_standing = 0
                continue
            else:
                num_standing += 1

            src_img = capture(hwnd)

            # ????????????????????????
            points = get_match_points(src_img, self.button_kaishirenwu_img)
            if points:
                print("?????????????????????")
                px, py = points[0]
                pos = (px + 30, py + 5)
                click(hwnd, pos, 50, 10)
                continue

            # ????????????
            points = get_match_points(src_img, self.duihua_jiequ_img)
            if points:
                print("???????????????")
                px, py = points[0]
                pos = (px + 40, py + 5)
                click(hwnd, pos)
                continue

            # ???????????????
            points = get_match_points(src_img, self.duihua_qianwangcanyu_img)
            if points:
                print("???????????????")
                px, py = points[0]
                pos = (px + 40, py + 5)
                click(hwnd, pos)
                continue

            points = get_match_points(src_img, self.duihua_jitianxia_img)
            if points:
                print("??????????????????")
                px, py = points[0]
                pos = (px + 40, py + 5)
                click(hwnd, pos)
                time.sleep(random.uniform(1.0, 1.2))
                continue

            points = get_match_points(src_img, self.duihua_queding_img)
            if points:
                print("?????????")
                px, py = points[0]
                pos = (px + 40, py + 5)
                click(hwnd, pos)
                continue

    def run_zhuxian(self):
        while True:
            for hwnd in self.hwnd_list:
                time.sleep(random.uniform(settings.inverval_min, settings.inverval_max))

                src_img = capture(hwnd)

                # 30?????????????????????????????????????????????????????????
                points = get_match_points(src_img, self.button_daoju_img)
                if points:
                    # pos = (814, 445)
                    # click(hwnd, pos)
                    continue

                points = get_match_points(src_img, self.duihua_duihua_img)
                if points:
                    px, py = points[0]
                    pos = (px + 40, py + 5)
                    click(hwnd, pos)
                    continue

                points = get_match_points(src_img, self.duihua_zhandou_img)
                if points:
                    px, py = points[0]
                    pos = (px + 40, py + 5)
                    click(hwnd, pos)
                    continue

                # ??????????????????
                points = get_match_points(src_img, self.press_kongbaiguanbi_img)
                if points:
                    px, py = points[0]
                    pos = (px + 30, py + 5)
                    click(hwnd, pos, 50, 5)
                    continue

                # ??????????????????
                points = get_match_points(src_img, self.button_close_jianyi_img, threshold=0.98)
                if points:
                    pos = points[0]
                    click(hwnd, pos)
                    continue

                # ??????????????????
                src_img_color = capture(hwnd, color=cv2.IMREAD_COLOR)
                points = get_match_points(src_img_color, self.button_close_img_color, threshold=0.95)
                if points:
                    px, py = points[0]
                    pos = (px + 7, py + 7)
                    click(hwnd, pos)
                    continue

                points = get_match_points(src_img, self.in_battle_img)
                if points:
                    continue

                time.sleep(1)
                src_img2 = capture(hwnd)
                points = get_match_points(src_img2, self.in_battle_img)
                if points:
                    continue

                points = get_match_points(src_img, src_img2, threshold=0.8)
                if points:
                    time.sleep(1)
                    src_img3 = capture(hwnd)
                    points = get_match_points(src_img3, self.in_battle_img)
                    if points:
                        continue

                    points = get_match_points(src_img2, src_img3, threshold=0.8)
                    if points:
                        points = get_match_points(src_img3, self.button_beibao_img)
                        if not points:
                            print("????????????")
                            for i in range(5):
                                pos = (190, 280)
                                click(hwnd, pos)
                                time.sleep(random.uniform(0.2, 0.3))

    def run_caiji(self):
        num_standing = 0
        while True:
            if num_standing >= 5:
                src_img = capture(hwnd)
                # ??????????????????
                points = get_match_points(src_img, self.duihua_duihua_img)
                if points:
                    print("???????????????")
                    px, py = points[0]
                    pos = (px + 40, py + 5)
                    click(hwnd, pos)
                    num_standing = 0
                    continue
                points = get_match_points(src_img, self.duihua_likai_img)
                if points:
                    print("???????????????")
                    px, py = points[0]
                    pos = (px + 40, py + 5)
                    click(hwnd, pos)
                    num_standing = 0
                    continue
                return

            for hwnd in self.hwnd_list:
                time.sleep(random.uniform(settings.inverval_min, settings.inverval_max))
                src_img = capture(hwnd)
                points = get_match_points(src_img, self.button_jixu_img)
                if points:
                    print("?????????")
                    px, py = points[0]
                    pos = (px + 30, py + 5)
                    click(hwnd, pos)
                    continue

                points = get_match_points(src_img, self.button_shiyong_img)
                if points:
                    print("?????????")
                    px, py = points[0]
                    pos = (px + 30, py + 5)
                    click(hwnd, pos)
                    continue

                status = self.get_status(hwnd, src_img)
                print(status)
                if status != "standing":
                    num_standing = 0
                else:
                    num_standing += 1

    def run_zidong_queding(self):
        while True:
            for hwnd in self.hwnd_list:
                time.sleep(random.uniform(settings.inverval_min, settings.inverval_max))
                src_img = capture(hwnd)
                points = get_match_points(src_img, self.button_paiwei_img)
                if points:
                    print("??????????????????")
                    px, py = points[0]
                    pos = (px + 30, py + 10)
                    click(hwnd, pos)
                    continue

                points = get_match_points(src_img, self.button_queding_paiwei_img)
                if points:
                    print("????????????????????????")
                    px, py = points[0]
                    pos = (px + 50, py + 10)
                    click(hwnd, pos)
                    continue

                # 30?????????????????????????????????????????????????????????
                # points = get_match_points(src_img, self.button_daoju_img)
                # if points:
                #     pos = (814, 445)
                #     click(hwnd, pos)
                #     continue


if __name__ == '__main__':
    task = Task([67206])
    task.run_xiayi()
