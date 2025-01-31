class Solution:
    # Approach:
    # - Create a mapping from song to genre using the given songGenres dictionary.
    # - Iterate through each user's song list, count the occurrences of each genre.
    # - Determine the most listened genre(s) for each user.
    # - Return a dictionary mapping each user to their favorite genre(s).

    def favoriteGenre(self, userSongs: Dict[str, List[str]], songGenres: Dict[str, List[str]]) -> Dict[str, List[str]]:
        # Step 1: Create a mapping from song to genre
        song_to_genre = {}
        for genre, songs in songGenres.items():
            for song in songs:
                song_to_genre[song] = genre

        result = {}

        # Step 2: Process each user and count their genre frequencies
        for user, songs in userSongs.items():
            genre_count = {}  # Dictionary to store genre counts
            max_count = 0  # Track the maximum genre count

            for song in songs:
                if song in song_to_genre:  # Check if song belongs to a genre
                    genre = song_to_genre[song]
                    genre_count[genre] = genre_count.get(genre, 0) + 1
                    max_count = max(max_count, genre_count[genre])

            # Step 3: Find the genres with the highest count
            favorite_genres = [genre for genre, count in genre_count.items() if count == max_count]
            result[user] = favorite_genres

        return result

# Time Complexity: O(U * S + G * S) ≈ O(N)
#     - U is the number of users, S is the number of songs per user
#     - G is the number of genres, S is the number of songs per genre
#     - We iterate over the songs in both userSongs and songGenres once, leading to linear time complexity.
# Space Complexity: O(N), where N is the number of songs mapped to genres + the result storage.
# Example usage
userSongs = {
    "David": ["song1", "song2", "song3", "song4", "song8"],
    "Emma": ["song5", "song6", "song7"]
}
songGenres = {
    "Rock": ["song1", "song3"],
    "Dubstep": ["song7"],
    "Techno": ["song2", "song4"],
    "Pop": ["song5", "song6"],
    "Jazz": ["song8", "song9"]
}
solution = Solution()
result = solution.favoriteGenre(userSongs, songGenres)
print(result)  # Expected Output: {'David': ['Rock', 'Techno'], 'Emma': ['Pop']}
