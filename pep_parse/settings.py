BOT_NAME = 'pep_parse'

SPIDER_MODULES = ['pep_parse.spiders']
NEWSPIDER_MODULE = 'pep_parse.spiders'

ROBOTSTXT_OBEY = True
FEEDS = {
    # Имя файла для сохранения данных теперь указываем здесь,
    # а не при вызове паука из консоли.
    'results/pep_%(time)s.csv': {
        # Формат файла.
        'format': 'csv',
        # Поля, данные из которых будут выведены в файл, и их порядок.
        # Выведем в этот файл только два поля из трёх.
        'fields': ['number', 'name', 'status'],
        # Если файл с заданным именем уже существует, то
        # при значении False данные будут дописываться в существующий файл;
        # при значении True существующий файл будет перезаписан.
        'overwrite': True
    },
    # # И ещё один файл.
    # 'status_summary_.csv': {
    #     'format': 'csv',
    #     # В этот файл попадёт только список авторов.
    #     'fields': ['author'],
    #     'overwrite': True
    # },
}
ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
