from django.db import models
from django.contrib.auth.models import User

class Document(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    pdf_file = models.FileField(upload_to='documents')
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='submitted_documents')
    approver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='documents_to_approve', null=True, blank=True)
    approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)