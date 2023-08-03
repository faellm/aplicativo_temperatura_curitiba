from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
import urllib.request
import json

class WeatherApp(App):

    def build(self):
        layout = BoxLayout(orientation='vertical')

        self.location_label = Label(text="Localização: ")
        layout.add_widget(self.location_label)

        self.temperature_label = Label(text="Temperatura: ")
        layout.add_widget(self.temperature_label)

        self.weather_label = Label(text="Condições climáticas: ")
        layout.add_widget(self.weather_label)

        self.wind_label = Label(text="Velocidade do vento: ")
        layout.add_widget(self.wind_label)

        self.get_weather_button = Button(text="Obter previsão do tempo", on_press=self.get_weather)
        layout.add_widget(self.get_weather_button)

        return layout

    def get_weather(self, instance):
        api_key = '806b0144b65e3f5f55af94246119d666'
        city_name = 'Curitiba'  # Substitua 'Cidade' pelo nome da cidade desejada.

        base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"

        try:
            with urllib.request.urlopen(base_url) as url:
                data = json.loads(url.read().decode())
                location = data['name']
                temperature_kelvin = data['main']['temp']
                temperature_celsius = temperature_kelvin - 273.15
                weather = data['weather'][0]['description']
                wind_speed = data['wind']['speed']

                self.location_label.text = f"Localização: {location}"
                self.temperature_label.text = f"Temperatura: {temperature_celsius:.2f}°C"
                self.weather_label.text = f"Condições climáticas: {weather}"
                self.wind_label.text = f"Velocidade do vento: {wind_speed} m/s"
        except urllib.error.HTTPError as e:
            self.location_label.text = "Falha ao obter dados da previsão do tempo."
            print(f"Erro HTTP: {e.code} - {e.reason}")
        except urllib.error.URLError as e:
            self.location_label.text = "Falha ao obter dados da previsão do tempo."
            print(f"Erro na URL: {e.reason}")
        except Exception as e:
            self.location_label.text = "Falha ao obter dados da previsão do tempo."
            print(f"Erro desconhecido: {e}")

if __name__ == '__main__':
    WeatherApp().run()