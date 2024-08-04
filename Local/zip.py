import os
import zipfile
def file_zip(source, target):
    f_zip = zipfile.ZipFile(source, 'w')
    f_zip.write(target, compress_type=zipfile.ZIP_DEFLATED)
    f_zip.close()
def files_zip(source, filetype_target):
    f_zip = zipfile.ZipFile(source, 'w')
    for folder, subfolders, files in os.walk(os.path.join(os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))), 'tmp')):
        for file in files:
            if file.endswith(filetype_target):
                f_zip.write(os.path.join(folder, file),
                            os.path.relpath(os.path.join(folder, file),
                                os.path.join(os.path.dirname(
                                os.path.dirname(os.path.abspath(__file__))), 'tmp')),
                            compress_type=zipfile.ZIP_DEFLATED)
    f_zip.close()
def file_unzip(source, target):
    f_zip = zipfile.ZipFile(source)
    f_zip.extract(target, os.path.dirname(os.path.abspath(__file__)))
    f_zip.close()
def file_all_unzip(source):
    f_zip = zipfile.ZipFile(source)
    f_zip.extractall(os.path.dirname(os.path.abspath(__file__)))
    f_zip.close()

if __name__ == "__main__":
    file_zip('compress.zip', 'source.file') #files_zip('compress.zip', './')
    file_unzip('compress.zip', 'source.file')
    file_all_unzip('compress.zip')
    os.remove('compress.zip')