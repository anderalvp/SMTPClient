# SMTP Client implementation with Python

The documentation of this mini-project contain have the following parts:

- The modules imported from Python
- SMTP connection secured by SSL (Secure Sockets Layer)
- Attachment of a plain-text and a PDF file to send

## Modules 

- <code>smtplib</code>
- <code>ssl</code>
- <code>email</code>

## SMTP connection secured by SSL (Secure Sockets Layer)

To send a mail using the Simple Mail Transfer Protocol we need to use the Python module called <code>smtplib</code>. After that we creates a SSL connection with the SMTP Gmail Server importing the <code>ssl</code> module and using <code>SMTP_SSL()</code>.

## Attachment of a plain-text and a PDF file to send

This project uses MIME messages, which allow us to send plait-text versions of a email and also HTML versions.

## References

- [SMTP Protocol Client](https://docs.python.org/3/library/smtplib.html)
- [Creating email and MIME objects from scratch](https://docs.python.org/es/3.8/library/email.mime.html)



