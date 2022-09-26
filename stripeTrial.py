import stripe 


stripe_secret = ''
stripe_public = ''


stripe.api_key = stripe_secret

def create_stripe_customer(email, user_data, payment_info):
  customer_id = stripe.Customer.create(email = email, description='what is being paid for', metadata = user_data)['id']
  payment_method_id = create_payment_method(payment_info)
  stripe.PaymentMethod.attach(
    payment_method_id,
    customer = customer_id
  )
  return {
    "customer_id": customer_id,
    'payment_method_id': payment_method_id,
    #"plan": create_stripe_plan(customer_id)
  }

def create_payment_method(payment_info):
  return stripe.PaymentMethod.create(
    type = "card",
    card = {
      "number": payment_info.get('cardNumber'), #type str without spaces 
      "exp_month": payment_info.get('expirationMonth'), #type int in 1 to 12 format
      "exp_year": payment_info.get('expirationYear'), #type int of 4 digit e.g 2024
      "cvc": payment_info.get('cvc'), #type string
    }).get('id')

def create_stripe_plan(customer_id):
    #this would work when a customer attached payment source or default payment method
  return stripe.Subscription.create(
    customer = customer_id,
    items = [{"price":'price_1LmJiSGWLd0EIHEE0IUPcBvK',
    #'this takes in the price ID of the plan we have created on stripe'
    }]).get("id")


def signup():
    card_data = {'cardNumber':'4242424242424242', 'expirationMonth':7, 'expirationYear':2024, 'cvc':'345'}
    #card_data = event.get('cardData')
    email = '10102jpx@gmail.com'
    attributes = {'order_id': '6735'}
    #create_stripe_customer(email, attributes, card_data)
    return {'status_code': 200, 'message':create_stripe_customer(email, attributes, card_data)}

def retrivepay_method(pmethod_id):
    return stripe.PaymentMethod.retrieve(
        f"{pmethod_id}")
    


print(signup())

#print(stripe.PaymentMethod.retrieve("pm_1LmJWWGWLd0EIHEEoRE7PZ7h"))