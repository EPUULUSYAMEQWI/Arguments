def product_and_greeting(*args,**kwargs):
    product=1
    for num in args:
        product*=num
    print(f"Hello {kwargs['name']} and you are {kwargs['age']}years old. The result is {product}")
    print(f"Hello{kwargs['name']} and you come from {kwargs['country']}. The result is {product}")