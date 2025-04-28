from django.db import models
import os
import uuid

def upload_to_tag_folder(instance, filename):
    # UwU, bikin nama file baru pake UUID biar ga ketauan asli filenya nya, tetep jaga ekstensi nya yaa~ >w<
    ext = os.path.splitext(filename)[1]
    new_filename = f"{uuid.uuid4().hex}{ext}"
    # Simpen file nya di folder media/docs/other/ pake nama baru yang kece badai ini~ nyaaa~
    return f'docs/other/{new_filename}'

class Tag(models.Model):
    CATEGORY = 'category'
    LANGUAGE = 'language'
    TAG_TYPE_CHOICES = [
        (CATEGORY, 'Category'),
        (LANGUAGE, 'Language'),
    ]

    name = models.CharField(max_length=50, unique=True)
    type = models.CharField(max_length=20, choices=TAG_TYPE_CHOICES, default=CATEGORY)

    def __str__(self):
        return self.name

class PDFDocument(models.Model):
    title = models.CharField(max_length=255)
    uploader_name = models.CharField(max_length=255)
    upload_date = models.DateTimeField(auto_now_add=True)
    accuracy_score = models.IntegerField(default=100)

    tags = models.ManyToManyField(Tag, related_name='pdf_documents')

    file = models.FileField(upload_to=upload_to_tag_folder)

    def __str__(self):
        return self.title

    @property
    def is_image(self):
        ext = os.path.splitext(self.file.name)[1].lower()
        # Cek deh, ini file nya gambar apa bukan, biar bisa tampil thumbnail nya kawaii~ >w<
        return ext in ['.jpg', '.jpeg', '.png', '.gif']

    @property
    def is_pdf_or_doc(self):
        ext = os.path.splitext(self.file.name)[1].lower()
        # Cek juga nih, file nya PDF atau DOC biar bisa dihandle dengan manis~ nyaaa~
        return ext in ['.pdf', '.doc', '.docx']

    @property
    def file_extension(self):
        ext = os.path.splitext(self.file.name)[1].lower()
        # Ambil ekstensi file nya, terus bikin huruf gede biar kece badai~ nyaaa~
        return ext[1:].upper() if ext else ''
