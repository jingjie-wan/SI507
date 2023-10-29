#########################################
##### Name:                         #####
##### Uniqname:                     #####
#########################################
import requests
import json
import webbrowser

class Media:

    def __init__(self, title="No Title", author="No Author", release_year =  "No Release Year", url = "No URL", json = None):
        if json == None:
            self.title = title
            self.author = author
            self.release_year = release_year
            self.url = url
        else:
            self.title = json.get('collectionName')
            self.author = json.get('artistName')
            self.release_year = json.get('releaseDate')[0:4] #can be revised
            self.url = json.get('collectionViewUrl')

    def info(self):
        return self.title + ' by ' + self.author + ' (' + str(self.release_year) +')'

    def length(self):
        return 0
# Other classes, functions, etc. should go here

class Song(Media):
    def __init__(self, title="No Title", author="No Author", release_year =  "No Release Year", url = "No URL", album = "No Album", genre = "No Genre", track_length = 0, json = None):
        super().__init__(title, author, release_year, url, json)
        if json == None:
            self.album = album
            self.genre = genre
            self.track_length = track_length
        else:
            self.title = json.get('trackName')
            self.album = json.get('collectionName')
            self.genre = json.get('primaryGenreName')
            self.track_length = json.get('trackTimeMillis')

    def info(self):
        return super().info() + ' [' + self.genre + ']'

    def length(self):
        return round(self.track_length / 1000)

class Movie(Media):
    def __init__(self, title="No Title", author="No Author", release_year="No Release Year", url="No URL", rating = "No Rating", movie_length = 0, json = None):
        super().__init__(title, author, release_year, url, json)
        if json == None:
            self.rating = rating
            self.movie_length = movie_length
        else:
            self.title = json.get('trackName')
            self.rating = json.get('contentAdvisoryRating')
            self.movie_length = json.get('trackTimeMillis')

    def info(self):
        return super().info() + ' [' + self.rating + ']'

    def length(self):
        return round(self.movie_length / (1000 * 60))

def show_request(query):
        response = requests.get("https://itunes.apple.com/search?term=" + query)
        json_str = response.text
        json_dict = json.loads(json_str)
        list_result = json_dict['results']
        song = []
        movie = []
        other = []
        if len(list_result) == 0:
            print("No result.\n")
            return 0, []
        url_s = []
        url_m = []
        url_o = []
        for item in list_result:
            if item.get('kind') == 'song':
                ob = Song(json=item)
                song.append(ob)
                url_s.append(item.get('trackViewUrl'))
            elif item.get('kind') == 'feature-movie':
                ob = Movie(json=item)
                movie.append(ob)
                url_m.append(item.get('trackViewUrl'))
            else:
                ob = Media(json=item)
                other.append(ob)
                url_o.append(item.get('trackViewUrl'))
        n = 1
        print('SONGS\n')
        if len(song) == 0: print('No result for song.')
        else:
            for s in song:
                print(str(n) + ' ' + s.info() + '\n')
                n += 1
        print('\n')
        print('MOVIES\n')
        if len(movie) == 0: print('No result for movie.')
        else:
            for m in movie:
                print(str(n) + ' ' + m.info() + '\n')
                n += 1
        print('\n')
        print('OTHER MEDIA\n')
        if len(other) == 0: print('No result for other media.')
        else:
            for o in other:
                print(str(n) + ' ' + o.info() + '\n')
                n += 1
        print('\n')
        return n-1, url_s + url_m + url_o

if __name__ == "__main__":
    # your control code for Part 4 (interactive search) should go here
    query = input('Enter a search term, or "exit" to quit: ')
    print('\n')
    if query == 'exit':
        print('Bye!')
        exit()
    else:
        n, url = show_request(query)
        while True:
            query2 = input('Enter a number for more info, or another search term, or exit: ')
            print('\n')
            if query2 == 'exit':
                print('Bye!')
                exit()
            elif query2.isnumeric() == True:
                number = int(query2)
                if (number < 1) or (number > n):
                    print('Invalid number, please try again.\n')
                else:
                    if url[number-1]:
                        print('Launching\n' + url[number-1] +'\nin web browser...\n')
                        webbrowser.open_new_tab(url[number-1])
                    else:
                        print('No preview url for this media.\n')
            else:
                n, url = show_request(query2)