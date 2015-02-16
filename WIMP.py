
__author__ = 'Daniel A. R. Evans'

import sys
from tkinter import *
from urllib.request import urlopen
from getpass import getpass
import math

#SAMPLE LINK
#https://weedmaps.com/dispensaries/in/california/east-bay

class weed:
    #Class Trait Variables
    gram = ""
    eighth =""
    quarter = ""
    half = ""
    oz = ""
    unit = ""
    type = ""
    name = ""
    half_gram = ""

    #Constructor
    def __init__(self, gram, eighth, quarter, half, oz, unit, type, name, half_gram):
        self.gram = gram
        self.half_gram = half_gram
        self.eighth = eighth
        self.half = half
        self.quarter = quarter
        self.oz = oz
        self.unit = unit
        self.type = type.upper()
        self.name = name.upper()

    #return prices of amounts
    def get_gram(self):
        return self.gram
    def get_eighth(self):
        return self.eighth
    def get_quarter(self):
        return self.quarter
    def get_half(self):
        return self.half
    def get_oz(self):
        return self.oz
    def get_unit(self):
        return self.unit
    def get_type(self):
        return self.type
    def get_name(self):
        return self.name
    def get_half_gram(self):
        return self.half_gram

    #toString
    def __str__(self):
        if self.type in "INDICA" or self.type in "SATIVA" or self.type in "HYBRID":
            return "Name: " + self.name + "\nType: " + self.type + "\nGram: " + self.gram + " \nEighth: " + self.eighth + " \nQuarter: " + self.quarter + \
                   "\nHalf: " + self.half + "\nOz: " + self.oz + ""
        if self.type == "CONCENTRATE":
            return "Name: " + self.name + "\nType: " + self.type + "\nHalf-Gram: " + self.half_gram + "\nGram: " + self.gram
        if self.type == "EDIBLE" or self.type == "DRINK" or self.type == "PREROLL":
            return "Name: " + self.name + "\nType: " + self.type + "\nUnit: " + self.unit
        if self.type == "WAX":
            return "Name: " + self.name + "\nType: " + self.type + "\nHalf-Gram: " + self.half_gram + "\nGram: " + self.gram

