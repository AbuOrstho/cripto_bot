import json
import aiohttp
import asyncio


class LBank:
    def __init__(self):
        # Загрузка данных из файла конфигурации
        self.web_data = json.load(
            open(r'C:\\Users\susur\OneDrive\Рабочий стол\Турпал Крипта\cripto\url_lib.json', 'r',
                 encoding="UTF-8"))  # Укажите правильный путь к файлу
        self.base_url = self.web_data["LBank"]["url"]

        # Создание списка URL и их соответствующих ключей
        self.url_keys = {
            self.web_data["LBank"]["all_tickers"]: "all_tickers",
            self.web_data["LBank"]["all_name_tickers"]: "all_name_tickers",
            self.web_data["LBank"]["commission"]: "commission"
        }
        self.urls = list(self.url_keys.keys())

    async def fetch(self, session, url):
        """Асинхронный запрос к URL."""
        async with session.get(url) as response:
            print(f"Запрос к {url} завершен с кодом: {response.status}")
            data = await response.text()
            # Использование ключа для создания имени файла
            key = self.url_keys[url]
            filename = f"LBank\\response_{key}.json"
            with open(filename, 'w', encoding="UTF-8") as file:
                file.write(data)
                print(f"Данные сохранены в {filename}")
            return data

    async def fetch_all(self):
        """Асинхронное выполнение всех запросов."""
        async with aiohttp.ClientSession() as session:
            tasks = [self.fetch(session, url) for url in self.urls]
            await asyncio.gather(*tasks)

    async def run(self):
        """Запуск асинхронной задачи."""
        await self.fetch_all()

    # Использование класса для выполнения запросов и сохранения результатов
lbank = LBank()