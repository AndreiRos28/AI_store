import openai
import os
from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product

# Set your OpenAI API key (from .env or direct, for now we read from env)
openai.api_key = os.getenv("OPENAI_KEY")  # Or replace with actual key for testing

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
            # Generate tags from OpenAI
            product.tags = generate_tags(product.product_name, product.product_description)
            product.save()
            return redirect('product_list')
    else:
        form = ProductForm()

    return render(request, 'store/add_product.html', {'form': form})
