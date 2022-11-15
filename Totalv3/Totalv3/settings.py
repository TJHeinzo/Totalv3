# Scrapy settings for Totalv3 project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "Totalv3"

SPIDER_MODULES = ["Totalv3.spiders"]
NEWSPIDER_MODULE = "Totalv3.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0"
)
"""COOKIE = (
    "twm-userStoreInformation=ispStore~2201:ifcStore~null@ifcStoreState~US-NY@method~INSTORE_PICKUP; idm_guid=N92fb3723-ed8e-49e3-a2b4-6be5ed1f49c6; smcLastVisitTime=1; overrideStore=true; 2022Q2_BR=variant; forterToken=73d2aace593143a7be52ec873bd37c04_1668538732493_1520_UAL9_6; AMCV_F0DA403D53C3CA7B0A490D4C%40AdobeOrg=1176715910%7CMCIDTS%7C19312%7CMCMID%7C43857443245013583733986334427310735469%7CMCAID%7CNONE%7CMCOPTOUT-1668545933s%7CNONE%7CvVersion%7C5.4.0; _pxhd=; BVBRANDID=c8dab0b6-bd6f-4acd-b9c0-826ac40fd842; OptanonConsent=isGpcEnabled=1&datestamp=Tue+Nov+15+2022+13%3A58%3A54+GMT-0500+(Eastern+Standard+Time)&version=6.18.0&isIABGlobal=false&hosts=&consentId=e1f88910-0b10-4e73-8e3f-7a21c62da25c&interactionCount=2&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0004%3A0%2CC0005%3A0&AwaitingReconsent=false&geolocation=US%3BVA; OptanonAlertBoxClosed=2022-11-08T15:48:23.701Z; _pxvid=78a31fa7-5f7d-11ed-afd2-687077627667; rcs=eF4Nx7ENgDAMBMAmFbs8wklsvzdgDYuAREEHzA_XXSnPti6dylETe41EPxqREYFRTYRBMdfpeu9zzN4bxIzaXJ20fwTkA25PEMo; at_check=true; AMCVS_F0DA403D53C3CA7B0A490D4C%40AdobeOrg=1; rrSessionId=2d7c4f00-5b77-11ec-aa00-17b17c557489; JSESSIONID=Y64-12247bf1-3879-4b09-9263-f95f23030bd0.app-94drq; showLogoutMsg="
    "; loginAn="
    "; lastPage=https://www.totalwine.com/; locationCookie=User location; pxcts=78a32f28-5f7d-11ed-afd2-687077627667; mbox=session#6b241a389c0746c6a088f1b1048ad992#1668540594; BVBRANDSID=642c5d49-89c9-47da-9644-0535e394c197; _pxff_cc=U2FtZVNpdGU9TGF4Ow==; _px2=eyJ1IjoiODI1MGNiZTMtNjUxNy0xMWVkLWFhZGQtNjg3MzU5NTI0NTU3IiwidiI6Ijc4YTMxZmE3LTVmN2QtMTFlZC1hZmQyLTY4NzA3NzYyNzY2NyIsInQiOjE1NjE1MDcyMDAwMDAsImgiOiIzMGMxMmI3NGY4YjkyYTJjZTBmYWM2NmM5NWU1NTAxNGIyOWZlMzg3MzdmYWUxMjU2MmY0NDg2NGFmMWFjNjExIn0=; _pxff_rf=1; _pxff_fp=1"
)"""


# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'Totalv3.middlewares.Totalv3SpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'Totalv3.middlewares.Totalv3DownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    "Totalv3.pipelines.Totalv3Pipeline": 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
