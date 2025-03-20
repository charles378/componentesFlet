import flet as ft


def main(page: ft.Page):
    bs = ft.BottomSheet(
        content=ft.Container(
            ft.Column(
                controls=[
                    ft.Text(value='Titulo', style=ft.TextThemeStyle.HEADLINE_LARGE),
                    ft.Text(value='conteúdo do bottomsheet', style=ft.TextThemeStyle.HEADLINE_MEDIUM),
                    ft.FilledButton(text='fechar'),
                ]
            ),
            padding=20,
        )
        
    )
    page.overlay.append(bs)
    bs.open = True
    page.update()

if __name__ == '__main__':
    ft.app(main)