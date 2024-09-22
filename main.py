import flet as ft
import random
import cv2
import pyautogui
import numpy as np

def main(page: ft.Page):
    page.title = "Скриншот 1.1"
    page.theme_mode = "dark"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_height = '241'
    page.window_width = '394'

    texts = ft.Text("Скриншота нету")
    textv = ft.Text("\t\t\t\t\t\t\t\t\t\t\t\t\t     Видео: нажмите на кнопку, \n а что-бы закончить видео закройте программу")
    def video(e):
        videoname = f"C:/Users/istor/OneDrive/Работен плот/video→{random.randint(0, 10000)}.avi"
        screnSize = (1366, 768)
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter(videoname, fourcc, 30.0, (screnSize))
        while True:
            img = pyautogui.screenshot()
            frame = np.array(img)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            out.write(frame)
            if cv2.waitKey(1) == ord('q'):
                break
        cv2.destroyAllWindows()
        out.release()
        page.update()
    def scr(e):
        scre = pyautogui.screenshot()
        scre.save(f'C:/Users/istor/OneDrive/Работен плот/screenshot→{random.randint(0, 10000)}.png')
        texts.value = "Скриншот есть он находится на Рабочем \n столе по именим → 'screenshot(1 и тд).png'"
        page.update()
    def theme(e):
        page.theme_mode = "light" if page.theme_mode == "dark" else "dark"
        page.update()
    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.SUNNY, on_click=theme),
                ft.Text("OREL Скриншот 1.1")
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row([texts], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([textv], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([
            ft.ElevatedButton(text="Сделать скриншот", on_click=scr),
            ft.ElevatedButton(text="Сделать видео", on_click=video)
                ], alignment=ft.MainAxisAlignment.CENTER)
    )


ft.app(target=main)