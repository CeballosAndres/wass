from django.core.mail import send_mail
from django.template.loader import render_to_string


def enviarEmail(accion, asesoria):
    # Pepare email
    email_context = {
        'accion': accion,
        'asesoria': asesoria,
    }
    msg_plain = render_to_string('asesoria/notificacion_email.txt', email_context)
    msg_html = render_to_string('asesoria/notificacion_email.html', email_context)
    # Send email
    send_mail(
        f'{accion.capitalize()} de asesoría',
        msg_plain,
        'wass.asesorias@gmail.com',
        [asesoria.asesor, asesoria.asesorado],
        # html_message=msg_html,
    )
