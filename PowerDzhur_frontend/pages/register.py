import flet as ft
import httpx

def register(page: ft.Page,content: ft.Column):
    # Зберігаємо кожне поле в змінну
    name_field = ft.TextField(width=400, text_align=ft.TextAlign.CENTER)
    surname_field = ft.TextField(width=400, text_align=ft.TextAlign.CENTER)
    email_field = ft.TextField(width=400, text_align=ft.TextAlign.CENTER)
    phone_field = ft.TextField(width=400, text_align=ft.TextAlign.CENTER)

    def show_success_message(msg_text):
        page.snack_bar = ft.SnackBar(
            content=ft.Text(msg_text, color="black"),
            bgcolor="#4CAF50",  # Яскравий зелений
            duration=3000,  # 3 секунди
            show_close_icon=False,
            behavior=ft.SnackBarBehavior.FLOATING
        )
        page.snack_bar.open = True
        page.update()

    def show_error_message(msg_text):
        page.snack_bar = ft.SnackBar(
            content=ft.Text(msg_text, color="black"),
            bgcolor="#FF5252",  # Яскравий червоний
            duration=3000,  # 3 секунди
            show_close_icon=False,
            behavior=ft.SnackBarBehavior.FLOATING
        )
        page.snack_bar.open = True
        page.update()

    # Обробник кнопки підтвердження
    def on_submit(e):
        print("sigma")
        data = {
            "name": name_field.value,
            "surname": surname_field.value,
            "email": email_field.value,
            "phone": phone_field.value,
        }
        try:
            print("http negr")
            response = httpx.post("http://127.0.0.1:8000/register", json=data)
            print(f"Response status code: {response.status_code}")
            print(f"Response text: {response.text}")
            if response.status_code == 200:
                show_success_message("Реєстрація успішна!")
                print("zaebon")
            else:
                show_error_message(f"Помилка реєстрації: {response.status_code} - {response.text}")
                print("pizda")
        except httpx.RequestError as e:
            show_error_message(f"Помилка мережі: {e}")
            print("boomer")
        except Exception as e:
            show_error_message(f"Невідома помилка: {e}")
            print("ebat suka")

        page.update()

    # Очищаємо контент
    content.controls.clear()

    # Додаємо все з полями
    content.controls.append(
        ft.Column([
            ft.Text("Реєстрація", size=36, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),

            ft.Row(
                controls=[ft.Icon(ft.Icons.ACCOUNT_CIRCLE, size=100)],
                alignment=ft.MainAxisAlignment.CENTER
            ),

            ft.Row([name_field, ft.Text("Вкажіть ім'я", width=150, text_align=ft.TextAlign.CENTER)]),
            ft.Row([surname_field, ft.Text("Вкажіть фамілію", width=150, text_align=ft.TextAlign.CENTER)]),
            ft.Row([email_field, ft.Text("Вкажіть email", width=150, text_align=ft.TextAlign.CENTER)]),
            ft.Row([phone_field, ft.Text("Вкажіть номер телефону", width=150, text_align=ft.TextAlign.CENTER)]),

            ft.ElevatedButton(
                "Підтвердити",
                width=150,
                bgcolor="#4CAF50",
                color=ft.Colors.BLACK,
                on_click=on_submit
            )
        ],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        )
    )

    page.update()

    return ft.View(
        "/register",
        [ft.AppBar(title=ft.Text("Реєстрація"), bgcolor=ft.Colors.ON_SURFACE_VARIANT), content]
    )