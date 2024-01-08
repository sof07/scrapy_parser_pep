import scrapy


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        all_peps = response.css('a[href^="pep-"]')
        for group in all_peps:
            yield response.follow(group, callback=self.parse_group)

    def parse_group(self, response):
        pep_title = response.css('h1.page-title::text').get()
        pep_number, pep_name = pep_title.split('–', 1)
        yield {'num': pep_number.replace('PEP', '').strip(),
               'name': pep_name.strip(),
               'status': response.css('abbr::text').get()}
