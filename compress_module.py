
import base64
import zlib


def compress(inputfile, outputfile):
    data = open(inputfile,'r').read()
    data_bytes = bytes(data,'utf-8')
    compressed_data = base64.b64encode(zlib.compress(data_bytes, 9))
    decoded_data = compressed_data.decode('utf-8')
    compressed_file= open(outputfile,'w')
    compressed_file.write(decoded_data)

def decompress(inputfile,outputfile):
    file_content = open(inputfile,'r').read()
    encoded_data = file_content.encode('utf-8')
    decompressed_data= zlib.decompress(base64.b64decode(encoded_data))
    decoded_data=decompressed_data.decode('utf-8')
    file = open(outputfile,'w')
    file.write(decoded_data)




