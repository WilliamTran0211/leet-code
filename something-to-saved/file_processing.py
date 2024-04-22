from django.core.files.uploadedfile import SimpleUploadedFile
from io import BytesIO
from PIL import Image
import moviepy.editor as mp
import mimetypes
import magic
import copy
import os

def write_bytesio_to_file(filename, bytesio):
    if type(bytesio) is bytesio:
        with open(filename, "wb") as outfile:
            outfile.write(bytesio.getbuffer())
    else:
        with open(filename, "wb") as outfile:
            outfile.write(bytesio.read())

def read_bytesio_from_file(filename):
    with open(filename, "rb") as fh:
        return BytesIO(fh.read())

class SupportedFiles:
    extension = {
        "IMAGE" : ['jpg', 'jpeg','png','gif','bmp','webp','svg'],
        "VIDEO" : ['mp4'],
        "ARCHIVE" : ['zip','rar'],
        "TEXT": ['txt', 'csv']
    }

    mime_type = {
        "IMAGE" : ['jpeg','png','bmp','svg+xml','webp','gif'],
        "VIDEO" : ['mp4'],
        "APPLICATION" : {
            "rar": ['rar', 'x-rar', 'x-rar-compressed', 'octet-stream', 'vnd.rar'],
            "zip":['zip', 'x-zip', 'x-zip-compressed']
        },
        "TEXT": ['plain', 'csv','comma-separated-values', 'x-comma-separated-values', 'x-csv']
    }

