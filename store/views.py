import openai
import os
from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product

openai.api_key = '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'

def generate_tags(product_name, description):
    try:
        # Create a prompt for OpenAI to generate tags
        prompt = f"Generate a list of descriptive, comma-separated tags for a product with the name '{product_name}' and description '{description}'."
        
        # Request tags from OpenAI using the ChatCompletion API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        
        # Extract and return the tags from the response
        tags = response.choices[0].message.content.strip()
        return tags
    except Exception as e:
        # Handle exceptions and return a fallback tag list
        print("OpenAI error:", e)
        return "tag1, tag2, tag3"

def product_list(request):
    # Retrieve all products from the database
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})

def add_product(request):
    if request.method == 'POST':
        # Process the form submission
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            
            # Generate tags for the product using OpenAI
            product.tags = generate_tags(product.product_name, product.product_description)
            
            # Save the product to the database
            product.save()
            
            # Redirect to the product list page
            return redirect('product_list')
    else:
        # Show an empty form if the request method is not POST
        form = ProductForm()

    return render(request, 'store/add_product.html', {'form': form})
