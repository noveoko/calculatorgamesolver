class foo:

    def bar():
        print("THIS WORKS!")

        
result = getattr(foo, 'bar')()