from scraper.scrape import Scrape
import pprint
pprint = pprint.PrettyPrinter(indent=4).pprint
scraper = Scrape()
res = scraper.scrape_devfolio()
pprint(res)

