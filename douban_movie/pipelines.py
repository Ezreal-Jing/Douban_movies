# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
#Pipeline的功能
#1.清洗数据
#2.验证数据的有效性
#3.过滤掉重复的数据
#4.将数据存入数据库

#将评价转换为星级
class Rating_Cov_Pipeline:#将评价等级转换为阿拉伯数字
    rating_map = {
        '很差': 1,
        '较差': 2,
        '还行': 3,
        '推荐': 4,
        '力荐': 5,
    }#构造映射字典
    def process_item(self, item, spider):
        item['rating'] = self.rating_map[item['rating']]#读取rating字段,将转换的结果赋值回rating字段
        return item
