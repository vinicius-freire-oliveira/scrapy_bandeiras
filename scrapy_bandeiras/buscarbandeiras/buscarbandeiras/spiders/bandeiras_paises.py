import scrapy

class BandeirasPaisesSpider(scrapy.Spider):
    name = 'bandeiras_paises'
    start_urls = ['https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_and_their_capitals_in_native_languages']

    def parse(self, response):
        tabelas = response.xpath('//table[contains(@class, "wikitable")]')
        
        for tabela in tabelas:
            for linha in tabela.xpath('.//tr')[1:]:
                pais = linha.xpath('.//td[1]//a/text()').get()
                bandeira = linha.xpath('.//td[1]//img/@src').get()
                if pais and bandeira:
                    yield {
                        'País': pais,
                        'Bandeira URL': response.urljoin(bandeira)
                    }
