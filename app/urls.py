from django.urls import path
from django.urls import path
from app.Views import Loginviews
from app.Views import Signupviews
from app.Views import Paymentview
from app.Views import  Paymentview
from app.Views import NccabView



from . import views

urlpatterns = [
    path('', Signupviews.index, name='index'),
    path('signup/', Signupviews.create, name='signup'),
    path('updateprofile/<int:id>',Signupviews.updateprofile, name ='updateprofile'),
    path('login', Loginviews.user_login, name='login'),
    path('logout',Loginviews.userLogout,name='logout'),
    path('sport',Loginviews.setting,name = 'sport'),
    path('update/<int:id>',Loginviews.update, name ='update'),
    path('buildmodel/', Signupviews.buildmodel, name ='buildmodel'),
    path('buildmodel/status/',Signupviews.buildmodelStatus, name ="buildmodel-status"),
    path('buildmodel/remove/',Signupviews.buildmodelremove, name ="buildmodel-remove"),
    path('buildmodelbutton',Signupviews.buildmodelbutton, name ="buildmodel-button"),
    path("reset",Signupviews.reset,name="reset"),
    path('register',Signupviews.create,name="register"),
    path('passwordchange/<int:id>',Loginviews.passwordchange, name ='passwordchange'),

    # path('buildmodel/percent/',Signupviews.buildmodelpercent, name ="buildmodel-percent"),

    
#payment urls
    path('stripe-checkout/', Paymentview.StripeCheckoutAPIView.as_view(), name = 'stripe_checkout'),
    path('stripe-checkout/success/',Paymentview.SuccessPayment.as_view(), name="success"),
    path('stripe-checkout/cancel/',Paymentview.cancel_subscription, name="cancel"),
    # path('webhook/', Paymentview.stripe_webhook), # new
    path('activate/<uidb64>/<token>/',Signupviews.activate, name='activate'),

    path('account',Signupviews.account,name="account"),
    path('membership',Signupviews.membership,name="membership"),
#NCAAB.urls
    path('create',NccabView.create,name="create"),


]





