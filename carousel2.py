import flet as ft 


def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.colors.WHITE

    def move_D(e):
        cariousel.scroll_to(delta=-100, duration=300, curve=ft.AnimationCurve.DECELERATE)
        cariousel.update()

    def move_S(e):
        cariousel.scroll_to(delta=100, duration=300,curve=ft.AnimationCurve.DECELERATE)
        cariousel.update()

    layout = ft.Container(
        shadow=ft.BoxShadow(blur_radius=100),
        content=ft.Column(
            controls=[
                cariousel := ft.Row(
                    scroll=ft.ScrollMode.HIDDEN,
                    controls=[
                        ft.Image(
                            src= f'https://picsum.photos/250/300?{num}'
                        )for num in range(10)
                    ]
                ),
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.IconButton(icon=ft.icons.KEYBOARD_ARROW_LEFT, on_click=move_D, icon_color=ft.colors.ORANGE_900),
                        ft.IconButton(icon=ft.icons.KEYBOARD_ARROW_RIGHT, on_click=move_S, icon_color=ft.colors.ORANGE_900)
                    ]
                )
            ]
        )
    )

    page.add(layout)

if __name__ == '__main__':
    ft.app(main)