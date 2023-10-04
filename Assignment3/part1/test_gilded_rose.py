# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self): # treating like a NORMAL ITEM
        items = [Item("foo", 0, 2)] # sellin, quality
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(0, items[0].quality) # degrades twice as fast after sell in date

        items = [Item("foo", 10, 0)] # min quality check
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(0, items[0].quality)
    
    def test_brie(self):
        item = [Item('Aged Brie', 2, 0)]
        gilded_rose = GildedRose(item)
        gilded_rose.update_quality()
        self.assertEqual(1, item[0].sell_in)
        self.assertEqual(1, item[0].quality)

        item = [Item('Aged Brie', 2, 50)]
        gilded_rose = GildedRose(item)
        gilded_rose.update_quality()
        self.assertEqual(50, item[0].quality)
    
    def test_Sulfuras(self):
        item = [Item("Sulfuras, Hand of Ragnaros", 0, 80)]
        gilded_rose = GildedRose(item)
        gilded_rose.update_quality()
        self.assertEqual(0, item[0].sell_in)
        self.assertEqual(80, item[0].quality)

        item = [Item("Sulfuras, Hand of Ragnaros", 0, 60)]
        gilded_rose = GildedRose(item)
        gilded_rose.update_quality()
        self.assertEqual(80, item[0].quality)
    
    def test_Backstage_Pass_Concert(self):
        more_than_10days = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20)]
        gilded_rose = GildedRose(more_than_10days)
        gilded_rose.update_quality()
        self.assertEqual(14, more_than_10days[0].sell_in)
        self.assertEqual(21, more_than_10days[0].quality)

        more_than_5days = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=45)]
        gilded_rose = GildedRose(more_than_5days)
        gilded_rose.update_quality()
        self.assertEqual(9, more_than_5days[0].sell_in)
        self.assertEqual(47, more_than_5days[0].quality)

        more_than_0 = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=30)]
        gilded_rose = GildedRose(more_than_0)
        gilded_rose.update_quality()
        self.assertEqual(4, more_than_0[0].sell_in)
        self.assertEqual(33, more_than_0[0].quality)

        after_conert = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=0, quality=49)]
        gilded_rose = GildedRose(after_conert)
        gilded_rose.update_quality()
        self.assertEqual(-1, after_conert[0].sell_in)
        self.assertEqual(0, after_conert[0].quality)

        max_quality = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=3, quality=49)]
        gilded_rose = GildedRose(max_quality)
        gilded_rose.update_quality()
        self.assertEqual(2, max_quality[0].sell_in)
        self.assertEqual(50, max_quality[0].quality)

    def test_Conjured(self):
        item = [Item(name="Conjured Mana Cake", sell_in=3, quality=6)]
        gilded_rose = GildedRose(item)
        gilded_rose.update_quality()
        self.assertEqual(2, item[0].sell_in)
        self.assertEqual(4, item[0].quality)

        item = [Item(name="Conjured Mana Cake", sell_in=0, quality=6)]
        gilded_rose = GildedRose(item)
        gilded_rose.update_quality()
        self.assertEqual(-1, item[0].sell_in)
        self.assertEqual(2, item[0].quality)

        item = [Item(name="Conjured Mana Cake", sell_in=3, quality=1)]
        gilded_rose = GildedRose(item)
        gilded_rose.update_quality()
        self.assertEqual(2, item[0].sell_in)
        self.assertEqual(0, item[0].quality)


if __name__ == '__main__':
    unittest.main()
