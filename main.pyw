import threading
import subprocess
import win32process

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
from multiprocessing import Process

from utils.base import *
from utils.wechat import senddata
from task import Task


def run_task(hwnd_list, task_name):
    task = Task(hwnd_list)
    print(task_name)
    hwnd = hwnd_list[0]
    if task_name == "刷侠义":
        task.run_xiayi()
    elif task_name == "单人一条":
        task.run_yitiao_single()
    elif task_name == "无限镇魔":
        task.run_wuxianzhenmo()
    elif task_name == "采集":
        task.run_caiji()
    elif task_name == "自动确定":
        task.run_zidong_queding()
    elif task_name == "组队一条":
        task.run_zudui_yitiao()
    elif task_name == "自动主线":
        task.run_zhuxian()
    elif task_name == "仙师试炼":
        task.run_xianshi(hwnd)
    elif task_name == "精英据点":
        task.run_jingying(hwnd)


class AppUI:
    def __init__(self):
        self.hwnd_main_list = []
        self.hwnd_list = []

        self.process = None
        self.subprocess = None

        self.running = None

        #self.hwnd_order_asc = True

        root = Tk()

        lf1 = ttk.Frame(root)
        lf1.pack(side=LEFT, fill=X, anchor=NW, padx=5, pady=5)

        lf1_0 = ttk.Frame(lf1)
        lf1_0.pack(side=TOP, fill=Y)

        lf1_1 = ttk.LabelFrame(lf1_0, text="启动")
        lf1_1.pack(side=LEFT, anchor=NW, fill=Y, padx=5, pady=5)

        lf1_2 = ttk.LabelFrame(lf1_0, text="功能")
        lf1_2.pack(side=RIGHT, anchor=NW, fill=Y, padx=5, pady=5)

        lf1_3 = ttk.Frame(lf1)
        lf1_3.pack(side=TOP, fill=Y, padx=5, pady=5)

        self.msg_list = Text(lf1_3, width=42, height=22)
        self.msg_list.pack(side=LEFT, fill=Y)
        self.msg_list.tag_config('important', foreground='blue')
        self.msg_list.tag_config('warning', foreground='red')
        scroll = Scrollbar(lf1_3)
        self.msg_list.configure(yscrollcommand=scroll.set)
        scroll.pack(side=RIGHT, fill=Y)

        lf2 = ttk.Frame(root)
        lf2.pack(side=LEFT, fill=X, anchor=NE, padx=5, pady=5)

        lf2_0 = ttk.LabelFrame(lf2, text="单人任务")
        lf2_0.pack(side=TOP, fill=Y, padx=5, pady=5)

        lf2_3 = ttk.LabelFrame(lf2, text="组队任务")
        lf2_3.pack(side=TOP, fill=Y, padx=5, pady=5)

        lf2_2 = ttk.LabelFrame(lf2, text="一条")
        lf2_2.pack(side=TOP, fill=Y, padx=5, pady=5)

        self.single_task = StringVar()
        self.cbx_single_target = ttk.Combobox(lf2_0, textvariable=self.single_task, width=6, state='readonly')
        self.cbx_single_target["values"] = ("刷侠义", "单人一条", "自动确定", "自动主线")
        self.cbx_single_target.current(0)
        self.cbx_single_target.pack(side=TOP, padx=2, pady=2, fill=X)

        self.btn_single_task = ttk.Button(lf2_0, text="开始任务", state=DISABLED, command=self.run_single_task)
        self.btn_single_task.pack(side=TOP, padx=2, pady=2, fill=X)

        self.team_task = StringVar()
        self.cbx_team_task = ttk.Combobox(lf2_3, textvariable=self.team_task, width=6, state='readonly')
        self.cbx_team_task["values"] = ("无限镇魔", "组队一条", "仙师试炼", "精英据点")
        self.cbx_team_task.current(0)
        self.cbx_team_task.pack(side=TOP, padx=2, pady=2, fill=X)

        self.btn_team_task = ttk.Button(lf2_3, text="开始任务", state=DISABLED, command=self.run_team_task)
        self.btn_team_task.pack(side=TOP, padx=2, pady=2, fill=X)

        frame1 = Frame(lf1_1)
        frame1.pack(fill=X, side=TOP, padx=5, pady=5)

        self.btn_open = ttk.Button(frame1, text="三开", width=6, command=self.open)
        self.btn_start = ttk.Button(frame1, text="开始", width=6, command=self.start)
        self.btn_close = ttk.Button(frame1, text="强关", width=6, command=self.close)
        self.btn_open.pack(side=LEFT, padx=2, fill=X)
        self.btn_start.pack(side=LEFT, padx=2, fill=X)
        self.btn_close.pack(side=LEFT, padx=2, fill=X)

        frame2 = Frame(lf1_2)
        frame2.pack(fill=X, side=TOP, padx=5, pady=5)

        # self.btn_baoshi = ttk.Button(frame2, text="饱食", width=6, state=DISABLED, command=self.test)
        # self.btn_zudui = ttk.Button(frame2, text="组队", width=6, state=DISABLED, command=self.test)
        # self.btn_baoshi.pack(side=LEFT, padx=2, fill=X)
        # self.btn_zudui.pack(side=LEFT, padx=2, fill=X)
        self.is_shutdown = BooleanVar()
        self.cbx_shutdown = ttk.Checkbutton(frame2, text="结束关机", variable=self.is_shutdown)
        self.cbx_shutdown.pack(side=LEFT, padx=2, fill=X)

        self.btn_task1 = ttk.Button(lf2_2, text="验证一条", state=DISABLED, command=self.test)
        self.btn_task2 = ttk.Button(lf2_2, text="无验证一条", state=DISABLED, command=self.test)
        self.btn_sichou = ttk.Button(lf2_2, text="暂无", state=DISABLED, command=self.test)
        self.btn_shilian = ttk.Button(lf2_2, text="暂无", state=DISABLED, command=self.test)
        self.btn_renwulian = ttk.Button(lf2_2, text="暂无", state=DISABLED, command=self.test)
        self.btn_task1.pack(side=TOP, padx=2, pady=2, fill=X)
        self.btn_task2.pack(side=TOP, padx=2, pady=2, fill=X)

        root.title("工作报告.xlsx - Excel")
        root.update()
        root.resizable(False, False)

        width = root.winfo_width()
        height = root.winfo_height()

        size = '%dx%d+%d+%d' % (width, height, 280, 560)
        root.geometry(size)

        monitor = threading.Thread(target=self.monitor_process)
        monitor.setDaemon(True)
        monitor.start()

        root.mainloop()

    def monitor_process(self):
        while True:
            if self.process or self.subprocess:
                # 已有任务开启
                while True:
                    time.sleep(1)
                    if self.process:
                        if self.process.is_alive():
                            continue
                    if self.subprocess:
                        if self.subprocess.poll() is None:
                            continue

                    # 恢复按键状态
                    self.btn_single_task.state(['!pressed', '!disabled'])
                    self.btn_team_task.state(['!pressed', '!disabled'])

                    if self.process:
                        self.process.terminate()
                        self.process = None

                    if self.subprocess:
                        try:
                            kill_proc_tree(self.subprocess.pid)
                        except:
                            pass
                        self.subprocess = None

                    if self.running:
                        self.msg_list.insert(END, "{}已结束。\n结束时间:{}\n".format(self.running, str(datetime.now())),
                                             'warning')
                        self.msg_list.see("end")
                        if self.running not in ["组队离队", ""]:
                            if self.is_shutdown.get():
                                # 关机
                                for hwnd in self.hwnd_main_list:
                                    _id = win32process.GetWindowThreadProcessId(hwnd)
                                    handle = win32api.OpenProcess(1, False, _id[1])
                                    win32api.TerminateProcess(handle, -1)
                                subprocess.Popen("shutdown -s -t 60", shell=True)
                            else:
                                senddata("{}已结束。结束时间:{}".format(self.running, str(datetime.now())), "")
                    else:
                        # 自己手动关闭的，不用发送通知
                        self.msg_list.insert(END, "任务已被强制结束。\n结束时间:{}\n".format(str(datetime.now())), 'warning')
                        self.msg_list.see("end")
                    break
            else:
                # 任务未开启
                time.sleep(1)
                continue

    def start(self):
        # print(self.is_shutdown.get())
        if self.running:
            if self.process:
                self.process.terminate()
                self.process = None
            if self.subprocess:
                try:
                    kill_proc_tree(self.subprocess.pid)
                except:
                    pass
                self.subprocess = None

        self.hwnd_main_list = []
        self.hwnd_list = []

        self.running = None

        #if not self.hwnd_main_list:
        # 获取主窗口句柄
        win32gui.EnumWindows(window_enumeration_handler, self.hwnd_main_list)
        self.hwnd_main_list.sort(reverse=True)
        if self.hwnd_main_list:
            for i in range(len(self.hwnd_main_list)):
                x, y = settings.coordinate_list[i]
                hwnd_main = self.hwnd_main_list[i]
                win32gui.MoveWindow(hwnd_main, x, y, settings.width, settings.height, False)
                # 查找子窗口句柄
                hwnd_child_list = []
                win32gui.EnumChildWindows(hwnd_main, lambda hwnd_c, param: param.append(hwnd_c), hwnd_child_list)
                try:
                    hwnd = hwnd_child_list[0]
                    self.hwnd_list.append(hwnd)
                    self.msg_list.insert(END, "窗口{}句柄:{}\n".format(i + 1, hwnd))
                except:
                    self.msg_list.insert(END, "主窗口{}:未发现子窗口\n".format(i + 1), 'warning')

        self.msg_list.see("end")

        self.btn_start.config(text="重置")
        self.btn_open.state(['!pressed', '!disabled'])
        self.btn_close.state(['!pressed', '!disabled'])
        self.btn_single_task.state(['!pressed', '!disabled'])
        self.btn_team_task.state(['!pressed', '!disabled'])

    def open(self):
        #self.hwnd_main_list = []
        cmd = settings.launcher
        for i in range(3):
            subprocess.Popen(cmd, shell=True)
            for j in range(5):
                time.sleep(1)
                hwnd_main_list = []
                win32gui.EnumWindows(window_enumeration_handler, hwnd_main_list)
                if len(hwnd_main_list) >= i + 1:
                    # for hwnd in hwnd_main_list:
                    #     if hwnd not in self.hwnd_main_list:
                    #         self.hwnd_main_list.append(hwnd)
                    break
        #print(self.hwnd_main_list)

    def close(self):
        if messagebox.askyesno('提示', "是否强制关闭所有游戏程序?"):
            for hwnd in self.hwnd_main_list:
                _id = win32process.GetWindowThreadProcessId(hwnd)
                handle = win32api.OpenProcess(1, False, _id[1])
                win32api.TerminateProcess(handle, -1)
            self.msg_list.insert(END, "游戏进程已关闭。\n关闭时间:{}\n".format(str(datetime.now())),
                                'warning')
            self.msg_list.see("end")

    def test(self):
        pass

    def run_single_task(self):
        self.running = self.single_task.get()
        self.btn_single_task.state(['pressed', 'disabled'])
        self.btn_team_task.state(['!pressed', 'disabled'])
        self.process = Process(target=run_task,
                          args=(self.hwnd_list, self.running))
        self.process.daemon = True
        self.process.start()
        """
        for hwnd in self.hwnd_list:
            process = Process(target=run_task,
                              args=(hwnd, self.running))
            process.daemon = True
            process.start()
            self.process_list.append(process)
        """
    def run_team_task(self):
        self.running = self.team_task.get()
        self.btn_single_task.state(['!pressed', 'disabled'])
        self.btn_team_task.state(['pressed', 'disabled'])
        self.process = Process(target=run_task,
                          args=(self.hwnd_list, self.running))
        self.process.daemon = True
        self.process.start()


if __name__ == "__main__":
    # 需要管理员权限
    if not is_admin():
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    else:
        AppUI()