#Get Prices from Lists
class dispensary:

     #Class Trait Variables
    name = "A"
    grass = []
    link = ""
    weed = []
    seeds = []
    tincture = []
    drink = []
    preroll = []
    wax = []
    concetrate = []
    edibles = []
    topicals = []
    clone = []

    def __iter__(self):
        return self

    def print_menu_list(self, input, file):
        list_to_print = []

        if input == "weed":
            for item in self.grass:
                if item.get_type() == "SATIVA" or item.get_type() == "INDICA" or item.get_type() == "HYBRID":
                    list_to_print.append(item)
        if input == "wax":
            for item in self.grass:
                if item.get_type() == "WAX":
                    list_to_print.append(item)
        if input == "concentrate":
            for item in self.grass:
                if item.get_type() == "CONCENTRATE":
                    list_to_print.append(item)
        if input == "edible":
            for item in self.grass:
                if item.get_type() == "EDIBLE":
                    list_to_print.append(item)
        if input == "preroll":
            for item in self.grass:
                if item.get_type() == "PREROLL":
                    list_to_print.append(item)
        if input == "clone":
            for item in self.grass:
                if item.get_type() == "CLONE":
                    list_to_print.append(item)
        if input == "drink":
            for item in self.grass:
                if item.get_type() == "DRINK":
                    list_to_print.append(item)
        if input == "topical":
            for item in self.grass:
                if item.get_type() == "TOPICALS":
                    list_to_print.append(item)
        if input == "seed":
            for item in self.grass:
                if item.get_type() == "SEED":
                    list_to_print.append(item)
        if input == "tincture":
            for item in self.grass:
                if item.get_type() == "TINCTURE":
                    list_to_print.append(item)

        if list_to_print:
            file.write(self.name)
            file.write("\n")
            file.write(self.get_url())
            file.write("\n")
            file.write("\n")

            for item in list_to_print:
                file.write(item.get_name())
                file.write("\n")
                file.write(item.get_type())
                file.write("\n")
                if item.get_type() == "WAX" or item.get_type() == "Concentrate":
                    file.write("$" + item.get_half_gram() + " .5G")
                    file.write("\n")
                    file.write("$" + item.get_gram() + " G")
                    file.write("\n")
                elif item.get_type() == "SATIVA" or item.get_type() == "INDICA" or item.get_type() == "HYBRID":
                    if item.get_gram() != "NA":
                        file.write("$" + item.get_gram() + " G")
                        file.write("\n")
                    if item.get_eighth() != "NA":
                        file.write("$" + item.get_eighth() + " 1/8OZ")
                        file.write("\n")
                    if item.get_quarter() != "NA":
                        file.write("$" + item.get_quarter() + " 1/4OZ")
                        file.write("\n")
                    if item.get_half() != "NA":
                        file.write("$" + item.get_half() + " 1/2OZ")
                        file.write("\n")
                    if item.get_oz() != "NA":
                        file.write("$" + item.get_oz() + " OZ")
                        file.write("\n")

                else:
                    file.write("$" + item.get_unit() + " Each")
                    file.write("\n")
                file.write("\n")
                file.write("\n")


     #Calculates Mode Values in a list
    def mode(self, stuff=[], *args):
        top = 0
        #Empty stuff. Why?
        mode_price = 0
        for p in stuff:
            if stuff.count(p) > top:

                top = stuff.count(p)
                mode_price = p
        return mode_price

    #Calculates the Highest Value in a list
    def high(self, stuff=[], *args):
        top = 0
        for p in stuff:
            if p > top:

                top = p
        return top

    #Calculates the Lowest Value in a list
    def low(self, stuff=[], *args):
        low = 10000000
        for p in stuff:
            if p < low:

                low = p
        return low

    #Get prices from the webpage of the dispensary
    def get_prices(self, menu_strings = [], *args):
        items = []

        for item in menu_strings:

            #Gram, Eighth, Quarter, Half, Oz, Unit, Type, Name, Half-Gram
            g = ""
            e = ""
            q = ""
            h = ""
            o = ""
            u = ""
            t = ""
            n = ""
            hg = ""

            #Get Strain Name
            sNum = item.partition('item_name">')
            sNum = sNum[2].partition('<')

            if sNum[0].strip():

                n = sNum[0].strip()
                n = n.replace("&#39;", "")

            else:
                n = "NA"

            #Get Strain Type
            sNum = item.partition("data-category-name=")
            sNum =sNum[2].partition('data')

            if sNum[0].replace('"', "").strip():
                t = sNum[0].replace('"', "").strip()

            else:
                t = "NA"

            #Price Half Gram
            gString = item.partition('"price_half_gram">')
            if gString != "":
                gNum = gString[2].partition('"price">')
                if "price_gram" not in gNum[0]:
                    gNum = gNum[2].partition('<')
                    if gNum[0].strip() != "":
                        hg = gNum[0].strip()

                    else:
                        hg = "NA"
                else:
                    hg = "NA"

            #Price Gram
            gString = item.partition('"price_gram">')
            if gString != "":
                gNum = gString[2].partition('"price">')
                if "price_eighth" not in gNum[0]:
                    gNum = gNum[2].partition('<')
                    if gNum[0].strip():
                        g = gNum[0].strip()

                    else:
                        g = "NA"
                else:
                    g = "NA"

            #Price Eighth
            gString = item.partition('"price_eighth">')
            if gString != "":
                gNum = gString[2].partition('"price">')
                if "price_quarter" not in gNum[0]:
                    gNum = gNum[2].partition('<')
                    if gNum[0].strip():
                        e = gNum[0].strip()

                    else:
                        e = "NA"
                else:
                    e = "NA"

            #Price Quarter
            gString = item.partition('"price_quarter">')
            if gString != "":
                gNum = gString[2].partition('"price">')
                if "price_half" not in gNum[0]:
                    gNum = gNum[2].partition('<')
                    if gNum[0].strip():
                        q = gNum[0].strip()

                    else:
                        q = "NA"
                else:
                    q = "NA"

            #Price Half
            gString = item.partition('"price_half_ounce">')
            if gString != "":
                gNum = gString[2].partition('"price">')
                if "price_ounce" not in gNum[0]:
                    gNum = gNum[2].partition('<')
                    if gNum[0].strip():
                        h = gNum[0].strip()

                    else:
                        h = "NA"
                else:
                    h = "NA"
            #Price Oz
            gString = item.partition('"price_ounce">')
            if gString != "":
                gNum = gString[2].partition('"price">')
                gNum = gNum[2].partition('<')
                if gNum[0].strip():
                    o = gNum[0].strip()

                else:
                    o = "NA"

            #Price Unit
            gString = item.partition('"price_unit">')
            if gString != "":
                gNum = gString[2].partition('"price">')
                gNum = gNum[2].partition('<')
                if gNum[0].strip():
                    u = gNum[0].strip()

                else:
                    u = "NA"

            #Prevent Gear from being calculated or counted as weed
            if t == "Gear":pass

            else:
                items.append(weed(g, e, q, h, o, u, t, n, hg))

        return items

    #Return Shop Name
    def get_name(self):
        return self.name

    def get_url(self):
        return self.link

    #Prints Shop Name and URL
    def __str__(self):
        return self.get_name() + "\n" + self.get_url()

    #Returns the list of all the weed in the shop
    def get_weed(self):
        return self.weed
    #Returns the list of all the wax in the shop
    def get_wax(self):
        return self.wax
    #Returns the list of all the concentrates in the shop
    def get_concetrate(self):
        return self.concetrate
    #Returns the list of all the edibles in the shop
    def get_edibles(self):
        return self.edibles
    #Returns the list of all the drinks in the shop
    def get_drinks(self):
        return self.drink
    #Returns the list of all the topicals in the shop
    def get_topicals(self):
        return self.topicals
    #Returns the list of all the tinctures in the shop
    def get_tincture(self):
        return self.tincture
    #Returns the list of all the clones in the shop
    def get_clones(self):
        return self.clone
    #Returns the list of all the seeds in the shop
    def get_seeds(self):
        return self.seeds
    #Returns the list of all the prerolls in the shop
    def get_preroll(self):
        return self.preroll

    def sort_by_amount(self, amount, stuff=[], *args):
        prices = []
        val = "NA"
        for flower in stuff:
            if amount == "gram":
                val = flower.get_gram()
            if amount == "eighth":
                val = flower.get_eighth()
            if amount == "quarter":
                val = flower.get_quarter()
            if amount == "half":
                val = flower.get_half()
            if amount == "oz":
                val = flower.get_oz()
            if amount == "unit":
                val = flower.get_unit()
            if amount == "half gram":
                val = flower.get_half_gram()

            if val != "NA":
                prices.append(val)
        return prices


    #Gets the mode price based on the given amount
    def get_mode_price(self, amount, stuff=[], *args):
        prices = self.sort_by_amount(amount,stuff)
        return self.mode(prices)

    def get_high_price(self, amount, stuff=[], *args):
        prices = self.sort_by_amount(amount,stuff)
        return self.high(prices)

    def get_low_price(self, amount, stuff=[], *args):
        prices = self.sort_by_amount(amount, stuff)
        return self.low(prices)

    def get_mode_gram(self):
        return self.get_mode_price("gram", self.weed)

    def get_mode_eighth(self):
        return self.get_mode_price("eighth", self.weed)

    def get_mode_quarter(self):
        return self.get_mode_price("quarter", self.weed)

    def get_mode_half(self):
        return self.get_mode_price("half", self.weed)

    def get_mode_oz(self):
        return self.get_mode_price("oz", self.weed)

    def separate_item(self, type, items=[], *args):
        returned = []
        for item in items:
            if item.get_type().upper() == "SATIVA" or item.get_type().upper() == "INDICA" or item.get_type().upper() == "HYBRID" and type == "weed":
                returned.append(item)
            if item.get_type() == "WAX" and type == "wax":
                returned.append(item)
            if item.get_type() == "DRINK" and type == "drink":
                returned.append(item)
            if item.get_type() == "CLONE" and type == "clone":
                returned.append(item)
            if item.get_type() == "EDIBLE" and type == "edible":
                returned.append(item)
            if item.get_type() == "TOPICAL" and type == "topical":
                returned.append(item)
            if item.get_type() == "PREROLL" and type == "preroll":
                returned.append(item)
            if item.get_type() == "TINCTURE" and type == "tincture":
                returned.append(item)
        return returned

    def sort_store(self, items = [], *args):
        for item in items:
            if item.get_type().upper() == "SATIVA" or item.get_type().upper() == "INDICA" or item.get_type().upper() == "HYBRID":
                self.weed.append(item)
            if item.get_type() == "WAX":
                self.wax.append(item)
            if item.get_type() == "DRINK":
                self.drink.append(item)
            if item.get_type() == "CLONE":
                self.clone.append(item)
            if item.get_type() == "EDIBLE":
                self.edibles.append(item)
            if item.get_type() == "TOPICAL":
                self.topicals.append(item)
            if item.get_type() == "PREROLL":
                self.preroll.append(item)
            if item.get_type() == "TINCTURE":
                self.tincture.append(item)

    #Constructor
    def __init__(self, url):
        self.link = url
        # Grab Source from Weedmaps
        html = urlopen(url)
        #Parse HTML Source
        source = html.read()
        html.close()
        #convert to string
        source = source.decode("utf-8")
        #Remove Pointless Characters
        source = source.replace("&quot;",'')

        name = source.partition('itemprop="name">')
        name = name[2].partition('<')
        self.name = name[0]
        print(self.name + " has begun processing")
        split = source.partition("data-category-id")
        first = split[0] + split[1]
        theRest = split[2]

        finalString = []
        menu = []

        self.grass = []

        repeat_string = theRest.partition('"')

        #Saves the strings for each item on a menu
        while repeat_string[2]:
            try:
                theRest = repeat_string[2]
                menu.append(theRest.partition("</div></div></div></div>")[0])
                repeat_string = theRest.partition("</div></div></div></div>")

            except:
                break
        self.grass = self.get_prices(menu)
        self.weed = self.separate_item("weed", self.grass)
        self.wax = self.separate_item("wax", self.grass)
        self.concentrate = self.separate_item("concentrate", self.grass)
        self.clone = self.separate_item("clone", self.grass)
        self.drink = self.separate_item("drink", self.grass)
        self.seeds = self.separate_item("seed", self.grass)
        self.edibles = self.separate_item("edible", self.grass)



