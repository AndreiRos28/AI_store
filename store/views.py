import openai
import os
from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product

openai.api_key ='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' 

def generate_tags(product_name, description):
    try:
        prompt = f"Generate a list of descriptive, comma-separated tags for a product with the name '{product_name}' and description '{description}'."
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        tags = response.choices[0].message.content.strip()
        return tags
    except Exception as e:
        print("OpenAI error:", e)
        return "tag1, tag2, tag3"

def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.tags = generate_tags(product.product_name, product.product_description)
            product.save()
            return redirect('product_list')
    else:
        form = ProductForm()

    return render(request, 'store/add_product.html', {'form': form})
