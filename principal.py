import flet as ft 
import bottomSheet


def main(page: ft.Page):
    def bott(e):
        page.overlay.append(bs)
        bs.open = True
        page.update()
    def bann(e):
        page.overlay.append(bn1)
        bn1.open = True
        page.update()
    def ban(e):
        bn1.open = False
        page.update()

    def alerta(e):
        adl.open = True
        page.update()
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
    adl = ft.AlertDialog(
        title=ft.Text(value='Titulo'),
        content=ft.Text(value='conteudo')
    )
    bn1 = ft.Banner(
        content=ft.Text(value='Banner 1'),
        actions=[
            ft.ElevatedButton(text='banner 01', on_click=ban)
        ]
    )
    tabs = ft.Tabs(
        tabs=[
            ft.Tab(
                text='Alarme De Aviso',
                content=ft.Container(
                    content=ft.Column(controls=[ft.ElevatedButton(text='Açâo', on_click=alerta)])
                )
            ),
            ft.Tab(
                text='Banner',
                content=ft.Container(
                    content=ft.Column(controls=[ft.ElevatedButton(text='Açâo',on_click=bann)])
                )
            ),
            ft.Tab(
                text='BottomSheet',
                content=ft.Container(
                    content=ft.Column(controls=[ft.ElevatedButton(text='Açâo',on_click=bott)])
                )
            )
        ]
    )
    page.overlay.append(adl)
   
    page.add(tabs)

if __name__ == '__main__':
    ft.app(main)