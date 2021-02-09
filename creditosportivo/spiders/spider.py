import re

import scrapy
from scrapy.exceptions import CloseSpider

from scrapy.loader import ItemLoader
from ..items import CreditosportivoItem
from itemloaders.processors import TakeFirst


class CreditosportivoSpider(scrapy.Spider):
	name = 'creditosportivo'
	start_urls = ['https://www.creditosportivo.it/stampa-e-comunicazione/news/']
	page = 1

	def parse(self, response):
		post_links = response.xpath('//article/a/@href').getall()
		yield from response.follow_all(post_links, self.parse_post)

		self.page += 1
		next_page = f'https://www.creditosportivo.it/stampa-e-comunicazione/news/page/{self.page}/'

		if not post_links:
			raise CloseSpider('no more pages')

		yield response.follow(next_page, self.parse)

	def parse_post(self, response):
		title = response.xpath('//h2[@class="title-header"]/text()').get()
		description = response.xpath('//div[@class="post_the_content"]//text()').getall()
		description = [p.strip() for p in description]
		description = ' '.join(description).strip()
		date = response.xpath('//div[@class="post_date"]/time/text()').get()

		item = ItemLoader(item=CreditosportivoItem(), response=response)
		item.default_output_processor = TakeFirst()
		item.add_value('title', title)
		item.add_value('description', description)
		item.add_value('date', date)

		return item.load_item()
