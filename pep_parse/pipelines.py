import datetime as dt
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
RESULT_DIR = 'results'
FILE_NAME = 'status_summary'
DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'


class PepParsePipeline:
    def open_spider(self, spider):
        self.count_status = {}

    def process_item(self, item, spider):
        self.count_status[item['status']] = self.count_status.get(
            item['status'], 0) + 1

        return item

    def close_spider(self, spider):
        now = dt.datetime.now()
        file_name = f'{FILE_NAME}_{now.strftime(DATETIME_FORMAT)}.csv'
        result = os.path.join(BASE_DIR, RESULT_DIR, file_name)
        with open(result, mode='w', encoding='utf-8') as f:
            f.write('Статус,Количество\n')
            for key, value in self.count_status.items():
                f.write(f'{key},{value}\n')
            f.write(f'Total,{sum(self.count_status.values())}\n')
