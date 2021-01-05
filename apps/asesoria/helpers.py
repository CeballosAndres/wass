from django.core.mail import send_mass_mail
from django.template.loader import render_to_string


def enviarEmail(accion, asesoria):
    # Pepare email
    email_context = {
        'accion': accion,
        'asesoria': asesoria,
    }
    #email para el asesorado
    msg_plain = render_to_string('asesoria/notificacion_email_asesorado.txt', email_context)
    #email para el asesor
    msg_plain_a = render_to_string('asesoria/notificacion_email_asesor.txt', email_context)
    #msg_html = render_to_string('asesoria/notificacion_email.html', email_context)
    # Send two emails
    datatuple = (
        (f'{accion.capitalize()} de asesoría', msg_plain, 'wass.asesorias@gmail.com', [asesoria.asesorado]),
        (f'{accion.capitalize()} de asesoría', msg_plain_a, 'wass.asesorias@gmail.com', [asesoria.asesor]),
    )
    
    send_mass_mail(datatuple)