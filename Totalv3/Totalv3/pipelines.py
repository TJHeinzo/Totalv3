# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv


class Totalv3Pipeline:
    def open_spider(self, spider):
        # Prep a csv file to write to. Write the headers
        self.myFile = open("wines.csv", "w", newline="")
        self.csv_writer = csv.DictWriter(
            self.myFile,
            fieldnames=["sku", "name", "size", "price", "product_url", "image_url"],
        )
        self.csv_writer.writeheader()

    def close_spider(self, spider):
        # Close the csv file
        self.myFile.close()

    def process_item(self, item, spider):
        # Cleanse data and write to csv
        item["name"] = self.trimYear(item["name"])
        # item["price"] = self.processPrice(item["price"])
        self.csv_writer.writerow(item)
        return item

    # Removes the vintage from a wines name if it has one
    def trimYear(self, name):
        if "," in name:
            return name[: name.index(",")]
        else:
            return name

    # Remove $ and ,
    def processPrice(self, price):
        price = price.replace(",", "")
        return price.replace("$", "")
