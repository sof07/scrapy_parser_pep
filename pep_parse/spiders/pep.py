from urllib.parse import urljoin

import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        all_peps = response.css('a[href^="pep-"]')
        for group in all_peps:
            # Тут я не понял, вроде все нормально отрабатывает без /
            url_group = urljoin(response.url, group.attrib["href"])
            yield response.follow(url_group, callback=self.parse_pep)

    def parse_pep(self, response):
        pep_title = response.css('h1.page-title::text').get()
        # У меня все норм, сплитим по этому знаку: – (всю голову сломал, почему сплит
        # не работает, оказалось это длинный минус:))
        pep_number, pep_name = pep_title.split('–', 1)
        data = {'number': pep_number.replace('PEP', '').strip(),
                'name': pep_name.strip(),
                # Да, в подсказке так писано: 'dt:contains("Status") + dd::text'
                # Но зачем, если по тегу abbr текст можно достать?
                # Да и не работает у меня так, ничегоне находит
                'status': response.css('abbr::text').get()}
        yield PepParseItem(data)
