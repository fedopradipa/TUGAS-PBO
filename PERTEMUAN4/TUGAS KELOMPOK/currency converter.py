from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.scrollview import ScrollView


class KonverterMataUangApp(MDApp):
    def build(self):
        self.screen = Screen()

        self.item_menu_mata_uang = [
            {"text": "Rupiah"},
            {"text": "Dolar Amerika"},
            {"text": "Euro"},
        ]
        self.menu_mata_uang = MDDropdownMenu(
            caller=self.screen,
            items=self.item_menu_mata_uang,
            position="center",
            width_mult=4,
        )
        self.menu_mata_uang.bind(on_release=self.on_pilih_mata_uang)

        self.mata_uang_terpilih = MDTextField(
            hint_text="Mata Uang Terpilih",
            size_hint=(0.8, 0.1),
            pos_hint={"center_x": 0.5, "center_y": 0.6},
            halign="center",
            on_focus=self.tampilkan_menu_mata_uang,
        )
        self.screen.add_widget(self.mata_uang_terpilih)

        self.jumlah_dolar = MDTextField(
            hint_text="Masukkan jumlah dalam USD",
            size_hint=(0.8, 0.1),
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            halign="center",
            input_filter="float"
        )
        self.screen.add_widget(self.jumlah_dolar)

        self.tombol_konversi = MDRectangleFlatButton(
            text="Konversi",
            size_hint=(0.8, 0.1),
            pos_hint={"center_x": 0.5, "center_y": 0.4},
            on_release=self.konversi
        )
        self.screen.add_widget(self.tombol_konversi)

        self.hasil_konversi = MDLabel(
            text="",
            halign="center",
            theme_text_color="Secondary",
            size_hint_y=None,
            height=self.screen.height * 0.5
        )
        self.screen.add_widget(self.hasil_konversi)

        self.scrollview = ScrollView()
        self.scrollview.add_widget(self.screen)

        return self.scrollview

    def tampilkan_menu_mata_uang(self, instance_textfield, value):
        if value:
            self.menu_mata_uang.open()

    def on_pilih_mata_uang(self, instance_menu, instance_menu_item):
        self.mata_uang_terpilih.text = instance_menu_item.text
        self.menu_mata_uang.dismiss()

    def konversi(self, instance):
        jumlah = self.jumlah_dolar.text
        mata_uang = self.mata_uang_terpilih.text

        try:
            jumlah = float(jumlah)
            kurs_konversi = {
                "Rupiah": 15.701,  # kurs Rupiah
                "Dolar Amerika": 1,
                "Euro": 0.93,  # kurs untuk Euro
            }

            if mata_uang in kurs_konversi:
                nilai_konversi = jumlah * kurs_konversi[mata_uang]
                nilai_konversi = "{:,.2f}".format(nilai_konversi)
                self.hasil_konversi.text = f"{jumlah} USD = {nilai_konversi} {mata_uang}"
            else:
                self.hasil_konversi.text = "Mata uang tidak valid"
        except ValueError:
            self.hasil_konversi.text = "Masukkan jumlah yang valid"


if __name__ == "__main__":
    KonverterMataUangApp().run()
