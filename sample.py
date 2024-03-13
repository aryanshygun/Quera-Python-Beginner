# all_users = {}
# all_albums= {}

# def add_user(username: str, age: int, city: str, albums: list, all_users: dict, all_albums: dict):
#     all_users[username] = {
#         'username': username,
#         'age': age,
#         'city': city,
#         'albums': albums,
#     }
# def add_album(name: str, artist_name: str, genre: str, tracks: int, all_users: dict, all_albums: dict):
#     all_albums[name] = {
#         'name': name,
#         'artist name': artist_name,
#         'genre': genre,
#         'tracks': tracks,
#     }

all_users = {
    'SAliB': {
        'username': 'SAliB', 
        'age': 19, 
        'city': 'Tehran', 
        'albums': ['tekunbede', 'barf', 'gavazn']
        }, 
    
    'Saeid': {
        'username': 'Saeid', 
        'age': 22, 
        'city': 'Esfehan', 
        'albums': ['eclipse', 'barf', 'gavazn']
        }, 
    
    'Ali': {
        'username': 'Ali', 
        'age': 12, 
        'city': 'Bushehr', 
        'albums': ['bidad', 'blaze']
        }
    
    }
all_albums = {
    'eclipse': {
        'name': 'eclipse', 
        'artist name': 'malmsteen', 
        'genre': 'classic', 
        'tracks': 10
        }, 
    
    'barf': {
        'name': 'barf', 
        'artist name': 'beeptunes', 
        'genre': 'pop', 
        'tracks': 22
        }, 
    
    'tekunbede': {
        'name': 'tekunbede', 
        'artist name': 'beeptunes', 
        'genre': 'pop', 
        'tracks': 14
        }, 
    
    'gavazn': {
        'name': 'gavazn', 
        'artist name': 'sorena', 
        'genre': 'persian', 
        'tracks': 18
        }, 
    
    'bidad': {
        'name': 'bidad', 
        'artist name': 'shajarian', 
        'genre': 'classic', 
        'tracks': 10
        }, 
    
    'blaze': {
        'name': 'blaze', 
        'artist name': 'ghorbani', 
        'genre': 'pop', 
        'tracks': 9
        }
    
    }


def query_user_artist(username: str, artist_name: str, all_users: dict, all_albums: dict) -> int:
    x = 0
    for album_name, album_details in all_albums.items():
        if album_details['artist name'] == artist_name:
            if album_name in all_users[username]['albums']:
                x += album_details['tracks']
    print(x)

def query_user_genre(username: str, genre: str, all_users: dict, all_albums: dict) -> int:
    x = 0
    for album_name, album_details in all_albums.items():
        if album_details['genre'] == genre:
            if album_name in all_users[username]['albums']:
                x += album_details['tracks']         
    print(x)
    
def query_age_artist(age, artist_name, all_users, all_albums):
    x = 0
    for user_name, user_details in all_users.items():
        if user_details['age'] == age:
            for album_name, album_details in all_albums.items():
                if album_details['artist name'] == artist_name:
                    if album_name in all_users[user_name]['albums']:
                        x += album_details['tracks']        
    print(x)

def query_age_genre(age, genre, all_users, all_albums):


# def query_user_genre(username: str, genre: str, all_users: dict, all_albums: dict) -> int:
#     x = 0
    
#     for i, j in all_albums.items():
#         if j['genre'] == genre:
#             selectedalbum = i
#             if i in all_users[username]['albums']:
#                 x += j['tracks']
                
#     print(x)
    
# def query_age_artist(age: int, artist_name: str, all_users: dict, all_albums: dict) -> int:
#     x = 0
    
#     for i, j in all_albums.items():
#         if j['artist name'] == artist_name:
#             selectedalbum = i
#             if i in all_users[username]['albums']:
#                 x += j['tracks']              
#     print(x)
    
    
