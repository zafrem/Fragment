import snappy
#pip install python-snappy

original_string = 'This is a test string to be compressed.'
compressed_string = snappy.compress(original_string)
print(f'Compressed string: {compressed_string}')

decompressed_string = snappy.decompress(compressed_string)
print(f'Decompressed string: {decompressed_string}')

