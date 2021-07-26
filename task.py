from datetime import datetime

from utils.base import *
from utils.wechat import senddata


class Task:
    def __init__(self, hwnd_list):
        self.hwnd_list = hwnd_list
        self.button_xiayi_img = cv2.cvtColor(cv2.imread("images/button_xiayi.png"), cv2.COLOR_BGR2GRAY)
        self.button_shenqing_img = cv2.cvtColor(cv2.imread("images/button_shenqing.png"), cv2.COLOR_BGR2GRAY)
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
        self.duihua_zhandou_img = cv2.cvtColor(cv2.imread("images/duihua_zhandou.png"), cv2.COLOR_BGR2GRAY)
        self.button_paiwei_img = cv2.cvtColor(cv2.imread("images/button_paiwei.png"), cv2.COLOR_BGR2GRAY)
        self.button_queding_paiwei_img = cv2.cvtColor(cv2.imread("images/button_queding_paiwei.png"), cv2.COLOR_BGR2GRAY)
        self.duihua_zhenmo_end_img = cv2.cvtColor(cv2.imread("images/duihua_zhenmo_end.png"), cv2.COLOR_BGR2GRAY)
        self.button_tongyirudui_img = cv2.cvtColor(cv2.imread("images/button_tongyirudui.png"),cv2.COLOR_BGR2GRAY)

        self.button_close_img_color = cv2.cvtColor(cv2.imread("images/button_close.png"), cv2.IMREAD_COLOR)
        self.icon_duiwu_shenqing1_img_color = cv2.cvtColor(cv2.imread("images/icon_duiwu_shenqing1.png"),
                                                           cv2.IMREAD_COLOR)
        self.icon_duiwu_shenqing2_img_color = cv2.cvtColor(cv2.imread("images/icon_duiwu_shenqing2.png"),
                                                           cv2.IMREAD_COLOR)

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

        # # 赏金，点开始任务
        # points = get_match_points(src_img, self.button_kaishirenwu_img)
        # if points:
        #     px, py = points[0]
        #     pos = (px + 30, py + 5)
        #     click(hwnd, pos, 50, 10)
        #     return "click_kaishirenwu"

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

        # # 30秒到时间，会自动挂智能技能，不要点自动
        # points = get_match_points(src_img, self.button_daoju_img)
        # if points:
        #     # pos = (814, 445)
        #     # click(hwnd, pos)
        #     return "in_battle"

        # 匹配状态
        points = get_match_points(src_img, self.button_duiwu_pipei_img)
        if points:
            return "waiting_pipei"

        points = get_match_points(src_img, self.duihua_likai_img, threshold=0.85)
        if points:
            print("对话选项")
            return "standing"

        # 关闭侠义窗口
        src_img_color = capture(hwnd, color=cv2.IMREAD_COLOR)
        points = get_match_points(src_img_color, self.button_close_img_color, threshold=0.95)
        if points:
            px, py = points[0]
            pos = (px + 7, py + 7)
            click(hwnd, pos)
            return "close_window"

        # 有人申请加入队伍，队伍收缩
        points = get_match_points(src_img_color, self.icon_duiwu_shenqing1_img_color)
        if points:
            # 展开任务栏,也有可能是正在匹配
            print("展开任务栏")
            pos = (837, 229)
            click(hwnd, pos)
            return "zhankai_duiwulan"

        # 有人申请加入队伍，队伍栏已展开
        points = get_match_points(src_img_color, self.icon_duiwu_shenqing2_img_color)
        if points:
            print("有人申请加入队伍")
            src_img = capture(hwnd)
            points = get_match_points(src_img, self.button_renwu_img, threshold=0.96)
            if points:
                print("点两下，打开队伍")
                # 点开队伍,点两下
                pos = (838, 172)
                click(hwnd, pos)
                time.sleep(random.uniform(0.4, 0.6))
                click(hwnd, pos)
            else:
                points = get_match_points(src_img, self.button_duiwu_img, threshold=0.96)
                if points:
                    print("点一下，打开队伍")
                    # 点开队伍,点一下
                    pos = (838, 172)
                    click(hwnd, pos)
                else:
                    print("未能发现队伍按钮")
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
                    pos = (172, 266)
                    click(hwnd, pos, 30, 30)
                    print("跳过对话")
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
                # 未知对话，点
                points = get_match_points(src_img, self.duihua_duihua_img)
                if points:
                    print("点未知对话")
                    px, py = points[0]
                    pos = (px + 40, py + 5)
                    click(hwnd, pos)
                    continue

                # 在野外挂机
                points = get_match_points(src_img, self.button_renwu_img, threshold=0.96)
                if points:
                    print("点两下，打开队伍")
                    # 点开队伍,点两下
                    pos = (838, 172)
                    click(hwnd, pos)
                    time.sleep(random.uniform(0.4, 0.6))
                    click(hwnd, pos)
                else:
                    points = get_match_points(src_img, self.button_duiwu_img, threshold=0.96)
                    if points:
                        print("点一下，打开队伍")
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
                points = get_match_points(src_img, self.button_buzhen_img)
                if not points:
                    # 切换至队伍界面
                    pos = (754, 107)
                    click(hwnd, pos, 10, 10)
                    time.sleep(random.uniform(1.0, 1.2))
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
                        else:
                            # 满员，继续等待
                            continue

                # 侠义button
                pos = (825, 379)
                click(hwnd, pos)
                time.sleep(random.uniform(1.0, 1.2))
                src_img = capture(hwnd)
                # 申请
                points = get_match_points(src_img, self.button_shenqing_img)
                if points:
                    points = get_clean_points(points)
                    for i in range(3):
                        try:
                            px, py = points[i]
                        except:
                            break
                        pos = (px + 30, py + 10)
                        click(hwnd, pos)
                        time.sleep(random.uniform(0.15, 0.2))

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

            status = self.get_status(hwnd)
            print(status)
            if status != "standing":
                num_standing = 0
                continue
            else:
                num_standing += 1

            src_img = capture(hwnd)

            points = get_match_points(src_img, self.duihua_zhenmo_end_img,threshold=0.85)
            if points:
                print("镇魔次数已用尽")
                #return
                senddata("镇魔次数已用尽，但仍开始新的一轮:{}".format(str(datetime.now())), "")
                continue

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
