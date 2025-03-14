import scrapy
import time

class RedditTariffsSpider(scrapy.Spider):
    name = "reddit_tariffs"
    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (compatible; MyScraper/1.0)"
    }
    

    start_urls = ["https://www.reddit.com/r/canada/search.json?q=tariffs&restrict_sr=1"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.search_start_time = time.time()
        self.articles_start_time = None
        self.articles = []

    def parse(self, response):

        search_end_time = time.time()
        self.logger.info("Time to fetch search results: {:.2f} seconds".format(search_end_time - self.search_start_time))
        
        data = response.json()

        posts = data["data"]["children"][:10]
        

        for post in posts:
            post_data = post["data"]
            title = post_data.get("title", "No Title")
            permalink = post_data.get("permalink", "")

            post_url = "https://www.reddit.com" + permalink
            json_url = post_url + ".json"
            

            yield scrapy.Request(
                url=json_url,
                callback=self.parse_post,
                meta={'title': title, 'post_url': post_url}
            )
        

        self.articles_start_time = time.time()

    def parse_post(self, response):

        json_response = response.json()

        detailed_post = json_response[0]["data"]["children"][0]["data"]
        selftext = detailed_post.get("selftext", "")
        title = response.meta.get("title", "No Title")
        post_url = response.meta.get("post_url", "")
        
        self.articles.append({
            "title": title,
            "url": post_url,
            "selftext": selftext
        })
        

        if len(self.articles) == 10:
            articles_end_time = time.time()
            self.logger.info("Time to fetch article details: {:.2f} seconds".format(articles_end_time - self.articles_start_time))
            total_time = articles_end_time - self.search_start_time
            self.logger.info("Total time for scraping process: {:.2f} seconds".format(total_time))
            
            self.logger.info("Scraped Articles:")
            for article in self.articles:
                self.logger.info("Title: %s", article["title"])
                self.logger.info("URL: %s", article["url"])
                excerpt = article["selftext"][:300] if article["selftext"] else "No selftext"
                self.logger.info("Selftext excerpt: %s", excerpt)
                self.logger.info("-" * 80)
