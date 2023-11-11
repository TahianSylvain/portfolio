import random
from celery import shared_task
from accounts.models import MyUser
from django.core.mail import send_mail


@shared_task(bind=True)
def smtp_func(self):
    """ U (the sender) need to check some account-security steps! """
    """ App passwords: team_esiia3 |-->> get(my_passd) """
    
    global key, new_user
    
    key = [random.randint(0, 9) for i in range(1, 10)]
    sender = MyUser.objects.get(email="ranjalahyandrytahianasylvain@gmail.com")
    mail_subject = "Hi! Mail confirmation by KEY-ing sent from Andry"
    message = f"""If you are new to our platform, please hit that key: {str(key)}"""

    to_email = new_user.email
    print(to_email)
    
    send_mail(
        subject=mail_subject,
        message=message,
        from_email=sender,  # default
        recipient_list=[to_email],
        fail_silently=True
    )
    print('Done')
