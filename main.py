
__author__ = 'Daniel A. R. Evans'

from urllib.request import urlopen
from tkinter import *

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
        if self.type == "NA":
            return ""

        if self.type == "CONCENTRATE":
            return "Name: " + self.name + "\nType: " + self.type + "\nHalf-Gram: " + self.half_gram + "\nGram: " + self.gram
        if self.type == "EDIBLE" or self.type == "DRINK" or self.type == "PREROLL":
            return "Name: " + self.name + "\nType: " + self.type + "\nUnit: " + self.unit
        if self.type == "WAX":
            return "Name: " + self.name + "\nType: " + self.type + "\nHalf-Gram: " + self.half_gram + "\nGram: " + self.gram
        return self.gram

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

     #Calculates Mode Values in a list
    def mode(self, list = [], *args):
        top = 0
        #Empty List. Why?
        mode_price = 0
        for p in list:
            if list.count(p) > top:

                top = list.count(p)
                mode_price = p
        return mode_price

    #Calculates the Highest Value in a list
    def high(self, list = [], *args):
        top = 0
        for p in list:
            if p > top:

                top = p
        return top

    #Calculates the Lowest Value in a list
    def low(self, list = [], *args):
        low = 10000000
        for p in list:
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
                gNum = gNum[2].partition('<')
                if gNum[0].strip() != "":
                    hg = gNum[0].strip()

                else:
                    hg = "NA"

            #Price Gram
            gString = item.partition('"price_gram">')
            if gString != "":
                gNum = gString[2].partition('"price">')
                gNum = gNum[2].partition('<')
                if gNum[0].strip():
                    g = gNum[0].strip()

                else:
                    g = "NA"

            #Price Eighth
            gString = item.partition('"price_eighth">')
            if gString != "":
                gNum = gString[2].partition('"price">')
                gNum = gNum[2].partition('<')
                if gNum[0].strip():
                    e = gNum[0].strip()

                else:
                    e = "NA"

            #Price Quarter
            gString = item.partition('"price_quarter">')
            if gString != "":
                gNum = gString[2].partition('"price">')
                gNum = gNum[2].partition('<')
                if gNum[0].strip():
                    q = gNum[0].strip()

                else:
                    q = "NA"

            #Price Half
            gString = item.partition('"price_half_ounce">')
            if gString != "":
                gNum = gString[2].partition('"price">')
                gNum = gNum[2].partition('<')
                if gNum[0].strip():
                    h = gNum[0].strip()

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

    def sort_by_amount(self, amount, list = [], *args):
        prices = []
        val = "NA"
        for flower in list:
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
    def get_mode_price(self, amount, list = [], *args):
        prices = self.sort_by_amount(amount,list)
        return self.mode(prices)

    def get_high_price(self, amount, list = [], *args):
        prices = self.sort_by_amount(amount,list)
        return self.high(prices)

    def get_low_price(self, amount, list = [], *args):
        prices = self.sort_by_amount(amount, list)
        return self.low(prices)

    def get_mode_gram(self):
        sweed = self.get_weed()
        return self.get_mode_price("gram", sweed)

    def get_mode_eighth(self):
        weed = self.get_weed()
        return self.get_mode_price("eighth", weed)

    def get_mode_quarter(self):
        weed = self.get_weed()
        return self.get_mode_price("quarter", weed)

    def get_mode_half(self):
        weed = self.get_weed()
        return self.get_mode_price("half", weed)

    def get_mode_oz(self):
        weed = self.get_weed()
        return self.get_mode_price("oz", weed)

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
        self.sort_store(self.grass)