class main:
    disps = []
    lowest_mode_disp = []
    lowest_mode_requested_price = ""

    def print_one_item(self, type, file):
        for item in self.disps:
            item.print_menu_list(type, file)

    def set_lowest_mode_dispensary_and_price(self, inp):
        self.lowest_mode_disp = []

        if inp == "1":
            self.get_lowest_mode_gram(self.disps)
        if inp == "2":
            self.get_lowest_mode_eighth(self.disps)
        if inp == "3":
            self.get_lowest_mode_quarter(self.disps)
        if inp == "4":
            self.get_lowest_mode_half(self.disps)
        if inp == "5":
            self.get_lowest_mode_oz(self.disps)


    def get_lowest_mode_dispensary(self):
        return self.lowest_mode_disp

    def get_lowest_mode_price(self):
        return self.lowest_mode_requested_price


    #Index all of the dispensaries through HTTP
    def raid_dispensaries(self, url = [], *args):
        dip = []
        var = 1
        for link in url:
            print(var.__str__() + " out of " + len(url).__str__())
            var += 1
            dip.append(dispensary(link))
        return dip

    def get_dispensaries(self):
        return self.disps

    def gui(self):
        #GUI WORK
        root = Tk()
        #Sets Title of Window
        root.wm_title("WeedMaps Indexer by DARE")
        #root.resizable(width=FALSE, height=FALSE)
        root.minsize(300, 300)
        root.geometry("500x500")

        w = Label(root, text="WeedMaps Price Mapper")
        w.pack()

        e = Entry(root)
        e.pack()
        e.focus_set()

        b = Button(root, text="Start Region Search", command=lambda: self.get_dispensary_urls(e.get()))
        b.pack()

        root.mainloop()
    def get_dispensary_urls(self, page=[], *args):
        #"http://www.weedmaps.com/" region link
        for item in page:
            link = item
        #Load the webpage
        web = urlopen(link)
        #Grab the document
        web = web.read()
        #Convert to string
        web = web.decode("UTF-8")
        #Remove filler characters
        web = web.replace("&quot;", "")

        #Get first url
        line = web.partition('"url":"')
        line = line[2].partition(":true}};")[0]

        #Stores urls
        urls = []

        #Gets urls from source page
        while line:
                line = line.partition('"')
                urls.append(line[0])
                line = line[2].partition('"url":"')
                line = line[2]

        #Gives list of indexed dispensaries
        return self.raid_dispensaries(urls)

    def get_lowest_mode_gram(self, stores = [], *args):
        low = 100000

        for item in stores:
            a = float(item.get_mode_gram())
            if 0 < a < low:
                low = a

        for item in stores:
            if low == float(item.get_mode_gram()):
                self.lowest_mode_disp.append(item)
        self.lowest_mode_requested_price = low.__str__()

    def get_lowest_mode_eighth(self, stores=[], *args):
        low = 100000

        for item in stores:
            a = float(item.get_mode_eighth())
            if 0 < a < low:
                low = a
        for item in stores:
            if low == float(item.get_mode_eighth()):
                self.lowest_mode_disp.append(item)
        self.lowest_mode_requested_price = low.__str__()

    def get_lowest_mode_quarter(self, stores = [], *args):
        low = 100000

        for item in stores:
            a = float(item.get_mode_quarter())
            if 0 < a < low:
                low = a
        for item in stores:
            if low == float(item.get_mode_quarter()):
                self.lowest_mode_disp.append(item)
        self.lowest_mode_requested_price = low.__str__()

    def get_lowest_mode_half(self, stores = [], *args):
        low = 100000

        for item in stores:
            a = float(item.get_mode_half())
            if 0 < a < low:
                low = a
        for item in stores:
            if low == float(item.get_mode_half()):
                self.lowest_mode_disp.append(item)
        self.lowest_mode_requested_price = low.__str__()

    def get_lowest_mode_oz(self, stores = [], *args):
        low = 100000

        for item in stores:
            a = float(item.get_mode_oz())
            if 0 < 0 < a < low:
                low = a
        for item in stores:
            if low == float(item.get_mode_oz()):
                self.lowest_mode_disp.append(item)
        self.lowest_mode_requested_price = low.__str__()

    def get_lowest_mode_half_gram(self, stores = [], *args):
        low = 100000

        for item in stores:
            a = float(item.get_mode_half_gram())
            if 0 < a < low:
                low = a
        for item in stores:
            if low == float(item.get_mode_half_gram()):
                self.lowest_mode_disp.append(item)
        self.lowest_mode_requested_price = low.__str__()

    def get_lowest_mode_unit(self, stores = [], *args):
        low = 100000

        for item in stores:
            a = float(item.get_mode_unit())
            if 0 < a < low:
                low = a
        for item in stores:
            if low == float(item.get_mode_unit()):
                self.lowest_mode_disp.append(item)
        self.lowest_mode_requested_price = low.__str__()

    def __init__(self, link=[], *args):
        #self.gui()
        self.disps = self.get_dispensary_urls(link)

