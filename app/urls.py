from django.urls import path
from django.urls import path
from app.Views import Loginviews
from app.Views import Signupviews
from app.Views import Paymentview
from app.Views import  Paymentview



from . import views

urlpatterns = [
    path('', Signupviews.index, name='index'),
    path('signup', Signupviews.create, name='signup'),
    path('login', Loginviews.user_login, name='login'),
    path('logout',Loginviews.userLogout,name='logout'),

    
#payment urls
    path('stripe-checkout/', Paymentview.StripeCheckoutAPIView.as_view(), name = 'stripe_checkout'),
    path('stripe-checkout/success/',Paymentview.SuccessPayment.as_view(), name="success"),
    path('stripe-checkout/cancel/',Paymentview.cancel_subscription, name="cancel"),
    # path('webhook/', Paymentview.stripe_webhook), # new
    path('activate/<uidb64>/<token>/',Signupviews.activate, name='activate'),
]





