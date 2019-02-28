from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import ContactForm, ContactModel


# Create, Reads, Updates, Deletes
# Create your views here.

#function that prints all the contacts on the index page
def index(request):
    contact_list = ContactModel.objects.all()
    print(contact_list)
    return render(request, "contactBookApp/index.html", {"contactList": contact_list})

#function that directs you to the form where you can create a new contact and redirect it to the index page when complete
def contacts(request):
    new_contact = ContactForm(request.POST or None)
    print("In contact view")
    if new_contact.is_valid():
        new_contact.save()
        return redirect('index')

    return render(request, 'contactBookApp/contactBook.html', {'newContact': new_contact})

#function that once the name is clicked it will edit the page and save the edit and redirect you to the index page
def edit(request, id):
    contact = get_object_or_404(ContactModel, pk=id)
    newContact = ContactForm(request.POST or None, instance=contact)
    if newContact.is_valid():
        newContact.save()
        return redirect("index")
    return render(request, "contactBookApp/contactBook.html", {'newContact': newContact})

# function that deletes that sneds you to the delete html and verrifies if you want to delete
def delete(request, id):
    contact = get_object_or_404(ContactModel, pk=id)
    if request.method == 'POST':
        contact.delete()
        return redirect('index')

    return render(request, "contactBookApp/deleteContact.html", {"selectedContact": contact})
