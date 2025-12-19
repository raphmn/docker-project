import os
import stripe
from flask import Flask, redirect, request

app = Flask(__name__)

stripe.api_key = os.getenv('STRIPE_SECRET_KEY')

@app.route('/')
def index():
    # Page minimaliste avec un bouton de paiement
    return '''
    <body style="background:#121212; color:white; display:flex; flex-direction:column; align-items:center; justify-content:center; height:100vh; font-family:sans-serif;">
        <h1>Produit Test - 20€</h1>
        <form action="/checkout" method="POST">
            <button type="submit" style="padding:15px 30px; border-radius:10px; border:none; background:#6772e5; color:white; font-weight:bold; cursor:pointer;">
                Payer maintenant
            </button>
        </form>
    </body>
    '''

@app.route('/checkout', methods=['POST'])
def create_checkout_session():
    try:
        # Création de la session Stripe
        checkout_session = stripe.checkout.Session.create(
            line_items=[{
                'price_data': {
                    'currency': 'eur',
                    'product_data': {'name': 'Achat Projet'},
                    'unit_amount': 2000,  # 20.00€ en centimes
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=request.host_url + 'success',
            cancel_url=request.host_url + 'cancel',
        )
        return redirect(checkout_session.url, code=303)
    except Exception as e:
        return str(e), 500

@app.route('/success')
def success():
    return '''
    <body style="background:#121212; color:white; display:flex; flex-direction:column; align-items:center; justify-content:center; height:100vh; font-family:sans-serif;">
        <h1 style='color:green; text-align:center;'>Paiement réussi ! 🎉</h1>
    </body>
    '''

@app.route('/cancel')
def cancel():
    return '''
    <body style="background:#121212; color:white; display:flex; flex-direction:column; align-items:center; justify-content:center; height:100vh; font-family:sans-serif;">
        <h1 style='color:red; text-align:center;'>Paiement annulé. ❌</h1>
    </body>
    '''
