from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Document
from .forms import DocumentForm

def home(request):
    return render(request, 'home.html')


@login_required
def document_list(request):
    documents = Document.objects.filter(submitted_by=request.user) | Document.objects.filter(approver=request.user)
    return render(request, 'document_list.html', {'documents': documents})

@login_required
def document_create(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)
            document.submitted_by = request.user
            document.save()
            return redirect('document_list')
    else:
        form = DocumentForm()
    return render(request, 'document_form.html', {'form': form})

@login_required
def document_update(request, pk):
    document = get_object_or_404(Document, pk=pk, submitted_by=request.user)
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES, instance=document)
        if form.is_valid():
            form.save()
            return redirect('document_list')
    else:
        form = DocumentForm(instance=document)
    return render(request, 'document_form.html', {'form': form})

@login_required
def document_delete(request, pk):
    document = get_object_or_404(Document, pk=pk, submitted_by=request.user)
    if request.method == 'POST':
        document.delete()
        return redirect('document_list')
    return render(request, 'document_confirm_delete.html', {'document': document})

@login_required
def document_approve(request, pk):
    document = get_object_or_404(Document, pk=pk, approver=request.user)
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'approve':
            document.approved = True
        elif action == 'reject':
            document.approved = False
        document.save()
        return redirect('document_list')
    return render(request, 'document_approve.html', {'document': document})