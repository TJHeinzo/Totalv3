import scrapy

""" SCRAPY SHELL COPY PASTAS:
    Open shell with spoofed user agent:
        scrapy shell -s USER_AGENT='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0' 'https://www.totalwine.com/wine/c/c0020?viewall=true&pageSize=120&aty=1,1,0,0&instock=1'
"""


class Totalv3(scrapy.Spider):

    name = "total"
    start_urls = [
        "https://www.totalwine.com/wine/c/c0020?viewall=true&pageSize=24&aty=1,1,0,0&instock=1"
    ]
    pageNum = 1

    # PARSES THE MAIN PAGE WITH ALL 120 ITEMS ON IT
    def parse(self, response):
        # Output raw HTML to file
        with open(f"Raw HTML/total{self.pageNum}.html", "w") as f:
            f.write(response.text)

        # Loop through all the product links on the page
        for product in response.css("article.productCard__2nWxIKmi"):
            yield response.follow(
                "https://www.totalwine.com" + product.xpath(".//h2/a/@href").get(),
                callback=self.parseProductPage,
            )

        # Find number of pages
        maxPage = int(
            response.css('a[data-at="product-search-pagination-link"]::text').getall()[
                -1
            ]
        )

        # If there are more pages, go to the next page
        self.pageNum += 1
        if False:  # self.pageNum <= maxPage:
            yield response.follow(
                f"https://www.totalwine.com/wine/c/c0020?viewall=true&page={self.pageNum}&pageSize=120&aty=1,1,0,0&instock=1",
                callback=self.parse,
            )

    # PARSES THE PRODUCT PAGES
    def parseProductPage(self, response):

        # Output raw HTML to file
        with open(
            (
                "Raw HTML/product"
                + response.css("h1.productTitle__3XDd9UVh::text").get()
                + ".html"
            ),
            "w",
        ) as f:
            f.write(response.text)

        # Get the product data
        data = response.css("div.detailsTableText__1SvcRdYn::text").getall()
        yield {
            "sku": data[-1],
            "name": response.css("h1.productTitle__3XDd9UVh::text").get(),
            "size": response.css("span.productSubTitle__3sTXP-XD::text").get(),
            "price": response.css("div.priceTxt__xftcAqUk::text").get(),
            "product_url": response.url,
            "image_url": response.css(
                "img.ProductImagestyled__Img-shared-packages__x66sdz-1::attr(src)"
            ).get(),
        }
