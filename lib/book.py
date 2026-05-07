#!/usr/bin/env python3

class Book:
    def __init__(self,title,page_count):
        self.title=title
        self.page_count=int(page_count)
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
    def get_count(self):
        return self._page_count
    def set_count(self,count):
        if(type(count) is int and 0<=count):
            self._page_count=count
        else:
            print("page_count must be an integer") 
    page_count=property(get_count,set_count)       