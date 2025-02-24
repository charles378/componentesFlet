import flet as ft


def main(page: ft.Page):
    adl = ft.AlertDialog(
        title=ft.Text(value='Alerta '),
        content=ft.Text(value='Voce quer deletar os dados'),
        content_padding=ft.padding.all(20),
        inset_padding=ft.padding.all(10),
        shape=ft.RoundedRectangleBorder(radius=40),
        modal=False
    )
    page.dialog = adl
    adl.open = True
    page.update()

if __name__ == '__main__':
    ft.app(main)