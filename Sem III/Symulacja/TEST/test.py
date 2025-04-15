import hashlib

album_jako_string = '2799'

print(hashlib.md5(album_jako_string.encode()).hexdigest())