while True:
    inp = getpass()
    if inp == "419":
        break
    else:
        print("Wrong Password")
        print("Please Try Again")
        print()
        print()
links = []
regions = open("regions.txt", "a+")
while True:
    print("Please enter a weedmaps.com region link or enter '1' to use regions.txt")
    print("Example: https://weedmaps.com/dispensaries/in/california/east-bay")
    inp = input()
    if inp == "1":
        for line in regions:
            if 'weedmaps.com' in line:
                links.append(line)
                break
            else:
                print("Please enter a valid link")
                print()
        if links:
            break
        else:
            print("No link was found")
            print()

    else:
        if 'weedmaps.com' in inp:
            links.append(inp)
            break
        else:
            print("Please enter a valid link")
            print()
m = main(links)
while True:

    while True:
        print()
        print()
        print("Welcome to W.I.M.P")
        print()
        print("Weed")
        print("Indexing")
        print("Menu")
        print("Program")
        print()
        print("Pick an option:")
        print("1. Get Lowest Mode Price")
        print("2. Print All of One Type")
        print("3. Print Dispensary Menu")
        print("4. Quit")
        inp = input()
        if inp == "1":
            while True:
                print()
                print("Please pick an amount to search index by lowest mode price for:")
                print("1. Gram")
                print("2. Eighth")
                print("3. Quarter")
                print("4. Half")
                print("5. Oz")
                print()
                print("Example Answer: 2")
                inp = input()
                #Set Lowest Mode Dispensary and Price of requested amount
                m.set_lowest_mode_dispensary_and_price(inp)
                #Retrieves Lowest Price
                lowest = m.get_lowest_mode_price()
                #Retrieves Dispensary
                disp = m.get_lowest_mode_dispensary()
                if lowest != "NA":
                    for item in disp:
                        if lowest != "NA" or lowest != "":
                            print("Lowest Mode: " + lowest)
                            print("Available at " + item.get_name())
                            print(item.get_url())
                            inp = ""
                        elif lowest == "NA":
                            print("That amount does not exist at any indexed dispensary")
                    break
                else:
                    print("You did not enter a number 1-5")

        file = open("results.txt", "w+")
        if inp == "2":
            while True:
                print()
                print("Please pick a type to print:")
                print("1. Weed")
                print("2. Wax")
                print("3. Concentrates")
                print("4. Edibles")
                print("5. Prerolls")
                print("6. Drinks")
                print("7. Seeds")
                print("8. Clones")
                print("9. Topicals")
                print("10. Tinctures")
                inp = input()

                if inp == "1":
                    inp = "weed"
                if inp == "2":
                    inp = "wax"
                if inp == "3":
                    inp = "concentrates"
                if inp == "4":
                    inp = "edible"
                if inp == "5":
                    inp = "preroll"
                if inp == "6":
                    inp = "drink"
                if inp == "7":
                    inp = "seed"
                if inp == "8":
                    inp = "clone"
                if inp == "9":
                    inp = "topical"
                if inp == "10":
                    inp = "tincture"

                m.print_one_item(inp, file)
                print("Please check 'results.txt' in the folder you ran this program from.")
                print()
                print("Print a different item? y/n")
                inp = input()
                if inp != "y":
                    break

        if inp == "3":
            while True:
                print()
                print("Pick a dispensary:")
                print()
                var = 1
                for item in m.get_dispensaries():
                    print(var.__str__() + ". " + item.get_name())
                    var += 1
                chosen_dispensary = int(input())-1

                print()
                print("Pick a category:")
                print()
                print("1. Weed")
                print("2. Wax")
                print("3. Concentrates")
                print("4. Edibles")
                print("5. Prerolls")
                print("6. Drinks")
                print("7. Seeds")
                print("8. Clones")
                print("9. Topicals")
                print("10. Tinctures")
                inp = input()

                if inp == "1":
                    inp = "weed"
                if inp == "2":
                    inp = "wax"
                if inp == "3":
                    inp = "concentrates"
                if inp == "4":
                    inp = "edible"
                if inp == "5":
                    inp = "preroll"
                if inp == "6":
                    inp = "drink"
                if inp == "7":
                    inp = "seed"
                if inp == "8":
                    inp = "clone"
                if inp == "9":
                    inp = "topical"
                if inp == "10":
                    inp = "tincture"

                #Make Method to print list of strains at dispensary
                print()
                m.get_dispensaries()[chosen_dispensary].print_menu_list(inp, file)
                print("Please check 'results.txt' in the folder you ran this program from.")

                print("Pick another dispensary? y/n")
                inp = input()
                if inp.lower() != "y":
                    break
        file.close()
        if inp == "4":
            break
        print("Use same data again? y/n")
        inp = input().lower()
        if inp != "y":
            break
        else:
            print()
            print("Press Enter to Continue")
            inp = input()
    break
#Comment Section