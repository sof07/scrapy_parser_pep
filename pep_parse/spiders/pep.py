import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        section_tag = response.css('section[id="numerical-index"]')
        tbody_tag = section_tag.css('tbody')
        href_tags = tbody_tag.css('a::attr(href)').getall()
        for href in href_tags:
            url = href + '/'
            yield response.follow(url, callback=self.parse_pep)

    def parse_pep(self, response):
        pep_title = response.css('h1.page-title::text').get()
        pep_number, pep_name = pep_title.split('–', 1)
        data = {'number': pep_number.replace('PEP', '').strip(),
                'name': pep_name.strip(),
                'status': response.css('abbr::text').get()}
        yield PepParseItem(data)
