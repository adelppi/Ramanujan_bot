from icrawler.builtin import GoogleImageCrawler

def imageCrawler(cmdInput):
    search_word = cmdInput

    crawler = GoogleImageCrawler(storage = {"root_dir" : "./images"})
    crawler.crawl(keyword = search_word, max_num = 1)