from django.core.mail import send_mail

send_mail(
    'Subject here',
    'Here is the message.',
    'vered.ros@gmail.com',
    ['thehightechgarden@gmail.com'],
    fail_silently=False,
)