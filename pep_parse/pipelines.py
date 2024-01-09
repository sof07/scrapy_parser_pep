# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class PepParsePipeline:
    def open_spider(self, spider):
        self.count_status = {}

    def process_item(self, item, spider):
        self.count_status[item['status']] = self.count_status.get(
            item['status'], 0) + 1

        return item

    def close_spider(self, spider):
        with open('./pep.csv', mode='w', encoding='utf-8') as f:
            # Записываем строки в csv-файл. Колонки разделяются запятой, без пробелов.
            f.write('Статус,Количество\n')
            for key, value in self.count_status.items():
                f.write(f'{key},{value}\n')
            # Здесь цикл с записью данных в файл.
            f.write(f'Total,{sum(self.count_status.values())}\n')
