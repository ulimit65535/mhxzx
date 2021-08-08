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
        self.window_shanghang_img = cv2.cvtColor(cv2.imread("images/window_shanghang.png"), cv2.COLOR_BGR2GRAY)

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

        # 在战斗准备状态
        points = get_match_points(src_img_color, self.button_daoju_img_color)
        if points:
            # 在战斗准备状态
            print("战斗准备状态，无法获取队伍人数")
            return None

        points = get_match_points(src_img_color, self.button_renwu_img_color, threshold=0.96)
        if points:
            # 切换至队伍显示
            print("切换至队伍显示")
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
                # 展开任务栏
                print("展开任务栏")
                pos = (837, 229)
                click(hwnd, pos)
                time.sleep(random.uniform(1.0, 1.2))
                src_img_color = capture(hwnd, color=cv2.IMREAD_COLOR)
                points = get_match_points(src_img_color, self.button_renwu_img_color, threshold=0.96)
                if points:
                    # 切换至队伍显示
                    print("切换至队伍显示")
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
                            print("不在队伍中")
                            num = 0
        if num:
            print("当前队伍人数:{}".format(num))
        return num

    def open_window_huodong(self, hwnd, src_img=None):
        if src_img is None:
            src_img = capture(hwnd)
        for i in range(3):
            points = get_match_points(src_img, self.button_beibao_img)
            if points:
                # 点击活动
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

        # 点击空白关闭
        points = get_match_points(src_img, self.press_kongbaiguanbi_img)
        if points:
            px, py = points[0]
            pos = (px + 30, py + 5)
            click(hwnd, pos, 50, 5)
            return "press_kongbaiguanbi"

        # 关闭建议弹窗
        points = get_match_points(src_img, self.button_close_jianyi_img, threshold=0.98)
        if points:
            pos = points[0]
            click(hwnd, pos)
            return "close_window_jianyi"

        # # 接取任务
        # points = get_match_points(src_img, self.duihua_jiequ_img)
        # if points:
        #     px, py = points[0]
        #     pos = (px + 40, py + 5)
        #     click(hwnd, pos)
        #     return "click_jiequrenwu"
        #
        # # 点击确定
        # points = get_match_points(src_img, self.button_queding_img)
        # if points:
        #     px, py = points[0]
        #     pos = (px + 40, py + 10)
        #     click(hwnd, pos)
        #     return "click_queding"

        # 30秒到时间，会自动挂智能技能，不要点自动
        points = get_match_points(src_img, self.button_daoju_img)
        if points:
            # pos = (814, 445)
            # click(hwnd, pos)
            return "in_battle"

        # 商行界面，等待
        points = get_match_points(src_img, self.window_shanghang_img)
        if points:
            return "standing"

        # 匹配状态
        points = get_match_points(src_img, self.button_duiwu_pipei_img)
        if points:
            return "waiting_pipei"

        # 点战斗
        points = get_match_points(src_img, self.duihua_zhandou_img)
        if points:
            px, py = points[0]
            pos = (px + 40, py + 5)
            click(hwnd, pos)
            return "click_battle"

        # 话本、仙师。点前往挑战
        points = get_match_points(src_img, self.button_qianwangtiaozhan_img)
        if not points:
            points = get_match_points(src_img, self.button_qianwangtiaozhan2_img)
        if points:
            print("点前往挑战")
            px, py = points[0]
            pos = (px + 50, py + 15)
            click(hwnd, pos)
            return "click_qianwangtiaozhan"

        points = get_match_points(src_img, self.duihua_duihua_img)
        if not points:
            points = get_match_points(src_img, self.duihua_duihua2_img)
        if points:
            print("对话选项，get_status不做操作")
            return "standing"

        # 继续挑战，点确定
        points = get_match_points(src_img, self.button_quxiao_img)
        if points:
            print("点确定")
            px, py = points[0]
            pos = (px + 230, py + 15)
            click(hwnd, pos)
            return "click_queding"

        # 关闭一些窗口
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
        # 有人申请加入队伍，队伍收缩
        points = get_match_points(opponent_img_color, self.icon_duiwu_shenqing1_img_color)
        if points:
            # 展开任务栏,也有可能是正在匹配
            print("展开任务栏")
            pos = (837, 229)
            click(hwnd, pos)
            return "zhankai_duiwulan"

        # 有人申请加入队伍，队伍栏已展开
        points = get_match_points(opponent_img_color, self.icon_duiwu_shenqing2_img_color)
        if points:
            print("有人申请加入队伍")
            points = get_match_points(src_img, self.button_renwu_img, threshold=0.96)
            if not points:
                points = get_match_points(src_img, self.button_duiwu_img, threshold=0.96)
            if points:
                print("点一下，打开队伍")
                # 点开队伍,点一下
                pos = (838, 172)
                click(hwnd, pos)
            else:
                print("任务栏未展开")
                return "error"

            # 允许加入队伍
            time.sleep(random.uniform(0.8, 1.2))
            src_img = capture(hwnd)
            points = get_match_points(src_img, self.button_tongyirudui_img)
            points = get_clean_points(points)
            if points:
                print("点同意入队")
                px, py = points[0]
                pos = (px + 30, py + 5)
                click(hwnd, pos)
                time.sleep(random.uniform(0.4, 0.6))
                # 点清空列表
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
                    print("跳过对话")
                    for i in range(5):
                        pos = (190, 280)
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
                # # 点击确定
                # points = get_match_points(src_img, self.button_queding_img)
                # if points:
                #     print("点击确定")
                #     px, py = points[0]
                #     pos = (px + 40, py + 10)
                #     click(hwnd, pos)
                #     continue

                # 特殊场景，直接退出
                points = get_match_points(src_img, self.button_tuichu_img, threshold=0.88)
                if points:
                    print("退出特殊场景")
                    px, py = points[0]
                    pos = (px + 10, py + 20)
                    click(hwnd, pos)
                    # 等3s，点确定
                    time.sleep(random.uniform(3.5, 4.0))
                    pos = (498, 329)
                    click(hwnd, pos, 30, 10)
                    continue

                # 未知对话，点
                points = get_match_points(src_img, self.duihua_duihua_img)
                if points:
                    print("点未知对话")
                    px, py = points[0]
                    pos = (px + 40, py + 5)
                    click(hwnd, pos)
                    continue

                num = self.get_members_num(hwnd)
                if num is None:
                    print("无法获取队伍人数，继续等待")
                    continue
                else:
                    # 人不满，离开队伍
                    if num == 0:
                        print("不在队伍中，打开侠义窗口")
                        pos = (825, 379)
                        click(hwnd, pos)
                        time.sleep(random.uniform(1.0, 1.2))
                        src_img = capture(hwnd)
                        # 申请
                        points = get_match_points(src_img, self.icon_xingxiazhangyi_img)
                        if not points:
                            time.sleep(random.uniform(1.0, 1.2))
                            # 点刷新
                            pos = (713, 442)
                            click(hwnd, pos, 25, 10)
                            time.sleep(random.uniform(1.0, 1.2))
                            src_img = capture(hwnd)
                            points = get_match_points(src_img, self.icon_xingxiazhangyi_img)
                        if points:
                            print("点击申请")
                            points = get_clean_points(points, reverse=True)
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
                        print("点一下，打开队伍")
                        # 点开队伍,点一下
                        pos = (838, 172)
                        click(hwnd, pos)
                        # 等待队伍界面打开
                        time.sleep(random.uniform(1.0, 1.2))
                        src_img = capture(hwnd)
                        points = get_match_points(src_img, self.button_likaiduiwu_img)
                        if points:
                            print("离开队伍")
                            px, py = points[0]
                            # 退出队伍
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
                            print("未能找到离开队伍按钮")
                            continue
                    else:
                        print("队伍满员，继续等待")
                        continue

    def run_yitiao_single(self):
        num_standing = 0
        while True:
            if num_standing >= 5:
                src_img = capture(hwnd)
                # 未知对话，点
                points = get_match_points(src_img, self.duihua_duihua_img)
                if points:
                    print("点未知对话")
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
                # 点前往参与
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
                print("60s未进战斗")
                return
            if num_standing >= 5:
                src_img = capture(hwnd)
                # 未知对话，点
                points = get_match_points(src_img, self.duihua_duihua_img)
                if points:
                    print("点未知对话")
                    px, py = points[0]
                    pos = (px + 40, py + 5)
                    click(hwnd, pos)
                    num_standing = 0
                    continue
                # 点地图
                pos = (36, 28)
                click(hwnd, pos, 25, 25)
                time.sleep(random.uniform(1.0, 1.2))
                # 点世界
                pos = (74, 156)
                click(hwnd, pos, 50, 5)
                time.sleep(random.uniform(1.0, 1.2))
                # 点河阳
                pos = (437, 239)
                click(hwnd, pos, 20, 20)
                time.sleep(random.uniform(1.0, 1.2))
                # 点镇魔令
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
                    # 新的一场战斗，查看队伍中的人数
                    if is_new_battle:
                        is_new_battle = False
                        num = self.get_members_num(hwnd)
                        if num:
                            if num_members is None:
                                num_members = num
                            print("之前队伍人数:{}".format(num_members))
                            print("当前队伍人数:{}".format(num))
                            if num < num_members:
                                print("队伍人数减少，发送通知")
                                senddata("队伍人数减少，当前队伍人数:{}".format(num), "")
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
                print("镇魔次数已用尽")
                return
                #senddata("镇魔次数已用尽，但仍开始新的一轮:{}".format(str(datetime.now())), "")

            # 接取任务
            points = get_match_points(src_img, self.duihua_jiequ_img)
            if points:
                px, py = points[0]
                pos = (px + 40, py + 5)
                click(hwnd, pos)
                continue

            points = get_match_points(src_img, self.duihua_jitianxia_img)
            if points:
                print("与计天下对话")
                px, py = points[0]
                pos = (px + 40, py + 5)
                click(hwnd, pos)
                time.sleep(random.uniform(1.0, 1.2))
                continue

            points = get_match_points(src_img, self.duihua_queding_img)
            if points:
                print("点确定")
                px, py = points[0]
                pos = (px + 40, py + 5)
                click(hwnd, pos)
                continue

    def run_xianshi(self, hwnd):
        num_err = 0
        while True:
            if num_err >= 3:
                print("打开活动窗口失败次数过多，结束")
                return

            time.sleep(random.uniform(1.0, 1.2))

            src_img = capture(hwnd)

            status = self.get_status(hwnd)
            print(status)
            if status != "standing":
                continue

            # 点击前往
            points = get_match_points(src_img, self.duihua2_qianwang_img)
            if points:
                print("点前往")
                px, py = points[0]
                pos = (px + 40, py + 5)
                click(hwnd, pos)
                continue

            # 人数不满，确认攻击
            points = get_match_points(src_img, self.duihua_queren_img)
            if points:
                print("点确认")
                px, py = points[0]
                pos = (px + 40, py + 5)
                click(hwnd, pos)
                continue

            result = self.open_window_huodong(hwnd, src_img)
            if result:
                num_err = 0
            else:
                num_err += 1
                print("打开活动窗口失败")
                continue

            time.sleep(random.uniform(settings.inverval_min, settings.inverval_max))

            src_img = capture(hwnd)
            points = get_match_points(src_img, self.title_xianshishilian_img)
            if not points:
                print("未找到子活动窗口，仙师试炼结束.")
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
                # 点击前往
                x, y = points[0]
                px = x + left
                py = y + top
                pos = (px + 30, py + 10)
                click(hwnd, pos)
                continue
            else:
                print("未找到前往按钮，仙师试炼已结束.")
                return

    def run_jingying(self, hwnd):
        num_err = 0
        while True:
            if num_err >= 3:
                print("打开活动窗口失败次数过多，结束")
                return

            time.sleep(random.uniform(settings.inverval_min, settings.inverval_max))

            src_img = capture(hwnd)

            status = self.get_status(hwnd)
            print(status)
            if status != "standing":
                continue

            # # 点击前往
            # points = get_match_points(src_img, self.duihua2_qianwang_img)
            # if points:
            #     print("点前往")
            #     px, py = points[0]
            #     pos = (px + 40, py + 5)
            #     click(hwnd, pos)
            #     continue

            # # 人数不满，确认攻击
            # points = get_match_points(src_img, self.duihua_queren_img)
            # if points:
            #     print("点确认")
            #     px, py = points[0]
            #     pos = (px + 40, py + 5)
            #     click(hwnd, pos)
            #     continue

            # 发起挑战
            points = get_match_points(src_img, self.button_faqitiaozhan_img)
            if points:
                print("点发起挑战")
                px, py = points[0]
                pos = (px + 60, py + 10)
                click(hwnd, pos)
                continue

            result = self.open_window_huodong(hwnd, src_img)
            if result:
                num_err = 0
            else:
                num_err += 1
                print("打开活动窗口失败")
                continue

            time.sleep(random.uniform(1.0, 1.2))

            src_img = capture(hwnd)
            points = get_match_points(src_img, self.title_jingyingjudian_img)
            if not points:
                print("未找到子活动窗口，精英据点结束.")
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
                # 点击前往
                x, y = points[0]
                px = x + left
                py = y + top
                pos = (px + 30, py + 10)
                click(hwnd, pos)
                continue
            else:
                print("未找到前往按钮，精英据点已结束.")
                return

    def run_zudui_yitiao(self):
        hwnd = self.hwnd_list[0]
        num_standing = 0
        while True:
            if num_standing >= 10:
                print("等待时间过长，开始仙师试炼、精英挑战")
                self.run_xianshi(hwnd)
                self.run_jingying(hwnd)
                print("组队一条结束")
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

            # 赏金，点开始任务
            points = get_match_points(src_img, self.button_kaishirenwu_img)
            if points:
                print("赏金，开始任务")
                px, py = points[0]
                pos = (px + 30, py + 5)
                click(hwnd, pos, 50, 10)
                continue

            # 接取任务
            points = get_match_points(src_img, self.duihua_jiequ_img)
            if points:
                print("点接取任务")
                px, py = points[0]
                pos = (px + 40, py + 5)
                click(hwnd, pos)
                continue

            # 点前往参与
            points = get_match_points(src_img, self.duihua_qianwangcanyu_img)
            if points:
                print("点前往参与")
                px, py = points[0]
                pos = (px + 40, py + 5)
                click(hwnd, pos)
                continue

            points = get_match_points(src_img, self.duihua_jitianxia_img)
            if points:
                print("与计天下对话")
                px, py = points[0]
                pos = (px + 40, py + 5)
                click(hwnd, pos)
                time.sleep(random.uniform(1.0, 1.2))
                continue

            points = get_match_points(src_img, self.duihua_queding_img)
            if points:
                print("点确定")
                px, py = points[0]
                pos = (px + 40, py + 5)
                click(hwnd, pos)
                continue

    def run_zhuxian(self):
        while True:
            for hwnd in self.hwnd_list:
                time.sleep(random.uniform(settings.inverval_min, settings.inverval_max))

                src_img = capture(hwnd)

                # 30秒到时间，会自动挂智能技能，不要点自动
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

                # 点击空白关闭
                points = get_match_points(src_img, self.press_kongbaiguanbi_img)
                if points:
                    px, py = points[0]
                    pos = (px + 30, py + 5)
                    click(hwnd, pos, 50, 5)
                    continue

                # 关闭建议弹窗
                points = get_match_points(src_img, self.button_close_jianyi_img, threshold=0.98)
                if points:
                    pos = points[0]
                    click(hwnd, pos)
                    continue

                # 关闭一些窗口
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
                            print("跳过对话")
                            for i in range(5):
                                pos = (190, 280)
                                click(hwnd, pos)
                                time.sleep(random.uniform(0.2, 0.3))

    def run_caiji(self):
        num_standing = 0
        while True:
            if num_standing >= 5:
                src_img = capture(hwnd)
                # 未知对话，点
                points = get_match_points(src_img, self.duihua_duihua_img)
                if points:
                    print("点未知对话")
                    px, py = points[0]
                    pos = (px + 40, py + 5)
                    click(hwnd, pos)
                    num_standing = 0
                    continue
                points = get_match_points(src_img, self.duihua_likai_img)
                if points:
                    print("点未知对话")
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
                    print("点继续")
                    px, py = points[0]
                    pos = (px + 30, py + 5)
                    click(hwnd, pos)
                    continue

                points = get_match_points(src_img, self.button_shiyong_img)
                if points:
                    print("点使用")
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
                    print("点确定或匹配")
                    px, py = points[0]
                    pos = (px + 30, py + 10)
                    click(hwnd, pos)
                    continue

                points = get_match_points(src_img, self.button_queding_paiwei_img)
                if points:
                    print("队长匹配，点确定")
                    px, py = points[0]
                    pos = (px + 50, py + 10)
                    click(hwnd, pos)
                    continue

                # 30秒到时间，会自动挂智能技能，不要点自动
                # points = get_match_points(src_img, self.button_daoju_img)
                # if points:
                #     pos = (814, 445)
                #     click(hwnd, pos)
                #     continue


if __name__ == '__main__':
    task = Task([67206])
    task.run_xiayi()
