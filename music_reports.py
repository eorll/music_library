

def get_albums_by_genre(albums, genre):
    """
    Get albums by genre

    :param list albums: albums' data
    :param str genre: genre to filter by

    :returns: all albums of given genre
    :rtype: list
    [Pink Floyd, The Dark Side Of The Moon, 1973, progressive rock, 43:00]
    """
    list_to_return = []
    for album in albums:
        if album[3] == genre:
            list_to_return.append(album)
    if list_to_return == []:
        raise ValueError("Wrong genre")
        
    return list_to_return


def get_genre_stats(albums):
    """
    Get albums' statistics showing how many albums are in each genre
    Example: { 'pop': 2, 'hard rock': 3, 'folk': 20, 'rock': 42 }

    :param list albums: albums' data
    :returns: genre stats
    :rtype: dict
    """
    genre_dict = {}

    for i in albums:
        genre_dict[i[3]] = 0
    for i in albums:
        genre_dict[i[3]] += 1
    return genre_dict 


def get_longest_album(albums):
    """
    Get album with biggest value in length field.
    If there are more than one such album return the first (by original lists' order)

    :param list albums: albums' data
    :returns: longest album
    :rtype: list
    """
    longest_album = albums[0]
    for i in albums:
        if to_time(i[4]) > to_time(longest_album[4]):
            longest_album = i
    return longest_album
    



def get_last_oldest(albums):
    """
    Get last album with earliest release year.
    If there is more than one album with earliest release year return the last
    one of them (by original list's order)

    :param list albums: albums' data
    :returns: last oldest album
    :rtype: list
    """
    oldest_album = albums[0]
    for i in albums:
        if int(i[2]) <= int(oldest_album[2]):
            oldest_album = i
    return oldest_album


def get_last_oldest_of_genre(albums, genre):
    """
    Get last album with earliest release year in given genre

    :param list albums: albums' data
    :param str genre: genre to filter albums by
    :returns: last oldest album in genre
    :rtype: list
    """
    list_to_test = []
    for i in albums:
        if i[3] == genre:
            list_to_test.append(i)

    oldest_album_by_genre = get_last_oldest(list_to_test)
        
    return oldest_album_by_genre


def to_time(str):
    """
    converts time in format "minutes:seconds" (string) to seconds (int)
    """
    str = str.split(':')
    str = ((int(str[0]) * 60) + int(str[1]))
    return str
    



def get_total_albums_length(albums):
    """
    Get sum of lengths of all albums in minutes, rounded to 2 decimal places
    Example: 3:51 + 5:20 = 9.18             
             231 + 320 seconds = 551 seconds

    :param list albums: albums' data
    :returns: total albums' length in minutes
    :rtype: float
    """
    lenght_s = 0
    for i in albums:
        lenght_s += to_time(i[4])
    lenght_min = round((lenght_s / 60),2)

    return lenght_min
