import os
import requests
import time
from datetime import datetime

class Itunes_API:
    def __init__(self,artist:str) -> None:
        self.artist = artist
        
        
    def get_songs(self, num_of_songs) ->None:
        self.num_of_songs = num_of_songs
        response =  requests.get(f'https://itunes.apple.com/search?entity=song&limit={self.num_of_songs}&term={self.artist}')
        
        if response.status_code == 200:
            print(f'Status: Connection to Itunes API good ...')
            time.sleep(4)
            os.system('cls')
            
            print(f'Heres {self.num_of_songs} song/s of {self.artist}: ')
            song_data = response.json()
            for song in song_data['results']:
                print(song['trackName'])  
    
    def get_albums(self):
        url = f'https://itunes.apple.com/search?entity=album&limit=10&term={self.artist}'  # Fetch more albums initially
        response = requests.get(url)
        album_data = response.json()
        
        if response.status_code == 200:
            print(f'Here are the Albums for {self.artist}:')            
            for result in album_data["results"]:
                
                release_year = result['releaseDate']
                # Parse the date string using datetime.datetime.fromisoformat()
                date_obj = datetime.fromisoformat(release_year)
                # Format the date object as desired (1 January 2010)
                formatted_date = date_obj.strftime("%d %B %Y")
                
                print( f'{result['collectionName']} - {formatted_date} - Tracks:{result['trackCount']} '  )
            print('')
            print('If the results are inaccurate , Blame the Itunes API, all this data comes from Itunes API')        
    #TESTING    
# def main():
#     api: Itunes_API = Itunes_API('Michael Jackson')
#     api.get_albums()
 
# if __name__ == "__main__":
#     main()
 
