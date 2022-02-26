# NoInheritFromObject
# ChainedExceptionHandler
# ProbablyMeantTuple

class LoginRequiredMixin(object):

    redirect_field_name = 'next'
    login_url = None
    fields = ('title')

    def format_product_option(self, product_string):
        products = product_string.split(',')
        try:
            list(map(int, products))
        except ValueError or SyntaxError:
            print(f'Product string invalid - {product_string}')
            return []
        return products