class FileProcessor:
    FILE_TYPE = ['image', 'video', 'application', 'text']
    SPECIAL_CASE = ['jpeg', 'jpg']

    def __init__(self, file):
        self.file = file
        self.magic_results = self.get_magic_mimetype_from_file(self.file.read(2048))
        self.file.seek(0)
        pass

    def get_file_instance(self):
        return self.file

    def get_file_name(self):
        return self.file.name

    @classmethod
    def get_magic_mimetype_from_file(cls, file, mime=True):
        if mime is None or mime not in [True, False]:
            mime = False
        if isinstance(file, bytes):
            result = magic.from_buffer(file, mime)
        else:
            result = magic.from_buffer(file.read(2048), mime)
            file.seek(0)
        return result

    @classmethod
    def check_file_is_support(cls, file_type=None, file_subtype=None, file_extension=None):
        if file_type is not None and file_subtype is not None:
            if file_extension is None:
                file_extension = file_subtype
            if file_type.upper() == 'IMAGE':
                return file_subtype in SupportedFiles.mime_type["IMAGE"] and file_extension in SupportedFiles.extension["IMAGE"]
            elif file_type.upper() == 'VIDEO':
                return file_subtype in SupportedFiles.mime_type["VIDEO"] and file_extension in SupportedFiles.extension["VIDEO"]
            elif file_type.upper() == 'APPLICATION':
                return file_subtype in SupportedFiles.mime_type["APPLICATION"] and file_extension in SupportedFiles.extension["APPLICATION"]
            elif file_type.upper() == 'TEXT':
                return file_subtype in SupportedFiles.mime_type["TEXT"] and file_extension in SupportedFiles.extension["TEXT"]
        return False


    @classmethod
    def check_archive(cls, file, archive_type=None):
        """
        this function will return the extension of the archive file
        >> return zip or rar
        """
        if file is not None:
            magic = cls.get_magic_mimetype_from_file(file, mime = True).lower()
            magic_full = cls.get_magic_mimetype_from_file(file, mime = False).lower()
            file_subtype = magic.split('/')[-1]
            mime_type_keywords = magic_full.split(' ')

            if archive_type is None:
                if file_subtype == "octet-stream" or "rar" in mime_type_keywords:
                    archive_type = "rar"
                elif "zip" in mime_type_keywords:
                    archive_type = "zip"
                else:
                    archive_type = file.name.split('.').pop()

            archive_type = archive_type.lower()
            if archive_type == 'zip' and magic_full.lower().find(archive_type) != -1:
                return "zip"
            elif archive_type == 'rar' and magic_full.lower().find(archive_type) != -1:
                return "rar"
        return None

    @classmethod
    def convert_filename(cls, old_filename, new_file_extension):
        """
        convert filename with old extension to new extension
        """
        if new_file_extension.find('.') != -1:
            new_file_extension = new_file_extension.split('.')[-1]
        old_file_name_arr = old_filename.split('.')
        old_file_name_arr.pop()
        new_file_name = '.'.join(old_file_name_arr)
        return "{file_name}.{file_extension}".format(file_name = new_file_name, file_extension = new_file_extension)

    @classmethod
    def convert_file_to_image(cls, file_name, image_extention = 'png'):
        """
        This function will convert a file to an image if the file can convert to image

        """
        if image_extention in SupportedFiles.extension['IMAGE']:
            with Image.open(file_name) as my_image:
                new_file_name = cls.convert_filename(file_name, image_extention)
                my_image.convert("RGBA")
                my_image.save(new_file_name)
                return new_file_name

    @classmethod
    def convert_file_to_video(cls, file_name, video_extention = 'mp4'):
        """
        This function will convert a file to an video if the file can convert to video
        """
        if video_extention in SupportedFiles.extension['VIDEO']:
            with mp.VideoFileClip(file_name) as video_clip:
                new_file_name = cls.convert_filename(file_name, video_extention)
                video_clip.write_videofile(new_file_name)
                return new_file_name

    def is_file_supported(self):
        """
        This function will check the file is supported in the app
        """
        if self.file is not None:
            file_type, file_subtype, guess_extension = self.get_file_information()
            if guess_extension is not None and guess_extension.find('.') != -1:
                guess_extension = guess_extension.split('.')[-1]
            return FileProcessor.check_file_is_support(file_type, file_subtype, guess_extension)
        return False

    def check_file_by_type(self, type = None):
        """
        This function will check the file is like the type in parameters

        type must be a string in ['Image', 'Video', 'Application', 'Archive']

        if file is an image and the type input is 'image' then return True
        if file is a video and the type input is 'image' then return False

        """
        if type is not None and type.lower() in self.FILE_TYPE:
            file_type, file_subtype, guess_extension = self.get_file_information()
            if type.lower() == 'archive':
                type = 'application'
            if file_type.lower() == type.lower():
                return True
        return False

    def get_file_information(self):
        """
        This function will return real type and extention of file using python_magic lib
        """
        guess_extension = mimetypes.guess_extension(self.magic_results)
        file_info = self.magic_results.split('/')
        file_type = file_info[0]
        file_subtype = file_info[1]
        return file_type, file_subtype, guess_extension


    def get_true_file(self):

        """
        This function will change the file extension in the name and content_type of file to the acturally file encode, by using the magic_python libs
        """
        self.file.seek(0)
        file_name = self.file.name
        file_extention_by_name = self.file.name.split('.')[-1]
        real_file_type, real_file_subtype, guess_extension = self.get_file_information()

        if real_file_type == 'application':
            file_archive_type = self.check_archive(self.file)
            if file_archive_type is not None:
                real_file_subtype = file_archive_type

        if file_extention_by_name in self.SPECIAL_CASE and guess_extension in self.SPECIAL_CASE:
            return self.file
        elif real_file_type == "text" and real_file_subtype == "plain":
            if file_extention_by_name == "csv":
                return self.file
        else:
            if guess_extension is not None and file_extention_by_name != guess_extension:
                self.file.seek(0)
                new_name = self.convert_filename(file_name, guess_extension)
                new_content_type = real_file_type + "/"+ real_file_subtype
                new_upload_file = SimpleUploadedFile(new_name, self.file.read(), new_content_type)
                new_upload_file.field_name = new_name
                self.file = copy.deepcopy(new_upload_file)
                return self.file

    def can_file_convert_to_video(self, file = None):
        """
        This function will check can the file can convert to a Video.
        If can convert to a Video
            >>> return True
        IF not then
            >>> return False
        """
        if file is None:
            file = self.get_file_instance()

        with Image.open(file.name) as my_file:
            duration = my_file.info.get('duration')

            if duration is not None and duration > 0 :
                my_file.close()
                return True
            else:
                my_file.close()
                return False

    def convert_gif(self):
        VIDEO_FILE_EXTENSION = 'mp4'
        IMAGE_FILE_EXTENSION = 'png'
        real_file_type, real_file_subtype, guess_extension = self.get_file_information()
        file_name = self.file.name
        if real_file_subtype == 'gif':
            write_bytesio_to_file(file_name, self.file)
            if self.can_file_convert_to_video():
                converted_file_name = self.convert_file_to_video(file_name, VIDEO_FILE_EXTENSION)
                new_content_type = 'video/'+ VIDEO_FILE_EXTENSION
            else:
                converted_file_name = self.convert_file_to_image(file_name, IMAGE_FILE_EXTENSION)
                new_content_type = 'image/'+ IMAGE_FILE_EXTENSION

            with open(converted_file_name, 'rb') as f:
                new_upload_file = SimpleUploadedFile(converted_file_name, f.read(), new_content_type)
                new_upload_file.field_name = converted_file_name
                self.file = copy.deepcopy(new_upload_file)
                f.close()
                if os.path.isfile(converted_file_name):
                    os.remove(converted_file_name)
                if os.path.isfile(file_name):
                    os.remove(file_name)

        return self.file.seek(0)


