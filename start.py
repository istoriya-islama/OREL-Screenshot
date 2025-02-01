import flet as ft
import random
import os

def main(page: ft.Page):
    page.title = "Закпуск Скриншот 2.0"
    page.theme_mode = "dark"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_height = '257'
    page.window_width = '394'

    def theme(e):
        page.theme_mode = "light" if page.theme_mode == "dark" else "dark"
        page.update()

    def startProgram(e):
        os.system("python main.py")
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.SUNNY, on_click=theme),
                ft.Text(f"OREL\t\t{random.randint(100, 999)}")
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [
                ft.Text("Не закрывайте камандную страку!!!")
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row([
            ft.ElevatedButton(text="Запуск", on_click=startProgram)
        ], alignment=ft.MainAxisAlignment.CENTER)
    )

ft.app(target=main)