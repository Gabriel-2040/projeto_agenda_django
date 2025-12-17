from django.shortcuts import get_object_or_404,render , redirect
from django.urls import reverse
from contact.models import Contact

from contact.forms import ContactForm 

def create(request):
    if request.method == 'POST':
        form_action = reverse('contact:create')

        if request.method =='POST':
            form = ContactForm(request.POST, request.FILES)

            context = {
                'form' : form,
                'form_action' : form_action,
            }

            if form.is_valid:
                contact = form.save()
                return redirect('contact:update',contact_id = contact.pk)

            return render(
                request,
                'contact/create.html',
                context
            )

    context = {
                'form' : ContactForm(),
                'form_action':form_action,
            }

    return render(
        request,
        'contact/create.html',
        context
    )

def update(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id, show=True)
    form_action = reverse('contact:update', args=(contact_id,))

    if request.method == 'POST':
        form = ContactForm(request.POST,request.FILES, instance=contact)

        if form.is_valid():
            form.save()
            return redirect('contact:update', contact_id=contact.pk)

        return render(
            request,
            'contact/create.html',
            {
                'form': form,
                'form_action': form_action,
            }
        )

    # GET → carregar formulário preenchido
    form = ContactForm(instance=contact)

    return render(
        request,
        'contact/create.html',
        {
            'form': form,
            'form_action': form_action,
        }
    )


def delete(request, contact_id):
    contact = get_object_or_404(
        Contact, pk = contact_id, show = True
        )
    confirmation = request.POST.get('confirmation','no')
    
    if confirmation == 'yes':
        contact.delete()
        return redirect('contact:index')

    #contact.delete()
    #return redirect('contact:index')
    return render(
        request,
        'contact/contact.html',
        {
            'contact':contact,
            'confirmation':confirmation,
        }
    )