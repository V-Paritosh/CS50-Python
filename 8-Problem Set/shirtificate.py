from fpdf import FPDF

name = input("Name: ")

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()
pdf.set_font("helvetica", "B", 20)
pdf.cell(50, 10, "CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", center=True)

pdf.ln(10)
pdf.image("shirtificate.png", w=200, h=200, x=5)

pdf.set_xy(55, 100)
pdf.set_font("helvetica", "B", 30)
pdf.set_text_color(255, 255, 255)
pdf.cell(100, 10, name, align="C")


pdf.output("shirtificate.pdf")