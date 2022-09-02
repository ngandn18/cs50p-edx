from fpdf import FPDF


def get_name():
    while True:
        if (name := input("Name: ").strip()):
        # if name:
            return name

def main():
    pdf = FPDF(orientation = "P", unit = "mm", format = "A4")
    pdf.add_page()
    pdf.set_font('helvetica', size=48)
    pdf.cell(0, 30, 'CS50 Shirtificate', 0, new_x="LMARGIN", new_y="NEXT", align='C')
    pdf.ln(5)
    pdf.image("shirtificate.png", w=pdf.epw, h=pdf.eph * 3/4, y=60)
    pdf.set_font('helvetica', size=24)
    pdf.set_text_color(r=255, g=255, b=255)
    # set font for full name
    pdf.cell(0, 180, get_name() + ' took CS50', 0, new_x="LMARGIN", new_y="NEXT", align='C')
    pdf.output("sh.pdf")
    # pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()