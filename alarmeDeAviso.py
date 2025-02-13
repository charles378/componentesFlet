import flet as ft


def main(page: ft.Page):

    ad1 = ft.AlertDialog(
        title=ft.Text('Aviso importate'), # o titulo da mensagem
        content=ft.Text(value='voce está prestes a deletar os dado '), # a mensagem
        content_padding=ft.padding.all(30),  # espasamanto imterno do aviso
        inset_padding=ft.padding.all(10),  # espasamento do alame na paginA
        modal=False,  # false click fora do aviso fecha True nao fecha
        shape=ft.RoundedRectangleBorder(radius=5),  # redodar a borda do aviso
        on_dismiss=lambda _: print('fechei'),  # fusao para click fora do aviso

        actions=[  # para adisionar um botao no alarne
            ft.TextButton('Cancerlar', style=ft.ButtonStyle(color=ft.colors.RED)),
            ft.ElevatedButton('Salvar', style=ft.ButtonStyle(bgcolor=ft.colors.GREEN, color=ft.colors.WHITE)),
        ],
        actions_alignment=ft.MainAxisAlignment.END # para alinhar os botães
    )

    def open_ad(e):
        page.overlay.append(ad1)
        ad1.open = True
        page.update()

    btn1 = ft.ElevatedButton('abri', on_click=open_ad)

    page.add(btn1)


if __name__ == '__main__':
    ft.app(main)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
