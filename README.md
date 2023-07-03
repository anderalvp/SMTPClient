# SMTP Client implementation with Python

The documentation of this mini-project contain have the following parts:

- The modules imported from Python
- SMTP connection secured by SSL (Secure Sockets Layer)
- Attachment of a plain-text and a PDF file to send

## Modules imported

## SMTP connection secured by SSL (Secure Sockets Layer)

To send a mail using the Simple Mail Transfer Protocol we need to use the Python module called <code>smtplib</code>. After that we creates a SSL connection with the SMTP Gmail Server importing the <code>ssl</code> module and using <code>SMTP_SSL()</code>.

## Attachment of a plain-text and a PDF file to send

In this case this project uses MIME messages, which allow us to send plait-text versions of a email and also HTML versions


