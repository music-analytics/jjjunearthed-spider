from scrapy import cmdline
from JJJUnearthed import File

File.delete_content("artists.json")
cmdline.execute("scrapy runspider JJJUnearthed/spiders/JJJUnearthedSpider.py -t json -o artists.json".split())
