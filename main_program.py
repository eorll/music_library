"""
The main program should use functions from music_reports and display modules
"""
import file_handling, music_reports, display, os


def delete_album_by_artist_and_album_name(albums, artist, album_name):
    """
    Deletes album of given name by given artist from list and updates data file

    :param list albums: currently existing albums
    :param str artist: artist who recorded the album
    :param str album_name: name of album to be deleted

    :returns: updated albums' list
    :rtype: list
    """
    for i in albums:
        if artist in i and album_name in i:
            albums.remove(i)
            return albums
    display.print_command_result('Wrong artist or/and album name!')
    return albums


def main():
    """
    Calls all interaction between user and program, handles program menu
    and user inputs. It should repeat displaying menu and asking for
    input until that moment.

    You should create new functions and call them from main whenever it can
    make the code cleaner
    """
    menu = ['Get album by genre.', 'Get genre stats.', 
    'Get longest album.', 'Get last album with earliest release year by genre',
    'Get sum of lengths of all albums in minutes', 'Delete album.' ]
    albums = file_handling.import_data()
    while True:
        
        display.print_program_menu(menu)
        try:
            option = int(input('Enter option number: '))
            os.system('cls')
            if option == 0 :
                try:
                    genre = input('Enter genre: ')
                    result = music_reports.get_albums_by_genre(albums, genre)
                    display.print_albums_list(result)
                except:
                    display.print_command_result('Genre not found!')

            elif option == 1: 
                result = music_reports.get_genre_stats(albums)
                print(result)

            elif option == 2:
                result = music_reports.get_longest_album(albums)
                display.print_album_info(result)

            elif option == 3:
                try:
                    genre = input('Enter genre: ')
                    result = music_reports.get_last_oldest_of_genre(albums,genre)
                    display.print_album_info(result)
                except:
                    display.print_command_result('Genre not found!')

            elif option == 4:
                result = music_reports.get_total_albums_length(albums)
                display.print_command_result(str(result))

            elif option == 5:
                display.print_albums_list(albums)
                artist = input('Enter artist name: ')
                album_name = input('Enter album_name: ')
                result = delete_album_by_artist_and_album_name(albums,artist,album_name)
                display.print_albums_list(result)
            else:
                print('Option not found')
        except ValueError:
            print('Enter only number!')
        

if __name__ == '__main__':
    main()
