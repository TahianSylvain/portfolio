from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth.models import User


@shared_task(bind=True)
def smtp_func(new_user, key):
    """ U (the sender) need to check some account-security steps! """
    """ App passwords: team_esiia3 |-->> get(my_passd) """
    
    
    sender = User.objects.get(email="ranjalahyandrytahianasylvain@gmail.com")
    mail_subject = "Hi! Mail confirmation by KEY-ing sent from Andry"
    message = f"""If you are new to our platform, please hit that key: {str(key)}"""

    to_email = new_user.email
    print(to_email)
    
    send_mail(
        subject=mail_subject,
        message=message,
        from_email=sender.email,  # default
        recipient_list=[to_email],
        fail_silently=True
    )
    print('Done')
