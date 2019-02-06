
class Marketplace:
    def __init__(self):
        self.listings = []
    
    def add_listing(self, new_listing):
        self.listings.append(new_listing)

    def remove_listing(self, listing):
        self.listings.remove(listing)

    def show_listings(self):
        for listing in self.listings:
            print(listing)
       




class Art:
    def __init__(self, artist, title, medium, year):
        self.artist = artist
        self.title  = title
        self.medium = medium
        self.year   = year

    def __repr__ (self):
        return ('{artist}. "{title}". {year}, {medium} '.format(artist = self.artist, title  =  self.title, medium = self.medium, year   =  self.year))


new_art = Art()
print(new_art)
veneer = Marketplace()
print(veneer.show_listings)