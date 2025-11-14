# reportes.py

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader


def generar_reporte_pdf(dest, start, reglas, tipo, razones, imagen_bytes=None):
    c = canvas.Canvas(dest, pagesize=LETTER)
    w, h = LETTER

    y = h - inch

    c.setFont("Helvetica-Bold", 16)
    c.drawString(inch, y, "Reporte – Chomsky Classifier AI")
    y -= 0.6*inch

    c.setFont("Helvetica", 12)
    c.drawString(inch, y, f"Símbolo inicial: {start}")
    y -= 0.3*inch
    c.drawString(inch, y, f"Clasificación: {tipo}")
    y -= 0.5*inch

    c.setFont("Helvetica-Bold", 13)
    c.drawString(inch, y, "Gramática:")
    y -= 0.3*inch

    c.setFont("Helvetica", 11)
    for A, rhss in reglas.items():
        c.drawString(inch, y, f"{A} -> " + " | ".join(rhss))
        y -= 0.25*inch

    y -= 0.3*inch
    c.setFont("Helvetica-Bold", 13)
    c.drawString(inch, y, "Explicación:")
    y -= 0.3*inch

    c.setFont("Helvetica", 11)
    for r in razones:
        c.drawString(inch, y, f"- {r}")
        y -= 0.22*inch

    if imagen_bytes:
        c.showPage()
        img = ImageReader(imagen_bytes)
        img_w = w - 2*inch
        img_h = img_w * 0.6
        c.drawImage(img, inch, h - img_h - inch, width=img_w, height=img_h)

    c.save()