class main:
    disps = []
    lowest_mode_disp = ["a"]
    lowest_mode_requested_price = ""

    def set_lowest_mode_dispensary_and_price(self, inp):
        #low = "10000"
        disp = ["a"]
        var = "NA"

        if inp == "1":
            var = self.get_lowest_mode_gram(self.disps)
        if inp == "2":
            var = self.get_lowest_mode_eighth(self.disps)
        if inp == "3":
            var = self.get_lowest_mode_quarter(self.disps)
        if inp == "4":
            var = self.get_lowest_mode_half(self.disps)
        if inp == "5":
            var = self.get_lowest_mode_oz(self.disps)


    def get_lowest_mode_dispensary(self):
        return self.lowest_mode_disp

    def get_lowest_mode_price(self):
        return self.lowest_mode_requested_price


    #Index all of the dispensaries through HTTP
    def raid_dispensaries(self, url = [], *args):
        dip = []
        for link in url:
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
    def get_dispensary_urls(self, page):
        #"http://www.weedmaps.com/" region link
        link = page
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
                #Print URL
                print(line[0])
                line = line[2].partition('"url":"')
                line = line[2]

        #Gives list of indexed dispensaries
        return self.raid_dispensaries(urls)

    def get_lowest_mode_gram(self, stores = [], *args):
        low = 100000

        for item in stores:
            a = int(item.get_mode_gram())
            if a < low:
                low = a
        self.lowest_mode_disp[0] = (item)
        self.lowest_mode_requested_price = low.__str__()

    def get_lowest_mode_eighth(self, stores = [], *args):
        low = 100000

        for item in stores:
            a = int(item.get_mode_eighth())
            if a < low:
                low = a
        self.lowest_mode_disp[0] = (item)
        self.lowest_mode_requested_price = low.__str__()

    def get_lowest_mode_quarter(self, stores = [], *args):
        low = 100000

        for item in stores:
            a = int(item.get_mode_quarter())
            if a < low:
                low = a
        self.lowest_mode_disp[0] = (item)
        self.lowest_mode_requested_price = low.__str__()

    def get_lowest_mode_half(self, stores = [], *args):
        low = 100000

        for item in stores:
            a = int(item.get_mode_half())
            if a < low:
                low = a
        self.lowest_mode_disp[0] = (item)
        self.lowest_mode_requested_price = low.__str__()

    def get_lowest_mode_oz(self, stores = [], *args):
        low = 100000

        for item in stores:
            a = int(item.get_mode_oz())
            if a < low:
                low = a
        self.lowest_mode_disp[0] = (item)
        self.lowest_mode_requested_price = low.__str__()

    def get_lowest_mode_half_gram(self, stores = [], *args):
        low = 100000

        for item in stores:
            a = int(item.get_mode_half_gram())
            if a < low:
                low = a
        self.lowest_mode_disp[0] = (item)
        self.lowest_mode_requested_price = low.__str__()

    def get_lowest_mode_unit(self, stores = [], *args):
        low = 100000

        for item in stores:
            a = int(item.get_mode_unit())
            if a < low:
                low = a
        self.lowest_mode_disp[0] = (item)
        self.lowest_mode_requested_price = low.__str__()

    def __init__(self, link):
        #self.gui()
        self.disps = self.get_dispensary_urls(link)

while True:
    print("Please enter a weedmaps.com region link")
    inp = input()
    if 'weedmaps.com' in inp:
        break;
    else:
        print("Please enter a valid link")
        print("Example: https://weedmaps.com/dispensaries/in/california/east-bay")
        print()
m = main(inp)

while True:

    while True:
        print()
        print()
        print("Welcome to W.I.M.P")
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
        m.set_lowest_mode_dispensary_and_price(inp)
        lowest = m.get_lowest_mode_price()
        disp = m.get_lowest_mode_dispensary()
        if lowest != "NA" or lowest != "":
            print("Lowest Mode: " + lowest)
            print("Available at " + disp[0].get_name())
            print(disp[0].get_url())
            break

        else:
            print("You did not enter a number 1-5")

    print("Use same data again? y/n")
    inp = input().lower()
    if inp == "n":
        break
    else:
        print()
        print()

#Comment Section
#Strains missing any cost besides OZ have it filled in by the next amount causing incorrect numbers
#Need to fix get_prices