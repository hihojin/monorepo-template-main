# -*- coding: utf-8 -*-


class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

class Brie(object):
    def __init__(self, item:Item):
        self.item = item
    
    def update_item(self):
        self.item.sell_in -= 1
        self.item.quality += 1
        # max quality of brie is 50
        if self.item.quality > 50:
            self.item.quality = 50

class Sulfuras(object):
    def __init__(self, item:Item):
        self.item = item

    def update_item(self):
        '''
        no update in quality needed nor sellin(number of days) value
        '''
        self.quality_validation()

    def quality_validation(self):
        # validation
        if self.item.quality != 80:
            self.item.quality = 80 # resetting to 80
            #raise ValueError('Sulfuras legendary item quality should not alter from 80')

class Backstage_Pass_Concert(object):
    def __init__(self, item:Item):
        self.item = item
    
    def update_item(self):
        self.item.sell_in -= 1

        if self.item.sell_in > 10:
            self.item.quality += 1
        elif self.item.sell_in > 5:
            self.item.quality += 2
        elif self.item.sell_in >= 0: # 0 <= x <= 5
            self.item.quality += 3
        else: # passed concert day
            self.item.quality = 0
        
        if self.item.quality > 50:
            self.item.quality = 50

class NormalItem(object):
    def __init__(self, item:Item):
        self.item = item
        self.normal_degradation = 1
        self.over_sell_in_degradation = self.normal_degradation * 2

    def update_item(self):
        self.item.sell_in -= 1

        if self.item.sell_in >= 0:
            self.item.quality -= self.normal_degradation
        else:
            self.item.quality -= self.over_sell_in_degradation

        if self.item.quality < 0:
            self.item.quality = 0

class Conjured(object):
    def __init__(self, item:Item):
        self.item = item
        self.degradation = 1 * 2 # twice as fast as normal items
    
    def update_item(self):
        self.item.sell_in -= 1
        if self.item.sell_in >= 0:
            self.item.quality -= self.degradation
        else: # when passed sell in date
            self.item.quality -= self.degradation * 2
        
        if self.item.quality < 0:
            self.item.quality = 0


class GildedRose(object):

    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items

    def update_quality(self):
        '''
        code refactoring - polymorphism 
        MIN_QUALITY = 0
        MAZ_QUALITY = 50 (excluding sulfuras=80)
        1.customized_items: brie, concert, sulfuras, conjured
        2.normal items
        '''
        for item in self.items:
            if item.name == 'Aged Brie':
                # create new brie object, call its update function
                Brie(item).update_item()
            elif item.name == 'Sulfuras, Hand of Ragnaros': # quality is fixed at 80, no need to sell
                Sulfuras(item).update_item()
            elif item.name == 'Backstage passes to a TAFKAL80ETC concert':
                Backstage_Pass_Concert(item).update_item()
            elif item.name == 'Conjured Mana Cake':
                Conjured(item).update_item()
            else: # normal items
                NormalItem(item).update_item()

            # if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
            #     if item.quality > 0: # min quality
            #         if item.name != "Sulfuras, Hand of Ragnaros":
            #             item.quality = item.quality - 1
            # else: # brie / Backstage passes to a TAFKAL80ETC concert
            #     if item.quality < 50: # max quality
            #         item.quality = item.quality + 1
            #         if item.name == "Backstage passes to a TAFKAL80ETC concert":
            #             if item.sell_in < 11:
            #                 if item.quality < 50:
            #                     item.quality = item.quality + 1
            #             if item.sell_in < 6:
            #                 if item.quality < 50:
            #                     item.quality = item.quality + 1
            # if item.name != "Sulfuras, Hand of Ragnaros":
            #     item.sell_in = item.sell_in - 1
            # if item.sell_in < 0:
            #     if item.name != "Aged Brie":
            #         if item.name != "Backstage passes to a TAFKAL80ETC concert":
            #             if item.quality > 0:
            #                 if item.name != "Sulfuras, Hand of Ragnaros":
            #                     item.quality = item.quality - 1
            #         else:
            #             item.quality = item.quality - item.quality
            #     else:
            #         if item.quality < 50:
            #             item.quality = item.quality + 1
