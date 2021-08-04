import psutil
import win32gui
import cv2
import win32ui
import win32con
import win32api
import time
import random
import numpy as np
import ctypes
import pyautogui

from etc import settings


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def window_enumeration_handler(hwnd, result_list):
    """
    Pass to win32gui.EnumWindows() to generate list of window handle,
    window text, window class tuples.
    """
    hwnd_title = win32gui.GetWindowText(hwnd)
    if hwnd_title == settings.hwnd_title and len(result_list) < 5:
        result_list.append(hwnd)


def kill_proc_tree(pid, including_parent=True):
    parent = psutil.Process(pid)
    children = parent.children(recursive=True)
    for child in children:
        child.kill()
    gone, still_alive = psutil.wait_procs(children, timeout=5)
    if including_parent:
        parent.kill()
        parent.wait(5)


# 前台窗口截屏
def capture(hwnd, color=cv2.COLOR_BGR2GRAY):
    left, top, right, bot = win32gui.GetWindowRect(hwnd)
    w = right - left
    h = bot - top
    hwin = win32gui.GetDesktopWindow()
    hwndDC = win32gui.GetWindowDC(hwin)
    srcDC = win32ui.CreateDCFromHandle(hwndDC)
    memDC = srcDC.CreateCompatibleDC()
    bmp = win32ui.CreateBitmap()
    bmp.CreateCompatibleBitmap(srcDC, w, h)
    memDC.SelectObject(bmp)
    memDC.BitBlt((0, 0), (w, h), srcDC, (left, top), win32con.SRCCOPY)

    signedIntsArray = bmp.GetBitmapBits(True)
    img = np.fromstring(signedIntsArray, dtype='uint8')
    img.shape = (h, w, 4)

    srcDC.DeleteDC()
    memDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, hwndDC)
    win32gui.DeleteObject(bmp.GetHandle())

    src_img = cv2.cvtColor(img, color)
    return src_img


# 前台鼠标点击，提供相对坐标
def click(hwnd, client_pos, randint_x_max=5, randint_y_max=5):
    randint_x = random.randint(0, randint_x_max)
    randint_y = random.randint(0, randint_y_max)
    left, top, right, bot = win32gui.GetWindowRect(hwnd)
    pyautogui.click(left + client_pos[0] + randint_x, top + client_pos[1] + randint_y)
    """
    print("click:{},{}".format(left + client_pos[0] + randint_x, top + client_pos[1] + randint_y))
    win32api.SetCursorPos([left + client_pos[0] + randint_x, top + client_pos[1] + randint_y])
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    time.sleep(random.uniform(0.07, 0.08))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    """


def get_match_points(src_img, template_img, threshold=0.9):
    res = cv2.matchTemplate(src_img, template_img, cv2.TM_CCOEFF_NORMED)
    points = []
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        points.append(pt)
    return points


def get_clean_points(point_list, reverse=False):
    clean_point_list = []
    for point in point_list:
        x, y = point
        is_clean = True
        for clean_point in clean_point_list:
            cx, cy = clean_point
            if abs(x - cx) <= 5 and abs(y - cy) <= 5:
                is_clean = False
                break
        if is_clean:
            clean_point_list.append(point)
    if reverse:
        clean_point_list.reverse()
    return clean_point_list

"""
# 后台窗口截屏
def window_capture(hwnd, color=cv2.COLOR_BGR2GRAY):
    left, top, right, bot = win32gui.GetWindowRect(hwnd)
    w = right - left
    h = bot - top
    hwndDC = win32gui.GetWindowDC(hwnd)
    srcDC = win32ui.CreateDCFromHandle(hwndDC)
    memDC = srcDC.CreateCompatibleDC()
    bmp = win32ui.CreateBitmap()
    bmp.CreateCompatibleBitmap(srcDC, w, h)
    memDC.SelectObject(bmp)
    memDC.BitBlt((0, 0), (w, h), srcDC, (0, 0), win32con.SRCCOPY)

    signedIntsArray = bmp.GetBitmapBits(True)
    img = np.fromstring(signedIntsArray, dtype='uint8')
    img.shape = (h, w, 4)

    srcDC.DeleteDC()
    memDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, hwndDC)
    win32gui.DeleteObject(bmp.GetHandle())

    src_img = cv2.cvtColor(img, color)
    return src_img
"""

"""
# 后台鼠标点击，提供相对坐标
def window_click(hwnd, client_pos, randint_x_max=5, randint_y_max=5):
    randint_x = random.randint(0, randint_x_max)
    randint_y = random.randint(0, randint_y_max)
    tmp = win32api.MAKELONG(client_pos[0] + randint_x, client_pos[1] + randint_y)
    win32gui.SendMessage(hwnd, win32con.WM_ACTIVATE, win32con.WA_ACTIVE, 0)
    win32gui.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, tmp)
    time.sleep(random.uniform(0.07, 0.08))
    win32gui.SendMessage(hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, tmp)
"""

"""
# 后台鼠标点击，提供相对坐标
def window_press(hwnd, key=win32con.VK_SPACE):
    #win32gui.PostMessage(hwnd, win32con.WM_ACTIVATE, win32con.WA_ACTIVE, 0)
    win32gui.PostMessage(hwnd, win32con.WM_KEYDOWN, key, 0)
    time.sleep(random.uniform(0.18, 0.22))
    win32gui.PostMessage(hwnd, win32con.WM_KEYUP, key, 0)
"""