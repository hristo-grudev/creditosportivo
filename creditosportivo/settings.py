BOT_NAME = 'creditosportivo'

SPIDER_MODULES = ['creditosportivo.spiders']
NEWSPIDER_MODULE = 'creditosportivo.spiders'
FEED_EXPORT_ENCODING = 'utf-8'
LOG_LEVEL = 'ERROR'
DOWNLOAD_DELAY = 0

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
	'creditosportivo.pipelines.CreditosportivoPipeline': 100,

}