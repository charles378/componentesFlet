import flet as ft


def main(page: ft.Page):
    def can(e):
        adl.open = False
        page.update()

    def ok(e):
        adl.open = False
        page.add(ft.Text(value='CONFIMAÇAO OK', color=ft.colors.GREEN))
        

    adl= ft.AlertDialog(
        title=ft.Text(value='Teste'),
        content=ft.Text(value='conteudo'),
        #content_padding=ft.padding.all(20)
        modal=True,
        actions=[
            ft.ElevatedButton(text='ook', on_click=ok),
            ft.TextButton(text='cancelar', on_click=can)
        ]
    )
    
    def bo(e):
        page.overlay.append(adl)
        adl.open = True
        page.update()

    page.add( ft.ElevatedButton(text='botao', on_click=bo))

if __name__ == '__main__':
    ft.app(main)